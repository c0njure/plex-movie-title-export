import os
import sys

from plexapi.server import PlexServer

PLEX_URL = os.environ.get("PLEX_URL", "http://locahost:32400")
PLEX_TOKEN = os.environ.get("PLEX_TOKEN")
LIBRARY_NAME = os.environ.get("PLEX_LIBRARY", "Movies")
OUTPUT_FILE = os.environ.get("OUTPUT_FILE", "plex_movies.txt")

if not PLEX_TOKEN:
    sys.exit("Error: set the PLEX_TOKEN environment variable first.")

plex = PlexServer(PLEX_URL, PLEX_TOKEN)
movies = plex.library.section(LIBRARY_NAME).all()

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    for m in sorted(movies, key=lambda x: x.titleSort):
        f.write(f"{m.title} ({m.year})\n")

print(f"Exported {len(movies)} movies to {OUTPUT_FILE}")
