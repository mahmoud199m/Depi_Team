from domain.Hospital import hospital
class hospital_repo:
    def __init__(self, conn):
        self.conn = conn
        self.cur = conn.cursor()
    def create(self, hospital : hospital):
        self.cur.execute(
            "INSERT INTO hospitals (hos_name, hos_location) VALUES (%s,%s) RETURNING hos_id;",
            (hospital.name, hospital.location)
        )
        self.conn.commit()

    def update(self, hospital : hospital):
        self.cur.execute(
            "UPDATE hospitals SET hos_name = %s, hos_location = %s WHERE hos_id = %s;",
            (hospital.name, hospital.location, hospital.hos_id)
        )
        self.conn.commit()
     