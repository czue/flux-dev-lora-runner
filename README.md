Flux Dev Lora Runner
====================

A little script to run the [Flux Dev Lora model](https://replicate.com/lucataco/flux-dev-lora) on Replicate.

See [this blog post](https://www.coryzue.com/writing/train-ai-on-your-face/) for more context.

## Usage

```
uv run main.py "writing a blog post" \
 --model="czue/me-v1" \
 --trigger=CZUE \
 --extra_context="a 40 year old man"\
 --count=4
```

Explanation of additional arguments:

- **model**: The hugging face model to use (repo id)
- **trigger**: The trigger word you used when training your model.
- **extra_context**: Any extra context to provide.
- **count**: The number of photos to generate
