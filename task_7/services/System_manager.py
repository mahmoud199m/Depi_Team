from domain.Department import department
from domain.Hospital import hospital
from domain.Staff import staff
from domain.Patient import patient
from repositories.Department_repo import department_repo
from repositories.Hospital_repo import hospital_repo
from repositories.Staff_repo import staff_repo
from repositories.Patient_repo import patient_repo
class system_manager:
    def __init__(self, department_repo,hospital_repo, staff_repo, patient_repo):
        self.department_repo = department_repo
        self.hospital_repo = hospital_repo
        self.staff_repo = staff_repo
        self.patient_repo = patient_repo
    def add_department(self, department : department):
        self.department_repo.create(department)
    def add_hospital(self, hospital : hospital):
        self.hospital_repo.create(hospital)
    def add_staff(self, staff : staff):
        self.staff_repo.create(staff)
    def add_patient(self, patient : patient):
        self.patient_repo.create(patient)
    def update_hospital(self, hospital : hospital):
        self.hospital_repo.update(hospital)
    def update_department(self, department : department):
        self.department_repo.update(department)
    def update_staff(self, staff : staff):
        self.staff_repo.update(staff)
    def update_patient(self, patient : patient):
        self.patient_repo.update(patient)
    