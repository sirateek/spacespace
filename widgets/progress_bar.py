import tkinter as tk
import tkinter.ttk as ttk


class ProgressBar(tk.Frame):
    def __init__(self, parent, length=300, init_progress_value=0, progress_bar_mode="determinate"):
        super().__init__(parent)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure("bar.Horizontal.TProgressbar",
                             background='orange')
        self.progress_value = tk.IntVar()
        self.progress_value.set(init_progress_value)
        self.progress_bar = ttk.Progressbar(
            self, length=length, style="bar.Horizontal.TProgressbar", variable=self.progress_value, mode=progress_bar_mode)
        self.progress_bar.grid(row=0, column=0, sticky="NEWS")

    def change_progress_value(self, value, time_interval=30):
        assert type(value) == int, "The type of the value must be int!"
        value_old = self.progress_value.get()
        self.progress_bar.update()
        if value_old == value:
            return
        new_value = value_old - 1 if value_old > value else value_old + 1
        self.progress_value.set(new_value)
        self.after(time_interval, lambda: self.change_progress_value(
            value, time_interval),)

    @property
    def value(self):
        return self.progress_value.get()

    @value.setter
    def value(self, value):
        self.progress_value.set(value if value <= 100 else 100)
