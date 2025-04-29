Queue = ['GAME123', 'GAME456', 'GAME123', 'GAME789', 'GAME456', 'GAME999', 'GAME123', 'GAME888', 'GAME999', 'GAME888']
HeadPointer = 0
TailPointer = 10

# Enqueue procedure
def Enqueue(item):
    global Queue, HeadPointer, TailPointer
    if TailPointer >= 50:
        print("Queue is full. Cannot enqueue:", item)
    else:
        if HeadPointer == -1:
            HeadPointer = 0
        Queue[TailPointer] = item
        TailPointer += 1

# Dequeue function
def Dequeue():
    global Queue, HeadPointer, TailPointer
    if HeadPointer == -1 or HeadPointer == TailPointer:
        print("Queue is empty.")
        return "Empty"
    else:
        item = Queue[HeadPointer]
        HeadPointer += 1
        return item

# RecordData class
class RecordData:
    # ID: string
    # Total: integer
    def __init__(self, ID):
        self.ID = ID
        self.Total = 1

# Global records array and counter
Records = []
NumberRecords = 0

# TotalData procedure
def TotalData():
    global Records, NumberRecords
    data_accessed = Dequeue()
    if data_accessed == "Empty":
        return

    flag = False

    if NumberRecords == 0:
        Records.append(RecordData(data_accessed))
        NumberRecords += 1
        flag = True
    else:
        for i in range(NumberRecords):
            if Records[i].ID == data_accessed:
                Records[i].Total += 1
                flag = True
                break

    if not flag:
        Records.append(RecordData(data_accessed))
        NumberRecords += 1

def OutputRecords():
    for i in range(NumberRecords):
        print("ID", Records[i].ID, "Total", Records[i].Total)
        
def main():
    for _ in range(TailPointer - HeadPointer):
        TotalData()
    OutputRecords()
main()