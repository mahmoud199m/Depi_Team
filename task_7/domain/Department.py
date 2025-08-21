class department:
    def __init__(self, name: str,hos_id: int = 0, dep_id: int = 0):
        self.name = name
        self.staffs = []
        self.patients = []
        self.hos_id = hos_id
        self.dep_id = dep_id
    def add_staff(self, staff_name: str):
        self.staffs.append(staff_name)
    def add_patient(self, patient_name: str):
        self.patients.append(patient_name)
    