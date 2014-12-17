import Tkinter as tk
import tkMessageBox
TITLE_FONT = ("Quark", 28, "bold")

    ######################
    ##   main Frame     ##
    ######################

class GameApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.wm_title(self, 'HANJIE')
        tk.Tk.wm_geometry(self, "500x500")
        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo, Page3, Page4, Page5, Page6):
            frame = F(container, self)
            self.frames[F] = frame
            # put all of the pages in the same location; 
            frame.grid(row = 0, column = 0, sticky="nsew")
        self.show_frame(StartPage)

    def show_frame(self, c):
        '''Show a frame for the given class'''
        frame = self.frames[c]
        frame.tkraise()
        
    #######################################################################
        
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        label = tk.Label(self, text="HANJIE", font=TITLE_FONT)
        label2 = tk.Label(self, text = "PAINT BY NUMBER", font = ("Quark" , 20))
        label.pack(side = "top", fill = "x", pady = 17)
        label2.pack()
        
        button1 = tk.Button(self, text = "Puzzle 001 (5 x 5)", width = 30, height = 2, command = lambda: controller.show_frame(PageOne))
        button2 = tk.Button(self, text = "Puzzle 002 (5 x 5)", width = 30, height = 2, command = lambda: controller.show_frame(PageTwo))
        button3 = tk.Button(self, text = "Puzzle 003 (5 x 5)", width = 30, height = 2, command = lambda: controller.show_frame(Page3))
        button4 = tk.Button(self, text = "Puzzle 004 (10 x 10)", width=30, height = 2, command = lambda: controller.show_frame(Page4))
        button5 = tk.Button(self, text = "Puzzle 005 (10 x 10)", width = 30, height = 2, command = lambda: controller.show_frame(Page5))
        button6 = tk.Button(self, text = "Puzzle 006 (10 x 10)", width = 30, height = 2, command = lambda: controller.show_frame(Page6))
        button = [button1, button2, button3, button4, button5, button6]
        for k in button:
            k.pack(pady = 5)
            
    #######################################################################
            
class Button_Table(tk.Frame):
    def __init__(self, parent, rows, columns, dButton, label_set):
        # form grid lines
        tk.Frame.__init__(self, parent) 
        self._widgets = []
        for row in range(rows):
            current_row = []
            for column in range(columns):
                if row in label_set or column in label_set :
                    label = tk.Label(self, width=2, height=1, bg= "#ffffff")
                    label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                    current_row.append(label)
                else:
                    button = tk.Button(self, width=2, height=1,command=lambda a=row,b=column: self.onButtonPressed(a,b))
                    button.grid(row=row, column=column, sticky="nsew")
                    current_row.append(button)
            self._widgets.append(current_row)           
        for column in range(columns):
            self.grid_columnconfigure(column, weight=5)

    def reset (self):
        '''reset button bg'''
        for l in self._widgets:
            for b in l:
                if not isinstance(b,tk.Button): continue;
                b['bg'] = "#f0f0f0"
        
    def onButtonPressed(self, row, column):
        '''chang botton bg color'''
        if self._widgets[row][column]['bg'] == "red":
            self._widgets[row][column]['bg'] = "black"
        else:
            self._widgets[row][column]['bg'] = "red"

    def set(self, row, column, value):
        '''set text in label'''
        widget = self._widgets[row][column]
        widget.configure(text=value)

    def countBG (self,row, column):
        '''count bg button is color black'''
        count = 0
        for i in range(row):
            for k in range(column):
                if self._widgets[i][k]['bg'] == "black":
                    count += 1
        return count

    def checkButton (self, dButton,row, column):
        '''check button background is black'''
        for i in dButton:
            if self._widgets[dButton[i][0]][dButton[i][1]]['bg']== "black"\
               and self.countBG(row, column) == len(dButton.keys()):
                checkAns = "Correct"
            else:
                checkAns = "Incorrect"
        tkMessageBox.showinfo("", checkAns)

    #######################################################################
        
