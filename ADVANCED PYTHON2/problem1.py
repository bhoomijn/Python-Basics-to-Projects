
# Program to input student details and format using format function

name = input("Enter name: ")
marks = int(input("Enter marks: "))
phone = int(input("Enter phone number: "))

s = "{} got {} marks and phone number is {}".format(name, marks, phone)
print(s)
