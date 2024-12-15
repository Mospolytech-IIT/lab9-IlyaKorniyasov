"""Importing sqlalchemny modules"""
from sqlalchemy import create_engine, Column, Integer, String, Text, ForeignKey
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import inspect

DATABASE_URL = "mssql+pyodbc://@DESKTOP-EK53461\\SQLEXPRESS/korniyasov?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes""" # pylint: disable=all
#DATABASE_URL = """mssql+pyodbc://@127.0.0.1\\SQLEXPR
##ESS/korniyasov?driver=ODBC+Driver+17+for+SQL+Server"""

engine = create_engine(DATABASE_URL)

Base = declarative_base()

class User(Base):
    """User class"""
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(255), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String, nullable=False)

class Post(Base):
    """Post class"""
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    user = relationship("User", backref="posts")

Base.metadata.create_all(engine)

inspector = inspect(engine)
print("Существующие таблицы:", inspector.get_table_names())
