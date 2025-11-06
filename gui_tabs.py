import tkinter as tk
from tkinter import ttk

class Gui_Tabs():
    def __init__(self, root):
        self.root = root

    def tabs(self):
        tab = ttk.Notebook(self.root)
        tab.pack(expand=True, fill="both")
        return tab

    def tempo_storage(self, notebook:ttk.Notebook):
        tempo_storage_tab = ttk.Frame(notebook)
        notebook.add(tempo_storage_tab, text="Piece and Tempo Storage")
        
        text_piece = tk.Label(tempo_storage_tab, text="Piece to Remember:")
        text_piece.pack(padx=8, pady=4)
        pieces_to_rember = tk.Entry(tempo_storage_tab)
        pieces_to_rember.pack(padx=8,pady=4)

        text_tempo = tk.Label(tempo_storage_tab, text="Tempo with piece:")
        text_tempo.pack(padx=8, pady=4)
        tempo_to_rember = tk.Entry(tempo_storage_tab)
        tempo_to_rember.pack(padx=16, pady=4)
        return tempo_storage_tab
    
    def meteronome_sound(self, notebook:ttk.Notebook):
        meteronome_sound_tab = ttk.Frame(notebook)
        notebook.add(meteronome_sound_tab, text="Meteronome Sound Selection")
        return meteronome_sound_tab
