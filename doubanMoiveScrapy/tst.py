import  pymysql
mhost='cdb-mzvws756.cd.tencentcdb.com'
muser='spider'
mpassword='zxc123!@#'
mport=10143
mdb = 'spider_data'
connect = pymysql.connect(host=mhost, user=muser, password=mpassword, db=mdb, port=mport)
cursor = connect.cursor()


insert_sql = """
insert into movie_type (movie_type_id,movie_type_name) VALUES(%s,%s)
"""
cursor.execute(insert_sql, (1,'重庆'))
connect.commit()



cursor.close()
connect.close()