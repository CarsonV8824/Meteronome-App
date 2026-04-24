import threading
import pygame
pygame.mixer.init()
class Meteronome():

    def __init__(self, file='metronome_click.ogg'):
        self.timer = None
        self.running = False
        self.tempo = 60
        self.sound = pygame.mixer.Sound(file)

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
    
    def change_sound(self, sound_file):
        try:
            self.sound = pygame.mixer.Sound(sound_file)
        except pygame.error as e:
            print(f"Error loading sound file: {e}")

pygame.quit()