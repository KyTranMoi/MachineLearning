from flask import Flask, render_template, request ,redirect, url_for
from tabulate import tabulate
# from flask_ngrok import run_with_ngrok
app = Flask(__name__)
# run_with_ngrok(app)
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
        return f"{self.name}, {self.age} years old"

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
        return f"Student: {super().__str__()}, Program: {self.program}, Year: {self.year}, Fee: {self.fee}"

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
        return f"Staff: {super().__str__()}, School: {self.school}, Pay: {self.pay}"
students = []
staffs = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add_student', methods=['POST'])
def add_student_route():
    name = request.form['name']
    age = request.form['age']
    program = request.form['program']
    year = request.form['year']
    fee = request.form['fee']
    student = Student(name, age, program, year, fee)
    students.append(student)
    print("Student đã được thêm vào.")
    return redirect(url_for('home'))

@app.route('/add_staff', methods=['POST'])
def add_staff_route():
    name = request.form['name']
    age = request.form['age']
    school = request.form['school']
    pay = request.form['pay']
    staff = Staff(name, age, school, pay)
    staffs.append(staff)
    print("Staff đã được thêm vào.")

    return redirect(url_for('home'))

@app.route('/search_student', methods=['POST'])
def search_student_route():
    search_name = request.form['search_name']
    results = [student for student in students if search_name.lower() in student.getName().lower()]

    if results != []:
        table = [["Student", "Name", "Age", "Program", "Year", "Fee"]]
        for student in results:
            print(student)
            table.append(["", student.getName(), student.getAge(), student.getProgram(), student.getYear(), student.getFee()])

        # Thêm màu sắc cho bảng HTML
        table_html = tabulate(table, headers="firstrow", tablefmt="html")
        styled_table_html = f'<table style="border-collapse: collapse; width: 100%;">{table_html}</table>'

        # Trả về HTML với CSS được thêm vào trực tiếp
        return f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Kết quả tìm kiếm</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background-color: #f4f4f4;
                    color: #333;
                }}
                div {{
                    max-width: 800px;
                    margin: 20px auto;
                    padding: 20px;
                    background-color: #fff;
                    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                }}
                h2 {{
                    color: #007bff;
                }}
                table {{
                    width: 100%;
                    border-collapse: collapse;
                    margin-top: 20px;
                }}
                th, td {{
                    border: 1px solid #ddd;
                    padding: 8px;
                    text-align: left;m ,k,,,,,,,,,,,,,,,
                }}
                th {{
                    background-color: #007bff;
                    color: #fff;
                }}
            </style>
        </head>
        <body>
            <div>
                <h2>Kết quả tìm kiếm</h2>
                {styled_table_html}
            </div>
        </body>
        </html>
        """
    else:
        return "Không tìm thấy Student có tên đó."

if __name__ == '__main__':
    # app.run(debug=True)
    app.run()
