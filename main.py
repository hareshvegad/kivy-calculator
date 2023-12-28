from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import kivy

kivy.require('2.0.4')

class MyRoot(BoxLayout):
    def __init__(self):
        super(MyRoot, self).__init__()
        
    def calc_symbol(self,symbol):
        self.calc_field.text += symbol
        
    def clear(self):
        self.calc_field.text = ""
        
    def get_result(self):
        self.calc_field.text = str(eval(self.calc_field.text))

class Calculator(App):
    def build(self):
        return MyRoot()
    
Calculator().run()