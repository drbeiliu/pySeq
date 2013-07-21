import Tkinter as tk
import os
from tkFileDialog import askopenfilename
#from tkMessageBox import showerror

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid()
        self.createWidgets()
    def createWidgets(self):
        self.pattern = tk.Entry(self, text = '').pack()
        self.database_path = tk.Button(self, text = 'Select your database',
                command = self.getfilepath).pack()
        self.searchButton = tk.Button(self, text = 'search',
                command = self.parseSeq).pack()
    def getfilepath(self):
        # define options for opening or saving a file
        self.file_opt = options = {}
        options['defaultextension'] = '.fasta'
        options['filetypes'] = [('all files', '.*'), ('database files', '.fasta')]
        options['initialdir'] =  os.getcwd()
        options['initialfile'] = 'myfile.txt'
        options['parent'] = root
        options['title'] = 'This is a title'
        fname = askopenfilename(**self.file_opt)
        print fname

    def parseSeq(self):
        return;

if   __name__  ==  "__main__":
    root = tk.Tk()
    app = Application(master = root)
    app.mainloop()