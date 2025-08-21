from domain.Person import person
class patient(person):
    def __init__(self, name: str, age: int, phone: str, dep_id: int = 0, medical_record: str = ""):
        super().__init__(name, age, phone, dep_id)
        self.medical_record = medical_record
    def view_record(self):
        return self.medical_record
