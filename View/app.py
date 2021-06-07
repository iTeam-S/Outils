import os
import webbrowser
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivy.properties import ObjectProperty
from kivymd_extensions.sweetalert import SweetAlert


class HomeScreen(MDScreen):
    controller = ObjectProperty()
    model = ObjectProperty()


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    

    def view_repos(self, **kwargs):
        SweetAlert(
            window_control_buttons="close"
        ).fire(text="Le repos a été ouvert dans votre navigateur.")

        webbrowser.open('https://github.com/iTeam-S/Outils')









Builder.load_file(os.path.join(os.path.dirname(__file__), 'home.kv'))