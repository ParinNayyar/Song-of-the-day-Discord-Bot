import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Load environment variables
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
SPOTIFY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")

# Initialize Spotify Client
sp = spotipy.Spotify(
    auth_manager=SpotifyClientCredentials(
        client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET
    )
)

# Initialize Discord Bot (case_insensitive allows !sotd, !SOTD, etc.)
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents, case_insensitive=True)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")

@bot.command(name="sotd")
async def song_of_the_day(ctx, *, query: str):
    """Submits a Song of the Day via track URL or search term."""
    try:
        results = sp.search(q=query, limit=1, type="track")
        tracks = results.get("tracks", {}).get("items", [])

        if not tracks:
            await ctx.send("No track found on Spotify!")
            return

        track = tracks[0]
        track_title = track.get("name", "Unknown Title")
        artist_name = ", ".join([a.get("name", "") for a in track.get("artists", [])]) or "Unknown Artist"
        
        # Album metadata
        album = track.get("album", {})
        album_images = album.get("images", [])
        album_art = album_images[0]["url"] if album_images else ""
        release_date = album.get("release_date", "N/A")
        
        spotify_url = track.get("external_urls", {}).get("spotify", "")
        popularity = track.get("popularity", "N/A")

        # Build Discord Embed
        embed = discord.Embed(
            title=f"🎵 Song of the Day: {track_title}",
            description=f"by **{artist_name}**",
            color=discord.Color.green(),
            url=spotify_url if spotify_url else None
        )
        if album_art:
            embed.set_thumbnail(url=album_art)

        embed.add_field(name="Release Date", value=release_date, inline=True)
        embed.add_field(name="Popularity Score", value=f"{popularity}/100" if popularity != "N/A" else "N/A", inline=True)
        embed.set_footer(text=f"Submitted by {ctx.author.display_name} • React to vote!")

        message = await ctx.send(embed=embed)
        await message.add_reaction("🔥")
        await message.add_reaction("🗑️")

    except Exception as e:
        await ctx.send(f"An error occurred: {str(e)}")

bot.run(DISCORD_TOKEN)