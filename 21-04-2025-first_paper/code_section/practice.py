
class Character:
    def __init__(self,name,x,y):
        self.name = name
        self.XPosition = x
        self.YPosition = y
        
    def GetXPosition(self):
        return self.XPosition
        
    def GetYPosition(self):
        return self.YPosition
        
    def SetXPosition(self,value):
        self.XPosition += value
        if self.XPosition > 10000:
            self.XPosition = 10000
        elif self.XPosition < 0:
            self.XPosition = 0
            
    def SetYPosition(self,value):
        self.YPosition += value
        if self.YPosition > 10000:
            self.YPosition = 10000
        elif self.YPosition < 0:
            self.YPosition = 0
                
        
    def Move(self , direction):
        if direction == "up":
            self.SetYPosition(10)
        elif direction == "down":
            self.SetYPosition(-10)
        elif direction == "right":
            self.SetXPosition(10)
        elif direction == "left":
            self.SetXPosition(-10)
        else:
            print("invalid input")                

jack = Character("jack",50,50)

class BikeCharacter(Character):
    def __init__(self, name, x, y):
        super().__init__(self, name,x,y)
    
    def Move(self , direction):
        if direction == "up":
            self.SetYPosition(20)
        elif direction == "down":
            self.SetYPosition(-20)
        elif direction == "right":
            self.SetXPosition(20)
        elif direction == "left":
            self.SetXPosition(-20) 

karla = BikeCharacter("karla",100,50)

               

def jackInfo():
    print(f"jack x :{jack.GetXPosition()} \n jack y {jack.GetYPosition()}")        

jackInfo()    
jack.SetXPosition(20)
jack.SetYPosition(20)
jackInfo()