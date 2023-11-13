from sqlalchemy import create_engine, text



engine = create_engine("sqlite+pysqlite:////users.db", echo=True)

with engine.connect() as conn:
  result = conn.execute(text("select * from users"))
  print(result.all())