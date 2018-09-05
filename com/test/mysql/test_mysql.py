#coding:utf-8
import pymysql
import time

# db=pymysql.connect("localhost","root","root","test")
db=pymysql.connect("172.17.162.5","riil","","test")
cursor=db.cursor()
# cursor.execute("select * from demo");
query_sql="select * from text"
cursor.execute(query_sql)
results = cursor.fetchall()
print("共%s条" %len(results))
for row in results:
      id = row[0]
      username = row[1]
      userlink = row[2]
      createtime = row[3]
      text = row[4]
      testlink = row[5]
      inserttime=row[13]
      comeform=row[15]
      print ("id=%s,username=%s,userlink=%s,createtime=%s,text=%s,testlink=%s,inserttime=%s,comeform=%s" % \
           (id, username, userlink, createtime, text, testlink, inserttime, comeform ))
      
insert_sql="insert into text(id, userName, userLink, createTime, text, textLink, comeFrom, comeLink, picLink,audioLink,videoLink, insertTime) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
parms=[]
parms.append("id")
parms.append("userName")
parms.append("userLink")
parms.append(time.localtime())
parms.append("text")
parms.append("textLink")
parms.append("comeFrom")
parms.append("comeLink")
parms.append("picLink")
parms.append("audioLink")
parms.append("videoLink")
parms.append(time.localtime())
try:
    cursor.execute(insert_sql, parms)
except Exception as e:
    print(e)
    db.rollback()
finally:
    db.commit()
    
delparms=[]
del_sql="delete from text where id=%s"
delparms.append("id")

try:
    cursor.execute(del_sql, delparms)
except Exception as e:
    print(e)
    db.rollback()
finally:
    db.commit()

