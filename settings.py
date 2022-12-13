"""
This module contains the gameplay options
"""

# Keys that match each character
WARRIORS_CHAR = "1"
ROBBERS_CHAR = "2"
WIZARDS_CHAR = "3"

# Full  names of each character
WARRIORS_STR = 'WARRIOR'
ROBBERS_STR = 'ROBBER'
WIZARDS_STR = "WIZARD"

# Names of stages
MSG_NAME_ATTACK_STAGE = 'You attack'
MSG_NAME_DEFENCE_STAGE = 'You defence'

# Results of "Defence stage"
MSG_DEFENCE_SUCCESS = 'YOUR DEFENCE IS SUCCESSFUL!'
MSG_DEFENCE_FAILED = 'YOUR DEFENCE IS FAILED!'
MSG_DEFENCE_DRAW = 'IT\'S A DRAW!'

# Results of "Attack stage"
MSG_ATTACK_SUCCESS = 'YOUR ATTACK IS SUCCESSFUL!'
MSG_ATTACK_FAILED = 'YOUR ATTACK IS FAILED!'
MSG_ATTACK_DRAW = 'IT\'S DRAW!'

# The parameter contains an invitation text to enter a player name
MSG_ENTER_NAME = 'Please, enter name player:'

# The parameter contains information message about the player name requirement
MSG_NAME_ERROR = 'Name must meet the identification requirements and longer one symbol'

# The parameter contains information message about keys to select character
MSG_PRESS_KEY_ERROR = 'Please, press one of these keys: '

# The parameter contains information message about errors of logical operation
MSG_TYPE_ERROR = '{0} not supported between instances of {1} and {2}'

# Information message about player Health done
MSG_HEALTH_ERROR = 'You is done!'

# Information message about player enemy done
MSG_ENEMY_DONE = 'Enemy is down!'
# Information message about player get extra points after enemy is done
MSG_EXTRA_POINTS = 'Your get extra points - {0}'

# Information message about KeyboardInterrupt
MSG_GOODBYE = 'Game over!'

# Information message about current players parameters
INFO_PLAYER_NAME = "name: "
INFO_PLAYER_HEALTH = "health: "
INFO_PLAYER_SCORE = "score: "

# Information message about current enemy parameters
INFO_ENEMY_HEALTH = "Enemy health: "
INFO_ENEMY_LEVEL = "Enemy level: "

# Information message about choice of enemy
INFO_ENEMY_CHOICE = "Enemy choice: "

# Information message about num of current Round
INFO_ROUND_NUM = "***** Round № {0} *****"

# starts  Health points of player
HEALTH_POINTS_INI = 5

# score points of player at start game
SCORE_INI = 0
# number points decrease health player after her is done
DECREASE_HEALTH_STEP = 1

# number points decrease health enemy after her is done
ENEMY_HEALTH_DOWN = 1

# enemy level at start game
START_ENEMY_LEVEL_INI = 5

# number of points that player get after win stage
POINT_WIN = 5
# number of points that player get after enemy is down
POINT_EXTRA = 10

# Parameters determine the match of battle results
DRAW_RESULT = 0
WIN_RESULT = 1
FAILED_RESULT = -1


def isidentifier(name_player: str) -> bool:
    """
    :param name_player: the player name that is entered
    :return: True if player name meet the requirements
    Function check player name, that is entered, the requirements
    """
    return name_player.isidentifier()


def isbigger(name_player: str) -> bool:
    """
    :param name_player: the player name that is entered
    :return: True if player name meet the requirements
    Function check player name, that is entered, the requirements
    """
    return len(name_player) > 1


# list the list contains a list of features that check to meet the requirements of the player name
name_player_requirements_funcs = [isidentifier, isbigger]

# setting for menu
MENU_NAME = ['Play', 'Scores', 'Exit']
MENU_CHAR = ['P', 'S', 'E']
MSG_MENU_SELECT_ERROR = 'Please, press one of these keys: '
MSG_MENU_HI = 'AVAILABLE MENU CHOICES: '

# setting for scores
FILE_NAME_SCORE = 'scores.txt'
MSG_INFO_SCORE = 'You get {0} points'
MSG_SCORE_TITLE = """
        Scores
Name            Points
"""
MSG_SCORE_EMPTY = 'Score  is empty'
