import tkinter as tk
from tkinter import ttk

class Gui_Tabs():
    def __init__(self, root, list_of_pieces:list[tuple[str,str,str]] = []):
        self.root = root
        self.list_of_pieces = list_of_pieces
        
    def tabs(self):
        tab = ttk.Notebook(self.root)
        tab.pack(expand=True, fill="both")
        return tab

    def tempo_storage(self, notebook:ttk.Notebook,):
        

        
        tempo_storage_tab = ttk.Frame(notebook)
        notebook.add(tempo_storage_tab, text="Piece and Tempo Storage")

        canvas = tk.Canvas(tempo_storage_tab)
        scrollbar = ttk.Scrollbar(tempo_storage_tab, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        frame = tk.Frame(scrollable_frame)
        
        #=======================================================================================================#
        
        length_of_data = []
        data_listbox = tk.Listbox(frame, width=10)
        for i in range(len(self.list_of_pieces)):
            data = f"Piece: {self.list_of_pieces[i][0]}, Section: {self.list_of_pieces[i][1]}, Tempo: {self.list_of_pieces[i][2]} BPM"
            length_of_data.append(len(data))
            data_listbox.insert(tk.END, data)
            data_listbox.config(width=max(length_of_data))
        
        text_piece = tk.Label(frame, text="Piece to Remember:")
        text_piece.pack(padx=8, pady=4)
        pieces_to_rember = tk.Entry(frame)
        pieces_to_rember.pack(padx=8,pady=4)
        frame.pack()

        text_section_piece = tk.Label(frame, text="Section of Piece:")
        text_section_piece.pack(padx=8, pady=4)
        
        section_to_rember = tk.Entry(frame)
        section_to_rember.pack(padx=16, pady=4)

        text_tempo = tk.Label(frame, text="Tempo with piece:")
        text_tempo.pack(padx=8, pady=4)
        tempo_to_rember = tk.Entry(frame)
        tempo_to_rember.pack(padx=16, pady=4)

        clear_button = tk.Button(frame, text="Clear Data", command=lambda: data_listbox.delete(0, tk.END))
        clear_button.pack(padx=8, pady=4)

        list_text = tk.Label(frame, text="List of Data:")
        list_text.pack(padx=8, pady=4)
        
        def add_data():
            data_listbox.delete(0, tk.END)
            
            piece = pieces_to_rember.get()
            section = section_to_rember.get()
            tempo = tempo_to_rember.get()
            
            data = f"Piece: {piece}, Section: {section}, Tempo: {tempo} BPM"
            
            self.list_of_pieces.append((piece, section, tempo))
            
            length_of_data = [len(i) for i in self.list_of_pieces]
            
            data_listbox.config(width=max(length_of_data))
    
            for i in self.list_of_pieces:
                data = f"Piece: {i[0]}, Section: {i[1]}, Tempo: {i[2]} BPM"
                length_of_data.append(len(data))
                data_listbox.insert(tk.END, data)
                data_listbox.config(width=max(length_of_data))

        self.root.bind('<Return>', lambda event: add_data())

        
        data_listbox.pack(padx=8, pady=4)

        return tempo_storage_tab
    
    def return_list_of_pieces(self):
        return self.list_of_pieces
    
    
    def meteronome_sound(self, notebook:ttk.Notebook):
        meteronome_sound_tab = ttk.Frame(notebook)
        notebook.add(meteronome_sound_tab, text="Meteronome Sound Selection")
        return meteronome_sound_tab
