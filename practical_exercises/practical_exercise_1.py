class Person:
    def __init__(self, name, age, email=None, password=None):
        self._name = name
        self._age = age

        # Task 6
        self._email = email
        self.__password = password

    def __str__(self):
        return f"{self._name} {self._age} years"
    
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
        
    # Task 6
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, new_email):
        # put email validation code here (TIP: regular expressions)
        self.email = new_email

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, new_password):
        if len(new_password) < 8:
            raise ValueError("Password needs to be at least 8 characters")

        self.__password = new_password


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

    def __str__(self):
        return f"Employee ID: {self.__employee_id}; {super().__str__()}"
    
    @classmethod
    def from_string(cls, string):
        parts = string.split(",")

        if len(parts) < 3:
            raise ValueError("The string has to contain the name, age and employee_id")
        
        parts[1] = int(parts[1])
        parts[2] = int(parts[2])

        return Employee(name=parts[0], age=parts[1], employee_id=parts[2])


class Customer(Person):
    def __init__(self, name, age, customer_id):
        super().__init__(name, age)
        self.__customer_id = customer_id
    
    def __str__(self):
        return f"Cust #{self.__customer_id}; {super().__str__()}"
    

# Task 5
def print_info(person):
    print(person.__str__())