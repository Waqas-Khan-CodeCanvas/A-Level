# Part (a)
class Character:
    # Private attributes
    # self.__Name : string
    # self.__XCoordinate : int
    # self.__YCoordinate : int

    def __init__(self, name, x, y):
        self.__Name = name
        self.__XCoordinate = x
        self.__YCoordinate = y

    # Part (b)
    def GetName(self):
        return self.__Name

    def GetX(self):
        return self.__XCoordinate

    def GetY(self):
        return self.__YCoordinate

    # Part (c)
    def ChangePosition(self, xChange, yChange):
        self.__XCoordinate += xChange
        self.__YCoordinate += yChange

# Part (d), (e), (f), (g)(i)
def main():
    Characters = []  # List to store Character objects

    # Read Characters.txt
    try:
        with open('Characters.txt', 'r') as file:
            lines = file.readlines()
            for i in range(0, len(lines), 3):  # Every 3 lines: name, x, y
                name = lines[i].strip()
                x = int(lines[i + 1].strip())
                y = int(lines[i + 2].strip())
                character = Character(name, x, y)
                Characters.append(character)
    except FileNotFoundError:
        print("Characters.txt file not found.")
        return

    # Ask user for a character name until valid
    found = False
    while not found:
        search_name = input("Enter character name: ").strip()
        for index, character in enumerate(Characters):
            if character.GetName().lower() == search_name.lower():
                found = True
                character_index = index
                break
        if not found:
            print("Character not found. Try again.")

    # Ask for movement direction until valid input
    valid_moves = ['A', 'W', 'S', 'D']
    move = ''
    while move not in valid_moves:
        move = input("Enter move (A=left, W=up, S=down, D=right): ").strip().upper()
        if move not in valid_moves:
            print("Invalid move. Try again.")

    # Move the character
    if move == 'A':  # Left
        Characters[character_index].ChangePosition(-1, 0)
    elif move == 'W':  # Up
        Characters[character_index].ChangePosition(0, 1)
    elif move == 'S':  # Down
        Characters[character_index].ChangePosition(0, -1)
    elif move == 'D':  # Right
        Characters[character_index].ChangePosition(1, 0)

    # Output new coordinates
    character = Characters[character_index]
    print(f"{character.GetName()} has changed coordinates to X = {character.GetX()} and Y = {character.GetY()}")

# Running the program
if __name__ == "__main__":
    main()
