import tkinter as tk
import pygame
import threading
from gui_tabs import Gui_Tabs
from meteronome import Meteronome
from database_class import Database

pygame.mixer.init()

root = tk.Tk()

class Start_Stop_Button_Count():
    def __init__(self):
        self.count = 0
    def add_count(self):
        self.count += 1
        return self.count

database = Database()

check = Start_Stop_Button_Count()
meteronome = Meteronome()
gui_tabs = Gui_Tabs(root, list(database.get_all_entries()))

database.delete_all_entries()
def main():
    


    #label that lists the tempo marking
    tempo_label = tk.Label(text="60",)
    tempo_label.pack(padx=4,pady=4)

    #user input of tempo they want
    input_of_tempo = tk.Entry(root)
    input_of_tempo.pack(padx=8,pady=4)
    input_of_tempo.insert(0,60)

    

    #starts and stops click and change tempo command
    def start_stop_click(label_value = int(input_of_tempo.get())):
        
        meteronome.stop_metronome()
        meteronome.start_metronome(label_value)
        tempo_label.config(text = input_of_tempo.get())
        count = check.add_count()
        if count % 2 == 0:
            start_stop_button.config(text="start")
            meteronome.stop_metronome()
            
        elif count % 2 == 1:
            start_stop_button.config(text="stop")
            meteronome.stop_metronome()
            meteronome.start_metronome(int(input_of_tempo.get()))
            

    #button for changing tempo and on and off
    start_stop_button = tk.Button(text="start",
                              command=start_stop_click)

    start_stop_button.pack(padx=6,pady=4)


    #Gui tab stuff
    
    notebook = gui_tabs.tabs()
    
    gui_tabs.tempo_storage(notebook)
    
    
    gui_tabs.meteronome_sound(notebook)


    root.mainloop()
    meteronome.stop_metronome()
    pygame.quit()

    gui_tabs_data = gui_tabs.return_list_of_pieces()
    print(gui_tabs_data)
    if gui_tabs_data == []:
        database.delete_all_entries()
    else:
        print(gui_tabs_data)
        for i in gui_tabs_data:
            if i not in database.get_all_entries():
                database.add_entry(i[0], i[1], i[2])

if __name__ == "__main__":
    main()
