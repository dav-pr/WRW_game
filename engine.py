"""
Represents the playing engine

"""
import sys

import settings as st
from models import Enemy, Player
from Menu import Menu
from Scores import Scores
from exceptions import PlayerNameError, EnemyDownError, GameOverError


class Round:
    """
    Class implements round identity

    """

    def __init__(self, player_inst: Player, enemy_inst: Enemy) -> None:
        """

        :param player_inst: instance of Player's class
        :param enemy_inst: instance of Enemy's class
        Method initialized Round  instance.
        play_strike[] - list that contains the   methods player instance
        enemy_strike[] - list that contains the   methods enemy  instance
        current_stage - 0 - Attack stage, 1 - defence stafe
        round_num - count of rounds
        new_round - indication of new round. Is needed to print info message about new round
        """
        if isinstance(player_inst, Player):
            self.play_strike = [player_inst.select_attack, player_inst.select_defence]
        if isinstance(enemy_inst, Enemy):
            self.enemy_strike = [enemy_inst.select_defence, enemy_inst.select_attack]
        self.stages_name = [st.MSG_NAME_ATTACK_STAGE, st.MSG_NAME_DEFENCE_STAGE]
        self.current_stage = 0
        self.round_num = 1
        self.new_round = True

    def next_stage(self) -> None:
        """
        :return: None
        Method implements next stage procedure
        """
        self.current_stage += 1
        self.new_round = False
        if self.current_stage == len(self.play_strike):
            self.current_stage = 0
            self.round_num += 1
            self.new_round = True

    def play_stage(self) -> tuple:
        """
        :return: tuple of result call function, that representation the choice of player and enemy
        Method print name of current stage,
        call function, that representation the choice of player and enemy,
        and return result of choice  player and enemy.
        """
        print(self.stages_name[self.current_stage])
        return self.play_strike[self.current_stage](), self.enemy_strike[self.current_stage]()


class Play:
    """
    Class implements games process
    """

    def __init__(self) -> None:
        """
        player_inst - instance of Player class
        enemy_inst - instance of Enemy  class
        round - instance of Round class
        game_over - indication of game over. If True - game loop continue. If False- break loop.
        """
        while True:
            try:
                self.player_inst = Player(self.get_player_name())
                break
            except PlayerNameError as er:
                print(er.args[0])

        self.enemy_inst = Enemy(st.START_ENEMY_LEVEL_INI)
        self.round = Round(self.player_inst, self.enemy_inst)
        self.game_over = False
        self.scores = Scores(st.FILE_NAME_SCORE)

    @staticmethod
    def get_player_name() -> str:
        """

        :return: input name of player
        Method get input name player and validate his.
        """
        print(st.MSG_ENTER_NAME)
        player_name = input().strip()
        return player_name

    def show_status(self) -> None:
        """

        :return: None
        Method print current information about Round, Enemy and Player (health, score etc.)
        """
        if self.round.new_round:
            print('\n', st.INFO_ROUND_NUM.format(self.round.round_num))
        print('\n', self.enemy_inst)
        print(self.player_inst)

    def game_stop(self, msg) -> None:
        """

        :param msg: message to print in game over
        :return: None
        Method process GameOver stage. Turn on flag "game_over" and print massage.
        """
        print(msg)
        print(st.MSG_INFO_SCORE.format(self.player_inst.score))
        self.scores.add(self.player_inst.name, self.player_inst.score)
        self.scores.save(st.FILE_NAME_SCORE)
        self.game_over = True

    def processing_of_the_results(self, res_fight) -> None:
        """

        :param res_fight: result of fight
        :return: None
        Method processing of the results: change health, points etc. If needed raise EnemyDownError or
        GameOverError exception.
        On EnemyDownError exception:
        - ini new instance of enemy with next level;
        - ini new instance of Round.
        On GameOverError exception:
         - call game_stop()
        """
        try:
            if res_fight == st.WIN_RESULT:
                self.player_inst.score += st.POINT_WIN
                self.enemy_inst.descrease_health()
            elif res_fight == st.FAILED_RESULT:
                self.player_inst.decrease_health()
            self.round.next_stage()

        except EnemyDownError as er:
            print(er.args[0])
            print(st.MSG_EXTRA_POINTS.format(st.POINT_EXTRA))
            self.enemy_inst = Enemy(self.enemy_inst.level + 1)
            self.round = Round(self.player_inst, self.enemy_inst)
            self.player_inst.score += st.POINT_EXTRA

        except GameOverError as er:

            self.game_stop(er.args[0])

    def print_result(self, res_fight: int) -> None:
        """

        :param res_fight: DrawResult, WinResult, FailedResult
        :return: None
        Method print result of fight.
        Test that the output depends on the round stage
        """
        results = [st.DRAW_RESULT, st.WIN_RESULT, st.FAILED_RESULT]
        if self.round.current_stage == 0:
            result_msg = [st.MSG_ATTACK_DRAW, st.MSG_ATTACK_SUCCESS, st.MSG_ATTACK_FAILED]
        else:
            result_msg = [st.MSG_DEFENCE_DRAW, st.MSG_DEFENCE_SUCCESS, st.MSG_DEFENCE_FAILED]
        for result, msg in zip(results, result_msg):
            if res_fight == result:
                print(msg)
                break

    def play(self) -> None:
        """

        :return: None
        Method implement game loop.
        Сycle continues while flag "game_over" is set.
        On first step of the loop prints status of player and enemy.
        On second step - get result of the fight.
        On third step - show result of fight
        On forth dtep -   processing of the results.
        If raise except GameOverError call method "game_stop", which stop game.
        """

        try:

            self.game_over = False
            self.player_inst.reset()
            while not self.game_over:
                self.show_status()
                res_fight = self.player_inst.fight(*self.round.play_stage())
                self.enemy_inst.show_strike_info()
                self.print_result(res_fight)
                self.processing_of_the_results(res_fight)

        except GameOverError as er:

            self.game_stop(er.args[0])

        except KeyboardInterrupt:
            print('\n', st.MSG_GOODBYE)

    @staticmethod
    def exit_script() -> None:
        """

        :return: None
        Method implement output "goodbye" message and exit from process
        """
        print('\n', st.MSG_GOODBYE)
        sys.exit()


if __name__ == '__main__':

    try:
        play_inst = Play()
        menu = Menu(play_inst.play, play_inst.scores.show, play_inst.exit_script)
        menu.start()
    except KeyboardInterrupt:
        print('\n', st.MSG_GOODBYE)
        sys.exit()
