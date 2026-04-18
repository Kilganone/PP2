import os
import pygame
import glob

class MusicPlayer:
    def __init__(self, music_dir):
        pygame.mixer.init()

        self.music_dir = music_dir
        self.playlist = []
        self.index = 0

        self.playing = False
        self.paused = False
        self.time = 0
        self.last = 0

        self.load_tracks()

    def load_tracks(self):
        if not os.path.exists(self.music_dir):
            os.makedirs(self.music_dir)

        for ext in ("*.mp3", "*.wav", "*.ogg"):
            self.playlist += glob.glob(os.path.join(self.music_dir, ext))

    def play(self):
        if not self.playlist:
            return

        pygame.mixer.music.load(self.playlist[self.index])
        pygame.mixer.music.play()

        self.playing = True
        self.paused = False
        self.time = 0
        self.last = pygame.time.get_ticks()

    def toggle_pause(self):
        if self.paused:
            pygame.mixer.music.unpause()
            self.paused = False
            self.last = pygame.time.get_ticks()
        else:
            pygame.mixer.music.pause()
            self.paused = True

    def stop(self):
        pygame.mixer.music.stop()
        self.playing = False
        self.paused = False
        self.time = 0

    def next_track(self):
        if not self.playlist:
            return
        self.index = (self.index + 1) % len(self.playlist)
        self.play()

    def prev_track(self):
        if not self.playlist:
            return
        self.index = (self.index - 1) % len(self.playlist)
        self.play()

    def update(self):
        if self.playing and not self.paused:
            now = pygame.time.get_ticks()
            self.time += (now - self.last) / 1000
            self.last = now

            if not pygame.mixer.music.get_busy():
                self.stop()

    def get_info(self):
        if not self.playlist:
            return {
                "name": "No tracks",
                "status": "Stopped",
                "pos": 0,
                "idx": 0,
                "total": 0
            }

        status = "Playing" if self.playing else "Paused" if self.paused else "Stopped"

        return {
            "name": os.path.basename(self.playlist[self.index]),
            "status": status,
            "pos": self.time,
            "idx": self.index + 1,
            "total": len(self.playlist)
        }