from huggingface_hub import hf_hub_download


REPO_ID = "TheBloke/CodeLlama-13B-Python-GGML"
FILENAME = "codellama-13b-python.ggmlv3.Q2_K.bin"

hf_hub_download(repo_id=REPO_ID, filename=FILENAME,local_dir = r"..\Resource\Model")
