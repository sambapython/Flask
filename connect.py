import psycopg2 as pg
def db_connect(username="postgres",password="root",host="localhost",database="flask",port=5433):
	try:
		conn = pg.connect(dbname=database,user=username, host=host, password=password,port=port)
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
def set_data_client(data):
	conn=db_connect()
	cur=conn.cursor()
	cur.execute("insert into client() ")
def set_data(table,data):
	try:
		vals=dict(zip(data.keys(),[i[0] for i in data.listvalues()]))
		cols=[i for i in data]
		cols.insert(0,'id')
		s=""
		for i in cols:
			s=s+"%("+i+")s,"
		s=s.rstrip(',')
		conn=db_connect()
		cur=conn.cursor()
		cur.execute('select id from '+table)
		max_id=max([i[0] for i in cur.fetchall()])
		vals.update({'id':int(max_id)+1})
		s1="INSERT INTO "+table+'('+','.join(cols)+") VALUES ("+s+")"
		cur.execute(s1, vals)
		conn.commit()
		cur.close()
		conn.close()
		return 1
	except Exception as err:
		return err

	
