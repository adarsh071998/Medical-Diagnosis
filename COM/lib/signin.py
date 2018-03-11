import pymysql
import json
import ast
from demjson import decode
def signin(data):
	try:
		sql = "INSERT INTO users(name,age,sex,email,password,phone,blood_grp)VALUES('%s',%s,'%s','%s','%s',%s,'%s')"%(data['name'],data['age'],data['sex'],data['email'],data['password'],data['phone'],data['blood'])
		conn = pymysql.connect(host='localhost',database='medical',user='root',password='satpute@123')
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute(sql)
		sql = "select *from users where email = '%s' and password = '%s'"%(data['email'],data['password']) 
		cursor.execute(sql)
		result = cursor.fetchall()
		result = str(result[0])
		result = decode(result)
		print(type(result))
		result["type"]="rsignin"
		result["status"]='success'
		conn.commit()
		return result
	except:
		return ('{"type"="rsignin","status":"fail"}')

"""data={}
data['name']='sachin'
data['sex']='M'
data['age']=16
data['email']='xyz@abc.in'
data['password']='123'
data['phone']=8789663
data['blood']='o+'
result = signin(data)
print(result)"""