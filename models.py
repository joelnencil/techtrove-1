
from sqlalchemy import create_engine, Column, String,PrimaryKeyConstraint,Integer
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "postgresql://joelnencil:Jojima2003@db:5432/postgres"
engine = create_engine(DATABASE_URL)
Base = declarative_base()

class UserDetails(Base):
    __tablename__ = "users"

    email = Column(String, primary_key=True, index=True)
    password = Column(String)

class Products(Base):
    __tablename__ = "products"
    id = Column(String, primary_key=True, index=True)
    product_name = Column(String)
    product_price = Column(String)

class Cart(Base):
    __tablename__ = "cart"
    order_id = Column(Integer,primary_key=True, index=True,autoincrement=True)
    id = Column(String, primary_key=True, index=True)
    product_name = Column(String)
    product_price = Column(String)
    __table_args__ = (
        PrimaryKeyConstraint('order_id','id'),
    )

class Orders(Base):
    __tablename__ = "orders"
    order_id = Column(Integer,primary_key=True, index=True,autoincrement=True)
    id = Column(String, primary_key=True, index=True)
    product_name = Column(String)
    product_price = Column(String)
    __table_args__ = (
        PrimaryKeyConstraint('order_id','id'),
    )
Base.metadata.create_all(bind=engine)