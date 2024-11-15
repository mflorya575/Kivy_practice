from kivy.app import App
from kivy.config import Config
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout


Config.set("graphics", "width", "800")
Config.set("graphics", "height", "700")
Config.set("graphics", "resizable", "0")


class FirstApp(App):
    def build(self):
        main_layout = FloatLayout()
        button_one = Button(text="КНОПКА",
                      italic=True, bold=True,
                      font_size=40, color=[0, 0, 0.75, 1],
                      background_color=[0.9, 0.6, 0, 1],
                      background_normal="",
                      size_hint_x=0.48,
                      size_hint_y=0.15,
                      x=0, y=250,
                      on_press=self.press_button)
        button_two = Button(text="КНОПКА",
                      italic=True, bold=True,
                      font_size=40, color=[0, 0, 0.75, 1],
                      background_color=[0.9, 0.6, 0, 1],
                      background_normal="",
                      size_hint_x=0.48,
                      size_hint_y=0.15,
                      x=420, y=250,
                      on_press=self.press_button_2)
        main_layout.add_widget(button_one)
        main_layout.add_widget(button_two)
        return main_layout

    def press_button(self, instance):
        instance.text = ":)"
        instance.background_color = [1, 0, 0, 1]

    def press_button_2(self, instance):
        instance.text = ":)"
        instance.background_color = [1, 0, 0, 1]

if __name__ == "__main__":
    FirstApp().run()
