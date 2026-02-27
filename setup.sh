export UV_CACHE_DIR="../.tmp/uv" # change the directory to your own uv cache directory
export HF_MODEL_DIR="./models"

uv venv --python 3.11
source .venv/bin/activate

uv pip install vllm==0.11.0

uv pip install flash-attn --no-build-isolation
uv pip install -e .

uv pip install gymnasium==0.29.1
uv pip install stable-baselines3==2.6.0
uv pip install alfworld

alfworld-download -f

uv pip install hf_transfer

mkdir -p "$HF_MODEL_DIR"
hf download Qwen/Qwen2.5-1.5B-Instruct --cache-dir "$HF_MODEL_DIR"
hf download Qwen/Qwen2.5-7B-Instruct --cache-dir "$HF_MODEL_DIR"

