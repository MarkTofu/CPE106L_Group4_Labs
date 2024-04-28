from tkinter import *
from tkinter import filedialog

def FileFinder():
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Text files",
                                                        "*.txt*"),
                                                       ("all files",
                                                        "*.*")))
                                                        
      
    label_main_program.configure(text="You have opened: "+filename)
                                                                                      
window = Tk()
  
window.title('File Explorer and Namer')
  
window.config(background = "white")
  
label_main_program = Label(window,
                            text = "I will name a file you choose, go try it now :)",
                            width = 220, height = 10,
                            fg = "red")
  
button_filechoose = Button(window,
                        text = "Choose your file",
                        command = FileFinder)
  
button_exit = Button(window,
                     text = "Exit Program",
                     command = exit)
  
label_main_program.grid(column = 0, row = 0)
  
button_filechoose.grid(column = 0, row = 2)
  
button_exit.grid(column = 0,row = 3)

window.wm_attributes('-fullscreen', 'True')
  
window.mainloop()