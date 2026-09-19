# 🎵 Song of the Day (SOTD) Discord Bot

A feature-packed Discord bot built with `discord.py` and `spotipy` that allows server members to share and vote on daily music tracks.

## Features
- **Track Metadata Lookup:** Fetch track titles, artists, album artwork, release dates, and popularity scores directly from Spotify.
- **Interactive Voting:** Automatically attaches voting reactions (🔥 / 🗑️) to track submissions.
- **24/7 Cloud Ready:** Features a built-in Flask web server wrapper for continuous hosting on platforms like Render.
- **Case-Insensitive Commands:** Flexible command handling for `!sotd`, `!SOTD`, etc.

---

## Tech Stack
- **Language:** Python 3.10+
- **Discord API Wrapper:** `discord.py`
- **Spotify API Wrapper:** `spotipy`
- **Web Server:** `Flask` / `gunicorn`
- **Hosting:** Render

---

## Setup & Installation

### 1. Prerequisites
- Python 3.10 or higher
- A [Discord Developer Portal](https://discord.com/developers/applications) App & Bot Token
- A [Spotify Developer Dashboard](https://developer.spotify.com/dashboard) Client ID & Secret

### 2. Local Setup
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/song-of-the-day-bot.git](https://github.com/YOUR_USERNAME/song-of-the-day-bot.git)
   cd song-of-the-day-bot
