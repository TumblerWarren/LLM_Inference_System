import os
import tkinter as tk
from tkinter import messagebox


options={}

def load_model_parameter_value():
    model_params = {}
    model_params["n_ctx"] = int(options["n_ctx"])
    model_params["n_parts"] = int(options["n_parts"])
    model_params["n_gpu_layers"] = int(options["n_gpu_layers"])
    model_params["seed"] = int(options["seed"])

    f16_kv_value = options["f16_kv"]
    if f16_kv_value.lower() == "true":
        model_params["f16_kv"] = True
    elif f16_kv_value.lower() == "false":
        model_params["f16_kv"] = False

    model_params["logits_all"] = options.get("logits_all", "False")
    if model_params["logits_all"].lower() == "true":
        model_params["logits_all"] = True
    else:
        model_params["logits_all"] = False

    model_params["vocab_only"] = options.get("vocab_only", "False")
    if model_params["vocab_only"].lower() == "true":
        model_params["vocab_only"] = True
    else:
        model_params["vocab_only"] = False

    model_params["use_mmap"] = options.get("use_mmap", "False")
    if model_params["use_mmap"].lower() == "true":
        model_params["use_mmap"] = True
    else:
        model_params["use_mmap"] = False

    model_params["use_mlock"] = options.get("use_mlock", "False")
    if model_params["use_mlock"].lower() == "true":
        model_params["use_mlock"] = True
    else:
        model_params["use_mlock"] = False

    model_params["embedding"] = options.get("embedding", "False")
    if model_params["embedding"].lower() == "true":
        model_params["embedding"] = True
    else:
        model_params["embedding"] = False

    if (os.environ.get("n_threads")) == 'None':
        model_params["n_threads"] = None
    else:
        model_params["n_threads"] = int(os.environ.get("n_threads"))

    model_params["n_batch"] = int(os.environ.get("n_batch"))
    model_params["last_n_tokens_size"] = int(os.environ.get("last_n_tokens_size"))

    if os.environ.get("lora_base") == 'None':
        model_params["lora_base"] = None
    else:
        model_params["lora_base"] = os.environ.get("lora_base")

    if os.environ.get("lora_path") == 'None':
        model_params["lora_path"] = None
    else:
        model_params["lora_path"] = os.environ.get("lora_path")

    model_params["low_vram"] = bool(os.environ.get("low_vram"))
    model_params["tensor_split"] = None
    model_params["rope_freq_base"] = float(os.environ.get("rope_freq_base"))
    model_params["rope_freq_scale"] = float(os.environ.get("rope_freq_scale"))

    if os.environ.get("n_gqa") == 'None':
        model_params["n_gqa"] = None
    else:
        model_params["n_gqa"] = int(os.environ.get("n_gqa"))

    if os.environ.get("rms_norm_eps") == 'None':
        model_params["rms_norm_eps"] = None
    else:
        model_params["rms_norm_eps"] = float(os.environ.get("rms_norm_eps"))


    model_params["verbose"] = bool(os.environ.get("verbose"))
    model_params["mul_mat_q"] = None
    return model_params


def save_to_env_file(options):
    with open("../env_model_param.txt", "w") as f:
        for key, value in options.items():
            f.write(f"{key}={value}\n")
    messagebox.showinfo("Saved", "Values have been saved to the .env file.")

def restore_defaults():
    n_ctx_var.set("2080")
    n_parts_var.set("-1")
    n_gpu_layers_var.set("0")
    seed_var.set("-1")
    f16_kv_var.set("True")
    logits_all_var.set("False")
    vocab_only_var.set("False")
    use_mmap_var.set("True")
    use_mlock_var.set("False")
    embedding_var.set("False")
    n_threads_var.set("None")
    n_batch_var.set("512")
    last_n_tokens_size_var.set("64")
    lora_base_var.set("None")
    lora_path_var.set("None")
    low_vram_var.set("False")
    tensor_split_var.set("None")
    rope_freq_base_var.set("10000.0")
    rope_freq_scale_var.set("1.0")
    n_gqa_var.set("None")
    rms_norm_eps_var.set("None")
    verbose_var.set("True")

