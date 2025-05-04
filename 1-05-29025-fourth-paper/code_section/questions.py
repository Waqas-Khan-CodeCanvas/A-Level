PROCEDURE Select(Start, End : INTEGER)
   DECLARE ThisNum, Total : INTEGER
   DECLARE LastDigit, SecondLastDigit : INTEGER   
   FOR ThisNum ← Start + 1 TO End - 1
      LastDigit ← ThisNum MOD 10
      SecondLastDigit ← (ThisNum DIV 10) MOD 10
      Total ← LastDigit + SecondLastDigit

      IF Total = 6 THEN
         OUTPUT ThisNum
      ENDIF
   NEXT ThisNum
ENDPROCEDURE