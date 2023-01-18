from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.lang import Builder

Builder.load_file('main.kv')

class Calculator(BoxLayout):
    def calculate(self, expression):
        if(expression):
            try:
                self.ids.resultlbl.text = str(eval(expression))
            except Exception:
                self.ids.resultlbl.text = "Error"

class myApp(App):
    def build(self):
        Window.size = (360, 600)
        return Calculator()
        
if __name__=="__main__":
    myApp().run()