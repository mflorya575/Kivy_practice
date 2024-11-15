from kivy.app import App
from kivy.config import Config


Config.set("graphics", "width", "400")
Config.set("graphics", "height", "700")
Config.set("graphics", "resizable", "0")


class FirstApp(App):
    pass


if __name__ == "__main__":
    FirstApp().run()
