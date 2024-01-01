import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Resistance")
window.geometry("350x250")
window.config(background="#57a1f8")
window.resizable(False, False)


######### ---------------------- CLASS DEFINATION ----------------------------
class Resistor:
    colourCode = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
    combination = ''
    cc1 = ''
    cc2 = ''
    cc3 = ''

    def __init__(self, colour1, colour2, colour3):
        self.resistance(colour1, colour2, colour3)

    def resistance(self, colour1, colour2, colour3):
        self.colour1 = colour1.lower()
        self.colour2 = colour2.lower()
        self.colour3 = colour3.lower()

    def set_resistance(self):
        j = 0
        while j < 10:
            if self.colourCode[j] == self.colour1:
                self.cc1 = str(j)
            elif Resistor.colourCode[j] == self.colour2:
                self.cc2 = str(j)
            elif self.colourCode[j] == self.colour3:
                self.cc3 = str(j)
            j += 1

        self.combination = self.cc1 + self.cc2

    def get_resistance(self):
        return int(self.combination) * self.multiplier(int(self.cc3))

    def multiplier(self, m):
        return 10 ** m


######### -------------- CREATING AN INSTANCE OF CLASS RESISTOR ---------------
# Example usage
resistor = Resistor("black", "brown", "red")


######### --------------- FUNCTIONAL PART OF THE INTERFACE ------------------
def submit():
    colour_entry = entry_var.get()
    colour_entry1 = entry1_var.get()
    colour_entry2 = entry2_var.get()

    if colour_entry == '' or colour_entry1 == '' or colour_entry2 == '':
        messagebox.showwarning(title='WARNING',message='Select all the fields')
    else:
        resistor.resistance(colour_entry, colour_entry1, colour_entry2)
        resistor.set_resistance()
        display_resistance = resistor.get_resistance()
        label6 = tk.Label(window,text="Resistance in Ohms: " + str(display_resistance))
        label6.grid(row=4, column=0, columnspan=2)


######### --------------------------------- GUI PART ---------------------------------------------
label = tk.Label(window,padx=45,pady=8, bg='#57a1f8',text="Select the first colour code")
label.grid(row=0, column=0)
entry_var = tk.StringVar()
entry = tk.OptionMenu(window, entry_var, *Resistor.colourCode)
entry.grid(row=0, column=1)
entry.config(border=0,bg='#57a1f8',cursor='hand2',fg='grey')

label1 = tk.Label(window,bg='#57a1f8', pady=8,text="Select the second colour code")
label1.grid(row=1, column=0)
entry1_var = tk.StringVar()
entry1 = tk.OptionMenu(window, entry1_var, *Resistor.colourCode)
entry1.grid(row=1, column=1)
entry1.config(border=0,bg='#57a1f8',cursor='hand2',fg='grey')

label2 = tk.Label(window,bg='#57a1f8',pady=8, text="Select the third colour codes")
label2.grid(row=2, column=0)
entry2_var = tk.StringVar()
entry2 = tk.OptionMenu(window, entry2_var, *Resistor.colourCode)
entry2.grid(row=2, column=1)
entry2.config(border=0,bg='#57a1f8',cursor='hand2',fg='grey')

button = tk.Button(window,bg='black',fg='#57a1f8', text="Calculate", command=submit,cursor='hand2',border=0)
button.grid(row=3, column=0, columnspan=2)

window.mainloop()
