
# Node class
class node:
    def __init__(self, theData, nextNodeNumber):
        self.data = theData
        self.nextNode = nextNodeNumber

# Output linked list nodes
def outputNodes(linkedList, currentPointer):
    while currentPointer != -1:
        print(linkedList[currentPointer].data)
        currentPointer = linkedList[currentPointer].nextNode

# Add node to linked list
def addNode(linkedList, currentPointer, emptyList):
    dataToAdd = int(input("Enter the data to add: "))
    if emptyList < 0 or emptyList > 9:
        return False

    newNode = node(dataToAdd, -1)
    linkedList[emptyList] = newNode

    previousPointer = 0
    while currentPointer != -1:
        previousPointer = currentPointer
        currentPointer = linkedList[currentPointer].nextNode

    linkedList[previousPointer].nextNode = emptyList
    # Update emptyList (not global, to keep function pure)
    return True

# Main logic for Q1
linkedList = [
    node(1,1), node(5,4), node(6,7), node(7,-1), node(2,2),
    node(-1,6), node(-1,7), node(56,3), node(-1,9), node(-1,-1)
]
startPointer = 0
emptyList = 5

print("\n--- Linked List Before Insertion ---")
outputNodes(linkedList, startPointer)

returnValue = addNode(linkedList, startPointer, emptyList)

if returnValue:
    print("Item successfully added")
else:
    print("Item not added, list full")

print("\n--- Linked List After Insertion ---")
outputNodes(linkedList, startPointer)







# Declare array
arrayData = [10, 5, 6, 7, 1, 12, 13, 15, 21, 8]

# Linear Search function
def linearSearch(searchValue):
    for x in range(10):
        if arrayData[x] == searchValue:
            return True
    return False

# Bubble Sort (descending)
def bubbleSort():
    for x in range(10):
        for y in range(9):
            if arrayData[y] < arrayData[y + 1]:
                temp = arrayData[y]
                arrayData[y] = arrayData[y + 1]
                arrayData[y + 1] = temp

# Main logic for Q2
searchValue = int(input("\nEnter the number to search for: "))
if linearSearch(searchValue):
    print("It was found")
else:
    print("It was not found")

print("\n--- Array Before Sort ---")
print(arrayData)

bubbleSort()
print("--- Array After Bubble Sort (Descending) ---")
print(arrayData)








# Treasure chest class
class treasureChest:
    def __init__(self, questionP, answerP, pointsP):
        self.__question = questionP
        self.__answer = int(answerP)
        self.__points = int(pointsP)

    def getQuestion(self):
        return self.__question

    def checkAnswer(self, answerP):
        return self.__answer == answerP

    def getPoints(self, attempts):
        if attempts == 1:
            return self.__points
        elif attempts == 2:
            return self.__points // 2
        elif attempts in [3, 4]:
            return self.__points // 4
        else:
            return 0

# Read data from file
arrayTreasure = []

def readData():
    filename = "treasureChestData.txt"
    try:
        with open(filename, "r") as file:
            while True:
                question = file.readline().strip()
                if not question:
                    break
                answer = file.readline().strip()
                points = file.readline().strip()
                arrayTreasure.append(treasureChest(question, answer, points))
    except IOError:
        print("Could not find file")

# Main logic for Q3
readData()
choice = int(input("\nPick a treasure chest to open (1-5): "))
if 1 <= choice <= 5:
    result = False
    attempts = 0
    while not result:
        answer = int(input(arrayTreasure[choice - 1].getQuestion() + " "))
        result = arrayTreasure[choice - 1].checkAnswer(answer)
        attempts += 1
    pointsEarned = arrayTreasure[choice - 1].getPoints(attempts)
    print("Points earned:", pointsEarned)
