import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import pygame
from meteronome import Meteronome
from PIL import Image, ImageTk
import io
from image_database import PhotoDatabase

pygame.mixer.init()

class Gui_Tabs():
    def __init__(self, root:tk.Tk, list_of_pieces:list[tuple[str,str,str]] = []):
       self.list_of_pieces = list_of_pieces
       self.root = root
       self.image_connection = PhotoDatabase()
       try:
           self.images = [row[1] for row in self.image_connection.get_data()]
       except Exception:
            self.images = []
       
       self.photo_refs = []
        
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
        frame.pack()
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
        
        text_section_piece = tk.Label(frame, text="Section of Piece:")
        text_section_piece.pack(padx=8, pady=4)
        
        section_to_rember = tk.Entry(frame)
        section_to_rember.pack(padx=16, pady=4)

        text_tempo = tk.Label(frame, text="Tempo with piece:")
        text_tempo.pack(padx=8, pady=4)
        tempo_to_rember = tk.Entry(frame)
        tempo_to_rember.pack(padx=16, pady=4)

        def clear_data():
            self.list_of_pieces = []
            data_listbox.delete(0, tk.END)
            length_of_data.clear()
            data_listbox.config(width=10)


        clear_button = tk.Button(frame, text="Clear Data", command=clear_data)
        clear_button.pack(padx=8, pady=4)

        list_text = tk.Label(frame, text="List of Data:")
        list_text.pack(padx=8, pady=4)
        
        def add_data():
            data_listbox.delete(0, tk.END)
            
            piece = pieces_to_rember.get()
            section = section_to_rember.get()
            tempo = tempo_to_rember.get()
            
            if piece == "" or section == "" or tempo == "":
                pass
            else:
            
                self.list_of_pieces.append((piece, section, tempo))

                for i in self.list_of_pieces:
                    data = f"Piece: {i[0]}, Section: {i[1]}, Tempo: {i[2]} BPM"
                    length_of_data.append(len(data))
                    data_listbox.insert(tk.END, data)
                data_listbox.config(width=max(length_of_data))

        
        def delete_selected_item(event):
            
            selected_indices = data_listbox.curselection()
            if not selected_indices:
                return

            index = selected_indices[0]
            
            data_listbox.delete(index)
            if 0 <= index < len(self.list_of_pieces):
                self.list_of_pieces.pop(index)
            if 0 <= index < len(length_of_data):
                length_of_data.pop(index)

            data_listbox.config(width=max(length_of_data) if length_of_data else 10)

        self.root.bind('<Return>', lambda event: add_data())
        
        data_listbox.bind("<<ListboxSelect>>", delete_selected_item)


        data_listbox.pack(padx=8, pady=4)

        return tempo_storage_tab
    
    def return_list_of_pieces(self):
        return self.list_of_pieces


    def meteronome_sound(self, notebook:ttk.Notebook, meteronome_instance:Meteronome=Meteronome()):
        meteronome_sound_tab = ttk.Frame(notebook)
        notebook.add(meteronome_sound_tab, text="Meteronome Sound Settings")

        canvas = tk.Canvas(meteronome_sound_tab)
        scrollbar = ttk.Scrollbar(meteronome_sound_tab, orient="vertical", command=canvas.yview)
        scrollable_frame_a = ttk.Frame(canvas)

        scrollable_frame_a.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        canvas.create_window((0, 0), window=scrollable_frame_a, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        frame = tk.Frame(scrollable_frame_a)
        frame.pack()
       
        #=======================================================================================================#

        default_button = tk.Button(frame, text="Default", command=lambda:self.change_meteronome_sound('metronome_click.ogg', meteronome_instance))
        default_button.pack(side="top", padx=8, pady=4)

        wood_block_button = tk.Button(frame, text="Woodblock", command=lambda:self.change_meteronome_sound('wood_block.ogg', meteronome_instance))
        wood_block_button.pack(side="top", padx=8, pady=4)

        return meteronome_sound_tab

    def change_meteronome_sound(self, sound_file, meteronome_instance):
        try:
            meteronome_instance.change_sound(sound_file)
        except pygame.error as e:
            print(f"Error loading sound file: {e}")

    def upload_music(self, notebook:ttk.Notebook):
        
        upload_music_tab = ttk.Frame(notebook)
        notebook.add(upload_music_tab, text="Upload Music Tab")

        canvas = tk.Canvas(upload_music_tab)
        scrollbar = ttk.Scrollbar(upload_music_tab, orient="vertical", command=canvas.yview)
        scrollable_frame_a = ttk.Frame(canvas)

        scrollable_frame_a.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        canvas.create_window((0, 0), window=scrollable_frame_a, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        frame = tk.Frame(scrollable_frame_a)
        frame.pack()

        #===================================================================================
            
        image_choose_button = tk.Button(frame, text="Upload Image", command=lambda:self.open_image(image_holder_canvas=image_holder_canvas))
        image_choose_button.pack()

        image_clear_button = tk.Button(frame, text="Clear Images", command=lambda:self.clear_images(image_holder_canvas=image_holder_canvas))
        image_clear_button.pack()

        image_holder_canvas = ttk.Frame(frame)
        image_holder_canvas.pack()

        if self.images != []:
            for saved_image in self.images:
                real_image = Image.open(io.BytesIO(saved_image))  # Use saved_image directly
                photo = ImageTk.PhotoImage(real_image)
                lbl = tk.Label(image_holder_canvas, image=photo)
                lbl.pack()
                self.photo_refs.append(photo)

        return upload_music_tab
    
    def open_image(self, image_holder_canvas):
        file_path = filedialog.askopenfilename(
            filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif")]
        )
        if not file_path:
            return

        img = Image.open(file_path)
        self.root.update_idletasks()
        #root_width = self.root.winfo_width()
        orig_width, orig_height = img.size
        max_width = min(self.root.winfo_width(), orig_width)
        if orig_width > max_width:
            new_height = int((max_width / orig_width) * orig_height)
            img_resized = img.resize((max_width, new_height), Image.LANCZOS)
        else:
            img_resized = img

        # Save as BLOB
        buffer = io.BytesIO()
        img_resized.save(buffer, format='PNG')
        image_blob = buffer.getvalue()
        self.images.append(image_blob)
        self.image_connection.add_data(image_blob)  # Only once

        # Clear previous images in the holder
        for widget in image_holder_canvas.winfo_children():
            widget.destroy()
        self.photo_refs = []

        # Display all images from the list
        for image_bytes in self.images:
            real_image = Image.open(io.BytesIO(image_bytes))
            photo = ImageTk.PhotoImage(real_image)
            lbl = tk.Label(image_holder_canvas, image=photo)
            lbl.pack()
            self.photo_refs.append(photo)

    def clear_images(self, image_holder_canvas):
        
        for widget in image_holder_canvas.winfo_children():
            widget.destroy()
            
            self.images = []
            self.photo_refs = []
            
            self.image_connection.clear_data()

pygame.quit()
