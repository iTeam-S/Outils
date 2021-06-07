from View.app import HomeScreen


class AppController:
	
	def __init__(self, model):
		self.model = model
		self.view = HomeScreen(controller=self, model=self.model)


	def get_screen(self):
		return self.view