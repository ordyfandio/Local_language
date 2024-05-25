from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang.builder import Builder
from kivy.core.window import Window
Window.clearcolor = 1,1,1,1

class WindowManager(ScreenManager):
    pass

class HeroScreen(Screen):
    pass
        

class FrontPageScreen(Screen):
    pass

class Speakeasy(App):
    def build(self):
        root = WindowManager()
        root.add_widget(HeroScreen(name='Hero'))
        root.add_widget(FrontPageScreen(name='FrontPage'))
        return root

if __name__ == '__main__':
    Builder.load_file('Hero.kv')
    Speakeasy().run()