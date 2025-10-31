import tkinter as tk
import pygame
import threading
pygame.init()


root = tk.Tk()


class Start_Stop_Button_Count():
    def __init__(self):
        self.count = 0
    def add_count(self):
        self.count += 1
        return self.count



def set_bpm_and_play(tempo:int=60, run):
    
    if run:
        interval = round(tempo/60)  # seconds
        threading.Timer(interval, set_bpm_and_play).start()
        print("hi")


def main():
    check = Start_Stop_Button_Count()
    def click(check=check):
        count = check.add_count()
        if count % 2 == 0:
            start_stop_button.config(text="start")
            
        elif count % 2 == 1:
            start_stop_button.config(text="stop")
            

    start_stop_button = tk.Button(text="start",
                              command=click)

    start_stop_button.pack(padx=4,pady=4)




    root.mainloop()
    pygame.quit()

main()