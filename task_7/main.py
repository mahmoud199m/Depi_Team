import psycopg2
from config import get_db_config
from repositories.Department_repo import department_repo
from repositories.Hospital_repo import hospital_repo
from repositories.Staff_repo import staff_repo
from repositories.Patient_repo import patient_repo
from services.System_manager import system_manager
from ui.Main_app import main_app
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys



if __name__ == '__main__':
    conn = psycopg2.connect(**get_db_config())
    dep_repo = department_repo(conn)
    hos_repo = hospital_repo(conn)
    stf_repo = staff_repo(conn)
    pt_repo = patient_repo(conn)
    manager = system_manager(dep_repo, hos_repo, stf_repo, pt_repo)

    app = QApplication(sys.argv)
    window = main_app(manager)
    window.show()
    sys.exit(app.exec_())