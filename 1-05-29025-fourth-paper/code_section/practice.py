def Select(Start, End):
    for ThisNum in range(Start + 1, End):
        LastDigit = ThisNum % 10
        SecondLastDigit = (ThisNum // 10) % 10
        Total = LastDigit + SecondLastDigit

        if Total == 6:
            print(ThisNum)

# Example usage
Select(10, 100)
