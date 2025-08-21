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
    
    def update(self, staff : staff):
        self.cur.execute(
            "UPDATE staffs SET stf_name = %s, stf_age = %s, stf_phone = %s, stf_position = %s, stf_address = %s, dep_id = %s WHERE stf_id = %s;",
            (staff.name, staff.age, staff.phone, staff.position, staff.address, staff.dep_id, staff.stf_id)
        )
        self.conn.commit()