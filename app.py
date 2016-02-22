from flask import Flask,render_template,url_for,request
from connect import get_data,set_data,db_connect   
import pandas as pd 
import numpy as np
import os
app = Flask(__name__) 
#app=Flask(__name__,template_folder="temp")  
@app.route('/')	
def hello_world():
	person_details=[{'name':'n1','age':25,'sal':20000},
					{'name':'n2','age':26,'sal':21000},
					{'name':'n3','age':27,'sal':22000}]
	return render_template('index.html',data=person_details)
@app.route('/emp/')
def emp_data():
	APP_ROOT = os.path.dirname(os.path.abspath(__file__))   # refers to application_top
	APP_STATIC = os.path.join(APP_ROOT, 'static') # refers the static directory
	df=pd.read_csv(os.path.join(APP_STATIC, 'e1.csv'))
	return render_template('emp.html',data=df)
@app.route('/emp_data')
def emp_data1():
	APP_ROOT = os.path.dirname(os.path.abspath(__file__))   # refers to application_top
	APP_STATIC = os.path.join(APP_ROOT, 'static') # refers the static directory
	df=pd.read_csv(os.path.join(APP_STATIC, 'e1.csv'))
	return df.to_html()
@app.route('/client/insertion')
def client_insertion():
	conn=db_connect() # to get the connection object
	cur=conn.cursor() # creting cursor object
	cur.execute('select id from client') 
	max_id=max([i[0] for i in cur.fetchall()]) # to get max id in the total ids of the client table
	max_id=max_id+1
	dict_vals={'id':str(max_id),
				'name':'name5',
				'address':'address5',
				'cell':'5689789',
				'course_id':'1',
				'remark1':'remarks1',
				'remark2':'remarks2',
				'remark3':'remarks3',
				'remark4':'remarks4',}
	query="INSERT INTO client(id,name,address,cell,course_id,remark1,remark2,remark3,remark4) VALUES (%(id)s,%(name)s,%(address)s,%(cell)s,%(course_id)s,%(remark1)s,%(remark2)s,%(remark3)s,%(remark4)s)"
	cur.execute(query,dict_vals)
	#cur.execute("insert into client(id,name,address,cell,course_id,remark1,remark2,remark3,remark4) values("+str(max_id+1)+",'name5','address5',5689789,1,'remarks1','remarks2','remarks3','remarks4') ") # query execution
	conn.commit() # To save the changes in database
	cur.close() # closing the cursor
	conn.close()  # closing the connection
	return "secussfully inserted!"
@app.route('/registration/<table_name>',methods=['GET','POST']):
def create(table_name):
	conn=db_connect() # to get the connection object
	cur=conn.cursor() # creting cursor object
	if request.method=="POST":
		flag=set_data(table_name,request.form)
	else:
		cur.execute("select column_name, data_type, character_maximum_length from INFORMATION_SCHEMA.COLUMNS where table_name = "+table_name+";")
		print cur.fetchall(),"$$$$$$$$$$$$$$$$"
		return render_template('common_form.html',column)
	

@app.route('/db_data/<table>')
def db_data(table):
	try:
		cols,data=get_data(table)
		return render_template('db.html',data=data,cols=cols)
	except Exception as err:
		return render_template('error.html',error=err)
@app.route('/client/registration',methods=['GET','POST'])
def client_reg():
	if request.method=="POST":
		flag=set_data('client',request.form)
	return render_template('client_reg.html')
# @app.route('/db_data')
# def db_data():
# 	cols,data=get_data('client')
# 	return render_template('db.html',data=data,cols=cols)
#@app.route('/table')	
# def fun_table():
# 	table=pd.read_table('http://www.w3schools.com/html/html_tables.asp')
# 	print table
# 	print "fun_table calledddddddd" 
# 	return "sdfsdfsdfd"   
# def hello_world():
#     return '''<html>
#     				<head>
#     					<title>
#     					hello World
#     					</title>
#     				</head>
#     				<body>
#     					<h1>Hello World!</h1>
#     				</body>
#     			</html>
#     '''
if __name__ == '__main__':
	app.run(debug=True)