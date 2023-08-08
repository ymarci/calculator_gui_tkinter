# Bibliothek Einbindung
import tkinter
import tkinter as tk
from tkinter import ttk

# Fenstereinstellungen
root = tk.Tk()
root.geometry("290x275")
root.title("Rechner")

# Variablen

text_result = tk.Text(root, height=2, width=16, font=("Times",24), bg="#9FFFFF", foreground="blue")
text_result.grid(columnspan=5)

calculation = ""

# Funktionen

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert (1.0, calculation)

def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "Fehler")

def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")


# Buttons 0 - 9

button1 = tk.Button(root, text="1", command=lambda: add_to_calculation(1), width=5, font="Times")
button1.grid(row=2, column=1)
button2 = tk.Button(root, text="2", command=lambda: add_to_calculation(2), width=5, font="Times")
button2.grid(row=2, column=2)
button3 = tk.Button(root, text="3", command=lambda: add_to_calculation(3), width=5, font="Times")
button3.grid(row=2, column=3)
button4 = tk.Button(root, text="4", command=lambda: add_to_calculation(4), width=5, font="Times")
button4.grid(row=3, column=1)
button5 = tk.Button(root, text="5", command=lambda: add_to_calculation(5), width=5, font="Times")
button5.grid(row=3, column=2)
button6 = tk.Button(root, text="6", command=lambda: add_to_calculation(6), width=5, font="Times")
button6.grid(row=3, column=3)
button7 = tk.Button(root, text="7", command=lambda: add_to_calculation(7), width=5, font="Times")
button7.grid(row=4, column=1)
button8 = tk.Button(root, text="8", command=lambda: add_to_calculation(8), width=5, font="Times")
button8.grid(row=4, column=2)
button9 = tk.Button(root, text="9", command=lambda: add_to_calculation(9), width=5, font="Times")
button9.grid(row=4, column=3)
button0 = tk.Button(root, text="0", command=lambda: add_to_calculation(0), width=5, font="Times")
button0.grid(row=5, column=2)

# Buttons  Rechenoperatoren

buttonplus = tk.Button(root, text="+", command=lambda: add_to_calculation("+"), width=5, font="Arial")
buttonplus.grid(row=2, column=4)
buttonminus = tk.Button(root, text="-", command=lambda: add_to_calculation("-"), width=5, font="Arial")
buttonminus.grid(row=3, column=4)
buttonmultiplikation = tk.Button(root, text="*", command=lambda: add_to_calculation("*"), width=5, font="Arial")
buttonmultiplikation.grid(row=4, column=4)
buttondivision = tk.Button(root, text="/", command=lambda: add_to_calculation("/"), width=5, font="Arial")
buttondivision.grid(row=5, column=4)

# Weitere Operatoren

buttonklammer = tk.Button(root, text="(", command=lambda: add_to_calculation("("), width=5, font="Arial")
buttonklammer.grid(row=5, column=1)
buttonklammer2 = tk.Button(root, text=")", command=lambda: add_to_calculation(")"), width=5, font="Arial")
buttonklammer2.grid(row=5, column=3)
buttongleich = tk.Button(root, text="=", command=evaluate_calculation, width=13, font="Arial")
buttongleich.grid(row=6, column=3, columnspan=2)
buttonlöschen = tk.Button(root, text="Löschen", command=clear_field, width=13, font="Arial")
buttonlöschen.grid(row=6, column=1, columnspan=2)

buttonquit = tk.Button(root, text="Verlassen", width=28, font="Arial", command=quit)
buttonquit.grid(row=7, column=1, columnspan=4)

# Endlosschleife

root.mainloop()