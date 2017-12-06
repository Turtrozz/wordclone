
import sqlite3
import os
import io
import tkinter as tk




class GuiComponents:



	def __init__(self,rootComponent,compType,compOptions,compGridOptions):

				self.rootC = rootComponent
				self.compT = compType
				self.compOpts = compOptions
				self.compGridOpts = compOptions

	

	def createComponents(self):


		comp = self.compT(self.rootC,self.compOpts)

		addCompToView(comp,compGridOptions)




	@staticmethod

	def addCompToView(compo,compoGridOptions):

		comp.grid(compGridOpts)



class GuiComponentType(GuiComponents):



		def __init__(self,rootComponent,compObjType,compOptions,compGridOpts):

			self.rootC = rootComponent
			self.compT = compObjType
			self.compOpts = compOptions
			self.compGridOpts = compGridOpts

			GuiComponents.__init__(self,self.rootC,self.compT,self.compOpts,self.compGridOpts)
			GuiComponents.createComponents(self)


		def objeMethod():

			print('I am working')



			




rootComp = tk.Tk()
background = "blue"

component1 = GuiComponentType(rootComponent=rootComp,compObjType = 'Frame',compOptions=background,compGrid)


				








