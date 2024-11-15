from kivy.app import App
from kivy.config import Config
from kivy.uix.button import Button


Config.set("graphics", "width", "400")
Config.set("graphics", "height", "700")
Config.set("graphics", "resizable", "0")


class FirstApp(App):
    def build(self):
        return Button(text="КНОПКА",
                      italic=True, bold=True,
                      font_size=40, color=[0, 0, 0.75, 1],
                      background_color=[0.9, 0.6, 0, 1],
                      background_normal="",
                      size_hint_x=0.48,
                      size_hint_y=0.15,
                      x=104, y=297.5,
                      on_press=self.press_button)

    def press_button(self, instance):
        instance.text = ":)"
        instance.background_color = [1, 0, 0, 1]

if __name__ == "__main__":
    FirstApp().run()
