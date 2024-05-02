from kivy.app import App
from kivy.uix.widget import Widget


class GifMenu(Widget):
    pass


class GifPlayerApp(App):
    def build(self):
        return GifMenu()
    

if __name__ == "__main__":
    GifPlayerApp().run()
