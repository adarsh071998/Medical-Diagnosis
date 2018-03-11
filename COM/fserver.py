from flask import Flask, abort, request 
from werkzeug import secure_filename
from flask import send_file
import json
import pymysql
from lib.cbc2 import CBC
from lib.evaluating import model 
from lib.pie import pie
app = Flask(__name__)


@app.route('/login_form', methods=['GET']) 
def login_form():
	form = """<form>
			<form action = "http://localhost:5000/login" method = "POST">
			Email: 
			<input type = "text" name = "email"  maxlength = "100" />
			<br/>
			 Password: 
			<input type = "password" name = "password"  maxlength = "100" />
			<input type = "submit"/>
			</form>"""
	return form  		

@app.route('/login', methods=['POST','GET']) 
def login():
	if not request.json:
		abort(400)
	else:    
		print (request.json)
		data = request.json
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
			print(row)
			return json.dumps(row)
		else:
			row ={}
			row["type"]="rlogin"
			row["status"]='fail'
			print(row)

			return json.dumps(row)
	
@app.route('/signin', methods=['POST']) 
def signin():
	if not request.json:
		abort(400)
	else:    
		print (request.json)
		try:
			data = request.json
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
			return json.dumps(request)
		except:
			return ('{"type"="rsignin","status":"fail"}')


@app.route('/cbc', methods=['POST','GET']) 
def cbc():
	#if not request.json:
	#	abort(400)
	#else:    
		data ={}
		data['user_id']='Guest'
		data['sex']='M'
		data['age']=16
		data['rbc']=3.9
		data['wbc']=6
		data['hgb']=12
		data['hct']=35
		data['mcv']=84
		data['mch']=30
		data['mchc']=34.8
		data['chcm']=34.8
		data['rdw']=14
		data['hdw']=3
		data['plt']=200
		data['mpv']=8
		data['neu']=100
		data['lymph']=20
		data['mono']=40
		data['eosin']=20
		data['baso']=20
		print (request.json)
		#data = request.json
		pie(data)
		result = str(CBC(data))
		return(result)

@app.route('/xray', methods=['POST']) 
def xray():
	f = request.files['image']
	f.save(secure_filename(f.filename))
	s = model(f.filename)	
	s= str(s)
	return json.dumps(s)


@app.route('/get_image', methods=['get']) 
def get_image():
	filename = '/home/pritesh/Desktop/COM/pie.png'
	return send_file(filename, mimetype='image/gif')
	

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug=True)
