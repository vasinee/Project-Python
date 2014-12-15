import Tkinter as tk
import tkMessageBox

class PageTwo(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        t = Button_Table(self, 7,7)
        t.pack(side="top", fill="x")
        check = tk.Button(self, text= "check",command=lambda: t.checkButton())
        check.pack(pady = 5)
        dic ={1:[0,2,"1"], 2:[0,4,"1"], 3:[0,6,"1"], 4:[1,2,"1"], 5:[1,3,"5"],
               6:[1,4,"1"], 7:[1,5,"5"], 8:[1,6,"1"], 9:[2,0,"1"], 10:[4,0,"1"],
               11:[6,0,"1"], 12:[2,1,"1"], 13:[3,1,"5"], 14:[4,1,"1"],
               15:[5,1,"5"], 16:[6,1,"1"]}
        for i in dic:
               t.set(dic[i][0], dic[i][1], dic[i][2])
        
  
class Button_Table(tk.Frame):
    def __init__(self, parent, rows, columns):
        # form grid lines
        tk.Frame.__init__(self, parent)
         
        self._widgets = []
        for row in range(rows):
            current_row = []
            for column in range(columns):
                if row == 0 or row == 1 or column == 1 or column == 0:
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
        dButton = {1:[2,3], 2:[2,5], 3:[3,2], 4:[3,3], 5:[3,4], 6:[3,5],
                   7:[3,6], 8:[4,3], 9:[4,5], 10:[5,2], 11:[5,3], 12:[5,4], 13:[5,5],
                   14:[5,6], 15:[6,3], 16:[6,5]}
        
        for i in dButton:
            if self._widgets[dButton[i][0]][dButton[i][1]]['bg']== "black":
                checkAns = "Correct"
            else:
                checkAns = "Incorrect"
        tkMessageBox.showinfo("", checkAns)
            

if __name__ == "__main__":
    app = PageTwo()
    app.mainloop()
