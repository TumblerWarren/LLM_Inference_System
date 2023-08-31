import os
from dotenv import load_dotenv




def get_prompt_template_param():
    load_dotenv("../.env_prompt_template_setting")
    template_params={}

    if os.environ.get("suffix") == "None" or os.environ.get("suffix") == "":
        template_params["suffix"]=None
    else:
        template_params["suffix"] = os.environ.get("suffix")

    if os.environ.get("logprobs") == "None" or os.environ.get("logprobs") == "":
        template_params["logprobs"] = None
    else:
        template_params["logprobs"] = int(os.environ.get("logprobs"))

    template_params["max_tokens"] = int(os.environ.get("max_tokens"))
    template_params["temperature"] = float(os.environ.get("temperature"))
    template_params["top_p"] = float(os.environ.get("top_p"))
    template_params["repeat_penalty"] = float(os.environ.get("repeat_penalty"))
    template_params["top_k"] = int(os.environ.get("top_k"))

    template_params["echo"] = False


    template_params["stream"] = False

    if os.environ.get("stop") == "":
        template_params["stop"] = []
    else:
        template_params["stop"] = [os.environ.get("stop")]

    return template_params



def get_model_parameter_value():
    load_dotenv("../.env_model_param")
    model_params = {}
    model_params["n_ctx"] = int(os.environ.get("n_ctx"))
    model_params["n_parts"] = int(os.environ.get("n_parts"))
    model_params["n_gpu_layers"] = int(os.environ.get("n_gpu_layers"))
    model_params["seed"] = int(os.environ.get("seed"))

    f16_kv_value = os.environ.get("f16_kv")
    if f16_kv_value.lower() == "true":
        model_params["f16_kv"] = True
    elif f16_kv_value.lower() == "false":
        model_params["f16_kv"] = False

    model_params["logits_all"] = os.environ.get("logits_all", "False")
    if model_params["logits_all"].lower() == "true":
        model_params["logits_all"] = True
    else:
        model_params["logits_all"] = False

    model_params["vocab_only"] = os.environ.get("vocab_only", "False")
    if model_params["vocab_only"].lower() == "true":
        model_params["vocab_only"] = True
    else:
        model_params["vocab_only"] = False

    model_params["use_mmap"] = os.environ.get("use_mmap", "False")
    if model_params["use_mmap"].lower() == "true":
        model_params["use_mmap"] = True
    else:
        model_params["use_mmap"] = False

    model_params["use_mlock"] = os.environ.get("use_mlock", "False")
    if model_params["use_mlock"].lower() == "true":
        model_params["use_mlock"] = True
    else:
        model_params["use_mlock"] = False

    model_params["embedding"] = os.environ.get("embedding", "False")
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

