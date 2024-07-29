# mlx-apis

API sets for [MLX](https://huggingface.co/docs/hub/mlx) Models.

## Runtime Environment

* Machine
  * Mac with Apple Silicon
* Python
  * \>= 3.10

## Run

```bash
pip install -r requirements.txt
python app/main.py
```

## Access

```bash
curl -XPOST http://localhost:18081/api/llm/gemma2_mlx -d '{"text": "入力テキスト"}' -H "Content-Type: application/json"
```