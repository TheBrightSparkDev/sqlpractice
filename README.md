In order to run queries against a postgres database in github you need to do the following commands into the terminal

set_pg - sets postgres
psql -d chinook

chinook being the database name of course 

/q quits 

this system uses the following requirements

psycopg2==2.9.3
SQLAlchemy==1.4.37

psycopg2 is the system that allows you to communicate in a python file to SQL using cursor.execute
SQLAlchemy allows you to do it easier using layers of abstraction 
SQLAlchemy also requires you to use the command set_pg

sql-orm sucks
