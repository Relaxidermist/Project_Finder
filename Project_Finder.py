from tkinter import *
from tkinter import ttk
import os
import configparser
import project as prj

#import everything from the tkinter module here

#Open project config file here:
config = configparser.ConfigParser()
config.read("config.ini")


#globals
bg = "#87CEEB"

project_repo = config['paths']['project']


#This is the application class

class Project_Finder_UI(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master["bg"] = bg
        self.master.title("Project_Finder")
        #should add widgets to self here.
        self.create_widgets()

    def create_widgets(self):
    	#Create Frames for the Screen
    	self.top_frame = Frame(self.master)
    	self.top_frame.pack(fill=X,expand=1,padx=10,pady=5)
    	self.top_frame["bg"] = bg

    	self.bottom_frame = Frame(self.master)
    	self.bottom_frame.pack(fill=BOTH,expand=1,padx=5,pady=5)
    	self.bottom_frame["bg"] = bg

    	#Create Widgets in Top Frame
    	self.search_string = Entry(self.top_frame)
    	self.search_button = Button(self.top_frame,text="Project Search")
    	self.search_button["command"] = self.search

    	#Create Widgets in Bottom Frame
    	self.results_scroll = Scrollbar(self.bottom_frame, orient=VERTICAL)
    	self.results = Listbox(self.bottom_frame, yscrollcommand=self.results_scroll.set)
    	self.results_scroll.config(command=self.results.yview)
    	self.results_scroll.pack(side=RIGHT, fill=Y)
    	self.results_label = Label(self.bottom_frame, text="Results")
    	self.results_label["bg"] = bg

    	self.search_string.pack(side=LEFT,fill=X,expand=1)
    	self.search_button.pack(side=RIGHT,fill=BOTH,expand=1,padx=5,pady=5)

    	self.results.pack(side=BOTTOM,fill=BOTH,expand=1)
    	self.results_label.pack(side=LEFT)

    def search(self):
    	# Delete items in the list
    	self.results.delete(0, END)
    	CCSProject = prj.IProject()
    	dirlist = os.listdir(project_repo)
    	for project in dirlist[0:5]:

    		if project.find(self.search_string.get()) >= 0:
    			project_path = project_repo + "\\" + project
    			if os.path.isdir(project_path):
    				CCSProject.subdir = os.listdir(project_path)
    				row = CCSProject.format(0)
    				print(row)
    				self.results.insert(END, row)

    			print(project_path)

    		

    	# use search string to parse list


#Instantiate the tkinter class
Root_Window = Tk()


#Instantiate the Project Finder UI - it will init itself
UI = Project_Finder_UI(master=Root_Window)


#Set the UI Title
#UI.master.title("Project_Finder")
UI.mainloop()