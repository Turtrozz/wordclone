

import os
import sqlite3

from tkinter import *





#============The Widgets related code====================#



		


#=========The app python main function implementation class==============#

class Main:


	
	




	@staticmethod

	def main():

		


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
		mainAppWindow.iconbitmap("favicon.ico")

		menuBar = Menu(mainAppWindow)


		menuTAB([menuBar,'VekaRito','Surprise','Shadrack','Kulani','Cythia','Revlon'])
		menuTAB([menuBar,'ChelaRito'])
		menuTAB([menuBar,'Vona','Rito tsavuriwa'])
		menuTAB([menuBar,'Langha'])
		menuTAB([menuBar,'Pfuneka','HiDictionary','AppFoni','Swihoxo','MS Webpage','Hi...'])

		


		mainAppWindow.config(menu=menuBar)

		Label(mainAppWindow,text="Vulavi:").grid(row=0,column=0,sticky="W",padx=4,pady=6)
		Entry(mainAppWindow).grid(row=0,column=1,sticky="W")
		Text(mainAppWindow).grid(row=1,column=0,sticky="W",padx=4)
		


		mainAppWindow.mainloop()








#=========The app boot strap class==============#

class AppBootstrap:

	@staticmethod
	def runApp():

		Main.main()

#=========The app class==============#

class App:


	AppBootstrap.runApp()









	



















