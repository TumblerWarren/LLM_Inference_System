from llama_cpp import Llama
import prompt_formatting
import Value_Reading
import subprocess
from dotenv import load_dotenv
import os

load_dotenv("../.env")
load_history = os.environ.get("load_history")
save_history = os.environ.get("save_history")

subprocess.call(['python','Model_Parameters.py'])
subprocess.call(['python','prompt_template_setting.py'])

prompt_template_param = Value_Reading.get_prompt_template_param()
model_params = Value_Reading.get_model_parameter_value()

def generate (prompt, user_name):

    completion = llm.create_completion(prompt,
                                       suffix=prompt_template_param["suffix"],
                                       max_tokens=prompt_template_param["max_tokens"],
                                       temperature=prompt_template_param["temperature"],
                                       top_p=prompt_template_param["top_p"],
                                       logprobs=prompt_template_param["logprobs"],
                                       echo=prompt_template_param["echo"],
                                       stop=[user_name + ":"],
                                       frequency_penalty=0.0, presence_penalty=0.0,
                                       repeat_penalty=prompt_template_param["repeat_penalty"],
                                       top_k=prompt_template_param["top_k"],
                                       stream=prompt_template_param["stream"],
                                       tfs_z=1.0,
                                       mirostat_mode=0,
                                       mirostat_tau=5.0, mirostat_eta=0.1,
                                       model=None, stopping_criteria=None,
                                       logits_processor=None)
    return completion


llm = Llama(model_path=os.environ.get("MODEL_PATH"),
            n_ctx=model_params['n_ctx'], n_parts=model_params["n_parts"],
            n_gpu_layers=model_params["n_gpu_layers"], seed=model_params["seed"],
            f16_kv=model_params["f16_kv"], logits_all=model_params["logits_all"],
            vocab_only=model_params["vocab_only"], use_mmap=model_params["use_mmap"],
            use_mlock=model_params["use_mlock"], embedding=model_params["embedding"],
            n_threads=model_params["n_threads"], n_batch=model_params["n_batch"],
            last_n_tokens_size=model_params["last_n_tokens_size"], lora_base=model_params["lora_base"],
            lora_path=model_params["lora_path"], low_vram=model_params["low_vram"],
            tensor_split=model_params["tensor_split"], rope_freq_base=model_params["rope_freq_base"],
            rope_freq_scale=model_params["rope_freq_scale"], n_gqa=model_params["n_gqa"],
            rms_norm_eps=model_params["rms_norm_eps"], verbose=model_params["verbose"])

chat = ""

if load_history == "True":

    prompt,user_name,char_name = prompt_formatting.history_read()
    while 1:

        user_input = user_name + ": " + input("Enter your chat: ")
        ai = char_name + ": "
        prompt = f"{prompt}\n{user_input}\n{ai}"

        completion = generate(prompt, user_name)
        text = completion['choices'][0]['text']

        chat = f"{chat}\n{user_input}\n{ai}{text}"
        segment = f"{user_input}\n{ai}{text}"
        prompt_formatting.save_history(segment)
        prompt = f"{prompt}{text}"

        t_text = prompt.encode()
        prompt_length = len(llm.tokenize(t_text))
        prompt, chat = prompt_formatting.prompt_trimming(prompt_length, chat, prompt)

        print("TEXT: ", text)

else:

    prompt,user_name,char_name = prompt_formatting.card_read()
    while 1:

        user_input = user_name + ": " + input("Enter your chat: ")
        ai = char_name + ": "

        prompt = f"{prompt}\n{user_input}\n{ai}"

        completion = generate(prompt, user_name)
        text = completion['choices'][0]['text']

        chat = f"{chat}\n{user_input}\n{ai}{text}"
        segment = f"{user_input}\n{ai}{text}"
        prompt_formatting.save_history(segment)
        prompt = f"{prompt}{text}"

        t_text = prompt.encode()
        prompt_length = len(llm.tokenize(t_text))
        prompt, chat = prompt_formatting.prompt_trimming(prompt_length, chat, prompt)

        print("TEXT: ", text)





