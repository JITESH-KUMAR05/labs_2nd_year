ChairC = float(input("Enter the cost of one chair: "))
TableC = float(input("Enter the cost of one table: "))
LabourC = float(input("Enter the cost of Labour per hour: "))
ChairNo = int(input("Enter the no of chairs : "))
TableNo = int(input("Enter the no of tables : "))
HourW = int(input("Enter no of hours worked: "))
TotalCost = (ChairC * ChairNo) + (TableC * TableNo) + (LabourC*HourW)

print("Total cost of setting the hotel is: ", TotalCost)
