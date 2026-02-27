class employee:
    def __init__(self):
        print("Started executing attributes/data")
        self.id = 456
        self.salary = 70000
        self.designation = 'SDE'
        print("Attributes/data have been initiated")
    
    def travel(self, destination):
        print("This travel method was called manually")
        print(f"Employee is travelling to {destination}")


# create an object/instance of the class
akhilesh = employee()
print(akhilesh.salary)

# printing the attributes
#akhilesh.travel("Hyderabad")

print(type(akhilesh))