class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        global row, column
        tk.Frame.__init__(self, parent)

        dic ={  1:[0,2,"1"], 2:[0,4,"1"], 3:[0,6,"1"], 4:[1,2,"1"],
                5:[1,3,"5"], 6:[1,4,"1"], 7:[1,5,"5"], 8:[1,6,"1"],
                9:[2,0,"1"], 10:[4,0,"1"], 11:[6,0,"1"], 12:[2,1,"1"],
                13:[3,1,"5"], 14:[4,1,"1"],15:[5,1,"5"], 16:[6,1,"1"] }
        
               
        dButton = {1:[2,3], 2:[2,5], 3:[3,2], 4:[3,3], 5:[3,4], 6:[3,5],
                   7:[3,6], 8:[4,3], 9:[4,5], 10:[5,2], 11:[5,3], 12:[5,4],
                   13:[5,5], 14:[5,6], 15:[6,3], 16:[6,5]}

        label_set = [0,1]

        label = tk.Label(self, text="Puzzle 001", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=13)
        
        t = Button_Table(self, 7, 7, dButton, label_set)
        t.pack(side="top")
        home = tk.Button(self, text = "HOME", width=10, height=2, command=lambda: controller.show_frame(StartPage))
        home.pack(side='left', padx = 50, pady = 10)
        
        check = tk.Button(self, text= "CHECK", width=10, height=2, command=lambda: t.checkButton(dButton, 7, 7 ))
        check.pack(side='left', padx = 40, pady = 10)
        
        clear = tk.Button(self, text='CLEAR', width=10, height=2, command=lambda: t.reset())
        clear.pack(side='right',padx = 30, pady = 10)
        for i in dic:
               t.set(dic[i][0], dic[i][1], dic[i][2])
               
     #######################################################################

class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        global row, column
        tk.Frame.__init__(self, parent)

        dic ={  1:[2,3,"3"], 2:[2,4,"1"], 3:[2,5,"5"], 4:[2,6,"1"], 5:[2,7,"3"],
                6:[3,0,"1"], 7:[4,0,"1 "], 8:[5,0,"1"], 9:[6,2,"3"], 10:[7,2,"1"],
                11:[3,1,"1"], 12:[3,2,"1"], 13:[4,1,"1"], 14:[4,2,"1"],15:[5,2,"1"], 16:[5,1,"1"]}
        
               
        dButton = {1:[2,3], 2:[2,5], 3:[2,7], 4:[3,3], 5:[3,5], 6:[3,7],
                   7:[4,3], 8:[4,5], 9:[4,7], 10:[5,4], 11:[5,5], 12:[5,6], 13:[6,5]}

        label_set = [0,1,2]

        label = tk.Label(self, text="Puzzle 002", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=13)
        
        t = Button_Table(self, 8, 8, dButton, label_set)
        t.pack(side="top")
        home = tk.Button(self, text = "HOME", width=10, height=2, command=lambda: controller.show_frame(StartPage))
        home.pack(side='left', padx = 50, pady = 10)
        
        check = tk.Button(self, text= "CHECK", width=10, height=2, command=lambda: t.checkButton(dButton))
        check.pack(side='left', padx = 40, pady = 10)
        
        clear = tk.Button(self, text='CLEAR', width=10, height=2, command=lambda: t.reset())
        clear.pack(side='right',padx = 30, pady = 10)
        for i in dic:
               t.set(dic[i][0], dic[i][1], dic[i][2])

     #######################################################################

class Page3(tk.Frame):
    def __init__(self, parent, controller):
        global row, column
        tk.Frame.__init__(self, parent)

        dic ={  1:[0,2,"2"], 2:[0,3,"2"], 3:[0,5,"2"], 4:[0,6,"2"], 5:[1,2,"1"],
                6:[1,3,"1"], 7:[1,4,"1"], 8:[1,5,"1"], 9:[1,6,"1"], 10:[2,0,"2"],
                11:[3,0,"2"], 12:[5,0,"1"], 13:[2,1,"2"], 14:[3,1,"2"], 15:[5,1,"1"],16:[6,1,"3"]}
        
               
        dButton = {1:[2,2], 2:[2,3], 3:[2,5], 4:[2,6], 5:[3,2], 6:[3,3],
                   7:[3,5], 8:[3,6], 9:[5,2], 10:[5,6], 11:[6,3], 12:[6,4], 13:[6,5]}

        label_set = [0,1]

        label = tk.Label(self, text="Puzzle 003", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=13)
        
        t = Button_Table(self, 7, 7, dButton, label_set)
        t.pack(side="top")
        home = tk.Button(self, text = "HOME", width=10, height=2, command=lambda: controller.show_frame(StartPage))
        home.pack(side='left', padx = 50, pady = 10)
        
        check = tk.Button(self, text= "CHECK", width=10, height=2, command=lambda: t.checkButton(dButton))
        check.pack(side='left', padx = 40, pady = 10)
        
        clear = tk.Button(self, text='CLEAR', width=10, height=2, command=lambda: t.reset())
        clear.pack(side='right',padx = 30, pady = 10)
        for i in dic:
               t.set(dic[i][0], dic[i][1], dic[i][2])

     #######################################################################
               
