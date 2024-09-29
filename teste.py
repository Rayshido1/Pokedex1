import tkinter as tk
from tkinter import ttk
from pokedex_data import pokedex  # Certifique-se de ter seus dados de pokedex aqui

class PokedexApp:
    def __init__(self, master):
        self.master = master
        master.title("Pokédex")
        master.geometry("400x400")
        master.configure(bg="#feffff")

        self.label_title = tk.Label(master, text="Pokédex", font=("Arial", 24), bg="#feffff")
        self.label_title.grid(row=0, column=0, sticky="nsew")

        self.combo_pokemon = ttk.Combobox(master, values=list(pokedex.keys()))
        self.combo_pokemon.grid(row=1, column=0, sticky="nsew")
        self.combo_pokemon.bind("<<ComboboxSelected>>", self.show_pokemon)

        # Label que será oculto inicialmente
        self.label_info = tk.Label(master, text="", justify="left", bg="#feffff")
        
        # Inicialmente, o Label não é exibido
        self.label_info.grid(row=2, column=0, sticky="nsew")
        self.label_info.grid_remove()  # Remove o Label do grid

        master.grid_rowconfigure(0, weight=1)
        master.grid_rowconfigure(1, weight=1)
        master.grid_rowconfigure(2, weight=2)
        master.grid_columnconfigure(0, weight=1)

    def show_pokemon(self, event):
        selected_pokemon = self.combo_pokemon.get()
        info = pokedex[selected_pokemon]["info"]

        self.label_info.config(text=info)
        
        # Exibe o Label
        self.label_info.grid()  # Coloca o Label no grid

if __name__ == "__main__":
    root = tk.Tk()
    app = PokedexApp(root)
    root.mainloop()
