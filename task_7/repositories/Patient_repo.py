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
    def update(self, patient : patient):
        self.cur.execute(
            "UPDATE patients SET pnt_name = %s, pnt_age = %s, pnt_phone = %s, pnt_medical_record = %s, dep_id = %s WHERE pnt_id = %s;",
            (patient.name, patient.age, patient.phone, patient.medical_record, patient.dep_id, patient.pnt_id)
        )
        self.conn.commit()
    