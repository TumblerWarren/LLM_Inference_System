import json
import os,re
import env_file_reading

history={}
name = ""
char_name = ""
char_persona = ""
world_scenario = ""
example_dialogue = ""
chat_history = ""
dilogue = ""

# Specify the path to the JSON file
env_data = env_file_reading.env_read()

read_name = os.environ.get("your_name")
Character_Card_path = env_data.get("Character_Card")
chat_history_path = env_data.get("chat_history")


def card_read():

    with open(Character_Card_path, "r") as json_file:
        data = json.load(json_file)

# Extract the required fields from the loaded JSON data
    global name,char_name,char_persona,world_scenario,example_dialogue,dilogue

    name = read_name
    char_name = data["char_name"]
    char_persona = data["char_persona"]
    world_scenario = data["world_scenario"]
    example_dialogue = data["example_dialogue"]
    updated_dialogue = re.sub(r'\b(USER|you)\b', data["name"], data["example_dialogue"], flags=re.IGNORECASE)
    example_dialogue = updated_dialogue

    dilogue = f"Character Name: {char_name}\nCharecter Personality: {char_persona}\nScenario: {world_scenario}\n<START>\n{example_dialogue}"

    return dilogue,name,char_name

def history_read():

    with open(chat_history_path, "r") as json_file:
        data = json.load(json_file)

    # Extract the required fields from the loaded JSON data
    global name, char_name, char_persona, world_scenario, example_dialogue,chat_history,dilogue

    name = read_name
    char_name = data["char_name"]
    char_persona = data["char_persona"]
    world_scenario = data["world_scenario"]
    example_dialogue = data["example_dialogue"]
    chat_history = data["history"]

    dilogue = f"Character Name: {char_name}\nCharecter Personality: {char_persona}\nScenario: {world_scenario}\n<START>\n{example_dialogue}\n{chat_history}"

    return dilogue, name, char_name


def prompt_trimming(prompt_length,chat,prompt):
    if prompt_length>=500:

        text = (chat).splitlines()
        text = [item for item in text if item.strip() != '']

        text = text[4:]
        formatted_conversation = []

        for sentence in text:
            speaker, content = sentence.split(': ', 1)
            formatted_conversation.append(f"{speaker}: {content.strip()}")

        formatted_text = "\n".join(formatted_conversation)
        new_prompt = f"Character Name: {char_name}\nCharecter Personality: {char_persona}\nScenario: {world_scenario}\n<START>\n{formatted_text}"


        return new_prompt,formatted_text
    else:

        return prompt,chat




def save_history(segment):
    global chat_history

    history["name"] = read_name
    history["char_name"] = char_name
    history["char_persona"] = char_persona
    history["world_scenario"] = world_scenario
    history["example_dialogue"] = example_dialogue

    chat_history =chat_history+"\n"+segment
    history["history"] = chat_history

    FILENAME = "prompt_history.json"
    directory = '/content/LLM_Inference_System/Resource/Card'
    FILE_PATH = os.path.join(directory, FILENAME)

    with open(FILE_PATH, 'w') as json_file:
        json.dump(history, json_file, indent=4)

