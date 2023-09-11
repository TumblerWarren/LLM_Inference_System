def env_read():
    with open('../env.txt', 'r') as file:
        lines = file.readlines()

    # Create a dictionary to store the configuration data
    env_data = {}

    # Parse the lines and populate the dictionary
    for line in lines:
        parts = line.strip().split('=')
        if len(parts) == 2:
            key, value = parts
            env_data[key] = value
        elif len(parts) == 1:
            # Handle lines without values, you can choose to ignore them or handle them differently
            key = parts[0]
            env_data[key] = None  # Set the value to None or handle it as needed

    return env_data


def env_model_param_read():
    with open('../env_model_param.txt', 'r') as file:
        lines = file.readlines()

    # Create a dictionary to store the configuration data
    env_data = {}

    # Parse the lines and populate the dictionary
    for line in lines:
        parts = line.strip().split('=')
        if len(parts) == 2:
            key, value = parts
            env_data[key] = value
        elif len(parts) == 1:
            # Handle lines without values, you can choose to ignore them or handle them differently
            key = parts[0]
            env_data[key] = None  # Set the value to None or handle it as needed

    return env_data

def env_prompt_template_read():
    with open('../env_prompt_template_setting.txt', 'r') as file:
        lines = file.readlines()

    # Create a dictionary to store the configuration data
    env_data = {}

    # Parse the lines and populate the dictionary
    for line in lines:
        parts = line.strip().split('=')
        if len(parts) == 2:
            key, value = parts
            env_data[key] = value
        elif len(parts) == 1:
            # Handle lines without values, you can choose to ignore them or handle them differently
            key = parts[0]
            env_data[key] = None  # Set the value to None or handle it as needed

    return env_data


print(env_read())