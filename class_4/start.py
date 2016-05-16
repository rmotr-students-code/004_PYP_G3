class GameCharacterTrait(object):
    def fight(self):
        pass


class FlyingTrait(object):
    def fly(self):
        print("Flying!")


class SuperSpeedTrait(object):
    def run(self):
        print("Running!")


class StrengthTrait(object):
    pass


if user_choice == ('fly', 'speed'):
    MyChar = type("MyChar", (GameCharacterTrait, FlyingTrait, SuperSpeedTrait), {})
    c1 = MyChar()
elif user_choice == ('fly', 'strength'):
    MyChar = type("MyChar", (GameCharacterTrait, FlyingTrait, StrengthTrait), {})
    c1 = MyChar()