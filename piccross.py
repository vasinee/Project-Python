import Tkinter as tk
import tkMessageBox

TITLE_FONT = ("Helvetica", 18, "bold")
class SampleApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, 'HANJIE')
        tk.Tk.wm_geometry(self, "500x500")
        

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            frame = F(container, self)
            self.frames[F] = frame
            # put all of the pages in the same location; 
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, c):
        '''Show a frame for the given class'''
        frame = self.frames[c]
        frame.tkraise()

class StartPage(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent) 
        label = tk.Label(self, text="HANJIE", font=TITLE_FONT)
        label2 = tk.Label(self, text="PAINT BY NUMBER", font=("Helvetica" , 14))
        label.pack(side="top", fill="x", pady=10)
        label2.pack()

        button1 = tk.Button(self, text="Puzzle 001 (5x5)", width=15, height=2,
                            command=lambda: controller.show_frame(PageOne))
        button2 = tk.Button(self, text="Puzzle 002 (5x5)", width=15, height=2,
                            command=lambda: controller.show_frame(PageTwo))
        button3 = tk.Button(self, text="Puzzle 003 (5x5)", width=15, height=2,
                            command=lambda: controller.show_frame(Page3))
        button4 = tk.Button(self, text="Puzzle 004 (5x5)", width=15, height=2,
                            command=lambda: controller.show_frame(Page4))
        button5 = tk.Button(self, text="Puzzle 005 (5x5)", width=15, height=2,
                            command=lambda: controller.show_frame(Page5))
        button6 = tk.Button(self, text="Puzzle 006 (5x5)", width=15, height=2,
                            command=lambda: controller.show_frame(Page6))
        button7 = tk.Button(self, text="Puzzle 007 (5x5)", width=15, height=2,
                            command=lambda: controller.show_frame(Page7))
        button8 = tk.Button(self, text="Puzzle 008 (5x5)", width=15, height=2,
                            command=lambda: controller.show_frame(Page8))
        button9 = tk.Button(self, text="Puzzle 009 (5x5)", width=15, height=2,
                            command=lambda: controller.show_frame(Page9))
        button1.pack(pady=2)
        button2.pack(pady=2)
        button3.pack(pady=2)
        button4.pack(pady=2)
        button5.pack(pady=2)
        button6.pack(pady=2)
        button7.pack(pady=2)
        button8.pack(pady=2)
        button9.pack(pady=2)
       
       

class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent) 
        label = tk.Label(self, text="This is page 1", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=10)

            
        button = tk.Button(self, text="HOME", 
                           command=lambda: controller.show_frame(StartPage))
        button.pack()

class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent) 
        t = Button_Table(self, 6,8)
        t.pack(side="top", fill="x")
        check = tk.Button(self, text= "CHECK",command=lambda: t.checkButton())
        check.pack(pady = 5)
        home = tk.Button(self, text="HOME", command=lambda: controller.show_frame(StartPage))
        home.pack()
        t.set(0,3,"3"), t.set(0,4,"1"), t.set(0,5,"5"), t.set(0,6,"1"), t.set(0,7,"3")
        t.set(1,0,"1"), t.set(2,0,"1 "), t.set(3,0,"1"), t.set(4,2,"3"), t.set(5,2,"1")
        t.set(1,1,"1"), t.set(1,2,"1"),t.set(2,1,"1"),t.set(2,2,"1")
        t.set(3,2,"1"), t.set(3,1,"1")
        
  
class Button_Table(tk.Frame):
    def __init__(self, parent, rows, columns):
        # form grid lines
        tk.Frame.__init__(self, parent)
         
        self._widgets = []
        for row in range(rows):
            current_row = []
            for column in range(columns):
                if row == 0 or column == 0 or column == 1 or column == 2:
                    label = tk.Label(self,width=8, height=4, bg= "#ffffff")
                    label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                    current_row.append(label)
                else:
                    button = tk.Button(self, width=8, height=4,command=lambda a=row,b=column: self.onButtonPressed(a,b))
                    button.grid(row=row, column=column, sticky="nsew")
                    current_row.append(button)
            self._widgets.append(current_row)           

        for column in range(columns):
            self.grid_columnconfigure(column, weight=5)
        
    def onButtonPressed(self, row, column):
        if self._widgets[row][column]['bg'] == "red":
            self._widgets[row][column]['bg'] = "black"
        else:
            self._widgets[row][column]['bg'] = "red"

    def set(self, row, column, value):
        widget = self._widgets[row][column]
        widget.configure(text=value)

    def checkButton (self):
        """check button background is black"""
        dButton = {1:[1,3], 2:[1,5], 3:[1,7], 4:[2,3], 5:[2,5], 6:[2,7],
                   7:[3,3], 8:[3,5], 9:[3,7], 10:[4,4], 11:[4,5], 12:[4,6], 13:[5,5]}
        
        for i in dButton:
            if self._widgets[dButton[i][0]][dButton[i][1]]['bg']== "black":
                checkAns = "Correct"
            else:
                checkAns = "Incorrect"
        tkMessageBox.showinfo("", checkAns)

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()
