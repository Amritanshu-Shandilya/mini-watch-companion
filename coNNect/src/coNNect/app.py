"""
A smartphone companion app for MiniWatch project on Github
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW

import time


class MiniWatchConnect(toga.App):

    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN))

        time = toga.Label(
            self.time,
            style=Pack(padding=(0, 5))
        )
        # self.name_input = toga.TextInput(style=Pack(flex=1))

        name_box = toga.Box(style=Pack(direction=ROW, padding=5))
        name_box.add(time)
        # name_box.add(self.name_input)

        # button = toga.Button(
        #     "Say Hello!",
        #     on_press=self.say_hello,
        #     style=Pack(padding=5)
        # )
        
        main_box.add(name_box)
        # main_box.add(button)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()
        
    def time(self):
        print(time.gmtime(0))
        # return time.gmtime(0)


def main():
    return MiniWatchConnect()
