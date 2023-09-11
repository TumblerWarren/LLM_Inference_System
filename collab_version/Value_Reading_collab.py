import os
import env_file_reading
def get_prompt_template_param():

    prompt_data=env_file_reading.env_prompt_template_read()
    template_params={}

    if prompt_data["suffix"] == "None" or prompt_data["suffix"] == "":
        template_params["suffix"]=None
    else:
        template_params["suffix"] = prompt_data["suffix"]

    if prompt_data["logprobs"] == "None" or prompt_data["logprobs"] == "":
        template_params["logprobs"] = None
    else:
        template_params["logprobs"] = int(prompt_data["logprobs"])

    template_params["max_tokens"] = int(prompt_data["max_tokens"])
    template_params["temperature"] = float(prompt_data["temperature"])
    template_params["top_p"] = float(prompt_data["top_p"])
    template_params["repeat_penalty"] = float(prompt_data["repeat_penalty"])
    template_params["top_k"] = int(prompt_data["top_k"])

    template_params["echo"] = False


    template_params["stream"] = False

    if prompt_data["stop"] == "":
        template_params["stop"] = []
    else:
        template_params["stop"] = [prompt_data["stop"]]

    return template_params



def get_model_parameter_value():
    model_data = env_file_reading.env_model_param_read()
    model_params = {}
    model_params["n_ctx"] = int(model_data["n_ctx"])
    model_params["n_parts"] = int(model_data["n_parts"])
    model_params["n_gpu_layers"] = int(model_data["n_gpu_layers"])
    model_params["seed"] = int(model_data["seed"])

    f16_kv_value = model_data["f16_kv"]
    if f16_kv_value.lower() == "true":
        model_params["f16_kv"] = True
    elif f16_kv_value.lower() == "false":
        model_params["f16_kv"] = False

    model_params["logits_all"] = model_data["logits_all"]
    if model_params["logits_all"].lower() == "true":
        model_params["logits_all"] = True
    else:
        model_params["logits_all"] = False

    model_params["vocab_only"] = model_data["vocab_only"]
    if model_params["vocab_only"].lower() == "true":
        model_params["vocab_only"] = True
    else:
        model_params["vocab_only"] = False

    model_params["use_mmap"] = model_data["use_mmap"]
    if model_params["use_mmap"].lower() == "true":
        model_params["use_mmap"] = True
    else:
        model_params["use_mmap"] = False

    model_params["use_mlock"] = model_data["use_mlock"]
    if model_params["use_mlock"].lower() == "true":
        model_params["use_mlock"] = True
    else:
        model_params["use_mlock"] = False

    model_params["embedding"] = model_data["embedding"]
    if model_params["embedding"].lower() == "true":
        model_params["embedding"] = True
    else:
        model_params["embedding"] = False

    if (model_data["n_threads"]) == 'None':
        model_params["n_threads"] = None
    else:
        model_params["n_threads"] = int(model_data["n_threads"])

    model_params["n_batch"] = int(model_data["n_batch"])
    model_params["last_n_tokens_size"] = int(model_data["last_n_tokens_size"])

    if model_data["lora_base"] == 'None':
        model_params["lora_base"] = None
    else:
        model_params["lora_base"] = model_data["lora_base"]

    if model_data["lora_path"] == 'None':
        model_params["lora_path"] = None
    else:
        model_params["lora_path"] = model_data["lora_path"]

    model_params["low_vram"] = bool(model_data["low_vram"])
    model_params["tensor_split"] = None
    model_params["rope_freq_base"] = float(model_data["rope_freq_base"])
    model_params["rope_freq_scale"] = float(model_data["rope_freq_scale"])

    if model_data["n_gqa"] == 'None':
        model_params["n_gqa"] = None
    else:
        model_params["n_gqa"] = int(model_data["n_gqa"])

    if model_data["rms_norm_eps"] == 'None':
        model_params["rms_norm_eps"] = None
    else:
        model_params["rms_norm_eps"] = float(model_data["rms_norm_eps"])


    model_params["verbose"] = bool(model_data["verbose"])
    model_params["mul_mat_q"] = None
    return model_params
