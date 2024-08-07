from kivy.config import ConfigParser
from kivy.app import App
from kivy.uix.widget import Widget
from plyer import filechooser


class GifMenu(Widget):

    config = ConfigParser(name="GifPlayerApp")


    def choose_dir(self):
        path = filechooser.choose_dir()
        
        self.config.set("folder", value = path)


    def launch(self):
        print(self.config.get("folder"))

class GifPlayerApp(App):
    def build(self):
        return GifMenu()
    

if __name__ == "__main__":
    GifPlayerApp().run()
