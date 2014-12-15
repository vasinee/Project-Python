import Tkinter as tk
import tkMessageBox
class PageTwo(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        t = Button_Table(self, 6,8)
        t.pack(side="top", fill="x")
        check = tk.Button(self, text= "check",command=lambda: t.checkButton())
        check.pack(pady = 5)
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
                    label = tk.Label(self,width=6, height=3, bg= "#ffffff")
                    label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
                    current_row.append(label)
                else:
                    button = tk.Button(self, width=6, height=3,command=lambda a=row,b=column: self.onButtonPressed(a,b))
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
    app = PageTwo()
    app.mainloop()