def update_values():
    n_ctx_var.set(os.getenv("n_ctx", 2080))
    n_parts_var.set(os.getenv("n_parts", -1))
    n_gpu_layers_var.set(os.getenv("n_gpu_layers", 0))
    seed_var.set(os.getenv("seed", 0))
    f16_kv_var.set(os.getenv("f16_kv", "True"))
    logits_all_var.set(os.getenv("logits_all", "False"))
    vocab_only_var.set(os.getenv("vocab_only", "False"))
    use_mmap_var.set(os.getenv("use_mmap", "True"))
    use_mlock_var.set(os.getenv("use_mlock", "False"))
    embedding_var.set(os.getenv("embedding", "False"))
    n_threads_var.set(os.getenv("n_threads", None))
    n_batch_var.set(os.getenv("n_batch", 512))
    last_n_tokens_size_var.set(os.getenv("last_n_tokens_size", 64))
    lora_base_var.set(os.getenv("lora_base", None))
    lora_path_var.set(os.getenv("lora_path", None))
    low_vram_var.set(os.getenv("low_vram", "False"))
    tensor_split_var.set(os.getenv("tensor_split", None))
    rope_freq_base_var.set(os.getenv("rope_freq_base", 10000.0))
    rope_freq_scale_var.set(os.getenv("rope_freq_scale", 1.0))
    n_gqa_var.set(os.getenv("n_gqa", None))
    rms_norm_eps_var.set(os.getenv("rms_norm_eps", 0))
    verbose_var.set(os.getenv("verbose", "True"))



def save_changes():
    global options
    options = {
        "n_ctx": n_ctx_var.get(),
        "n_parts": n_parts_var.get(),
        "n_gpu_layers": n_gpu_layers_var.get(),
        "seed": seed_var.get(),
        "f16_kv": f16_kv_var.get(),
        "logits_all": logits_all_var.get(),
        "vocab_only": vocab_only_var.get(),
        "use_mmap": use_mmap_var.get(),
        "use_mlock": use_mlock_var.get(),
        "embedding": embedding_var.get(),
        "n_threads": n_threads_var.get(),
        "n_batch": n_batch_var.get(),
        "last_n_tokens_size": last_n_tokens_size_var.get(),
        "lora_base": lora_base_var.get(),
        "lora_path": lora_path_var.get(),
        "low_vram": low_vram_var.get(),
        "tensor_split": tensor_split_var.get(),
        "rope_freq_base": rope_freq_base_var.get(),
        "rope_freq_scale": rope_freq_scale_var.get(),
        "n_gqa": n_gqa_var.get(),
        "rms_norm_eps": rms_norm_eps_var.get(),

        "verbose": verbose_var.get(),
    }
    save_to_env_file(options)


def validate_range(entry_var, min_value, max_value):
    try:
        value = int(entry_var.get())
        if value < min_value:
            entry_var.set(str(min_value))
        elif value > max_value:
            entry_var.set(str(max_value))
    except ValueError:
        pass
def close_interface():
    root.destroy()

root = tk.Tk()
root.title("Model Configuration Editor")


text_color = "white"

custom_font = ("Ariel", 8, "bold")

n_ctx_label = tk.Label(root, text="N CTX",font=custom_font)
n_ctx_var = tk.StringVar()
n_ctx_entry = tk.Entry(root, textvariable=n_ctx_var)
n_ctx_entry.bind("<FocusOut>", lambda event: validate_range(n_ctx_var, 0, 4080))

n_parts_label = tk.Label(root, text="N PARTS",font=custom_font)
n_parts_var = tk.StringVar()
n_parts_entry = tk.Entry(root, textvariable=n_parts_var)
n_parts_entry.bind("<FocusOut>", lambda event: validate_range(n_parts_var, -1, -1))

n_gpu_layers_label = tk.Label(root, text="N GPU LAYERS",font=custom_font)
n_gpu_layers_var = tk.StringVar()
n_gpu_layers_entry = tk.Entry(root, textvariable=n_gpu_layers_var)
n_gpu_layers_entry.bind("<FocusOut>", lambda event: validate_range(n_gpu_layers_var, 0, 128))

seed_label = tk.Label(root, text="SEED",font=custom_font)
seed_var = tk.StringVar()
seed_entry = tk.Entry(root, textvariable=seed_var)
seed_entry.bind("<FocusOut>", lambda event: validate_range(seed_var, -1, 1000000))  # Adjust range as needed


