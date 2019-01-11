# -*- coding: utf-8 -*-

import sqlalchemy as db

engine = db.create_engine('sqlite:///photodb.sqlite')  # Create test.sqlite automatically
connection = engine.connect()
metadata = db.MetaData()

photos = db.Table('photos', metadata,
               db.Column('Id', db.Integer(), autoincrement=True),
               db.Column('file_id', db.String(255), nullable=False)
               )

metadata.create_all(engine)  # Creates the table

""""
engine = db.create_engine('sqlite:///foo.db')
connection = engine.connect()
metadata = db.MetaData()
photos = db.Table('photos', metadata, autoload=True, autoload_with=engine)

# Equivalent to 'SELECT * FROM photos'
query = db.select([photos])

ResultProxy = connection.execute(query)
ResultSet = ResultProxy.fetchall()  # Result of query

# SQL :
# SELECT * FROM photos
# WHERE id = 1
# SQLAlchemy :
db.select([photos]).where(photos.columns.id == '1')

where

SQL :
SELECT * FROM census 
WHERE sex = F
SQLAlchemy :
db.select([census]).where(census.columns.sex == 'F')

in

SQL :
SELECT state, sex
FROM census
WHERE state IN (Texas, New York)
SQLAlchemy :
db.select([census.columns.state, census.columns.sex]).where(census.columns.state.in_(['Texas', 'New York']))

and, or, not

SQL :
SELECT * FROM census
WHERE state = 'California' AND NOT sex = 'M'
SQLAlchemy :
db.select([census]).where(db.and_(census.columns.state == 'California', census.columns.sex != 'M'))

order by

SQL :
SELECT * FROM census
ORDER BY State DESC, pop2000
SQLAlchemy :
db.select([census]).order_by(db.desc(census.columns.state), census.columns.pop2000)

functions

SQL :
SELECT SUM(pop2008)
FROM census
SQLAlchemy :
db.select([db.func.sum(census.columns.pop2008)])
other functions include avg, count, min, max…

group by

SQL :
SELECT SUM(pop2008) as pop2008, sex
FROM census
SQLAlchemy :
db.select([db.func.sum(census.columns.pop2008).label('pop2008'), census.columns.sex]).group_by(census.columns.sex)

distinct

SQL :
SELECT DISTINCT state
FROM census
SQLAlchemy :
db.select([census.columns.state.distinct()])

Creating and Inserting Data into Tables
By passing the database which is not present, to the engine then sqlalchemy automatically creates a new database.


import sqlalchemy as db
import pandas as pd
Creating Database and Table
In [32]:
engine = db.create_engine('sqlite:///test.sqlite') #Create test.sqlite automatically
connection = engine.connect()
metadata = db.MetaData()

emp = db.Table('emp', metadata,
              db.Column('Id', db.Integer()),
              db.Column('name', db.String(255), nullable=False),
              db.Column('salary', db.Float(), default=100.0),
              db.Column('active', db.Boolean(), default=True)
              )

metadata.create_all(engine) #Creates the table
Inserting Data
In [37]:
#Inserting record one by one
query = db.insert(emp).values(Id=1, name='naveen', salary=60000.00, active=True) 
ResultProxy = connection.execute(query)
In [ ]:
#Inserting many records at ones
query = db.insert(emp) 
values_list = [{'Id':'2', 'name':'ram', 'salary':80000, 'active':False},
               {'Id':'3', 'name':'ramesh', 'salary':70000, 'active':True}]
ResultProxy = connection.execute(query,values_list)
In [43]:
results = connection.execute(db.select([emp])).fetchall()
df = pd.DataFrame(results)
df.columns = results[0].keys()
df.head(4)
Out[43]:
Id	name	salary	active
0	1	vinay	60000.0	True
1	1	satvik	60000.0	True
2	1	naveen	60000.0	True
3	2	rahul	80000.0	False

Updating data in Databases
db.update(table_name).values(attribute = new_value).where(condition)

In [7]:
import sqlalchemy as db
import pandas as pd
In [5]:
engine = db.create_engine('sqlite:///test.sqlite')
metadata = db.MetaData()
connection = engine.connect()
emp = db.Table('emp', metadata, autoload=True, autoload_with=engine)
In [8]:
results = connection.execute(db.select([emp])).fetchall()
df = pd.DataFrame(results)
df.columns = results[0].keys()
df.head(4)
Out[8]:
Id	name	salary	active
0	1	vinay	60000.0	True
1	1	satvik	60000.0	True
2	1	naveen	60000.0	True
3	2	rahul	80000.0	False
In [12]:
# Build a statement to update the salary to 100000
query = db.update(emp).values(salary = 100000)
query = query.where(emp.columns.Id == 1)
results = connection.execute(query)
In [13]:
results = connection.execute(db.select([emp])).fetchall()
df = pd.DataFrame(results)
df.columns = results[0].keys()
df.head(4)
Out[13]:
Id	name	salary	active
0	1	vinay	100000.0	True
1	1	satvik	100000.0	True
2	1	naveen	100000.0	True
3	2	rahul	80000.0	False

Delete Table
db.delete(table_name).where(condition)

In [2]:
import sqlalchemy as db
import pandas as pd
In [4]:
engine = db.create_engine('sqlite:///test.sqlite')
metadata = db.MetaData()
connection = engine.connect()
emp = db.Table('emp', metadata, autoload=True, autoload_with=engine)
In [5]:
results = connection.execute(db.select([emp])).fetchall()
df = pd.DataFrame(results)
df.columns = results[0].keys()
df.head(4)
Out[5]:
Id	name	salary	active
0	1	vinay	100000.0	True
1	1	satvik	100000.0	True
2	1	naveen	100000.0	True
3	2	rahul	80000.0	False
In [6]:
# Build a statement to delete where salary < 100000
query = db.delete(emp)
query = query.where(emp.columns.salary < 100000)
results = connection.execute(query)
In [7]:
results = connection.execute(db.select([emp])).fetchall()
df = pd.DataFrame(results)
df.columns = results[0].keys()
df.head(4)
Out[7]:
Id	name	salary	active
0	1	vinay	100000.0	True
1	1	satvik	100000.0	True
2	1	naveen	100000.0	True

Dropping a Table
table_name.drop(engine) #drops a single table
metadata.drop_all(engine) #drops all the tables in the database
"""""
