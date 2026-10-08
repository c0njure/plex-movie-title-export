# Plex Movie Title Export

A small Python script I made that exports the titles of every movie in a Plex library to a plain text file, one per line, sorted alphabetically (ignoring leading words like "The").

Example output:

```
Alien (1979)
Back to the Future (1985)
The Matrix (1999)
```

I made this script to be able to feed LLMs my collection list to recommend other movies I may like, gaps in my collection, etc.

## Requirements

- Python 3.8+
- A running Plex Media Server you can reach from your computer
- Your Plex token (see below)
- The [python-plexapi](https://github.com/pkkid/python-plexapi) library

## Installation

```bash
git clone https://github.com/c0njure/plex-movie-export.git
cd plex-movie-title-export
```

Install the dependency using whichever method suits your system:

**Virtual environment (works everywhere):**

```bash
python -m venv venv
source venv/bin/activate
pip install plexapi
```

**Arch / CachyOS / Manjaro:**

```bash
sudo pacman -S python-plexapi
```

## Finding your Plex token

1. Open Plex Web and sign in.
2. Open any movie, click the **⋯** menu, and choose **Get Info**.
3. Click **View XML**.
4. Copy the value after `X-Plex-Token=` in the browser's address bar.

## Usage

Set your token as an environment variable, then run the script:

```bash
export PLEX_TOKEN="your-token-here"
python export_plex.py
```

On Windows (Command Prompt):

```cmd
set PLEX_TOKEN=your-token-here
python export_plex.py
```

This creates `plex_movies.txt` in the current folder.

## Configuration

All settings are environment variables:

| Variable       | Required | Default                  | Description                          |
|----------------|----------|--------------------------|--------------------------------------|
| `PLEX_TOKEN`   | Yes      | none                     | Your Plex authentication token       |
| `PLEX_URL`     | No       | `http://localhost:32400` | Address of your Plex server          |
| `PLEX_LIBRARY` | No       | `Movies`                 | Name of the library to export        |
| `OUTPUT_FILE`  | No       | `plex_movies.txt`        | Name of the file to write            |

Example for a server on another machine with a custom library name:

```bash
PLEX_URL="http://192.168.1.50:32400" PLEX_LIBRARY="Films" PLEX_TOKEN="your-token-here" python export_plex.py
```

## Customizing the output

Each movie object exposes more fields than title and year. To include genres, for example, change the write line in `export_plex.py`:

```python
f.write(f"{m.title} ({m.year}) - {', '.join(g.tag for g in m.genres)}\n")
```

Other useful attributes include `m.rating`, `m.duration`, `m.summary`, and `m.directors`.

## Troubleshooting

- **`Unauthorized` error:** your token is wrong or expired. Grab a fresh one.
- **Connection refused / timeout:** check `PLEX_URL`. If Plex runs on another machine, use its IP address instead of `localhost`.
- **`NotFound` error for the library:** `PLEX_LIBRARY` must exactly match the library name shown in Plex.
- **`pip: command not found`:** use the virtual environment or package manager instructions above.
