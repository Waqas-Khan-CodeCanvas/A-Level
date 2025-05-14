# Section 1: String Processing (Vowel Counting)

# Question1_N23.py (IterativeVowels)

def IterativeVowels(value):
    total = 0
    length = len(value)
    for _ in range(length):
        first_char = value[0]
        if first_char in 'aeiou':
            total += 1
        value = value[1:]
    return total

print("Vowel count in 'house':", IterativeVowels("house"))


def RecursiveVowels(value):
    if value == "":
        return 0
    first_char = value[0]
    if first_char in 'aeiou':
        return 1 + RecursiveVowels(value[1:])
    else:
        return RecursiveVowels(value[1:])
    
print("Vowel count in 'imagine':", RecursiveVowels("imagine"))


# -----------------------
# Question2_N23.py
# -----------------------

# Global queue and pointers

Queue = [""] * 50  # Can store 50 game IDs
HeadPointer = -1
TailPointer = 0

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

# Read data from QueueData.txt
def ReadData():
    try:
        with open("QueueData.txt", "r") as file:
            for line in file:
                Enqueue(line.strip())
    except FileNotFoundError:
        print("QueueData.txt not found.")

# RecordData class
class RecordData:
    # ID: string
    # Total: integer
    def __init__(self, ID):
        self.ID = ID
        self.Total = 1

# Global records array and counter
Records = [None] * 50
NumberRecords = 0

print(Queue)
# TotalData procedure
def TotalData():
    global Records, NumberRecords
    data_accessed = Dequeue()
    if data_accessed == "Empty":
        return

    flag = False

    if NumberRecords == 0:
        Records[NumberRecords] = RecordData(data_accessed)
        NumberRecords += 1
        flag = True
    else:
        for i in range(NumberRecords):
            if Records[i].ID == data_accessed:
                Records[i].Total += 1
                flag = True
                break

    if not flag:
        Records[NumberRecords] = RecordData(data_accessed)
        NumberRecords += 1

# OutputRecords procedure
def OutputRecords():
    for i in range(NumberRecords):
        print("ID", Records[i].ID, "Total", Records[i].Total)

# Main Program
def main():
    ReadData()
    for _ in range(TailPointer - HeadPointer):
        TotalData()
    OutputRecords()

# Run the main program
main()
print(HeadPointer)
print(TailPointer)


# -------------------------
# Question3_N23.py
# -------------------------
# """
# Character class
class Character:
    # Name: string
    # XPosition: integer
    # YPosition: integer

    def __init__(self, name, x, y):
        self.Name = name
        self.XPosition = x
        self.YPosition = y

    def GetXPosition(self):
        return self.XPosition

    def GetYPosition(self):
        return self.YPosition

    def SetXPosition(self, value):
        self.XPosition += value
        if self.XPosition > 10000:
            self.XPosition = 10000
        elif self.XPosition < 0:
            self.XPosition = 0

    def SetYPosition(self, value):
        self.YPosition += value
        if self.YPosition > 10000:
            self.YPosition = 10000
        elif self.YPosition < 0:
            self.YPosition = 0

    def Move(self, direction):
        if direction.lower() == "up":
            self.SetYPosition(10)
        elif direction.lower() == "down":
            self.SetYPosition(-10)
        elif direction.lower() == "left":
            self.SetXPosition(-10)
        elif direction.lower() == "right":
            self.SetXPosition(10)

# Declare a new Character instance - Jack
jack = Character("Jack", 50, 50)

# BikeCharacter class (inherits from Character)
class BikeCharacter(Character):
    def __init__(self, name, x, y):
        super().__init__(name, x, y)

    def Move(self, direction):
        if direction.lower() == "up":
            self.SetYPosition(20)
        elif direction.lower() == "down":
            self.SetYPosition(-20)
        elif direction.lower() == "left":
            self.SetXPosition(-20)
        elif direction.lower() == "right":
            self.SetXPosition(20)

# Declare a new BikeCharacter instance - Karla
karla = BikeCharacter("Karla", 100, 50)

# Main interaction program
def move_character():
    character_name = input("Which character would you like to move? (jack/karla): ").strip().lower()
    direction = input("Enter direction to move (up/down/left/right): ").strip().lower()

    if direction not in ["up", "down", "left", "right"]:
        print("Invalid direction.")
        return

    if character_name == "jack":
        jack.Move(direction)
        print(f"Jack's new position is X = {jack.GetXPosition()} Y = {jack.GetYPosition()}")
    elif character_name == "karla":
        karla.Move(direction)
        print(f"Karla's new position is X = {karla.GetXPosition()} Y = {karla.GetYPosition()}")
    else:
        print("Invalid character name.")

# Call main interaction function twice for required testing
print("Test 1:")
move_character()  # Use input: jack right

print("\nTest 2:")
move_character()  # Use input: karla down

        # """


