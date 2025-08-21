from domain.Department import department
import psycopg2

class department_repo:
    def __init__(self, conn):
        self.conn = conn
        self.cur = conn.cursor()

    def create(self, department : department):
        self.cur.execute(
            "INSERT INTO departments (dep_name, hos_id) VALUES (%s,%s) RETURNING dep_id;",
            (department.name, department.hos_id)
        )
        self.conn.commit()