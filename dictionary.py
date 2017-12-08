
import sqlite3
import os
import io
from tkinter import *




class GuiComponents:

	parentCompFrame = ""
	parentCompMenu = ""


	def __init__(self,rootComponent,compType,pkOrder,compOptions,compGridOptions,randOptions):

				self.rootC = rootComponent
				self.compT = compType
				self.compPk = pkOrder
				self.compOpts = compOptions
				self.compGridOpts = compOptions
				self.randOpts = randOptions

	

	def createChildComps(self):


		comp = self.compT(self.parentCompFrame,self.compOpts)

		self.addCompToView(comp)



	def createParentComps(self):


		if(self.compT == Frame):

			self.frameParentCompType()
		else:

			self.menuParentCompType()

			

	def frameParentCompType(self):


		self.parentCompFrame = self.compT(self.rootC)
		self.addCompToView(self.parentCompFrame)



	def menuParentCompType(self,optional = ''):

		if(optional != ''):


			tabM = optional(self.parentCompMenu,tearoff = 0)

			return tabM

		else:

			if(self.parentCompFrame == ""):

				self.parentCompMenu = self.compT(self.rootC)
				self.menuItems(self.parentCompMenu)
				


			else:

				self.menuItems(self.parentCompMenu)
				self.parentCompMenu = self.compT(parentCompFrame)
			

	def menuItems(self,parenM):


		


		if(isinstance(self.randOpts,list)):



			listLen = len(self.randOpts)



			li = 0

			while(li < listLen):

				tabMenu = self.menuParentCompType(Menu)

				tabMenu.add_command(label=self.randOpts[li])
				tabMenu.add_command(label=self.randOpts[li])
				tabMenu.add_command(label=self.randOpts[li])

				self.parentCompMenu.add_cascade(label=self.randOpts[li],menu=tabMenu)
				print(self.randOpts[li])

				li += 1



			






	







	@staticmethod

	def addCompToView(compo):

		compo.grid()



class GuiComponentType(GuiComponents):



		def __init__(self,rootComponent,compObjType,pkOrder,compOptions = '',compGridOpts = '',randOptions = ''):

			
			GuiComponents.__init__(self,rootComponent,compObjType,pkOrder,compOptions,compGridOpts,randOptions)

			if(self.compPk['peckOrder'] == "child"):

				self.createChildComps()
			else:

				self.createParentComps()


		def objeMethod(self):

			print('I am working')
			print('The random opts are as follows:',self.randOpts)
			self.rootC.config(menu = self.parentCompMenu)
			self.rootC.mainloop()



			




rootComp = Tk()
rootComp.title("InteLexicon")

frame = GuiComponentType(rootComp,Frame,{'peckOrder':'parent'})
menu = GuiComponentType(rootComp,Menu,{'peckOrder':'parent'},randOptions = ['Bookmarks','Copy','View','Options','help'])

menu.objeMethod()





				








