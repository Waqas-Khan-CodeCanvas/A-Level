# Treasure Chest Quiz Game (full program)
# Following AS & A Level Computer Science 9618/41 May/June 2021 Question 3

# --- Class Declaration ---
class TreasureChest:
    def __init__(self, question, answer, points):
        # private attributes
        self.__question = question
        self.__answer = answer 
        self.__points = points

    # --- getQuestion() method ---
    def getQuestion(self):
        return self.__question

    # --- checkAnswer(userAnswer) method ---
    def checkAnswer(self, userAnswer):
        return userAnswer == self.__answer

    # --- getPoints(attempts) method ---
    def getPoints(self, attempts):
        if attempts == 1:
            return self.__points
        elif attempts == 2:
            return self.__points // 2
        elif attempts == 3 or attempts == 4:
            return self.__points // 4
        else:
            return 0

# --- Procedure to read data from file and create TreasureChest objects ---
def readData():
    arrayTreasure = []
    try:
        file = open("TreasureChestData.txt", "r")
        lines = file.readlines()
        file.close()

        # Read every 3 lines (question, answer, points)
        # while line != "":
        # while True:
        for i in range(0, len(lines), 3):
            question = lines[i].strip()
            answer = int(lines[i+1].strip())
            points = int(lines[i+2].strip())
            chest = TreasureChest(question, answer, points)
            arrayTreasure.append(chest)
            
    except FileNotFoundError:
        print("Error: TreasureChestData.txt file not found.")

    return arrayTreasure

# --- Main Program ---
arrayTreasure = readData()

if arrayTreasure:  # Proceed only if data was loaded successfully
    try:
        # Ask user for question number
        questionNumber = int(input("Enter a question number between 1 and 5: "))

        if 1 <= questionNumber <= 5:
            chest = arrayTreasure[questionNumber - 1]
            attempts = 0
            correct = False

            # Repeat until user gives correct answer
            while not correct:
                print("Question:", chest.getQuestion())
                userAnswer = int(input("Enter your answer: "))
                attempts += 1
                correct = chest.checkAnswer(userAnswer)

                if not correct:
                    print("Incorrect. Try again.")

            # When correct, calculate points awarded
            pointsAwarded = chest.getPoints(attempts)
            print(f"Correct! You scored {pointsAwarded} points.")

        else:
            print("Invalid question number. Must be between 1 and 5.")

    except ValueError:
        print("Invalid input. Please enter a valid integer.")
else:
    print("Program terminated because file could not be read.")