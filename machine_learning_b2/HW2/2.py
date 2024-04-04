from tabulate import tabulate

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def getName(self):
        return self.name
    def getAge(self):
        return self.age
    def setName(self, name):
        self.name = name
    def setAge(self, age):
        self.age = age
        
    def __str__(self):
        return f"{self.getName}, {self.getAge} years old"

class Student(Person):
    def __init__(self, name, age, program, year , fee):
        super().__init__(name, age)
        self.program = program
        self.year = year
        self.fee = fee
    
    def getProgram(self):
        return self.program
    def getYear(self):
        return self.year
    def getFee(self):
        return self.fee
    def setProgram(self, program):
        self.program = program
    def setYear(self, year):
        self.year = year
    def setFee(self, fee):
        self.fee = fee

    def __str__(self):
        return f"Student: {super().__str__()}, Program: {self.getProgram}, Year: {self.getYear}, Fee: {self.getFee}"

class Staff(Person):
    def __init__(self, name, age, school, pay):
        super().__init__(name, age)
        self.school = school
        self.pay = pay
        
    def getSchool(self):
        return self.school
    def getPay(self):
        return self.pay
    def setSchool(self, school):
        self.school = school
    def setPay(self, pay):
        self.pay = pay
        

    def __str__(self):
        return f"Staff: {super().__str__()}, School: {self.getSchool}, Pay: {self.getPay}"

def add_student(students):
    name = input("Nhập tên: ")
    age = input("Nhập tuổi: ")
    program = input("Nhập chương trình học: ")
    year = input("Nhập năm sinh: ")
    fee = input("Nhập học phí: ")
    student = Student(name, age, program, year, fee)
    students.append(student)
    print("Student đã được thêm vào.")

def add_staff(staffs):
    name = input("Nhập tên: ")
    age = input("Nhập tuổi: ")
    school = input("Nhập trường: ")
    pay = input("Nhập lương: ")
    staff = Staff(name, age, school, pay)
    staffs.append(staff)
    print("Staff đã được thêm vào.")

def search_student(students):
    search_name = input("Nhập tên cần tìm kiếm: ")
    results = [student for student in students if student.name.lower() == search_name.lower()]

    if results:
        table = [["Student", "Name", "Age", "Program", "Year", "Fee"]]
        for student in results:
            table.append(["", student.name, student.age, student.program, student.year, student.fee])
        print(tabulate(table, headers="firstrow", tablefmt="pretty"))
    else:
        print("Không tìm thấy Student có tên đó.")

def main_menu():
    menu = """
    1. Thêm sinh viên
    2. Thêm nhân viên
    3. Tìm kiếm sinh viên
    4. Thoát
    """
    max_width = max(len(line) for line in menu.split("\n"))
    menu_lines = [f"{line:{max_width}}".replace(" ", "　") for line in menu.split("\n") if line.strip()]

    print(tabulate([menu_lines], tablefmt="fancy_grid", colalign=("center",)))

if __name__ == "__main__":
    students = []
    staffs = []

    while True:
        main_menu()
        choice = input("Nhập lựa chọn của bạn (1, 2, 3 hoặc 4): ")

        if choice == '1':
            add_student(students)

        elif choice == '2':
            add_staff(staffs)

        elif choice == '3':
            search_student(students)

        elif choice == '4':
            print("Chương trình đã thoát.")
            break

        else:
            print("Lựa chọn không hợp lệ. Vui lòng nhập lại.")