class Page4(tk.Frame):
    def __init__(self, parent, controller):
        global row, column
        tk.Frame.__init__(self, parent)

        dic ={  1:[0,4,"1"], 2:[0,10,"1"], 3:[1,4,"1"], 4:[1,5,"1"], 5:[1,6,"3"],
                6:[1,4,"1"], 7:[1,5,"1"], 8:[1,6,"3"], 9:[1,7,"1"], 10:[1,8,"1"],
                11:[1,9,"2"], 12:[1,10,"1"], 13:[1,11,"2"], 14:[2,3,"7"],
                15:[2,4,"4"], 16:[2,5,"7"], 17:[2,6,"2"], 18:[2,7,"1"], 19:[2,8,"1"],
                20:[2,9,"1"], 21:[2,10,"1"], 22:[2,11,"3"], 23:[2,12,"7"], 24:[6,0,"1"],
                25:[8,0,"1"], 26:[3,1,"1"], 27:[4,1,"1"], 28:[6,1,"2"], 29:[7,1,"3"],
                30:[8,1,"1"], 31:[9,1,"3"], 32:[10,1,"4"], 33:[12,1,"1"], 34:[3,2,"1"],
                35:[4,2,"1"], 36:[5,2,"10"], 37:[6,2,"2"], 38:[7,2,"1"], 39:[8,2,"1"],
                40:[9,2,"1"], 41:[10,2,"2"], 42:[11,2,"10"], 43:[12,2,"1"]}
                
        dButton = {1:[3,5], 2:[3,10], 3:[4,6], 4:[4,9], 5:[5,3], 6:[5,4],
                   7:[5,5], 8:[5,6], 9:[5,7], 10:[5,8], 11:[5,9], 12:[5,10], 13:[5,11],
                   14:[5,12], 15:[6,3], 16:[6,5], 17:[6,6], 18:[6,11], 19:[6,12],
                   20:[7,3], 21:[7,4], 22:[7,5], 23:[7,12], 24:[8,3], 25:[8,5], 26:[8,12],
                   27:[9,3], 28:[9,4], 29:[9,5], 30:[9,12], 31:[10,3], 32:[10,4], 33:[10,5],
                   34:[10,6], 35:[10,11], 36:[10,12], 37:[11,3], 38:[11,4], 39:[11,5],
                   40:[11,6], 41:[11,7], 42:[11,8], 43:[11,9], 44:[11,10], 45:[11,11],
                   46:[11,12], 47:[12,4], 46:[12,11]}

        label_set = [0,1,2]

        label = tk.Label(self, text="Puzzle 004", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=13)
        
        t = Button_Table(self, 13, 13, dButton, label_set)
        t.pack(side="top")
        home = tk.Button(self, text = "HOME", width=10, height=2, command=lambda: controller.show_frame(StartPage))
        home.pack(side='left', padx = 50, pady = 10)
        
        check = tk.Button(self, text= "CHECK", width=10, height=2, command=lambda: t.checkButton(dButton))
        check.pack(side='left', padx = 40, pady = 10)
        
        clear = tk.Button(self, text='CLEAR', width=10, height=2, command=lambda: t.reset())
        clear.pack(side='right',padx = 30, pady = 10)
        for i in dic:
               t.set(dic[i][0], dic[i][1], dic[i][2])

     #######################################################################
               
