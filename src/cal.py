import tkinter as tk
from tkinter import font
from src.Calculator import Calculator


class CalculatorApp:
    """Tkinter GUI for the Calculator."""

    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Calculator")
        self.root.resizable(False, False)
        self.root.configure(bg="#1e1e2e")

        self.calc = Calculator()
        self.expression = ""
        self._build_ui()

    def _build_ui(self):
        display_font = font.Font(family="Courier New", size=28, weight="bold")
        btn_font = font.Font(family="Courier New", size=16, weight="bold")

        # Display
        self.display_var = tk.StringVar(value="0")
        display_frame = tk.Frame(self.root, bg="#1e1e2e", pady=10, padx=10)
        display_frame.pack(fill="x")

        tk.Label(
            display_frame,
            textvariable=self.display_var,
            font=display_font,
            bg="#2a2a3e",
            fg="#cdd6f4",
            anchor="e",
            padx=15,
            pady=15,
            relief="flat",
        ).pack(fill="x")

        # Button layout
        buttons = [
            ["C", "±", "%", "÷"],
            ["7", "8", "9", "×"],
            ["4", "5", "6", "−"],
            ["1", "2", "3", "+"],
            ["0", ".", "⌫", "="],
        ]

        colors = {
            "operator": {"bg": "#f38ba8", "fg": "#1e1e2e", "active": "#eb6e91"},
            "action": {"bg": "#585b70", "fg": "#cdd6f4", "active": "#6c6f85"},
            "number": {"bg": "#313244", "fg": "#cdd6f4", "active": "#45475a"},
            "equals": {"bg": "#a6e3a1", "fg": "#1e1e2e", "active": "#8fd99a"},
        }

        grid_frame = tk.Frame(self.root, bg="#1e1e2e", padx=10, pady=5)
        grid_frame.pack()

        for r, row in enumerate(buttons):
            for c, label in enumerate(row):
                style = (
                    "equals"
                    if label == "="
                    else "operator"
                    if label in ("÷", "×", "−", "+")
                    else "action"
                    if label in ("C", "±", "%", "⌫")
                    else "number"
                )
                s = colors[style]
                btn = tk.Button(
                    grid_frame,
                    text=label,
                    font=btn_font,
                    bg=s["bg"],
                    fg=s["fg"],
                    activebackground=s["active"],
                    activeforeground=s["fg"],
                    relief="flat",
                    width=4,
                    height=2,
                    cursor="hand2",
                    command=lambda lbl=label: self._on_click(lbl),
                )
                btn.grid(row=r, column=c, padx=4, pady=4)

    def _on_click(self, label: str):
        expr = self.expression

        if label == "C":
            self.expression = ""
            self.display_var.set("0")

        elif label == "⌫":
            self.expression = expr[:-1]
            self.display_var.set(self.expression or "0")

        elif label == "±":
            if expr.startswith("-"):
                self.expression = expr[1:]
            elif expr:
                self.expression = "-" + expr
            self.display_var.set(self.expression or "0")

        elif label == "%":
            try:
                val = float(expr) / 100
                self.expression = str(val)
                self.display_var.set(self.expression)
            except ValueError:
                self.display_var.set("Error")
                self.expression = ""

        elif label == "=":
            try:
                # Replace display symbols with Python operators
                py_expr = (
                    expr.replace("÷", "/")
                    .replace("×", "*")
                    .replace("−", "-")
                )
                # safe: only digits & operators
                result = eval(py_expr, {"__builtins__": None}, {})
                # Clean up float display
                if isinstance(result, float) and result.is_integer():
                    result = int(result)
                self.expression = str(result)
                self.display_var.set(self.expression)
            except ZeroDivisionError:
                self.display_var.set("÷ by 0!")
                self.expression = ""
            except Exception:
                self.display_var.set("Error")
                self.expression = ""

        else:
            self.expression = expr + label
            self.display_var.set(self.expression)


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()