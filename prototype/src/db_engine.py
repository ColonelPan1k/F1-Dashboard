import sqlalchemy as sa

engine = sa.create_engine("mysql+pymysql://user:pw@172.19.0.2:3306/f1db")
