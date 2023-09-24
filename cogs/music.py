from discord.ext import commands
import discord
from discord import app_commands
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from config import client_id, client_secret, playlist
import random

# Initialize the Spotify API client
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def get_random_song(playlist_url):
    # Extract the playlist ID from the URL
    playlist_id = playlist_url.split('/')[-1]

    try:
        # Get the playlist tracks
        results = sp.playlist_tracks(playlist_id)

        # Extract the list of track objects
        tracks = results['items']

        if len(tracks) == 0:
            return "No songs found in the playlist."

        # Choose a random track from the playlist
        random_track = random.choice(tracks)

        # Extract the track name and external URL
        track_name = random_track['track']['name']
        track_url = random_track['track']['external_urls']['spotify']

        return f"Random Song: {track_name}\nSpotify URL: {track_url}"

    except Exception as e:
        return f"An error occurred: {str(e)}"

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="music", description="Links to music")
    async def music(self, interaction: discord.Interaction):
        await interaction.response.send_message(get_random_song(playlist))

async def setup(bot):
    await bot.add_cog(Music(bot))
