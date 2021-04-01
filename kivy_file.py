import kivy
from kivy.app import App
from kivy.uix.label import Label

class DemoApp(App):
    def build(self):
        return Label(text='Your Demo App')


if __name__=='__main__':
    DemoApp().run()