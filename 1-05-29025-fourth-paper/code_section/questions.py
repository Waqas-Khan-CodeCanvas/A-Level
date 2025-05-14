# PROCEDURE Select(Start, End : INTEGER)
#    DECLARE ThisNum, Total : INTEGER
#    DECLARE LastDigit, SecondLastDigit : INTEGER   
#    FOR ThisNum ← Start + 1 TO End - 1
#       LastDigit ← ThisNum MOD 10
#       SecondLastDigit ← (ThisNum DIV 10) MOD 10
#       Total ← LastDigit + SecondLastDigit

#       IF Total = 6 THEN
#          OUTPUT ThisNum
#       ENDIF
#    NEXT ThisNum
# ENDPROCEDURE

def Select(Start, End):
    for ThisNum in range(Start + 1, End):
        LastDigit = ThisNum % 10
        SecondLastDigit = (ThisNum // 10) % 10
        Total = LastDigit + SecondLastDigit

        if Total == 6:
            print(ThisNum)

# Example usage
Select(10, 100)