f16_kv_label = tk.Label(root, text="F16 KV", font=custom_font)
f16_kv_var = tk.StringVar()
f16_kv_menu = tk.OptionMenu(root, f16_kv_var, "True", "False")

logits_all_label = tk.Label(root, text="LOGITS ALL", font=custom_font)
logits_all_var = tk.StringVar()
logits_all_menu = tk.OptionMenu(root, logits_all_var, "True", "False")

vocab_only_label = tk.Label(root, text="VOCAB ONLY", font=custom_font)
vocab_only_var = tk.StringVar()
vocab_only_menu = tk.OptionMenu(root, vocab_only_var, "True", "False")

use_mmap_label = tk.Label(root, text="USE MMAP", font=custom_font)
use_mmap_var = tk.StringVar()
use_mmap_menu = tk.OptionMenu(root, use_mmap_var, "True", "False")


use_mlock_label = tk.Label(root, text="USE MLOCK", font=custom_font)
use_mlock_var = tk.StringVar()
use_mlock_menu = tk.OptionMenu(root, use_mlock_var, "True", "False")


embedding_label = tk.Label(root, text="EMBEDDING", font=custom_font)
embedding_var = tk.StringVar()
embedding_menu = tk.OptionMenu(root, embedding_var, "True", "False")

n_threads_label = tk.Label(root, text="N THREADS",font=custom_font)
n_threads_var = tk.StringVar()
n_threads_entry = tk.Entry(root, textvariable=n_threads_var)
n_threads_entry.bind("<FocusOut>", lambda event: validate_range(n_threads_var, 0, 32))  # Adjust range as needed

n_batch_label = tk.Label(root, text="N BATCH",font=custom_font)
n_batch_var = tk.StringVar()
n_batch_entry = tk.Entry(root, textvariable=n_batch_var)
n_batch_entry.bind("<FocusOut>", lambda event: validate_range(n_batch_var, 1, 2041))  # Adjust range as needed


last_n_tokens_size_label = tk.Label(root, text="LAST N TOKEN SIZE",font=custom_font)
last_n_tokens_size_var = tk.StringVar()
last_n_tokens_size_entry = tk.Entry(root, textvariable=last_n_tokens_size_var)
last_n_tokens_size_entry.bind("<FocusOut>", lambda event: validate_range(last_n_tokens_size_var, 1, 1000))  # Adjust range as needed


lora_base_label = tk.Label(root, text="LORA BASE",font=custom_font)
lora_base_var = tk.StringVar()
lora_base_entry = tk.Entry(root, textvariable=lora_base_var)


lora_path_label = tk.Label(root, text="LORA PATH",font=custom_font)
lora_path_var = tk.StringVar()
lora_path_entry = tk.Entry(root, textvariable=lora_path_var)

low_vram_label = tk.Label(root, text="LOW VRAM",font=custom_font)
low_vram_var = tk.StringVar()
low_vram_entry = tk.Entry(root, textvariable=low_vram_var)

tensor_split_label = tk.Label(root, text="TENSOR SPLIT",font=custom_font)
tensor_split_var = tk.StringVar()
tensor_split_entry = tk.Entry(root, textvariable=tensor_split_var)

rope_freq_base_label = tk.Label(root, text="ROPE FREQUENCY BASE",font=custom_font)
rope_freq_base_var = tk.StringVar()
rope_freq_base_entry = tk.Entry(root, textvariable=rope_freq_base_var)

rope_freq_scale_label = tk.Label(root, text="ROPE FREQUENCY SCALE",font=custom_font)
rope_freq_scale_var = tk.StringVar()
rope_freq_scale_entry = tk.Entry(root, textvariable=rope_freq_scale_var)

n_gqa_label = tk.Label(root, text="N GPA",font=custom_font)
n_gqa_var = tk.StringVar()
n_gqa_entry = tk.Entry(root, textvariable=n_gqa_var)
n_gqa_entry.bind("<FocusOut>", lambda event: validate_range(n_gqa_var, 0, 16))  # Adjust range as needed

rms_norm_eps_label = tk.Label(root, text="RMS NORM EPS",font=custom_font)
rms_norm_eps_var = tk.StringVar()
rms_norm_eps_entry = tk.Entry(root, textvariable=rms_norm_eps_var)
rms_norm_eps_entry.bind("<FocusOut>", lambda event: validate_range(rms_norm_eps_var, 0, 0.00001))  # Adjust range as needed

