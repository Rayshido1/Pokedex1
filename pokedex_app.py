import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import requests                          #biblioteca para comunicação com a web
from io import BytesIO                   #biblioteca para ler o objeto imagem em bytes
from pokedex_data import pokedex


class PokedexApp:
    def __init__(self, master):
        self.master = master
        master.title("Pokédex")
        master.geometry("400x400")
        master.configure(bg="#feffff")
  
        self.label_title = tk.Label(master, text="Pokédex", font=("Arial", 24), bg="#feffff", bd=0)
        self.label_title.grid(row=0, column=0, sticky="nsew")

        self.combo_pokemon = ttk.Combobox(master, values=list(pokedex.keys()))
        self.combo_pokemon.grid(row=1, column=0, sticky="n")
        self.combo_pokemon.bind("<<ComboboxSelected>>", self.show_pokemon)

        self.label_image = tk.Label(master, bg="#feffff", bd=0)
        self.label_image.grid(row=2, column=0, sticky="nsew")
        
        self.frame_line = tk.Frame(master, height=1,bg="black")
        self.frame_line.grid(row=3, column=0, pady=(10, 0), sticky="nsew")
        self.frame_line.grid_remove()

        self.label_info = tk.Label(master, text="", justify="left", bg="#feffff", bd=20, anchor="center", font=("Arialblack", 10))
        self.label_info.grid(row=4, column=0, sticky="nsew")

        master.bind("<Escape>", self.reset_interface)
        master.bind("<Alt-F4>", self.close_aplication)
        master.bind("<Right>", lambda event: self.change_pokemon("right"))
        master.bind("<Left>", lambda event: self.change_pokemon("left"))

        master.grid_rowconfigure(0, weight=1)  # Título
        master.grid_rowconfigure(1, weight=1)  # Combobox
        master.grid_rowconfigure(2, weight=2)  # Imagem
        master.grid_columnconfigure(3, weight=0)  # Coluna
        master.grid_rowconfigure(4, weight=2)  # Informações
        master.grid_columnconfigure(0, weight=5)  # linha de divisão
                                                         

    def show_pokemon(self, event):
        selected_pokemon = self.combo_pokemon.get()
        info = pokedex[selected_pokemon]["info"]
        image_url = pokedex[selected_pokemon]["image"]
        color = pokedex[selected_pokemon]["color"]

        self.label_info.config(text=info)
        self.master.configure(bg=color)
        self.frame_line.grid()

        response = requests.get(image_url)                       #armazena os dados da imagem da web
        img_data = Image.open(BytesIO(response.content))         #armazena os dados em bytes da imagem
        img_data = img_data.resize((150,150), Image.LANCZOS)
        img = ImageTk.PhotoImage(img_data)                       #converte a imagem pillow para uma versão do tkinter

        self.label_image.config(image=img)
        self.label_image.image = img                             # Manter referência da imagem

        self.label_title.config(bg=color)                        # Inclui a cor ao fundo do label         
        self.label_image.config(bg=color)
    
    def change_pokemon(self, direction):
        current_index = self.combo_pokemon.current()
        if direction == "right":
            new_index = (current_index + 1) % len(self.combo_pokemon["values"])
        elif direction == "left":
            new_index = (current_index - 1) % len(self.combo_pokemon["values"])
        self.combo_pokemon.current(new_index)
        self.show_pokemon(None)
    
    def reset_interface(self, event): #Remove os valores da interface
        self.combo_pokemon.set("")
        self.label_info.config(text="", bg="#feffff")
        self.master.configure(bg="#feffff")
        self.label_title.config(bg="#feffff")
        self.label_image.config(image="", bg="#feffff")
        self.frame_line.grid_remove()

    def close_aplication(self, event):
        self.master.quit()     
     

