import json
import os
from dotenv import load_dotenv
load_dotenv()

# Specify the path to the JSON file
Character_Card_path = os.environ.get("Character_Card")
chat_history = os.environ.get("chat_history")
def card_read():
    with open(Character_Card_path, "r") as json_file:
        data = json.load(json_file)

# Extract the required fields from the loaded JSON data
    name = data["name"]
    char_name = data["char_name"]
    char_persona = data["char_persona"]
    world_scenario = data["world_scenario"]
    example_dialogue = data["example_dialogue"]

    dilogue = f"Character Name: {char_name}\nCharecter Personality: {char_persona}\nScenario: {world_scenario}\n<START>\n{example_dialogue}"
    return dilogue,name

def history_read():

    with open(chat_history, 'r') as json_file:
        content = json.load(json_file)

    sections = content.split('\n')

    # Initialize the formatted output variable
    formatted_output = ""

    # Process each section
    for section in sections:
        if ':' in section:
            key, value = section.split(':', 1)
            key = key.strip()
            value = value.strip()
            formatted_output += key + ": " + value + "\n"
        else:
            formatted_output += section.strip() + "\n"  # Handle lines without ':' differently

    return formatted_output

def check_prompt_length():

    pass

