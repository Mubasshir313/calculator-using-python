# calculator_with_visualization.py

import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x600")
        self.expression = ""
        self.history = []

        self.input_text = tk.StringVar()
        self.input_frame = self.create_input_frame()
        self.buttons_frame = self.create_buttons_frame()

        self.create_input_field()
        self.create_buttons()

    def create_input_frame(self):
        frame = tk.Frame(self.root, height=100, bg="lightgrey")
        frame.pack(expand=True, fill="both")
        return frame

    def create_buttons_frame(self):
        frame = tk.Frame(self.root)
        frame.pack(expand=True, fill="both")
        return frame

    def create_input_field(self):
        input_field = tk.Entry(self.input_frame, textvariable=self.input_text, font=('arial', 18, 'bold'), bg="white", bd=10, justify="right")
        input_field.grid(row=0, column=0, ipadx=8, ipady=8, sticky="nsew")

    def create_buttons(self):
        buttons = [
            '7', '8', '9', '/', 'C',
            '4', '5', '6', '*', 'H',
            '1', '2', '3', '-', '=',
            '0', '.', '+'
        ]

        row = 0
        col = 0
        for button in buttons:
            if button == '=':
                btn = tk.Button(self.buttons_frame, text=button, font=('arial', 18, 'bold'), bg="lightblue", fg="black", bd=1, command=self.evaluate)
            elif button == 'C':
                btn = tk.Button(self.buttons_frame, text=button, font=('arial', 18, 'bold'), bg="lightcoral", fg="black", bd=1, command=self.clear)
            elif button == 'H':
                btn = tk.Button(self.buttons_frame, text=button, font=('arial', 18, 'bold'), bg="lightgreen", fg="black", bd=1, command=self.show_history)
            else:
                btn = tk.Button(self.buttons_frame, text=button, font=('arial', 18, 'bold'), bg="white", fg="black", bd=1, command=lambda x=button: self.append_expression(x))

            btn.grid(row=row, column=col, ipadx=20, ipady=20, sticky="nsew")
            col += 1
            if col > 4:
                col = 0
                row += 1

        for i in range(5):
            self.buttons_frame.grid_columnconfigure(i, weight=1)
        for i in range(4):
            self.buttons_frame.grid_rowconfigure(i, weight=1)

    def append_expression(self, value):
        self.expression += str(value)
        self.input_text.set(self.expression)

    def clear(self):
        self.expression = ""
        self.input_text.set("")

    def evaluate(self):
        try:
            result = str(eval(self.expression))
            self.history.append(self.expression + " = " + result)
            self.input_text.set(result)
            self.expression = result
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input")
            self.expression = ""
            self.input_text.set("")

    def show_history(self):
        if not self.history:
            messagebox.showinfo("History", "No history available")
            return

        completed = len(self.history)
        pending = 0  # No pending tasks in this context
        labels = 'Completed', 'Pending'
        sizes = [completed, pending]
        colors = ['#4CAF50', '#FF5722']
        explode = (0.1, 0)  # explode the 1st slice (Completed)

        plt.pie(sizes, explode=explode, labels=labels, colors=colors,
                autopct='%1.1f%%', shadow=True, startangle=140)
        plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.title('Calculation History')
        plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
