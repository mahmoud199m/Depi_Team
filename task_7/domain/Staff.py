from domain.Person import person
class staff(person):
    def __init__(self, name: str, age: int, phone: str, dep_id: int = 0, position: str = "", address: str = ""):
        super().__init__(name, age, phone, dep_id)
        self.position = position
        self.address = address
    def __str__(self):
        return f"Staff Name: {self.name}, Age: {self.age}, Phone: {self.phone}, Department ID: {self.dep_id}, Position: {self.position}, Address: {self.address}"
        