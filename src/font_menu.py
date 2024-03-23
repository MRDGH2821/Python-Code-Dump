"""Font menu."""

import tkinter as tk
from tkinter import ttk

win = tk.Tk()
main_menu = tk.Menu(win)
win.config(menu=main_menu)
format_menu = tk.Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="Format", menu=format_menu)


class FontMenu(tk.Toplevel):
    """Font menu GUI."""

    def __init__(self) -> None:
        """Initialize FontMenu."""
        tk.Toplevel.__init__(self)
        self.find_popup = tk.Toplevel()
        self.find_popup.geometry("450x200")
        self.find_popup.title("Fonts")
        self.find_popup.resizable(width=False, height=False)
        # Frame for find
        self.find_frame = ttk.LabelFrame(self.find_popup, text="Font Style")
        self.font_style = tk.StringVar()
        self.font_style_box = ttk.Combobox(
            self.find_frame,
            width=14,
            textvariable=self.font_style,
            state="readonly",
        )
        self.font_style_box["values"] = (1, 2, 3)
        self.font_style_box.current(0)
        self.font_style_box.pack()
        self.find_frame.pack(pady=20)
        self.find_popup.update()
        format_menu.add_command(label="Font", command=FontMenu)  # font_func)
        win.mainloop()


p = FontMenu()
