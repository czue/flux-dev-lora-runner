# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "replicate",
# ]
# ///
import uuid
import replicate
import argparse

DEFAULT_MODEL = "czue/me-v1"
DEFAULT_TOKEN = "CZUE"
DEFAULT_EXTRA_CONTEXT = ""
DEFAULT_COUNT = 1


def get_input(prompt, model=DEFAULT_MODEL, token=DEFAULT_TOKEN, additional_context=DEFAULT_EXTRA_CONTEXT, count=DEFAULT_COUNT):
    formatted_prefix = f"A photo of {token}{', ' + additional_context if additional_context else ''}"
    return {
        "prompt": f"{formatted_prefix}, {prompt}",
        "hf_lora": model,
        "num_outputs": count
    }

def slugify(text):
        # Convert to lowercase and replace spaces with hyphens
        text = text.lower().strip()
        # Remove special characters and replace spaces with hyphens
        result = ""
        for char in text:
            if char.isalnum() or char in [' ', '-']:
                result += char
        return '-'.join(result.split())


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("prompt", help="Prompt for the photo")
    parser.add_argument("--model", default=DEFAULT_MODEL,
                      help="Model to use (default: %(default)s)")
    parser.add_argument("--extra_context", default=DEFAULT_EXTRA_CONTEXT,
                      help="Prefix template for the prompt (default: %(default)s)")
    parser.add_argument("--token", default=DEFAULT_TOKEN,
                      help="Token to use in prefix (default: %(default)s)")
    parser.add_argument("--count", default=DEFAULT_COUNT,
                      help="Number of photos to generate (default: %(default)s)", type=int)
    args = parser.parse_args()

    input = get_input(args.prompt, args.model, args.token, args.extra_context, args.count)
    output = replicate.run(
        "lucataco/flux-dev-lora:091495765fa5ef2725a175a57b276ec30dc9d39c22d30410f2ede68a3eab66b3",
        input=input
    )
    import os

    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    prompt_slug = slugify(args.prompt)[:20]  # Limit length to 20 chars
    for index, item in enumerate(output):
        file_id = uuid.uuid4().hex[:5]
        output_path = os.path.join(output_dir, f"{prompt_slug}-{file_id}.webp")
        with open(output_path, "wb") as file:
            file.write(item.read())
            print(f"Saved photo {output_path}")
if __name__ == "__main__":
    main()
