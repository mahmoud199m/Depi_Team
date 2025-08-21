from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
from PyQt5.QtCore import QTimer
import sys
import time
from domain.Department import department
from domain.Hospital import hospital
from domain.Staff import staff
from domain.Patient import patient
from services.System_manager import system_manager

class main_app(QMainWindow):
    def __init__(self,manger : system_manager):
        super(main_app, self).__init__()
        uic.loadUi('C:/Users/6y6yy/Desktop/Depi_Team/task_7/ui/hospital.ui', self)
        self.manger = manger
        self.InitUI()
        self.handle_btn()
    
    def InitUI(self):
        self.setWindowTitle("Hospital Management System")
        self.statusBar().showMessage("Welcome to the Hospital Management System")
    
    def handle_btn(self):
        self.hos_add_btn.clicked.connect(self.add_hos_info)
        self.hos_upd_btn.clicked.connect(self.update_hos_info)
        self.dep_add_btn.clicked.connect(self.add_dep_info)
        self.dep_upd_btn.clicked.connect(self.update_dep_info)
        self.stf_add_btn.clicked.connect(self.add_stf_info)
        self.stf_upd_btn.clicked.connect(self.update_stf_info)
        self.ptn_add_btn.clicked.connect(self.add_ptn_info)
        self.ptn_upd_btn.clicked.connect(self.update_ptn_info)
    
    def add_hos_info(self):
        hos_name = self.hos_name_text.text()
        hos_location = self.hos_loc_text.text()
        if hos_name and hos_location:
            hos = hospital(hos_name, hos_location)
            self.manger.add_hospital(hos)
            self.hos_name_text.setText("")
            self.hos_loc_text.setText("")
            self.statusBar().showMessage("Hospital added successfully")
        else:
            self.statusBar().showMessage("Please fill all fields for Hospital")
    
    
    def update_hos_info(self):
        hos_name = self.hos_name_text.text()
        hos_location = self.hos_loc_text.text()
        hos_id = self.hos_id_text.text()
        if hos_name and hos_location and hos_id:
            hos = hospital(hos_name, hos_location, int(hos_id))
            self.manger.update_hospital(hos)
            self.hos_name_text.setText("")
            self.hos_loc_text.setText("")
            self.hos_id_text.setText("")
            self.statusBar().showMessage("Hospital updated successfully")
        else:
            self.statusBar().showMessage("Please fill all fields for Hospital")
    def add_dep_info(self):
        deb_name = self.dep_name_text.text()
        hos_id = self.dep_hos_id_text.text()
        if deb_name and hos_id:
            dep = department(deb_name, hos_id)
            self.manger.add_department(dep)
            self.dep_name_text.setText("")
            self.dep_hos_id_text.setText("")
            self.statusBar().showMessage("Department added successfully")
        else:
            self.statusBar().showMessage("Please fill all fields for Department")
    def update_dep_info(self):
        dep_name = self.dep_name_text.text()
        hos_id = self.dep_hos_id_text.text()
        dep_id = self.dep_id_text.text()
        if dep_name and hos_id and dep_id:
            dep = department(dep_name, hos_id, int(dep_id))
            self.manger.update_department(dep)
            self.dep_name_text.setText("")
            self.dep_hos_id_text.setText("")
            self.dep_id_text.setText("")
            self.statusBar().showMessage("Department updated successfully")
        else:
            self.statusBar().showMessage("Please fill all fields for Department")
    def add_stf_info(self):
        stf_name = self.stf_name_text.text()
        stf_age = self.stf_age_text.text()
        stf_phone = self.stf_phone_text.text()
        stf_position = self.stf_pos_text.text()
        stf_address = self.stf_ads_text.text()
        dep_id = self.stf_dep_id_text.text()
        if stf_name and stf_age and stf_phone and stf_position and stf_address and dep_id:
            stf = staff(stf_name, stf_age, stf_phone, dep_id ,stf_position, stf_address)
            self.manger.add_staff(stf)
            self.stf_name_text.setText("")
            self.stf_age_text.setText("")
            self.stf_phone_text.setText("")
            self.stf_pos_text.setText("")
            self.stf_ads_text.setText("")
            self.stf_dep_id_text.setText("")
            self.statusBar().showMessage("Staff added successfully")
        else:
            self.statusBar().showMessage("Please fill all fields for Staff")
    def update_stf_info(self):
        stf_name = self.stf_name_text.text()
        stf_age = self.stf_age_text.text()
        stf_phone = self.stf_phone_text.text()
        stf_position = self.stf_pos_text.text()
        stf_address = self.stf_ads_text.text()
        dep_id = self.stf_dep_id_text.text()
        stf_id = self.stf_id_text.text()
        if stf_name and stf_age and stf_phone and stf_position and stf_address and dep_id and stf_id:
            stf = staff(stf_name, stf_age, stf_phone, dep_id, stf_position, stf_address, int(stf_id))
            self.manger.update_staff(stf)
            self.stf_name_text.setText("")
            self.stf_age_text.setText("")
            self.stf_phone_text.setText("")
            self.stf_pos_text.setText("")
            self.stf_ads_text.setText("")
            self.stf_dep_id_text.setText("")
            self.stf_id_text.setText("")
            self.statusBar().showMessage("Staff updated successfully")
        else:
            self.statusBar().showMessage("Please fill all fields for Staff")
    def add_ptn_info(self):
        ptn_name = self.ptn_name_text.text()
        ptn_age = self.ptn_age_text.text()
        ptn_phone = self.ptn_phone_text.text()
        ptn_medical_record = self.ptn_med_text.text()
        dep_id = self.ptn_dep_id_text.text()
        if ptn_name and ptn_age and ptn_phone and ptn_medical_record and dep_id:
            ptn = patient(ptn_name, ptn_age, ptn_phone, dep_id, ptn_medical_record)
            self.manger.add_patient(ptn)
            self.ptn_name_text.setText("")
            self.ptn_age_text.setText("")
            self.ptn_phone_text.setText("")
            self.ptn_med_text.setText("")
            self.ptn_dep_id_text.setText("")
            self.statusBar().showMessage("Patient added successfully")
        else:
            self.statusBar().showMessage("Please fill all fields for Patient")
    def update_ptn_info(self):
        ptn_name = self.ptn_name_text.text()
        ptn_age = self.ptn_age_text.text()
        ptn_phone = self.ptn_phone_text.text()
        ptn_medical_record = self.ptn_med_text.text()
        dep_id = self.ptn_dep_id_text.text()
        ptn_id = self.ptn_id_text.text()
        if ptn_name and ptn_age and ptn_phone and ptn_medical_record and dep_id and ptn_id:
            ptn = patient(ptn_name, ptn_age, ptn_phone, dep_id, ptn_medical_record, int(ptn_id))
            self.manger.update_patient(ptn)
            self.ptn_name_text.setText("")
            self.ptn_age_text.setText("")
            self.ptn_phone_text.setText("")
            self.ptn_med_text.setText("")
            self.ptn_dep_id_text.setText("")
            self.ptn_id_text.setText("")
            self.statusBar().showMessage("Patient updated successfully")
        else:
            self.statusBar().showMessage("Please fill all fields for Patient")
            

        

