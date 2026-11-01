import os
import socket
from flask import Flask, jsonify, request
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)

def db():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "employee-postgres"),
        port=int(os.getenv("DB_PORT", "5432")),
        dbname=os.getenv("POSTGRES_DB", "employees"),
        user=os.getenv("POSTGRES_USER", "employee_app"),
        password=os.getenv("POSTGRES_PASSWORD", "change-me-lab-only"),
        connect_timeout=3,
    )

def init_db():
    with db() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS employees (
                    id SERIAL PRIMARY KEY,
                    name TEXT NOT NULL,
                    department TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL
                )
            """)
            cur.execute("""
                INSERT INTO employees (name, department, email)
                VALUES ('Asha Kumar', 'Engineering', 'asha@example.test')
                ON CONFLICT (email) DO NOTHING
            """)

@app.get("/")
def home():
    return jsonify(service="employee-api", message="Employee API is running",
                   pod=socket.gethostname())

@app.get("/health/live")
def live():
    return jsonify(status="alive"), 200

@app.get("/health/ready")
def ready():
    try:
        with db() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT 1")
        return jsonify(status="ready"), 200
    except Exception as exc:
        return jsonify(status="not-ready", error=str(exc)), 503

@app.get("/employees")
@app.get("/api/employees")
def employees():
    try:
        init_db()
        with db() as conn:
            with conn.cursor(cursor_factory=RealDictCursor) as cur:
                cur.execute("SELECT id, name, department, email FROM employees ORDER BY id")
                return jsonify(cur.fetchall())
    except Exception as exc:
        return jsonify(error=str(exc)), 503

@app.post("/employees")
@app.post("/api/employees")
def create_employee():
    body = request.get_json(silent=True) or {}
    required = ("name", "department", "email")
    if not all(body.get(k) for k in required):
        return jsonify(error="Provide name, department and email"), 400
    try:
        with db() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "INSERT INTO employees(name, department, email) VALUES (%s,%s,%s) RETURNING id",
                    (body["name"], body["department"], body["email"]),
                )
                employee_id = cur.fetchone()[0]
        return jsonify(id=employee_id, **{k: body[k] for k in required}), 201
    except Exception as exc:
        return jsonify(error=str(exc)), 409

if __name__ == "__main__":
    # Initialise table when DB is ready; readiness probe handles temporary DB startup delay.
    try:
        init_db()
    except Exception:
        pass
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "5000")))
