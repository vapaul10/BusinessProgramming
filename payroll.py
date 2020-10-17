"""
Program: payroll.py
and data.txt
Valeri Paul

Print a payroll report. Write a program that inputs a filename from the user
and prints to the terminal a report of the wages paid to the employees for the given period.
The report should be in tabular format with the appropriate header.
Each line should contain an employee’s name, the hours worked, and the wages paid for that period.

Input
   A file in which each line has the form
   
   <last name> <hourly wage> <hours worked>

Output
   A report in tabular format.  Each line has the form

   <last name> <hours worked> <total wages>   
"""

# Take the inputs
fileName = input("Enter the filename -> data.txt:  ")

# Open the input file
inputFile = open(fileName, 'r')

# Read the data and print the report
print("%-15s%6s%15s" % ("Name", "Hours", "Total Pay"))
for line in inputFile:
    dataList = line.split()
    name = dataList[0]
    hours = int(dataList[1])
    payRate = float(dataList[2])
    totalPay = hours * payRate
    print("%-15s%6d%15.2f" % (name, hours, totalPay))
    

print(inputFile)
    
pause = str(input("Click enter to close. \n"))
