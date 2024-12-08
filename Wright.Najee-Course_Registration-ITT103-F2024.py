# Greet the user
print("Welcome!")

# Variables
admin_username = "Admin01"
admin_password = "Program1234"
admin_choice = ""
deposit_amount = 0
balance = 0

class Course:
    def __init__(self,course_id, course_name, fee):
        self.course_id = course_id
        self.course_name = course_name
        self.fee = fee

    def __str__(self):
        return self.course_id + " - " +  " | Fee: $" + str(self.fee)

class Student:
    def __init__(self, id,name,email):
        self.id = id
        self.name = name
        self.email = email
        self.courses = []
        self.balance = 0

    def enroll(self, course):
        if course in self.courses:
            print("Student " + self.name + " is already enrolled in " + course.name + "." )
        else:
            self.courses.append(course)
            self.balance += course.fee

    def get_total_fee(self):
        return self.balance

    def __str__(self):
        return self.id + " - " + self.name + " | Email: " + self.email + " | Balance: $" + str(self.balance)

# Class for the Registration
class Registry:
    def __init__(self):
        self.students = []
        self.courses = {}

    def add_course(self):
        course_id = input("Enter course ID: ")

        # CHeck to see if there are any duplicates
        if course_id in self.courses:
            print("Error! Course ID " + course_id + " already exists.")
            return

        # Input course name
        course_name = input("Enter course name for course ID " + course_id + ": ")

        # Check to see if fee entered is a digit
        while True:
            course_fee = input("Enter " + course_name +   " | " + course_id + " fee: ")
            if course_fee.isdigit():
                course_fee = float(course_fee)
                break
            else:
                print("Error! You have not entered a valid number.")

        # Dictionary for courses
        self.courses[course_id] = Course(course_id,course_name,course_fee)
        print("Course " + course_name +   ", " + course_id + " with a fee of $" + str(course_fee) + " has been successfully added.")

    def Register(self):
        name = input("Enter student name:")

        # Ensuring ID is only numbers and it is exactly 7 digits long
        while True:
            id = input("Enter student ID (7 digits): ")

            if id.isdigit() and len(id) == 7:
                break
            else:
                print("Error! Please ensure ID contains only numbers and are 7 digits long")

        email = input("Enter student email:")

        course_id= input("Enter Course ID to be registered :")

        if course_id in self.courses:
            course = self.courses[course_id]
        else:
            print("Error! This course does not exist")
            return

           # Check to see if there are duplicates
        for student in self.students:
            if student.id == id:
                print("Error! Student ID " + id + "already exists. Registration was unsuccessful.")
                return

        # Adding students to the registry
        student = Student(id, name, email)
        student.enroll(course)
        self.students.append(student)
        print(name + " has been successfully register to " + course.course_name + " ("+ course_id +")")

    def view_students(self):
        if self.students:
            for student in self.students:
                print(student)
        else:
                print("No students registered. Please register students.")

    def view_courses(self):
        if self.courses:
            for course in self.courses.values():
                print(course)
        else:
            print("No courses are available. Please add courses to continue.")

    def payment(self, id):
        for student in self.students:
            if student.id == id:
                total_fee = student.get_total_fee()
                min_payment = total_fee * 0.4
                print("Total fee: $" + str(total_fee) + "| Minimum fee: $" + str(min_payment))

                # Accept Payments
                payment_amount = input("Enter amount to pay: $")

                # Ensuring payment is a digit
                if payment_amount.isdigit():
                    payment = float(payment_amount)
                    if payment < min_payment:
                        print("Please ensure payment is atleast " + str(min_payment) + ". Try again.")
                    else:
                        student.balance -= payment
                        print("Payment of $" + str(payment) + " received. Outstanding balance: $" + str(student.balance))
                else:
                    print("Invalid Payment. Please try again.")


registry = Registry()

# Prompt user to input their password and validate it
while True:
    print("Please enter username:")
    input_username = input()

    print("Please enter password:")
    input_password = input()

    # Login validation
    if input_username == admin_username and input_password == admin_password:
        break
    else:
        print("Username or Password is incorrect. Please enter correct Username or Password")

# Dashboard
while True:
    print("Please select an option:")
    print("1. Student Registry")
    print("2. Manage Course Listings")
    print("3. Log Out")

    admin_choice = input()

    # Admin's choice for options
    if admin_choice == '1':
        print("Please select option:")
        print("1. Register Student")
        print("2. View Registered Students")
        print("3. Payment Processing")
        print("4. Back to Dashboard")

        admin_choice = input()

        if admin_choice == '1':
            registry.Register()
        elif admin_choice == '2':
            registry.view_students()
        elif admin_choice == '3':
            id = input("Enter Student ID to process payment: ")
            registry.payment(id)
        elif admin_choice == '4':
            continue
        else:
            print("Invalid choice! Please select one of the options to continue.")


    elif admin_choice == '2':
        print("Please select an option:")
        print("1. Add course")
        print("2. View courses available")
        print("3. Back to Dashboard")

        admin_choice = input()

        if admin_choice == '1':
            registry.add_course()
        elif admin_choice == '2':
            registry.view_courses()
        elif admin_choice == '3':
            continue
        else:
            print("Invalid choice! Please select one of the options to continue.")


    elif admin_choice == '3':
        print("Logging out")
        break
    else:
        print("Invalid choice. Please select a valid option.")



# “I CERTIFY THAT I HAVE NOT GIVEN OR RECEIVED ANY UNAUTHORIZED ASSISTANCE ON THIS ASSIGNMENT”. N.Wright