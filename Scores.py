"""
Represents the scores
"""
import settings as st
from typing import List


class Scores:
    """
    Class implements scores identity

    """

    def __init__(self, fname: str) -> None:
        """

        :param fname: file name, which contains information about scores.
        One line in file - one player.
        Create instance class Score. self.names[] - list of the player's names.
        self.score[]- list of the player's scrore.
        function self.load(fname) read information about scores from file.
        """
        self.names: List[str] = []
        self.score: List[int] = []
        self.load(fname)

    def is_empty(self) -> bool:
        """
        Метод здійснює перевірку на пустоту рейтинга
        для майбутнього використання
        :return:
        """
        return not self.names

    def get_num_names(self) -> int:
        """

        :return:int - count of records in score.
        Method return the count of record in score/
        """
        return len(self.names)

    def get_score(self, name: str) -> int:
        """
        :param name:
        :return: int
        Method return score of name-player/
        """
        try:
            return self.score[self.names.index(name)]
        except ValueError:
            return -1

    def add(self, name: str, score: int) -> None:
        """

        :param name: name of player.
        :param score: current score.
        :return: None.
        Method add the score of player with name == 'name'.
        """

        if name not in self.names:
            self.names.append(name)
            self.score.append(score)
        else:
            if self.score[self.names.index(name)] < score:
                self.score[self.names.index(name)] = score

    def pop(self, name: str) -> None:
        """

        :param name: name of player
        :return: None
        delete score with name player == name.
        """
        i = self.names.index(name)
        self.names.pop(i)
        self.score.pop(i)

    def sort(self) -> None:
        """
        :return: None
        sort scores  in descending order
        """
        if self.names:
            zip_list = list(zip(self.names, self.score))
            zip_list.sort(key=lambda x: x[1], reverse=True)
            self.names = []
            self.score = []
            for names, score in zip_list:
                self.names.append(names)
                self.score.append(score)

    def __str__(self) -> str:
        """

        :return: str- string representation
        Return string representation of 10 highest score values
        """

        res_str = []
        if self.names:
            self.sort()
            res_str.append(f'\n {st.MsgScoreTitle:<20}')
            zip_list = list(zip(self.names, self.score))
            for name, score in zip_list[:10]:
                res_str.append(f"{name:<20}" + f"{score:<20}")
            res_str.append(" ")
        else:
            res_str.append(st.MsgScoreEmpty)
        res_str = '\n'.join(res_str)
        return res_str

    def show(self):
        print(self)

    @staticmethod
    def _write_to_file_(fname: str, mode: str, zip_list: List) -> None:
        """

        :param fname: file name
        :param mode: file  access mode
        :param zip_list: zip list of names and scores
        :return:  None
        Write data to file.
        """

        with open(fname, mode) as f:
            for item in zip_list:
                f.write(str(item) + '\n')

    def save(self, fname: str) -> None:
        """

        :param fname: file name
        :return: None
        Save score to the file. Call the  def _write_to_file_()
        """

        zip_list = list(zip(self.names, self.score))
        mode = 'x'
        while True:
            try:
                self._write_to_file_(fname, mode, zip_list)
                break
            except FileExistsError:
                mode = 'w'

    @staticmethod
    def _clear_str(item: str) -> str:
        """

        :param item: strinf to cleaning
        :return: clean string
        Function clear string, which read from file
        """
        item = item.replace("(", "").replace(")", "")
        item = item.replace("[", "").replace("]", "")
        item = item.replace("\'", "")
        return item

    def load(self, fname) -> None:
        """

        :param fname: file name
        :return: None
        Read scores information from file.
        """
        try:
            with open(fname, 'r') as f:
                zip_list = f.readlines()

            for item in zip_list:
                item = self._clear_str(item)
                item = item.split(",")
                self.names.append(item[0].strip())
                self.score.append(int(item[1].strip()))
        except FileNotFoundError:
            self.names: List[str] = []
            self.score: List[int] = []
