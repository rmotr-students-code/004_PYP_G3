class GameCharacterTrait():
    """
    Creates the score variable for when the fight method is called
    also creates the power variables for both you and other
    contains methods that are called at the result of the fight method
    """

    def __init__(self, power1, power2, opponent=None):
        self.power1 = power1
        self.power2 = power2
        self.score = 0
        self.opponent = opponent
        
    def lose(self):
        print self.opponent.name + " Beat You! Game Over!"

    def win(self):
        print "You have defeated " + self.opponent.name

    def tie(self):
        print "You and " + self.opponent.name + " have tied!"


class FlyingTrait(GameCharacterTrait):
    def fly1(self):
        return self._fly('power1')
        
    def fly2(self):
        return self._fly('power2')

    def _fly(self, power_name):
        power = getattr(self.opponent, power_name)

        if power == "Flying":
            pass
        if power == "Superspeed":
            self.score -= 1
        if power == "Superstrength":
            self.score += 1

op1 = FlyingTrait("Flying", "Superspeed")
op2 = FlyingTrait("Flying", "Superstrength", op1)
op2.fly1()
op2.fly2()

print(op2.score)