import psycopg2 as pg
def db_connect(username="postgres",password="root",host="localhost",database="flask"):
	try:
		conn = pg.connect(dbname=database,user=username, host=host, password=password,port=5433)
		print "successfully connected!!!"
		return conn
	except Exception as err:
		return err
def get_data(table):
	conn=db_connect()
	cur=conn.cursor()
	cur.execute('select * from '+table)
	columns=cur.description
	data=cur.fetchall()
	cur.close()
	conn.close()
	return [col[0] for col in columns],data
def set_data(table,data):
	print data,"Dataaaaaaaaaaaaaaaaa"
	try:
		cols=[i for i in data if not data[i]=='']
		vals=[data[i] for i in data if not data[i]=='']
		conn=db_connect()
		cur=conn.cursor()
		cur.execute('insert into '+table+' ('+','.join(cols)+') values('+','.join(vals)+')')
		conn.commit()
		cur.close()
		conn.close()
		return 1
	except Exception as err:
		return err

	
