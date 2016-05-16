class GameCharacterTrait(object):
    pass


class FlyingTrait(GameCharacterTrait):
    pass


class SuperSpeedTrait(GameCharacterTrait):
    pass


class StrengthTrait(GameCharacterTrait):
    pass


class SpeedFlyingCharacter(SuperSpeedTrait, FlyingTrait):
    pass


class StrengthFlyingCharacter(SuperSpeedTrait, FlyingTrait):
    pass


if user_choice == ('fly', 'speed'):
    c = SpeedFlyingCharacter()
elif user_choice == ('fly', 'strength'):
    c = StrengthFlyingCharacter()