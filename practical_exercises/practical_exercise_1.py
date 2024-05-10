class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def __str__(self):
        return f"{self.name} {self.age} years"
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, new_age):
        if isinstance(new_age, int):
            if new_age < 0:
                raise ValueError("Age cannot be negative")
            else:
                self._age = new_age
        else:
            raise ValueError("Age has to be an integer")



class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)

        self.__employee_id = employee_id

    @property
    def employee_id(self):
        return self.__employee_id
    
    @employee_id.setter
    def employee_id(self, new_id):
        if isinstance(new_id, int):
            self.__employee_id = new_id
        