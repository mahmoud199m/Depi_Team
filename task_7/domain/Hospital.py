class hospital:
    def __init__(self, name : str, location : str, hos_id: int = None):
        self.name = name
        self.hos_id = hos_id
        self.location = location
        self.departments = []
    def add_department(self, department_name: str):
        self.departments.append(department_name)
     