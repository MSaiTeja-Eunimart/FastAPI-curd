from sqlalchemy import create_engine,MetaData
meta = MetaData()
engine = create_engine("mysql+pymysql://root:admin@localhost/eunimart")

conn = engine.connect()