import tkinter as tk

Large_font_style = ("Arial", 40, "bold")
Light_gray = "#F5F5F5"
Label_color = "#25265E"
Digit_Font_Size = ("Arial", 24, "bold")
Small_font_style = ("Arial", 16)
white = "#FFFFFF"
default_font_style = ("Arial", 20)
Off_white = "#F8FAFF"
Light_blue = "#CCEDFF"

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("400x650")
        self.window.resizable(0, 0)
        self.window.title("Calculator")

        self.total_expression = ""
        self.current_expression = ""

        self.digits = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            0: (4, 2), '.': (4, 1)
        }

        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}

        self.display_frame = self.create_display_frame()
        self.buttons_frame = self.create_buttons_frame()

        self.total_label, self.label = self.create_display_labels()
        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_special_buttons()

    def create_display_frame(self):
        frame = tk.Frame(self.window, height=221, bg=Light_gray)
        frame.pack(expand=True, fill="both")
        return frame

    def create_display_labels(self):
        total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E,bg=Light_gray, fg=Label_color, padx=24, font=Small_font_style)
        total_label.pack(expand=True, fill="both")

        label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E,
            bg=Light_gray, fg=Label_color, padx=24, font=Large_font_style
        )
        label.pack(expand=True, fill="both")

        return total_label, label

    def add_to_expression(self, value):
        self.current_expression += str(value)
        self.update_label()

    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(digit),bg=white, fg=Label_color, font=Digit_Font_Size,
                borderwidth=0, command=lambda x=digit: self.add_to_expression(x)
            )
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    def create_operator_buttons(self):
        operator_positions = {"/": 0, "*": 1, "-": 2, "+": 3}
        for operator, row in operator_positions.items():
            symbol = self.operations[operator]
            button = tk.Button(self.buttons_frame, text=symbol,bg=Off_white, fg=Label_color, font=default_font_style, borderwidth=0,
                command=lambda x=operator: self.add_to_expression(x)
            )
            button.grid(row=row, column=4, sticky=tk.NSEW)

    def create_clear_button(self):
        button = tk.Button(self.buttons_frame, text="C",bg=Off_white, fg=Label_color, font=default_font_style, borderwidth=0,
            command=self.clear
        )
        button.grid(row=0, column=1, sticky=tk.NSEW)

    def square(self):
        self.current_expression = str(eval(f"{self.current_expression}**2"))
        self.update_label()

    def create_square_button(self):
        button = tk.Button(self.buttons_frame, text="x\u00b2",bg=Off_white, fg=Label_color, font=default_font_style, borderwidth=0,
            command=self.square
        )
        button.grid(row=0, column=2, sticky=tk.NSEW)


    def sqrt(self):
        self.current_expression = str(eval(f"{self.current_expression}**0.5"))
        self.update_label()

    def create_sqrt_button(self):
        button = tk.Button(self.buttons_frame, text="\u221ax",bg=Off_white, fg=Label_color, font=default_font_style, borderwidth=0,
            command=self.sqrt
        )
        button.grid(row=0, column=3, sticky=tk.NSEW)


    def create_equals_button(self):
        button = tk.Button(self.buttons_frame, text="=",bg=Light_blue, fg=Label_color, font=default_font_style, borderwidth=0,
            command=self.evaluate
        )
        button.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)

    def create_special_buttons(self):
        self.create_clear_button()
        self.create_equals_button()
        self.create_square_button()
        self.create_sqrt_button()

    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")

        for i in range(5):
            frame.rowconfigure(i, weight=1)
        for j in range(5):
            frame.columnconfigure(j, weight=1)

        return frame

    def update_total_label(self):
        self.total_label.config(text=self.total_expression)

    def update_label(self):
        self.label.config(text=self.current_expression)

    def evaluate(self):
        try:
            self.total_expression = self.current_expression
            self.current_expression = str(eval(self.current_expression))
        except Exception:
            self.current_expression = "Error"
        finally:
            self.update_total_label()
            self.update_label()

    def clear(self):
        self.current_expression = ""
        self.total_expression = ""
        self.update_label()
        self.update_total_label()

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    calc = Calculator()
    calc.run()
