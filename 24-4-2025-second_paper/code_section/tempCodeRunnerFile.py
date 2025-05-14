class insan:
    def __init__(self,name,friend):
        self.name= name
        self.friend = friend
        
hamza = insan("hamza","sufyan")
sufyan = insan("sufyan","waqas")
waqas = insan("waqas","zaryab")

friendList = [hamza,sufyan,waqas ]
print(friendList[0].name)

for i in range(len(friendList)):
    print(f"[ {friendList[i].name} | {friendList[i].friend} ]  " , end=" -> ")