class Page5(tk.Frame):
    def __init__(self, parent, controller):
        global row, column
        tk.Frame.__init__(self, parent)

        dic ={ 1:[0,11,"1"], 2:[1,4,"5"], 3:[1,5,"2"], 4:[1,6,"1"], 5:[1,7,"2"],
               6:[1,9,"2"], 7:[1,10,"5"], 8:[1,11,"1"], 9:[1,12,"2"], 10:[2,3,"1"],
               11:[2,4,"1"], 12:[2,5,"7"], 13:[2,6,"4"], 14:[2,7,"7"],
               15:[2,8,"7"], 16:[2,9,"7"], 17:[2,10,"1"], 18:[2,11,"1"], 19:[2,12,"1"],
               20:[3,0,"1"], 21:[4,0,"1"], 22:[8,0,"2"], 23:[11,0,"1"], 24:[3,1,"1"],
               25:[4,1,"1"], 26:[7,1,"2"], 27:[8,1,"4"], 28:[11,1,"5"], 29:[3,2,"1"],
               30:[4,2,"1"], 31:[6,2,"7"], 32:[7,2,"6"], 33:[8,2,"1"], 34:[9,2,"8"],
               35:[10,2,"7"], 36:[11,2,"1"], 37:[12,2,"8"]}
               
        dButton = {1:[3,5], 2:[3,7], 3:[4,9], 4:[4,5], 5:[4,7], 6:[4,4],
                   7:[6,4], 8:[6,5], 9:[6,6], 10:[6,7], 11:[6,8], 12:[6,9], 13:[6,10],
                   14:[7,4], 15:[7,5], 16:[7,7], 17:[7,8], 18:[7,9], 19:[7,10],
                   20:[7,11], 21:[7,12], 22:[8,4], 23:[8,5], 24:[8,7], 25:[8,8], 26:[8,9],
                   27:[8,10], 28:[8,12], 29:[9,4], 30:[9,5], 31:[9,6], 32:[9,7], 33:[9,8],
                   34:[9,9], 35:[9,10], 36:[9,11], 37:[10,4], 38:[10,5], 39:[10,6],
                   40:[10,7], 41:[10,8], 42:[10,9], 43:[10,10], 44:[11,3], 45:[11,5],
                   46:[11,6], 47:[11,7], 46:[11,8], 47:[11,9], 48:[11,12], 49:[12,4],
                   50:[12,5], 51:[12,6], 52:[12,7], 53:[12,8], 54:[12,9], 55:[12,10], 55:[12,11]}

        label_set = [0,1,2]

        label = tk.Label(self, text="Puzzle 005", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=13)
        
        t = Button_Table(self, 13, 13, dButton, label_set)
        t.pack(side="top")
        home = tk.Button(self, text = "HOME", width=10, height=2, command=lambda: controller.show_frame(StartPage))
        home.pack(side='left', padx = 50, pady = 10)
        
        check = tk.Button(self, text= "CHECK", width=10, height=2, command=lambda: t.checkButton(dButton))
        check.pack(side='left', padx = 40, pady = 10)
        
        clear = tk.Button(self, text='CLEAR', width=10, height=2, command=lambda: t.reset())
        clear.pack(side='right',padx = 30, pady = 10)
        for i in dic:
               t.set(dic[i][0], dic[i][1], dic[i][2])

     #######################################################################

class Page6(tk.Frame):
    def __init__(self, parent, controller):
        global row, column
        tk.Frame.__init__(self, parent)

        dic ={1:[0,8,"2"], 2:[1,7,"1"], 3:[1,8,"1"], 4:[2,7,"1"], 5:[2,8,"1"],
               6:[2,9,"6"], 7:[2,11,"1"], 8:[2,12,"1"], 9:[2,13,"1"], 10:[3,4,"1"],
               11:[3,5,"1"], 12:[3,6,"3"], 13:[3,7,"2"], 14:[3,8,"1"], 15:[3,9,"1"],
               16:[3,10,"8"], 17:[3,11,"2"], 18:[3,12,"1"], 19:[3,13,"1"], 20:[11,0,"1"],
               21:[11,1,"1"], 22:[10,2,"1"], 23:[11,2,"1"], 24:[13,2,"2"], 25:[4,3,"2"],
               26:[5,3,"2"], 27:[6,3,"5"], 28:[7,3,"4"], 29:[8,3,"2"], 30:[9,3,"3"],
               31:[10,3,"1"], 32:[11,3,"1"], 33:[12,3,"8"], 34:[13,3,"2"]}
               
        dButton = {1:[4,8], 2:[4,9], 3:[5,8], 4:[5,9], 5:[6,9], 6:[6,10],
                   7:[6,11], 8:[6,12], 9:[6,13], 10:[7,7], 11:[7,8], 12:[7,9], 13:[7,10],
                   14:[8,9], 15:[8,10], 16:[9,8], 17:[9,9], 18:[9,10], 19:[10,7],
                   20:[10,10], 21:[11,4], 22:[11,6], 23:[11,10], 24:[11,13], 25:[12,5], 26:[12,6],
                   27:[12,7], 28:[12,8], 29:[12,9], 30:[12,10], 31:[12,11], 32:[12,12], 33:[13,6],
                   34:[13,7], 35:[13,10], 36:[13,11]}

        label_set = [0,1,2,3]

        label = tk.Label(self, text="Puzzle 006", font=TITLE_FONT)
        label.pack(side="top", fill="x", pady=13)
        
        t = Button_Table(self, 14, 14, dButton, label_set)
        t.pack(side="top")
        home = tk.Button(self, text = "HOME", width=10, height=2, command=lambda: controller.show_frame(StartPage))
        home.pack(side='left', padx = 50, pady = 10)
        
        check = tk.Button(self, text= "CHECK", width=10, height=2, command=lambda: t.checkButton(dButton))
        check.pack(side='left', padx = 40, pady = 10)
        
        clear = tk.Button(self, text='CLEAR', width=10, height=2, command=lambda: t.reset())
        clear.pack(side='right',padx = 30, pady = 10)
        for i in dic:
               t.set(dic[i][0], dic[i][1], dic[i][2])


if __name__ == "__main__":
    app = GameApp()
    app.mainloop()
