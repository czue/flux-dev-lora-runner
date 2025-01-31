Flux Dev Lora Runner
====================

A little script to run the [Flux Dev Lora model](https://replicate.com/lucataco/flux-dev-lora) on Replicate.

See [this blog post](https://www.coryzue.com/writing/train-ai-on-your-face/) for more context.

## Usage

```
uv run main.py "a vintage photo of CZUE, a 40 year old man, writing a blog post" \
 --model="czue/me-v1" \
 --count=4
```

Additional arguments:

- **model**: The hugging face model to use (repo id)
- **count**: The number of photos to generate (1-4, defaults to 1)
