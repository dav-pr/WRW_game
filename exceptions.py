"""
 Represents the playing exception.
"""


class GameOverError(Exception):
    """
    Class implements GameOverError
    """

    def __init__(self, message: str) -> None:
        """

        :param message: usually st.MsgHealthError,
        """
        self.message = message

    def __str__(self) -> str:
        """
        :return: string representation  of instance  GameOverError  class
        """
        return self.message


class PlayerNameError(Exception):
    """
    Class implements PlayerNameError.
    Raise when input name does not meet the requirements
    """

    def __init__(self, message: str) -> None:
        """
        :param message: usually st.MsgNameError
        """
        self.message = message

    def __str__(self):
        """
        :return: string representation  of instance  PlayerNameError  class
        """
        return self.message


class IdHeroError(Exception):
    """
    Class implements IdHeroError.
    Raise then input code of Hero  does not meet the requirements
    """

    def __init__(self, message: str) -> None:
        """
        :param message: any msg
        """
        self.message = message

    def __str__(self) -> str:
        """
        :return: string representation  of instance  IdHeroError  class
        """
        return self.message


class EnemyDownError(Exception):
    """
    Class implements EnemyDownError.
    Raise then enemy health lower EnemyHealthDown
    """

    def __init__(self, message: str) -> None:
        """
        :param message: usually MsgEnemyDone
        """
        self.message = message

    def __str__(self) -> str:
        """
        :return: string representation  of instance  EnemyDownError  class
        """
        return self.message


class MenuSelectError(Exception):
    """
    Class implements MenuSelectError.
    Raise when  code Menu  does not meet the requirements
    """

    def __init__(self, message: str) -> None:
        """
        :param message: usually MsgEnemyDone
        """
        self.message = message

    def __str__(self) -> str:
        """
        :return: string representation  of instance  EnemyDownError  class
        """

        return self.message
