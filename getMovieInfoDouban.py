from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import time
import pymysql
import re

#初始化浏览器
options=Options()
options.add_argument('--headless')
browser = webdriver.Chrome(chrome_options=options)

#初始化数据库
mhost='cdb-mzvws756.cd.tencentcdb.com'
muser='spider'
mpassword='zxc123!@#'
mport=10143
mdb = 'spider_data'
connect = pymysql.connect(host=mhost, user=muser, password=mpassword, db=mdb, port=mport)
cursor = connect.cursor()


def getInfo(url):

    # 进入网址
    browser.get(url)

    # 数据库链接打开

    # 爬取movie表
    movieName = browser.find_element_by_xpath('/html/body/div[3]/div[1]/h1/span[1]').text
    movieName = ''.join(re.findall('[\u4e00-\u9fa5]', movieName))
#    movieScroe = browser.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/strong').text
#    movieScroe = browser.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/strong').text
    movieScroe = browser.find_element_by_xpath('/html/body/div[3]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/strong').text

#    movieScroe = browser.find_element_by_class_name('ll rating_num').text
    print('score: ',movieScroe)
    movieScroe = float(movieScroe)
#    picUrl = browser.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/a/img').get_attribute('src')
    picUrl = browser.find_element_by_xpath('/html/body/div[3]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/a/img').get_attribute('src')

    insert_sql = """
            insert into movie (movie_name,movie_rate,movie_image) VALUES(%s,%s,%s)
            """
    cursor.execute(insert_sql, (movieName,movieScroe,picUrl))
    connect.commit()

    # 获取电影ID
#    sql = "select movie_id from movie where movie_name="+movieName
    sql = "select movie_id from movie where movie_name=%s"
    cursor.execute(sql,movieName)  # 执行sql
    movieId = cursor.fetchall()
    movieId = movieId[0][0]
    print('movieId: ',movieId)


    # 导演
    movieDirector = browser.find_element_by_xpath('//*[@id="info"]/span[1]').text
    movieDirector = movieDirector[4:]
    print(movieDirector)
    # 查找导演
    sql = "select director_id from director where director_name=%s"
    cursor.execute(sql,movieDirector)  # 执行sql
    directorId = cursor.fetchall()
    # 如果不存在导演，插入
    if len(directorId)==0:
        insert_sql = """
                    insert into director (director_name) VALUES(%s)
                    """
        cursor.execute(insert_sql, (movieDirector))
        connect.commit()
        #获取导演id
        sql = "select director_id from director where director_name=%s"
        cursor.execute(sql, movieDirector)  # 执行sql
        directorId = cursor.fetchall()

    # 得到导演ID
    directorId = directorId[0][0]

    # 将导演ID和电影插入映射表
    insert_sql = """
                insert into director_movie_map (director_id,movie_id) VALUES(%s,%s)
                """
    cursor.execute(insert_sql, (directorId,movieId))
    connect.commit()

    # 演员
    movieStar = browser.find_element_by_class_name('actor').text
    print(movieStar)
    movieStar = re.split('[ / ]',movieStar)
    for i in movieStar:
        if i == '更多...' or i=='主演:':
            movieStar.remove(i)
    while '' in movieStar:
        movieStar.remove('')
    print(movieStar)
    #查找演员
    for star in movieStar:
        sql = "select actor_id from actor where actor_name=%s"
        cursor.execute(sql, star)  # 执行sql
        actorId = cursor.fetchall()
        if len(actorId)==0:
            insert_sql = """
                        insert into actor (actor_name) VALUES(%s)
                        """
            cursor.execute(insert_sql, (star))
            connect.commit()

            sql = "select actor_id from actor where actor_name=%s"
            cursor.execute(sql, star)  # 执行sql
            actorId = cursor.fetchall()
            actorId = actorId[0][0]
        insert_sql = """
                    insert into actor_movie_map (movie_id,actor_id) VALUES(%s,%s)
                    """
        cursor.execute(insert_sql, (movieId,actorId))
        connect.commit()



    # 获取电影类型
    types = []
    for i in range(2,12):
        temp = browser.find_element_by_xpath('//*[@id="info"]/span['+str(i)+']').text
        if temp == '类型:':
            i = i + 1
            mtype = browser.find_element_by_xpath('//*[@id="info"]/span[' + str(i) + ']').text
            print(mtype)
            sql = "select movie_type_id from movie_type where movie_type_name=%s"
            cursor.execute(sql, mtype)  # 执行sql
            typeId = cursor.fetchall()
            while len(typeId)!=0:
                typeId = typeId[0][0]
                insert_sql = """
                                    insert into movie_type_map (movie_id,movie_type_id) VALUES(%s,%s)
                                    """
                cursor.execute(insert_sql, (movieId, typeId))
                connect.commit()

                i = i + 1
                mtype = browser.find_element_by_xpath('//*[@id="info"]/span[' + str(i) + ']').text
                sql = "select movie_type_id from movie_type where movie_type_name=%s"
                cursor.execute(sql, mtype)  # 执行sql
                typeId = cursor.fetchall()
    # 延迟两秒
    time.sleep(5)


with open('./spiderdata.json') as fileObj:
    contents = fileObj.readlines(25000)

for content in contents:
    URL = content[10:-3]
    print(URL)
    getInfo(URL)

# 关闭浏览器
browser.quit()

# 关闭链接
cursor.close()
connect.close()