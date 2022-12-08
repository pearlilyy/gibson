from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

# Connect to Postgres database
'''
we create a database connection using what SQLAlchemy calls an "engine". 
We give this engine the URI connection string for our Postgres database, which is 'postgresql://postgres@localhost:5432/gibson'.
Under the hood, this engine uses psycopg2 to establish the connection. 
'''
engine = create_engine('postgresql://postgres@localhost:5432/gibson')
'''
we create an SQLAlchemy sessionmaker that gives us the ability to interact with the database via the engine. 
This is similar to the concept of a cursor in the previous exercise. We will demonstrate how to use this shortly.
'''
Session = sessionmaker(bind=engine)
'''
We also create the Base class using an SQLAlchemy utility called declarative_base(). 
Each model (Python class) that we want SQLAlchemy to map to a database table must inherit this Base class. 
We will also demonstrate this shortly.
'''
Base = declarative_base()
