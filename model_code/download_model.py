from huggingface_hub import hf_hub_download
import os


REPO_ID = "TheBloke/Pygmalion-13B-SuperHOT-8K-GGML"
FILENAME = "pygmalion-13b-superhot-8k.ggmlv3.q4_K_S.bin"
LOCAL_DIR = "../Resource/Model"  # Use forward slashes for directory paths

# Check if the local directory exists, and if not, create it
if not os.path.exists(LOCAL_DIR):
    os.makedirs(LOCAL_DIR)

# Check if the model file already exists in the local directory
model_path = os.path.join(LOCAL_DIR, FILENAME)
if not os.path.exists(model_path):
    print("Initiating Model Download!")
    # Download the model to the local directory
    hf_hub_download(repo_id=REPO_ID, filename=FILENAME, local_dir=LOCAL_DIR)
    print("MODEL DOWNLOAD COMPLETE")
else:
    print("Model already exists in the local directory. Skipping download.")

# Now you can proceed with using the model from `model_path` if it exists.
