

import os
import sqlite3

from tkinter import *





#============The Widgets related code====================#



		


#=========The app python main function implementation class==============#

class Main:

	@staticmethod

	def main():

		mainAppWindow = Tk()

		
		mainAppWindow.resizable(width=True,height=True)
		mainAppWindow.minsize(width=600,height=500)
		mainAppWindow.maxsize(width=1400,height=1400)
		mainAppWindow.title('MaritoXitsonga')
		mainAppWindow.iconbitmap("favicon.ico")

		menuBar = Menu(mainAppWindow)

		m_bookmarkTab = Menu(menuBar,tearoff = 0)

		m_bookmarkTab.add_command(label="Surprise")
		m_bookmarkTab.add_command(label="Shadrack")
		m_bookmarkTab.add_command(label="Happy")
		m_bookmarkTab.add_separator()
		m_bookmarkTab.add_command(label="Ntiyiso")
		m_bookmarkTab.add_command(label="Sophy")

		menuBar.add_cascade(label="Bookmark",menu = m_bookmarkTab)

		mainAppWindow.config(menu=menuBar)


		mainAppWindow.mainloop()








#=========The app boot strap class==============#

class AppBootstrap:

	@staticmethod
	def runApp():

		Main.main()

#=========The app class==============#

class App:


	AppBootstrap.runApp()









	



















