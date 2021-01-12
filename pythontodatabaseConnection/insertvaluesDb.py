from dbconnectpgm.dbconnect import *
db=get_connection()
cursor=db.cursor()
id=input("enter value for id")
name=input()
sql="insert into faculty(id,name,subject)values('101','vijay','operatingSystem')"

try:
    cursor.execute(sql)
    db.commit()
    print("query executed")
except Exception as e:
    print(e.args)
finally:

    db.close()



#html 1
#css 2
#bootstrap 2
#javascript
#django
#fubv
#cbv(1month)


#minum 4 prjt
#