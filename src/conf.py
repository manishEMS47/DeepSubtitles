from os import environ as env

from dotenv import load_dotenv
load_dotenv()

# Put your deepgram key here
DEEPGRAM_KEY = env.get("DEEPGRAM_KEY")

# Put your 60db key here (used when STT_PROVIDER is "60db")
SIXTYDB_KEY = env.get("SIXTYDB_KEY") or env.get("60DB_KEY")

# This is for Windows users
IMAGEMAGIK_LOCATION= r"C:\Program Files\ImageMagick-7.1.0-Q16-HDRI\magick.exe"

CONFIG = {
    "OUTPUT_FPS": 24,
    "AUDIO" : True,
    "VIDEO_CODEC": "libx264",
    "OUTPUT_FILE": "output.mp4",

    # Which speech-to-text engine to use: "deepgram" or "60db".
    "STT_PROVIDER": "deepgram",

    # Language passed to the STT engine. Deepgram uses locales like "en-US";
    # 60db uses ISO 639-1 codes ("en") and the region suffix is stripped
    # automatically. Use "auto" to let 60db detect the language.
    "STT_LANGUAGE": "en-US",
}