"""
A smartphone companion app for MiniWatch project on Github
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, CENTER


import time
import asyncio


class MiniWatchConnect(toga.App):
    
    def fetch_data(self):
        """This will be called only once to give initial data"""
        local_time = time.localtime()
        return time.asctime(local_time).split(" ")
    
    def update_time(self):
        """This will be used to update the time only"""
        pass

    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN, alignment = CENTER))
        
        # self.main_data = toga.Label(
        #     id = "Data",
        #     text=self.fetch_data(),
        #     style=Pack(padding=(0,5))
        # )

        self.display_time = toga.Label(
            id="Time",
            text="Time : "+ self.fetch_data()[3],
            style=Pack(padding=3, text_align = CENTER)
        )   
        
        self.display_date = toga.Label(
            id="Date",
            text="Date : " + self.fetch_data()[2]+" "+self.fetch_data()[1]+" "+self.fetch_data()[4],
            style=Pack(padding=3, text_align = CENTER)
        )
        
        self.display_day = toga.Label(
            id="Day",
            text="Day : " +  self.fetch_data()[0],
            style=Pack(padding=3, text_align = CENTER)
        )
        
        self.add_background_task(self.update_time())

        name_box = toga.Box(style=Pack(direction=COLUMN, padding=5, alignment = CENTER))
        # name_box.add(self.main_data)
        name_box.add(self.display_time)
        name_box.add(self.display_date)
        name_box.add(self.display_day)

        main_box.add(name_box)
        # main_box.add(button)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()
        



def main():
    return MiniWatchConnect()
