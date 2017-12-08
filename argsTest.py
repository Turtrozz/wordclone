


from tkinter import *





class MakeWidget:
	
	def __init__(self,widget,options,grid=0):

		self.widgetType = widget
		self.options = options
		self.grid = grid

		self.root = Tk()



	def makeWidget(self):

		widg = self.widgetType(self.root,self.options)

		widg.grid()

	def displayWidg(self):


		self.root.mainloop()






widget = MakeWidget(Button,{'background':"yellow",'width': 50})
widget.makeWidget()
widget.displayWidg()



