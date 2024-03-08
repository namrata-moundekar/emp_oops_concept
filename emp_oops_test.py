"""Employee CLass"""
class Employee():
    """empty list for employee details"""
    emp_list= list()


    def __init__(self, emp_id, name,  department, title):
        self.name = name
        self.emp_id = emp_id
        self.department = department
        self.title = title

    """employee insert into list"""
    def add_employee(self):
        Employee.emp_list.append(self)

    """display employee list"""
    def get_employee(self):
        return Employee.emp_list

    """display department list"""
    def display_dept(self):
        return Employee.emp_list

    """remove employee using id from emp list"""
    def remove_emp(self, emp_id):
        for emp in Employee.emp_list:
            if emp.get_id() == emp_id:
                Employee.emp_list.remove(emp)
                return True
        return False


    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_id(self, emp_id):
        self.emp_id = emp_id

    def get_id(self):
        return self.emp_id

    def set_department (self, department):
        self.department = department

    def get_department(self):
        return self.department

    def set_title (self, title):
        self.title = title

    def get_title(self):
        return self.title

    def __str__(self):
        return "%d %s"%(self.emp_id, self.name)

"""Department Class inheritance"""
class Department(Employee):
    def __init__(self, emp_id, name, department, title):
        Employee.__init__(self, emp_id, name, department, title)

    def __str__(self):
        return "%d %s %s %s "%(self.emp_id, self.name, self.department, self.title)



"""choise for all options created"""
choice=1
employee = Employee(0,"","","")

while choice >=1 and choice <=4:
    print("1. Add New Employee\n2. Display ALl Employee\n3. Remove Employee\n4. Display Department")
    choice=int(input("Enter your choice: "))
    if choice==1:
        emp_id =int(input("Enter Employee ID"))
        name = input("Enter Employee NAme")
        department = input("Enter Department name")
        title = input("Enter Employee Title")
        emp = Employee(emp_id,name,department,title)
        emp.add_employee()

    elif choice==2:
        print("\n")
        for emp in employee.get_employee():
            print(emp)

    elif choice==3:
        emp_id = int(input("Enter Employee Id: "))
        emp = employee.remove_emp(emp_id)

        if emp == False:
            print("\nSorry...! Employee not found for ID: ",emp_id)
        else:
            print("Successfully removed for Id: ",emp_id)

    elif choice==4:
        for emp in employee.display_dept():
            print(emp.department)

    else:
        print("Expected Options")


