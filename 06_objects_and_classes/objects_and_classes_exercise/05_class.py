class Class:
    __student__count = 0

    def __init__(self, name):
        self.name = name
        self.students = []
        self.grades = []

    def add_student(self, name: str, grade: float):
        if self.__student__count < 22:
            self.students.append(name)
            self.grades.append(grade)
            self.__student__count += 1

    def get_average_grade(self):
        result = sum([float(el) for el in self.grades]) / self.__student__count
        return result

    def __repr__(self):
        return f"The students in {self.name}: {', '.join(self.students)}. Average grade: {self.get_average_grade():.2f}"


# a_class = Class("11B")
# a_class.add_student("Peter", 4.80)
# a_class.add_student("George", 6.00)
# a_class.add_student("Amy", 3.50)
# print(a_class)


'''
TASK:
Create a class Class. The __init__ method should receive the name of the class. It should also have 2 lists 
(students and grades). Create a class attribute __students_count equal to 22. The class should also have 3 additional methods:
add_student(name, grade) - if there is space in the class, add the student and the grade in the two lists
get_average_grade() - returns the average of all existing grades formatted to the second decimal point (as a number)
__repr__ - returns the string (single line): "The students in {class_name}: {students}.
Average grade: {get_average_grade()}". The students must be seperated by ", "
'''