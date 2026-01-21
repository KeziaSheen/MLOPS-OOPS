# Initiate a class
class employee:
    # special method/magic method/dunder method
    def __init__(self):
        print("Started executing attributes\data")
        self.id = 101
        self.salary = 50000
        self.desg = "SDE"
        print("attributes\data have been initiated")

    def travel(self, destination):
        print("This travel function is called manually")
        print(f"Employee is travelling to {destination}")

# create an obj/instance of clas
sam = employee()

#print(sam.id)
sam.travel("Kerala")