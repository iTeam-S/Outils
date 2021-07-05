from kivymd.app import MDApp
from Controller.app import AppController
from Model.app import AppModel


class Outils(MDApp):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.model = AppModel()
		self.controller = AppController(self.model)


	def build(self):
		return self.controller.get_screen()



Outils().run()