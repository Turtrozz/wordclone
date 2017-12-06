

import os
import sqlite3

from tkinter import *
from tkinter import ttk







#============The Widgets related code====================#



		


#=========The app python main function implementation class==============#

class Main:


	
	




	@staticmethod

	def main():

		
		def changeCol(btObj):

			btObj.config(background="blue")


		def menuTAB(m_options):


			
			m_tab = Menu(m_options[0],tearoff = 0)

			if(len(m_options) > 2):

				m_tab_options = m_options[2:]
				
				for m_tab_option in range(0,len(m_tab_options)):

					m_tab.add_command(label=m_tab_options[m_tab_option])
					


			m_options[0].add_cascade(label=m_options[1],menu = m_tab)






		

		mainAppWindow = Tk()

		
		mainAppWindow.resizable(width=True,height=True)
		mainAppWindow.minsize(width=600,height=500)
		mainAppWindow.maxsize(width=1400,height=1400)
		mainAppWindow.title('MaritoXitsonga')
		mainAppWindow.iconbitmap("tsongDic_ico.ico")


		menuBar = Menu(mainAppWindow)


		menuTAB([menuBar,'VekaRito','Surprise','Shadrack','Kulani','Cythia','Revlon'])
		menuTAB([menuBar,'ChelaRito'])
		menuTAB([menuBar,'Vona','Rito tsavuriwa'])
		menuTAB([menuBar,'Langha'])
		menuTAB([menuBar,'Pfuneka','HiDictionary','AppFoni','Swihoxo','MS Webpage','Hi...'])

		


		mainAppWindow.config(menu=menuBar)

		fR = Frame(mainAppWindow,width=800)

		lb = Label(mainAppWindow,text="Vulavi:")
		lb.grid(row=0,column=0,sticky=W,padx=4,pady=6)
		bBox = mainAppWindow.grid_slaves()

		entW = Entry(mainAppWindow,width=100)
		entW.grid(column=1,row=0)

		

		entW.config(width=150)

		
		
		entW.insert(0,bBox)

		bt = Button(mainAppWindow,width=20,text="Search",borderwidth=1,background="red")
		bt.grid(row=0,column=2,sticky=W)
		bt.bind("Enter",lambda : bt.config(background="blue"))
		Button(mainAppWindow,width=8,borderwidth=1,bitmap="info").grid(row=0,column=3,sticky=W)

		Text(mainAppWindow,width=150).grid(row=1,column=0,columnspan=4,padx=4)




		


		mainAppWindow.mainloop()








#=========The app boot strap class==============#

class AppBootstrap:

	@staticmethod
	def runApp():

		Main.main()

#=========The app class==============#

class App:


	AppBootstrap.runApp()









	



















