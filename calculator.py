import tkinter as tk
from tkinter import messagebox


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("360x500")
        self.root.resizable(False, False)

        self.expression = ""

        # Display
        self.display_var = tk.StringVar()

        display = tk.Entry(
            root,
            textvariable=self.display_var,
            font=("Arial", 24),
            bd=10,
            relief=tk.RIDGE,
            justify="right"
        )
        display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=5, pady=5, ipady=15)

        # Button Layout
        buttons = [
            ['C', '(', ')', '⌫'],
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '%', '+'],
            ['', '', '=', '']
        ]

        for r in range(6):
            root.grid_rowconfigure(r + 1, weight=1)

        for c in range(4):
            root.grid_columnconfigure(c, weight=1)

        for row, values in enumerate(buttons):
            for col, value in enumerate(values):
                if value == "":
                    continue

                if value == "=":
                    btn = tk.Button(
                        root,
                        text=value,
                        font=("Arial", 18),
                        command=self.calculate,
                        bg="#4CAF50",
                        fg="white"
                    )
                    btn.grid(
                        row=row + 1,
                        column=col,
                        sticky="nsew",
                        padx=3,
                        pady=3,
                        rowspan=1
                    )

                else:
                    btn = tk.Button(
                        root,
                        text=value,
                        font=("Arial", 18),
                        command=lambda x=value: self.click(x)
                    )
                    btn.grid(
                        row=row + 1,
                        column=col,
                        sticky="nsew",
                        padx=3,
                        pady=3
                    )

        # Keyboard Support
        root.bind("<Key>", self.key_press)
        root.bind("<Return>", lambda event: self.calculate())
        root.bind("<BackSpace>", lambda event: self.backspace())
        root.bind("<Escape>", lambda event: self.clear())

    def click(self, value):
        if value == "C":
            self.clear()

        elif value == "⌫":
            self.backspace()

        elif value == "%":
            self.expression += "/100"

        else:
            self.expression += value

        self.display_var.set(self.expression)

    def clear(self):
        self.expression = ""
        self.display_var.set("")

    def backspace(self):
        self.expression = self.expression[:-1]
        self.display_var.set(self.expression)

    def calculate(self):
        try:
            result = str(eval(self.expression))
            self.display_var.set(result)
            self.expression = result
        except:
            self.display_var.set("Error")
            self.expression = ""

    def key_press(self, event):
        char = event.char

        allowed = "0123456789+-*/()."

        if char in allowed:
            self.expression += char
            self.display_var.set(self.expression)

        elif char == "%":
            self.expression += "/100"
            self.display_var.set(self.expression)


if __name__ == "__main__":
    root = tk.Tk()
    Calculator(root)
    root.mainloop()