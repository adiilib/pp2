import pygame
import os


class MusicPlayer:
    def __init__(self, music_dir="music"):
        pygame.mixer.init()
        self.tracks = []
        self.index = 0
        self.playing = False

        if os.path.isdir(music_dir):
            for f in sorted(os.listdir(music_dir)):
                if f.endswith((".mp3", ".wav", ".ogg")):
                    self.tracks.append(os.path.join(music_dir, f))

    def current_name(self):
        if not self.tracks:
            return "No tracks found"
        return os.path.basename(self.tracks[self.index])

    def play(self):
        if not self.tracks:
            return
        pygame.mixer.music.load(self.tracks[self.index])
        pygame.mixer.music.play()
        self.playing = True

    def stop(self):
        pygame.mixer.music.stop()
        self.playing = False

    def next(self):
        if not self.tracks:
            return
        self.index = (self.index + 1) % len(self.tracks)
        if self.playing:
            self.play()

    def prev(self):
        if not self.tracks:
            return
        self.index = (self.index - 1) % len(self.tracks)
        if self.playing:
            self.play()

    def status(self):
        if not self.tracks:
            return "No tracks"
        return "Playing" if self.playing else "Stopped"
