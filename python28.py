class telephone():
    def call(self):
        print('You can use me for call')
    def message(self):
        print('I cannot send messages')
    
class smartphone(telephone):
    def videoCall(self):
        print('Now i can make video calls')
    def playGames(self):
        print('You can play game on me')
sObj=smartphone()
sObj.call()
sObj.message()
sObj.videoCall()
sObj.playGames()
print(issubclass(smartphone, telephone))