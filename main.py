from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from jds import *

class JDS(App):
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
            text = "get DashBoard",
            size_hint = (0.5, 0.5),
            bold = True,
            font_size = 30
        )
        self.button.bind(on_press = self.callback)
        self.window.add_widget(self.button)

        self.button2 = Button(
            text = "Print Recipients",
            size_hint = (0.5, 0.5),
            bold = True,
            font_size = 30
        )
        self.button2.bind(on_press = self.printRec)
        self.window.add_widget(self.button2)

        self.button3 = Button(
            text = "Print Audit Log",
            size_hint = (0.5, 0.5),
            bold = True,
            font_size = 30
        )
        self.button3.bind(on_press = self.printAudit)
        self.window.add_widget(self.button3)
        
        self.button4 = Button(
            text = "Print Error Log",
            size_hint = (0.5, 0.5),
            bold = True,
            font_size = 30
        )
        self.button4.bind(on_press = self.printError)
        self.window.add_widget(self.button4)

        return self.window

    def callback(self,event):
        self.SendDashNow.text = slicer(postReq(self.EnterGUID.text))
    def printRec(self,event):
        printList()
    def printAudit(self, event):
        printAuditLog()
    def printError(self,event):
        printLog()


if __name__ == "__main__":
    JDS().run()




