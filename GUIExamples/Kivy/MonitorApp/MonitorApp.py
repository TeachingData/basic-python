from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

### This is ugly as sin but it gives a building model for everyone to pull
### Make sure to check each commit from init to last for progression
###TODO: add class for monitoring tools and call each function from kivy using button

class MenuScreen(Screen):
    pass

class ResultsScreen(Screen):
    pass

class MonitorApp(App):

    def build(self):
        # Create our screen manager base for everyone to pull
        sm = ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(ResultsScreen(name='results'))

        return sm

if __name__ == '__main__':
    MonitorApp().run()
