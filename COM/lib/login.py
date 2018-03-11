import pymysql
#from demjson import decode
def login(data):
	pwd = data['password']
	email = data['email']
	conn = pymysql.connect(host='localhost',database='medical',user='root',password='satpute@123')
	cursor = conn.cursor(pymysql.cursors.DictCursor)
	sql = "select *from users where email = '%s' and password = '%s'"%(email,pwd) 
	cursor.execute(sql)
	row = cursor.fetchone()
	print(type(row))
	if row is not None:
		row["type"]="rlogin"
		row["status"]='success'
		return row
	else:
		row ={}
		row["type"]="rlogin"
		row["status"]='fail'
		return row  #"Email ID or Password Wrong,Try again!"	


#result = login({"email":"1xyz@abc.in","password":"123"})		
#print(result)