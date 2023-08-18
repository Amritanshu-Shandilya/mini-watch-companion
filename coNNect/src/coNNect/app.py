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
        
        # self.main_data = toga.Label(
        #     id = "Data",
        #     text=self.fetch_time(),
        #     style=Pack(padding=(0,5))
        # )

        self.display_time = toga.Label(
            id="Time",
            text="Time : "+self.fetch_time()[3],
            style=Pack(padding=(1, 5))
        )   
        
        self.display_date = toga.Label(
            id="Date",
            text="Date : " + self.fetch_time()[1]+" "+self.fetch_time()[2]+" "+self.fetch_time()[4],
            style=Pack(padding=(2,5))
        )
        
        self.display_day = toga.Label(
            id="Day",
            text="Day : " +  self.fetch_time()[0],
            style=Pack(padding=(3,5))
        )

        name_box = toga.Box(style=Pack(direction=COLUMN, padding=5))
        # name_box.add(main_data)
        name_box.add(self.display_time)
        name_box.add(self.display_date)
        name_box.add(self.display_day)

        main_box.add(name_box)
        # main_box.add(button)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()
        
    def fetch_time(self):
        time_val = time.localtime()
        data =  time.asctime(time_val)
        
        return data.split(" ")


def main():
    return MiniWatchConnect()
