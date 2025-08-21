from domain.Patient import patient
class patient_repo:
    def __init__(self, conn):
        self.conn = conn
        self.cur = conn.cursor()

    def create(self, patient : patient):
        self.cur.execute(
            "INSERT INTO patients (pnt_name, pnt_age, pnt_phone, pnt_medical_record, dep_id) VALUES (%s,%s,%s,%s,%s) RETURNING pnt_id;",
            (patient.name, patient.age, patient.phone, patient.medical_record, patient.dep_id)
        )
        self.conn.commit() 