"""
Represents the identity
"""

from exceptions import MenuSelectError
import settings as st


class Menu:
    """
    Class implements menu identity
    """
    def __init__(self, *args) -> None:
        """

        :param args: function that meet menu
        links menu element to function and key

        """
        self.menu_name = st.menu_name
        self.menu_char = st.menu_char
        self.menu_func = []
        for arg in args:
            self.menu_func.append(arg)

    def show(self) -> None:
        """

        :return: None
        Show the menu
        """
        print(st.MsgMenuHi, self)

    def __str__(self) -> str:
        """

        :return: str
        Implement string representation of instance
        """
        msg = ''
        for key, name in zip(self.menu_name, self.menu_char):
            msg += key + '-' + name + ' '
        return msg

    def check_choice(self, symb: str) -> bool:
        """

        :param symb: press symbol
        :return: True if press symbol in self.menu_char
        Validate press key.
        """

        if symb in self.menu_char:
            return True
        else:
            raise MenuSelectError(st.MsgMenuSelectError + ' '.join(self.menu_char))

    def get_choice(self) -> str:
        """

        :return: str-presses key.
        Get and processed pressed key
        """
        while True:
            try:
                symb = input().capitalize()
                if self.check_choice(symb):
                    break
            except MenuSelectError as er:
                print(er.args[0])
        return symb

    def start(self) -> None:
        """

        :return: None
        Start event menu loop.
        """

        while True:
            self.show()
            symb = self.get_choice()
            idx = self.menu_char.index(symb)
            self.menu_func[idx]()
