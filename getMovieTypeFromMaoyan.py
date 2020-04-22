from selenium import webdriver
import time
import pymysql

#初始化浏览器
browser = webdriver.Chrome()
browser.get("https://maoyan.com/films/")

#初始化数据库
mhost='cdb-mzvws756.cd.tencentcdb.com'
muser='spider'
mpassword='zxc123!@#'
mport=10143
mdb = 'spider_data'
connect = pymysql.connect(host=mhost, user=muser, password=mpassword, db=mdb, port=mport)
cursor = connect.cursor()

for i in range(2,27):
    num = i-1
    type = browser.find_element_by_xpath('/html/body/div[4]/div/div[1]/ul/li[1]/ul/li['+str(i)+']/a').text

    insert_sql = """
            insert into movie_type (movie_type_id,movie_type_name) VALUES(%s,%s)
            """
    cursor.execute(insert_sql, (num, type))
    connect.commit()

time.sleep(2)
browser.quit()