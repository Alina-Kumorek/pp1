# The student has a name, surname, id (album number) and a field of study.
# All students study at the same university (UEK Kraków). Create a class describing a student.
# Student id should be assigned automatically as a sequential natural number starting from 100000.
# For this purpose, create a class attribute to store the last student’s ID number.
# When creating a new student (object), in the __ininit__ method, increase the value of this class attribute
# by one and then use it as the initial value of student’s ID. Then write a program that creates 3 different
# # students and displays their personal data in the format as below. Use the __str__ method.

#     Anna MAJ (100001), Applied Informatics, UEK Kraków

class Student():

    university = "UEK Kraków"
    last_ID = 100000

    def __init__(self, name, surname, field_of_study):
        self.name = name
        self.surname = surname
        self.field_of_study = field_of_study

        Student.last_ID += 1
        self.id = Student.last_ID
    
    def __str__(self):
        x = self.name + " " + self.surname.upper() + " (" + str(self.id) + "), " + self.field_of_study + ", " + Student.university
        return x

student1 = Student("Anna", "Maj", "Applied Informatics")
print(student1)
student2 = Student("Jan", "Nowak", "Accounting")
print(student2)
student3 = Student("Małgorzata", "Kowalska", "Economics")
print(student3)