verbose_label = tk.Label(root, text="VERBOSE",font=custom_font)
verbose_var = tk.StringVar()
verbose_entry = tk.Entry(root, textvariable=verbose_var)

custom_font_2 = ("Roboto", 8, "bold")
load_button = tk.Button(root, text="LOAD VALUES",font=custom_font_2, command=update_values)
save_button = tk.Button(root, text="SAVE CHANGES",font=custom_font_2, command=save_changes)
restore_button = tk.Button(root, text="RESTORE DEFAULT",font=custom_font_2, command=restore_defaults)
close_button = tk.Button(root, text="CLOSE",font=custom_font_2, command=close_interface)

n_ctx_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
n_ctx_entry.grid(row=0, column=1, padx=10, pady=5)

n_parts_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
n_parts_entry.grid(row=1, column=1, padx=10, pady=5)

n_gpu_layers_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
n_gpu_layers_entry.grid(row=2, column=1, padx=10, pady=5)

seed_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
seed_entry.grid(row=3, column=1, padx=10, pady=5)

f16_kv_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")
f16_kv_menu.grid(row=4, column=1, padx=10, pady=5)

logits_all_label.grid(row=5, column=0, padx=10, pady=5, sticky="w")
logits_all_menu.grid(row=5, column=1, padx=10, pady=5)


vocab_only_label.grid(row=6, column=0, padx=10, pady=5, sticky="w")
vocab_only_menu.grid(row=6, column=1, padx=10, pady=5)


use_mmap_label.grid(row=7, column=0, padx=10, pady=5, sticky="w")
use_mmap_menu.grid(row=7, column=1, padx=10, pady=5)


use_mlock_label.grid(row=8, column=0, padx=10, pady=5, sticky="w")
use_mlock_menu.grid(row=8, column=1, padx=10, pady=5)

embedding_label.grid(row=9, column=0, padx=10, pady=5, sticky="w")
embedding_menu.grid(row=9, column=1, padx=10, pady=5)

n_threads_label.grid(row=10, column=0, padx=10, pady=5, sticky="w")
n_threads_entry.grid(row=10, column=1, padx=10, pady=5)

n_batch_label.grid(row=11, column=0, padx=10, pady=5, sticky="w")
n_batch_entry.grid(row=11, column=1, padx=10, pady=5)

last_n_tokens_size_label.grid(row=12, column=0, padx=10, pady=5, sticky="w")
last_n_tokens_size_entry.grid(row=12, column=1, padx=10, pady=5)

lora_base_label.grid(row=13, column=0, padx=10, pady=5, sticky="w")
lora_base_entry.grid(row=13, column=1, padx=10, pady=5)

lora_path_label.grid(row=14, column=0, padx=10, pady=5, sticky="w")
lora_path_entry.grid(row=14, column=1, padx=10, pady=5)

low_vram_label.grid(row=15, column=0, padx=10, pady=5, sticky="w")
low_vram_entry.grid(row=15, column=1, padx=10, pady=5)

tensor_split_label.grid(row=16, column=0, padx=10, pady=5, sticky="w")
tensor_split_entry.grid(row=16, column=1, padx=10, pady=5)

rope_freq_base_label.grid(row=17, column=0, padx=10, pady=5, sticky="w")
rope_freq_base_entry.grid(row=17, column=1, padx=10, pady=5)

rope_freq_scale_label.grid(row=18, column=0, padx=10, pady=5, sticky="w")
rope_freq_scale_entry.grid(row=18, column=1, padx=10, pady=5)

n_gqa_label.grid(row=19, column=0, padx=10, pady=5, sticky="w")
n_gqa_entry.grid(row=19, column=1, padx=10, pady=5)

rms_norm_eps_label.grid(row=20, column=0, padx=10, pady=5, sticky="w")
rms_norm_eps_entry.grid(row=20, column=1, padx=10, pady=5)

verbose_label.grid(row=21, column=0, padx=10, pady=5, sticky="w")
verbose_entry.grid(row=21, column=1, padx=10, pady=5)

load_button.grid(row=24, column=0, columnspan=2, pady=10)
save_button.grid(row=25, column=0, pady=10)
restore_button.grid(row=25, column=1, pady=10)
close_button.grid(row=26, column=0, columnspan=2, pady=10)




update_values()
root.mainloop()



