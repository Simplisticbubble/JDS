from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from jds import *

class AgeCalculator(App):
    def build(self):
        
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5 }
        self.window.add_widget(Image(source = "jds-logo.png"))


        self.SendDashNow = Label(
            text = "Enter the guid of the Dashboard you want to see: ", 
            font_size = 20,
            color = "#ffffff",
            bold = True
        )
        self.window.add_widget(self.SendDashNow)
        
        self.EnterGUID = TextInput(
            multiline=False,
            padding_y = (30, 30),
            size_hint = (1, 0.7),
            font_size = 30
        )
        self.window.add_widget(self.EnterGUID)

        self.button = Button(
            text = "SendNow",
            size_hint = (0.5, 0.5),
            bold = True,
            font_size = 30
        )
        self.button.bind(on_press = self.callback)
        self.window.add_widget(self.button)

        return self.window

    def callback(self,event):
        self.SendDashNow.text = slicer(postReq(self.EnterGUID.text))


if __name__ == "__main__":
    AgeCalculator().run()




