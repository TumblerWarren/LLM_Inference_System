from huggingface_hub import hf_hub_download
import os

REPO_ID = "TheBloke/Pygmalion-2-7B-GGUF"
FILENAME = "pygmalion-2-7b.Q5_K_M.gguf"
LOCAL_DIR = "../Resource/Model"  # Use forward slashes for directory paths

# Check if the local directory exists, and if not, create it
if not os.path.exists(LOCAL_DIR):
    os.makedirs(LOCAL_DIR)

# Download the model to the local directory
hf_hub_download(repo_id=REPO_ID, filename=FILENAME, local_dir=LOCAL_DIR)
