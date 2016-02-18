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
	print conn
	#cur=conn.cursor()
	cur=conn.cursor()
	cur.execute('select * from '+table)
	columns=cur.description
	data=cur.fetchall()
	cur.close()
	conn.close()
	return [col[0] for col in columns],data