import os
import webbrowser

from kivy.metrics import dp
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivymd.uix.menu import MDDropdownMenu
from kivy.properties import ObjectProperty, StringProperty
from kivymd.uix.list import OneLineAvatarIconListItem
from kivymd_extensions.sweetalert import SweetAlert
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.utils import get_color_from_hex


class ContentNavigationDrawer(MDBoxLayout):
    nav_drawer = ObjectProperty()


class HomeScreen(MDScreen):
    controller = ObjectProperty()
    model = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def view_repos(self, **kwargs):
        SweetAlert(
            color_button=get_color_from_hex('008080'),
            animation_type="pulse"
        ).fire(text="Le repos a été ouvert dans votre navigateur.")

        webbrowser.open('https://github.com/iTeam-S/Outils')

    def show_help(self, *args):
        SweetAlert(
            animation_type="pulse",
            color_button=get_color_from_hex('008080'),
            font_style_text="Body2",
        ).fire(
            type="info",
            text="Application regroupant les différents scripts de la communauté.\n" + \
            "Dans le but de pouvoir les utiliser depuis une interface graphique",
        )

    def on_pre_open(self, event):
        pass


Builder.load_file(os.path.join(os.path.dirname(__file__), 'home.kv'))
