import tkinter as tk
import xlrd
from tkinter import messagebox


# Responsible for displaying network UI to users 

def run_network():
    messagebox.showinfo("Result", "test")


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, width=1000, height=1000)
        self.master = master
        self.grid()
        self.create_widgets()


    # Adds dropdown menus and run button as "widgets" to user interface
    def create_widgets(self):        
        workbook = xlrd.open_workbook('idmc_disaster_all_dataset.xlsx')
        sheet = workbook.sheet_by_index(0)
        region_list = []
        for i in range(2, sheet.nrows):
            region = sheet.cell(i, 0).value

            if region is not None:
                region = region.upper()
                if region not in region_list:
                    region_list.append(region)

        region_label = tk.Label(self, text="Pick Region (ISO3):")
        region_label.grid(row=0, column=0)

        tkvar = tk.StringVar(self.master)
        tkvar.set(region_list[0])
        region_drop = tk.OptionMenu(self, tkvar, *region_list)
        region_drop.grid(row=1, column=0)

        category_label = tk.Label(self, text="Pick Natural Disaster Type:")
        category_label.grid(row=2, column=0)

        # runs network from saved weights and biases when "run network" button is pressed
        btn = tk.Button(self.master, text="Run Network", command=run_network)
        btn.grid(row=3, column=0)



        tkvar = tk.StringVar(self.master)
        tkvar.set("Flood")
        category = tk.OptionMenu(self, tkvar, 'Flood', 'Extreme Temperature', 'Earthquake', 'Wet Mass Movement', 'Storm', 'Dry Mass Movement', 'Drought', 'Volcanic Eruption', 'Wildfire', 'Mass Movement', 'Volcanic Activity', 'Severe Winter Condition')
        category.grid(row=3, column=0)


root = tk.Tk()
app = Application(master=root)
app.configure(background='blue')
app.mainloop()
