from huggingface_hub import hf_hub_download
import os
from tqdm import tqdm  # Import tqdm for the progress bar

print("Initiating Model Download!")
REPO_ID = "TheBloke/Pygmalion-13B-SuperHOT-8K-GGML"
FILENAME = "pygmalion-13b-superhot-8k.ggmlv3.q4_K_S.bin"
LOCAL_DIR = "../Resource/Model"  # Use forward slashes for directory paths

# Check if the local directory exists, and if not, create it
if not os.path.exists(LOCAL_DIR):
    os.makedirs(LOCAL_DIR)

# Download the model to the local directory with a progress bar
with tqdm(total=1, unit="model") as pbar:
    def progress_callback(items_completed, total_items):
        pbar.n = items_completed
        pbar.total = total_items
        pbar.update()

    hf_hub_download(repo_id=REPO_ID, filename=FILENAME, local_dir=LOCAL_DIR, progress_callback=progress_callback)
    pbar.close()

print("MODEL DOWNLOAD COMPLETE")
