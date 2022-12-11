"""
This module contains the gameplay options
"""

# Keys that match each character
WarriorsChar = "1"
RobbersChar = "2"
WizardsChar = "3"

# Full  names of each character
WarriorsStr = 'WARRIOR'
RobbersStr = 'ROBBER'
WizardsStr = "WIZARD"

# Names of stages
MsgNameAttackStage = 'You attack'
MsgNameDefenceStage = 'You defence'

# Results of "Defence stage"
MsgDefenceSuccess = 'YOUR DEFENCE IS SUCCESSFUL!'
MsgDefenceFailed = 'YOUR DEFENCE IS FAILED!'
MsgDefenceDraw = 'IT\'S A DRAW!'

# Results of "Attack stage"
MsgAttackSuccess = 'YOUR ATTACK IS SUCCESSFUL!'
MsgAttackFailed = 'YOUR ATTACK IS FAILED!'
MsgAttackDraw = 'IT\'S DRAW!'

# The parameter contains an invitation text to enter a player name
MsgEnterName = 'Please, enter name player:'

# The parameter contains information message about the player name requirement
MsgNameError = 'Name must meet the identification requirements and longer one symbol'

# The parameter contains information message about keys to select character
MsgPressKeyError = 'Please, press one of these keys: '

# The parameter contains information message about errors of logical operation
MsgTypeError = '{0} not supported between instances of {1} and {2}'

# Information message about player Health done
MsgHealthError = 'You is done!'

# Information message about player enemy done
MsgEnemyDone = 'Enemy is down!'
# Information message about player get extra points after enemy is done
MsgExtraPoints = 'Your get extra points - {0}'

# Information message about KeyboardInterrupt
MsgGoodbye = 'Game over!'

# Information message about current players parameters
InfoPlayerName = "name: "
InfoPlayerHealth = "health: "
InfoPlayerScore = "score: "

# Information message about current enemy parameters
InfoEnemyHealth = "Enemy health: "
InfoEnemyLevel = "Enemy level: "

# Information message about choice of enemy
InfoEnemyChoice = "Enemy choice: "

# Information message about num of current Round
InfoRoundNum = "***** Round № {0} *****"

# starts  Health points of player
HealthPointsIni = 5

# score points of player at start game
ScoreIni = 0
# number points decrease health player after her is done
DecreaseHealthStep = 1

# number points decrease health enemy after her is done
EnemyHealthDown = 1

# enemy level at start game
StartEnemyLevelIni = 5

# number of points that player get after win stage
PointWin = 5
# number of points that player get after enemy is down
PointExtra = 10

# Parameters determine the match of battle results
DrawResult = 0
WinResult = 1
FailedResult = -1


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
NamePlayerRequirements = [isidentifier, isbigger]

# setting for menu
menu_name = ['Play', 'Scores', 'Exit']
menu_char = ['P', 'S', 'E']
MsgMenuSelectError = 'Please, press one of these keys: '
MsgMenuHi = 'AVAILABLE MENU CHOICES: '

# setting for scores
FileNameScore = 'scores.txt'
MsgInfoScore = 'You get {0} points'
MsgScoreTitle = """
        Scores
Name            Points
"""
MsgScoreEmpty = 'Score  is empty'
