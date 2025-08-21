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
     