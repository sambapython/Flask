from flask import Flask,render_template,url_for
from connect import db_connect   
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