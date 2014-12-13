import Tkinter as tk

class show_table_but(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        t = Button_Table(self, 6,6)
        t.pack(side="top", fill="x" ,padx=30, pady=30)

class Button_Table(tk.Frame):
    def __init__(self, parent, rows, columns):
        # form grid lines
        tk.Frame.__init__(self, parent)
        self._widgets = []
        for row in range(rows):
            current_row = []
            for column in range(columns):
                if row == 0 or column == 0:
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

if __name__ == "__main__":
    app = show_table_but()
    app.mainloop()
