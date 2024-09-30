import tkinter as tk
from pokedex_app import PokedexApp
from tkinter import ttk


if __name__ == "__main__":
    root = tk.Tk()
    style = ttk.Style()
    style.theme_use("clam")
    app = PokedexApp(root)
    root.mainloop()
