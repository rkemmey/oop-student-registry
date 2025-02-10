class Student:
    def __init__(self, name, age=13, grade="12th"):
        self._name = name
        self._age = age
        self._grade = grade

    def __str__(self):
        return f'Student 1: Name: {self._name}, Age: {self._age}, Grade: {self._grade}'
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and new_name.isalnum():
            if len(new_name) > 3 and new_name.istitle():
                self._name = new_name
        else:
            print("""Name must be longer than three letters, 
                  not contain any special charcters, and the first letter must be capitalized.""")
            
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, new_age):
        if isinstance(new_age, int):
            if new_age > 11 and new_age < 18:
                self._age = new_age
        else:
            print("Age must be between 11 and 18")

    @property
    def grade(self):
        return self._grade
    
    @grade.setter
    def grade(self, new_grade):
        valid_grades = ["9th", "10th", "11th", "12th"]
        if new_grade in valid_grades:
            self._grade = new_grade
        else:
            print("Grade must fall within falls within 9th - 12th grade and contain 'th'.")
    
    def study(self, subject):
        print(f'{self._name} is studying {subject}')