from flask import Flask, request, jsonify
from llama_cpp import Llama
import prompt_formatting
import Value_Reading
from dotenv import load_dotenv
import os
import subprocess

load_dotenv(".env")

app = Flask(__name__)

# Load model parameters and initialize Llama model
subprocess.call(['python', 'Model_Parameters.py'])
subprocess.call(['python', 'prompt_template_setting.py'])
prompt_template_param = Value_Reading.get_prompt_template_param()
model_params = Value_Reading.get_model_parameter_value()
llm = Llama(model_path=os.environ.get("MODEL_PATH"),
            n_ctx=model_params['n_ctx'], n_parts=model_params["n_parts"],
            # ... (other model params)
            verbose=model_params["verbose"])

@app.route('/generate_response', methods=['POST'])
def generate_response():
    try:
        user_input = request.json['user_input']

        # Generate completion
        prompt = prompt_formatting.card_read()
        prompt = f"{prompt}\nWarren: {user_input}\nAyaka: "
        completion = llm.create_completion(prompt,
                                           suffix=prompt_template_param["suffix"],
                                           max_tokens=prompt_template_param["max_tokens"],
                                           temperature=prompt_template_param["temperature"],
                                           top_p=prompt_template_param["top_p"],
                                           logprobs=prompt_template_param["logprobs"],
                                           echo=prompt_template_param["echo"],
                                           stop=prompt_template_param["stop"],
                                           frequency_penalty=0.0, presence_penalty=0.0,
                                           repeat_penalty=prompt_template_param["repeat_penalty"],
                                           top_k=prompt_template_param["top_k"],
                                           stream=prompt_template_param["stream"],
                                           tfs_z=1.0,
                                           mirostat_mode=0,
                                           mirostat_tau=5.0, mirostat_eta=0.1,
                                           model=None, stopping_criteria=None,
                                           logits_processor=None)

        text = completion['choices'][0]['text']

        return jsonify({"response": text})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)