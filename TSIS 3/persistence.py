import json
from pathlib import Path

# Base directory of the current file
BASE_DIR = Path(__file__).resolve().parent

# Paths to JSON files
SETTINGS_PATH = BASE_DIR / "settings.json"
LEADERBOARD_PATH = BASE_DIR / "leaderboard.json"

# Default settings used if no file exists or data is missing
DEFAULT_SETTINGS = {
    "sound": True,
    "car_color": "red",
    "difficulty": "medium",
}

def read_json(path, default_value):
    """
    Read JSON data from a file.
    If file does not exist or is corrupted, return default value.
    """
    if not path.exists():
        return default_value

    try:
        with path.open("r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        # Return default if JSON is invalid or file can't be read
        return default_value

def write_json(path, data):
    """
    Write data to a JSON file with indentation.
    """
    with path.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

def load_settings():
    """
    Load settings from file and merge with defaults.
    Ensures missing fields are filled with default values.
    """
    settings = read_json(SETTINGS_PATH, DEFAULT_SETTINGS.copy())

    # Merge loaded settings with defaults
    merged = DEFAULT_SETTINGS.copy()
    merged.update(settings)

    return merged

def save_settings(settings):
    """
    Save current settings to file.
    """
    write_json(SETTINGS_PATH, settings)

def load_leaderboard():
    """
    Load leaderboard entries from file.
    Returns an empty list if data is invalid.
    """
    leaderboard = read_json(LEADERBOARD_PATH, [])

    # Ensure leaderboard is a list
    if not isinstance(leaderboard, list):
        return []

    return leaderboard

def save_leaderboard(entries):
    """
    Save top 10 leaderboard entries to file.
    """
    write_json(LEADERBOARD_PATH, entries[:10])

def add_leaderboard_entry(entry):
    """
    Add a new entry to the leaderboard,
    sort it, and keep only top 10 results.
    """
    entries = load_leaderboard()

    # Add new result
    entries.append(entry)

    # Sort by score first, then distance (both descending)
    entries.sort(key=lambda item: (item["score"], item["distance"]), reverse=True)

    # Save only top 10
    save_leaderboard(entries[:10])

    return entries[:10]