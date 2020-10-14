class Player:

    def __init__(self, name):
        self.name = name
        # self.speed = speed

    def getName(self):
        return self.name

    # def getSpeed(self):
    #     return self.speed

    def getSkill(self):
        return 'normal'

class SlemanPlayer(Player):
    def __init__(self, name):
        super().__init__(name)
        print("hello sleman")

class BantulPlayer(Player):
    def getSkill(self):
        return 'lambat'

# class JogjaPlayer(Player):
#     pass




player = SlemanPlayer('adi ')
# player1 = JogjaPlayer('ida ', ' 86')

print(player.getName() + "punya speed " + player.getSkill())
# print(player1.getName() + "punya speed" + player1.getSkill())