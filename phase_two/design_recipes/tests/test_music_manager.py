# File: tests/test_music_manager

from lib.music_manager import *

def test_music_manager_one_track():
    manager = MusicManager()
    manager.add_track("Arabesque", "Lily Chou-Chou")
    result = manager.view_tracks()
    assert result == ("Arabesque by Lily Chou-Chou")

def test_music_manager_two_tracks():
    manager = MusicManager()
    manager.add_track("Arabesque", "Lily Chou-Chou")
    manager.add_track("Porcelain", "Ichiko Aoba")
    result = manager.view_tracks()
    assert result == ("Arabesque by Lily Chou-Chou\nPorcelain by Ichiko Aoba")

def test_music_manager_no_tracks():
    manager = MusicManager()
    result = manager.view_tracks()
    assert result == ("- No tracks added -")

def test_music_manager_same_tracks():
    manager = MusicManager()
    manager.add_track("Arabesque", "Lily Chou-Chou")
    manager.add_track("Arabesque", "Lily Chou-Chou")
    result = manager.view_tracks()
    assert result == ("Arabesque by Lily Chou-Chou")