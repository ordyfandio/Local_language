from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang.builder import Builder
from kivy.core.window import Window
from kivy.base import runTouchApp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.button import Button
Window.clearcolor = 1,1,1,1

class WindowManager(ScreenManager):
    pass

class HeroScreen(Screen):
    pass
class FrontPageScreen(Screen):
    pass

class IntroScreen(Screen):
    pass

class profileScreen(Screen):
    pass

class NoAboutScreen(Screen):
    def change(self):
        HB=BoxLayout(orientation="horizontal")
        
        img=Image(source="family.jpg",size_hint=(0.2, 0.2))
        btn1=Button(text="Family/Friend",size_hint=(None,None),width="100px",height="70px")
        HB.add_widget(img)
        HB.add_widget(btn1)
class Speakeasy(App):
    def build(self):
        root = WindowManager()
        root.add_widget(HeroScreen(name='Hero'))
        root.add_widget(FrontPageScreen(name='FrontPage'))
        root.add_widget(profileScreen(name='Profile'))
        root.add_widget(NoAboutScreen(name='NoAbout'))
        runTouchApp(root.add_widget(IntroScreen(name='Intro')))
        self.icon="logo.jpeg"
        return root

if __name__ == '__main__':
    Builder.load_file('Hero.kv')
    Speakeasy().run()