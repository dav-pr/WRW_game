"""
    Represents the playing enemy-bot and playing user.

"""
import random
import settings as st
from exceptions import PlayerNameError, IdHeroError, GameOverError, EnemyDownError


class Hero:
    """
    Class implements playable characters and hierarchy of  strength.
    As well, implements basic method such as '==', '<' and __next__

    name: is list of hero code.
    hierarchy: list contains a person index that is lower in the power hierarchy
    full_name: list contains a full name of Hero


    """
    name = [st.WarriorsChar, st.RobbersChar, st.WizardsChar]
    hierarchy = [1, 2, 0]
    full_name = [st.WarriorsStr, st.RobbersStr, st.WizardsStr]

    def __init__(self, symb: str) -> None:
        """

        :param symb:

        Method checks that the input value matches one of the character codes.
        if there is such correspondence, the corresponding instance is initialized
        """
        if symb in self.name:
            self.name_ist = symb
        else:
            raise IdHeroError(st.MsgPressKeyError + ' '.join(self.name))

    def __next__(self) -> None:
        """

        :return: None
        Method get next object in hierarchy of heroes
        """

        idx_current = self.name.index(self.name_ist)
        idx_next = self.hierarchy[idx_current]
        return self.name[idx_next]

    def __eq__(self, other: object) -> bool:
        """

        :param other: instance of Hero class
        :return: True if self == other, else False

        Method implement " == " operation for instance of Hero class
        """

        if isinstance(other, Hero):
            return self.name_ist == other.name_ist or False
        else:
            raise TypeError(st.MsgTypeError.format('==', type(self), type(other)))

    def __gt__(self, other: object) -> bool:
        """

        :param other: instance of Hero class
        :return: True if self > other, else False

        Method implement " >" operation for instance of Hero class
        """

        if isinstance(other, Hero):
            return self.__next__() == other.name_ist or False
        else:
            raise TypeError(st.MsgTypeError.format('>', type(self), type(other)))

    def __str__(self) -> str:
        """

        :return: string representation  of instance  Hero class

        Method implement string representation  of instance  Hero class
        """
        idx = self.name.index(self.name_ist)
        return self.full_name[idx]


class Player:
    """
    Class implements Player instance
    """

    def __init__(self, name: str) -> None:
        """
        :param name: name of player

        Initialize player instance.
        Initializer should receive player's name as an argument - name: str.
        Health points are to be set from settings.
        Score points should be initialized set from settings.
        Name of player transform to "capitalize" view
        """

        if self.validate_name(name):
            self.name = name.capitalize()
            self.hp = st.HealthPointsIni
            self.score = st.ScoreIni
        else:
            raise PlayerNameError(st.MsgNameError)

    def reset(self):
        self.hp = st.HealthPointsIni
        self.score = st.ScoreIni

    @staticmethod
    def validate_name(name: str) -> bool:
        """
        :param name: the player name that is entered
        :return: True if player name meet the requirements
        Method check player name, that is entered, the requirements
        """

        for func in st.NamePlayerRequirements:
            if not func(name):
                return False
        return True

    def decrease_health(self):
        """
        Method decreases the health points value by DecreaseHealthStep - settings.py.
        If this value becomes less that 1 (one) the GameOver exception is raised.
        If health of enemy lower EnemyHealthDown to raise GameOverError
        """
        self.hp -= st.DecreaseHealthStep
        if self.hp < st.EnemyHealthDown:
            raise GameOverError(st.MsgHealthError)

    def select_attack(self) -> Hero:
        """
        Return a fight choice made by the user.
        Performs choice validation.
        Method uses recursion in case of input error
        """
        try:
            msg = ''
            for key, name in zip(Hero.name, Hero.full_name):
                msg += key + '-' + name + ' '
            print(st.MsgPressKeyError + msg)
            key = input()
            res = Hero(key)
            return res
        except IdHeroError:
            return self.select_attack()

    def select_defence(self) -> Hero:
        """
        Return a fight choice made by the user. Performs choice validation.
        """
        return self.select_attack()

    @staticmethod
    def fight(attack_pl: Hero, defence_bot: Hero) -> int:
        """

        :param attack_pl:
        :param defence_bot:
        :return: result of fight: DrawResult, WinResult, FailedResult

        Static method to perform a fight.
        Takes two arguments representing attack and defence choices.
        Performs fight result calculation and return it back.
        """
        if attack_pl == defence_bot:
            return st.DrawResult
        elif attack_pl > defence_bot:
            return st.WinResult
        else:
            return st.FailedResult

    def attack(self, enemy_inst: object):
        """
        Perform defence from an enemy attack.
        This method takes an enemy instance as an argument.
        After that, it takes defence choice from the player model and the attack choice from an enemy model.
        After fight result calculation required operation are to be performed (decrease player health).
        Based on fight result should print out a message:
            "YOUR DEFENCE IS SUCCESSFUL!"
            "YOUR DEFENCE IS FAILED!"
            "IT'S A DRAW!"
        """
        def_choice = self.select_defence()
        enemy_choice = enemy_inst.select_attack()
        res_fight = self.fight(def_choice, enemy_choice)
        return res_fight

    def __str__(self) -> str:
        """
        :return: string representation  of instance  Player class
        Method implement string representation  of instance  Player class
        """

        res_str = []
        res_str.append(st.InfoPlayerName + self.name)
        res_str.append(st.InfoPlayerHealth + str(self.hp))
        res_str.append(st.InfoPlayerScore + str(self.score))
        return " ".join(res_str)


class Enemy:
    def __init__(self, level: int) -> None:
        """
        Initialize enemy instance.
        Initializer should receive one argument of integer type - level: int.
        Health points value should be set equal to level value.
        """
        self.hp = level
        self.level = level
        self.last_strike = None

    def descrease_health(self) -> None:
        """
        Method decreases the health points value by 1 (one).
        If this value becomes less that 1 (one) the EnemyDown exception is raised.
        :return:
        """
        self.hp -= st.DecreaseHealthStep
        if self.hp < st.EnemyHealthDown:
            raise EnemyDownError(st.MsgEnemyDone)

    def select_attack(self) -> Hero:
        """
        :return: instance of Hero
        Return a random attack choice from valid choices.
        """
        attack = random.randint(0, len(Hero.name) - 1)
        self.last_strike = Hero(Hero.name[attack])
        return self.last_strike

    def select_defence(self) -> Hero:
        """
        :return: instance of Hero
        Return a random defence choice from valid choices.
        """
        return self.select_attack()

    def show_strike_info(self) -> None:
        """

        :return: None
        Method print the choice of enemy
        """

        if not isinstance(self.last_strike, type(None)):
            print(st.InfoEnemyChoice, self.last_strike)

    def __str__(self):
        """
        :return: string representation  of instance  Enemy class
        Method implement string representation  of instance  Enemy class
        """
        return st.InfoEnemyHealth + str(self.hp) + ' ' + st.InfoEnemyLevel + str(self.level)


if __name__ == '__main__':
    war = Hero(st.WarriorsChar)
    rob = Hero(st.RobbersChar)
    wiz = Hero(st.WizardsChar)
