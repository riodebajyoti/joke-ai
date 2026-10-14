"""Click Play to open Joke AI in your browser."""
from pathlib import Path
import webbrowser
page = Path(__file__).with_name("joke_ai_browser.html")
webbrowser.open(page.resolve().as_uri())
print("Joke AI is open in your browser. Have fun!")
