import sqlalchemy as sa

engine = sa.create_engine("mysql+pymysql://user:password@172.19.0.1:3306/db")

with engine.begin() as conn:
    qry = """
    SELECT * FROM circuits
    """

    res = conn.execute(sa.text(qry)).all()

    print(res)
