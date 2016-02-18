import psycopg2 as pg
def db_connect(username="postgres",password="root",host="localhost",database="flask"):
	try:
		conn = pg.connect(dbname=database,user=username, host=host, password=password)
		cur=conn.cursor()
		return cur
	except Exception as err:
		return err