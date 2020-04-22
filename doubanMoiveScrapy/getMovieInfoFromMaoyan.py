from selenium import webdriver
import time
import pymysql

url = 'https://maoyan.com/films/1277939'


def getMovieInfo(mUrl):
    # 初始化浏览器
    browser = webdriver.Chrome()
    browser.get("https://maoyan.com/films/")

    # 初始化数据库
    mhost = 'cdb-mzvws756.cd.tencentcdb.com'
    muser = 'spider'
    mpassword = 'zxc123!@#'
    mport = 10143
    mdb = 'spider_data'

    connect = pymysql.connect(host=mhost, user=muser, password=mpassword, db=mdb, port=mport)
    cursor = connect.cursor()

    # 执行
    movieName = browser.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[1]/h1').text
    movieScore = browser.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[3]/div[1]/div/span/span').text



    # 结束