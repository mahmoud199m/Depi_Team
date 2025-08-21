from domain.Staff import staff
class staff_repo:
    def __init__(self, conn):
        self.conn = conn
        self.cur = conn.cursor()

    def create(self, staff : staff):
        self.cur.execute(
            "INSERT INTO staffs (stf_name, stf_age, stf_phone, stf_position, stf_address, dep_id) VALUES (%s,%s,%s,%s,%s,%s) RETURNING stf_id;",
            (staff.name, staff.age, staff.phone, staff.position, staff.address, staff.dep_id)
        )
        self.conn.commit()