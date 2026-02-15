
from kivy.app import App
from kivy.uix.label import Label

class KrementsovApp(App):
    def build(self):
        return Label(text="Кременцовъ\nРемесленные деликатесы")

if __name__ == "__main__":
    KrementsovApp().run()
