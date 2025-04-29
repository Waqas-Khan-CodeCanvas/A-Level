
#     # Total: integer
#     def __init__(self, ID):
#         self.ID = ID
#         self.Total = 1

# # Global records array and counter
# Records = [] 
# NumberRecords = 0
# print(Queue)
# hello = RecordData(Dequeue(),1)
# print(hello.ID)
# print(hello.Total)

# # TotalData procedure
# def TotalData():
#     global Records, NumberRecords
#     data_accessed = Dequeue()
#     if data_accessed == "Empty":
#         return

#     flag = False

#     if NumberRecords == 0:
#         Records[NumberRecords] = RecordData(data_accessed)
#         NumberRecords += 1
#         flag = True
#     else:
#         for i in range(NumberRecords):
#             if Records[i].ID == data_accessed:
#                 Records[i].Total += 1
#                 flag = True
#                 break

#     if not flag:
#         Records[NumberRecords] = RecordData(data_accessed)
#         NumberRecords += 1

# # OutputRecords procedure
# def OutputRecords():
#     for i in range(NumberRecords):
#         print("ID", Records[i].ID, "Total", Records[i].Total)

# # Main Program
# def main():
#     ReadData()
#     for _ in range(TailPointer - HeadPointer):
#         TotalData()
#     OutputRecords()

# # Run the main program
# main()

  
# print(Queue)  
# for i in range(5):
#     print(Dequeue())
# print(HeadPointer)    
# print(TailPointer)    