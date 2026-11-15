from flask import Flask, jsonify, request
import os, time, psycopg2
from psycopg2.extras import RealDictCursor
app=Flask(__name__)
def connect():
 return psycopg2.connect(host=os.getenv("DB_HOST","employee-postgres"), dbname=os.getenv("DB_NAME","employees"), user=os.getenv("DB_USER","appuser"), password=os.getenv("DB_PASSWORD","demo-password-change-me"))
def init_db():
 for _ in range(30):
  try:
   with connect() as c, c.cursor() as cur:
    cur.execute("CREATE TABLE IF NOT EXISTS employees (id SERIAL PRIMARY KEY,name TEXT NOT NULL,department TEXT NOT NULL,email TEXT UNIQUE NOT NULL)")
    c.commit()
   return
  except Exception: time.sleep(2)
 raise RuntimeError("Database did not become available")
@app.get("/health")
def health(): return jsonify(status="ok")
@app.get("/ready")
def ready():
 try:
  with connect() as c: c.cursor().execute("SELECT 1")
  return jsonify(status="ready")
 except Exception as e: return jsonify(error=str(e)),503
@app.get("/api/employees")
def get_employees():
 with connect() as c, c.cursor(cursor_factory=RealDictCursor) as cur:
  cur.execute("SELECT id,name,department,email FROM employees ORDER BY id")
  return jsonify(cur.fetchall())
@app.post("/api/employees")
def add_employee():
 d=request.get_json(force=True)
 with connect() as c, c.cursor(cursor_factory=RealDictCursor) as cur:
  cur.execute("INSERT INTO employees(name,department,email) VALUES (%s,%s,%s) RETURNING id,name,department,email",(d["name"],d["department"],d["email"]))
  row=cur.fetchone(); c.commit(); return jsonify(row),201
@app.get("/api/demo-load")
def demo_load():
 end=time.time()+min(max(int(request.args.get("seconds","2")),1),10); x=0
 while time.time()<end: x=(x+1)%1000003
 return jsonify(message="CPU demo completed",iterations=x)
if __name__=="__main__": init_db(); app.run(host="0.0.0.0",port=5000)
