import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


options={}
values={}
template_params={}

DEFAULT_VALUES = {
    "suffix": None,
    "max_tokens": 56,
    "temperature": 1.31,
    "top_p": 0.14,
    "logprobs": None,
    "echo": False,
    "stop": [],
    "repeat_penalty": 1.17,
    "top_k": 40,
    "stream": False
}

def save_to_env_file(values):
    with open("../env_prompt_template_setting.txt", "w") as f:
        for key, value in values.items():
            f.write(f"{key}={value}\n")
    messagebox.showinfo("Saved", "Values have been saved to the .env file.")





def update_slider_label(slider_var, label_var):
    label_var.set(slider_var.get())

def create_slider_frame(root1, label_text, slider_min, slider_max, default_value, step=1):
    frame = ttk.Frame(root1)
    label = ttk.Label(frame, text=label_text)
    label.pack(side=tk.LEFT, padx=10)

    slider_var = tk.DoubleVar(value=default_value)
    slider = ttk.Scale(frame, from_=slider_min, to=slider_max, variable=slider_var, orient=tk.HORIZONTAL)
    slider.pack(side=tk.LEFT, padx=10)

    value_label_var = tk.StringVar()
    value_label = ttk.Label(frame, textvariable=value_label_var)
    value_label.pack(side=tk.LEFT, padx=10)

    update_slider_label(slider_var, value_label_var)
    slider_var.trace_add("write", lambda *args: update_slider_label(slider_var, value_label_var))

    return frame, slider_var


def create_dropdown_frame(root1, label_text, options, default_value):
    frame = ttk.Frame(root1)
    label = ttk.Label(frame, text=label_text)
    label.pack(side=tk.LEFT, padx=10)

    option_var = tk.StringVar(value=default_value)
    dropdown = ttk.Combobox(frame, textvariable=option_var, values=options, state="readonly")
    dropdown.pack(side=tk.LEFT, padx=10)

    return frame, option_var

def create_input_frame(root1, label_text, default_value=None):
    frame = ttk.Frame(root1)
    label = ttk.Label(frame, text=label_text)
    label.pack(side=tk.LEFT, padx=10)

    input_var = tk.StringVar(value=default_value)
    input_box = ttk.Entry(frame, textvariable=input_var)
    input_box.pack(side=tk.LEFT, padx=10)

    return frame, input_var

def load_defaults():
    suffix_var.set(DEFAULT_VALUES["suffix"])
    max_tokens_var.set(DEFAULT_VALUES["max_tokens"])
    temperature_var.set(DEFAULT_VALUES["temperature"])
    top_p_var.set(DEFAULT_VALUES["top_p"])
    logprobs_var.set(DEFAULT_VALUES["logprobs"])
    echo_var.set(DEFAULT_VALUES["echo"])
    stop_var.set(DEFAULT_VALUES["stop"])
    repeat_penalty_var.set(DEFAULT_VALUES["repeat_penalty"])
    top_k_var.set(DEFAULT_VALUES["top_k"])
    stream_var.set(DEFAULT_VALUES["stream"])
    messagebox.showinfo("Default", "Default Values have been loaded!")

def save_values():
    global values
    values = {
        "suffix": suffix_var.get(),
        "max_tokens": int(max_tokens_var.get()),
        "temperature": temperature_var.get(),
        "top_p": top_p_var.get(),
        "logprobs": logprobs_var.get(),
        "echo": echo_var.get(),
        "stop": stop_var.get(),
        "repeat_penalty": repeat_penalty_var.get(),
        "top_k": int(top_k_var.get()),
        "stream": stream_var.get()
    }
    save_to_env_file(values)
    messagebox.showinfo("Saved", "Values have been saved!")


root1 = tk.Tk()
root1.title("Text Generation Parameters")

suffix_frame, suffix_var = create_input_frame(root1, "Suffix:", DEFAULT_VALUES["suffix"])
suffix_frame.pack(pady=10)

max_tokens_frame, max_tokens_var = create_slider_frame(root1, "Max Tokens:", 0, 2000, DEFAULT_VALUES["max_tokens"], step=1)
max_tokens_frame.pack(pady=10)

temperature_frame, temperature_var = create_slider_frame(root1, "Temperature:", 0.01, 2.0, DEFAULT_VALUES["temperature"])
temperature_frame.pack(pady=10)

top_p_frame, top_p_var = create_slider_frame(root1, "Top P:", 0.01, 1.0, DEFAULT_VALUES["top_p"])
top_p_frame.pack(pady=10)

logprobs_frame, logprobs_var = create_input_frame(root1, "Logprobs:", DEFAULT_VALUES["logprobs"])
logprobs_frame.pack(pady=10)

echo_frame, echo_var = create_dropdown_frame(root1, "Echo:", ["True", "False"], DEFAULT_VALUES["echo"])
echo_frame.pack(pady=10)

stop_frame, stop_var = create_input_frame(root1, "Stop:", DEFAULT_VALUES["stop"])
stop_frame.pack(pady=10)

repeat_penalty_frame, repeat_penalty_var = create_slider_frame(root1, "Repeat Penalty:", 1,1.5, DEFAULT_VALUES["repeat_penalty"])
repeat_penalty_frame.pack(pady=10)

top_k_frame, top_k_var = create_slider_frame(root1, "Top K:", 1, 200, DEFAULT_VALUES["top_k"])
top_k_frame.pack(pady=10)

stream_frame, stream_var = create_dropdown_frame(root1, "Stream:", ["True", "False"], DEFAULT_VALUES["stream"])
stream_frame.pack(pady=10)

load_defaults_button = ttk.Button(root1, text="Load Defaults", command=load_defaults)
load_defaults_button.pack(pady=5)

save_button = ttk.Button(root1, text="Save Values", command=save_values)
save_button.pack(pady=5)


root1.mainloop()
