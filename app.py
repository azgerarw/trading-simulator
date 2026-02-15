from tkinter import *
from frontend.gui.frames import init_frames
import ttkbootstrap as ttk # type: ignore
from ttkbootstrap.constants import * # type: ignore

root = Tk()

style = ttk.Style("cyborg")
root.title("app")
root.geometry("1200x650")

root.columnconfigure(0, weight=1, minsize=400)
root.columnconfigure(1, weight=1, minsize=800)
root.rowconfigure(0, weight=1, minsize=400)

init_frames(root)

root.update_idletasks()

if __name__ == "__main__":
    root.mainloop()