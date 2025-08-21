class hospital:
    def __init__(self, name : str, location : str):
        self.name = name
        self.location = location
        self.departments = []
    def add_department(self, department_name: str):
        self.departments.append(department_name)
     