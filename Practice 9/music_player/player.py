import os
import pygame
import glob

class MusicPlayer:
    def __init__(self, music_dir):
        self.music_dir = music_dir
        self.playlist = []
        self.current_index = 0
        self.is_playing = False
        self.is_paused = False
        self.elapsed_time = 0.0
        self.last_update_time = 0

        pygame.mixer.init()
        self.playlist = self._scan_tracks()
        
        if not self.playlist:
            print("⚠️ Нет доступных аудиофайлов в папке 'music/'")

    def _is_valid_audio_file(self, filepath):
        try:
            pygame.mixer.music.load(filepath)
            return True
        except:
            return False

    def _scan_tracks(self):
        if not os.path.exists(self.music_dir):
            os.makedirs(self.music_dir, exist_ok=True)
            return []

        extensions = ('*.mp3', '*.wav', '*.ogg')
        all_tracks = []
        for ext in extensions:
            all_tracks.extend(glob.glob(os.path.join(self.music_dir, ext)))
        
        valid_tracks = []
        for track in sorted(all_tracks):
            if self._is_valid_audio_file(track):
                valid_tracks.append(track)
        
        return valid_tracks

    def _get_track_name(self, path):
        return os.path.splitext(os.path.basename(path))[0]

    def play(self):
        if not self.playlist: return
        
        if self.is_paused:
            self.toggle_pause()
            return

        try:
            pygame.mixer.music.load(self.playlist[self.current_index])
            pygame.mixer.music.play()
            self.is_playing = True
            self.is_paused = False
            self.elapsed_time = 0.0
            self.last_update_time = pygame.time.get_ticks()
            print(f"▶️ Playing: {self._get_track_name(self.playlist[self.current_index])}")
        except Exception as e:
            print(f"❌ Ошибка воспроизведения: {e}")
            self.is_playing = False
            if len(self.playlist) > 1:
                self.next_track()

    def toggle_pause(self):
        if not self.playlist: return

        if self.is_playing and not self.is_paused:
            pygame.mixer.music.pause()
            self.is_paused = True
            print("⏸️ Paused")
        elif self.is_paused:
            pygame.mixer.music.unpause()
            self.is_paused = False
            self.last_update_time = pygame.time.get_ticks()
            print("▶️ Resumed")

    def stop(self):
        pygame.mixer.music.stop()
        self.is_playing = False
        self.is_paused = False
        self.elapsed_time = 0.0
        self.last_update_time = 0

    def next_track(self):
        if not self.playlist: return
        self.current_index = (self.current_index + 1) % len(self.playlist)
        self.is_paused = False
        self.play()

    def prev_track(self):
        if not self.playlist: return
        self.current_index = (self.current_index - 1) % len(self.playlist)
        self.is_paused = False
        self.play()

    def update(self):
        if self.is_playing and not self.is_paused:
            now = pygame.time.get_ticks()
            self.elapsed_time += (now - self.last_update_time) / 1000.0
            self.last_update_time = now
            
            if not pygame.mixer.music.get_busy():
                self.stop()

    def get_info(self):
        if not self.playlist:
            return {"name": "Нет треков", "status": "Stopped", "pos": 0, "idx": 0, "total": 0}

        if self.is_paused:
            status = "Paused"
        elif self.is_playing:
            status = "Playing"
        else:
            status = "Stopped"

        return {
            "name": self._get_track_name(self.playlist[self.current_index]),
            "status": status,
            "pos": self.elapsed_time,
            "idx": self.current_index + 1,
            "total": len(self.playlist)
        }