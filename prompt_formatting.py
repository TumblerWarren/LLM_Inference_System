import json
import os
from dotenv import load_dotenv
load_dotenv()

# Specify the path to the JSON file
Character_Card_path = os.environ.get("Character_Card")

def card_read():
    with open(Character_Card_path, "r") as json_file:
        data = json.load(json_file)

# Extract the required fields from the loaded JSON data
    char_name = data["char_name"]
    char_persona = data["char_persona"]
    world_scenario = data["world_scenario"]
    char_greeting = data["char_greeting"]
    example_dialogue = data["example_dialogue"]

    dilogue = f"Character Name: {char_name}\nCharecter Personality: {char_persona}\nScenario: {world_scenario}\n<START>\n{example_dialogue}"
    return dilogue

