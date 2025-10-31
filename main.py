import tkinter as tk
import pygame
import threading
pygame.mixer.init()


root = tk.Tk()

class Start_Stop_Button_Count():
    def __init__(self):
        self.count = 0
    def add_count(self):
        self.count += 1
        return self.count

class Meteronome():
    
    def __init__(self):
        self.timer = None
        self.running = False
        self.tempo = 60
        self.sound = pygame.mixer.Sound('metronome_click.ogg')
    
    def set_bpm_and_play(self,tempo: int = 60):
        

        if not self.running:
            return  # stop ticking if not running

        print("Tick")
        self.sound.play(0)  # this is where you'd play a sound

    # Schedule the next tick
        self.tempo = tempo
        interval = 60 / self.tempo  # seconds per beat
        self.timer = threading.Timer(interval, self.set_bpm_and_play, args=[tempo])
        self.timer.start()
        
        

    def start_metronome(self,tempo: int = 60):
        """Start ticking at the given tempo."""
   
        self.running = True
        self.set_bpm_and_play(tempo)
        

    def stop_metronome(self):
        """Stop the metronome."""
        
        self.running = False
        if self.timer:
            self.timer.cancel()
        self.sound.stop()
    def get_tempo(self):
        return self.tempo
     

check = Start_Stop_Button_Count()
meteronome = Meteronome()

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

    
    
    root.mainloop()
    meteronome.stop_metronome()
    pygame.quit()
    

main()