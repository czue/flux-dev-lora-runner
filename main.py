# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "replicate",
# ]
# ///
import argparse
import os
import re
import replicate
import uuid

DEFAULT_MODEL = "czue/me-v1"
DEFAULT_COUNT = 1


def get_input(prompt, model=DEFAULT_MODEL, count=DEFAULT_COUNT):
    return {
        "prompt": prompt,
        "hf_lora": model,
        "num_outputs": count
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("prompt", help="Prompt for the photo")
    parser.add_argument("--model", default=DEFAULT_MODEL,
                      help="Model to use (default: %(default)s)")
    parser.add_argument("--count", default=DEFAULT_COUNT,
                      help="Number of photos to generate (default: %(default)s)", type=int)
    args = parser.parse_args()

    input = get_input(args.prompt, args.model, args.count)
    output = replicate.run(
        "lucataco/flux-dev-lora:091495765fa5ef2725a175a57b276ec30dc9d39c22d30410f2ede68a3eab66b3",
        input=input
    )

    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    # Remove special characters and convert to lowercase for the slug
    prompt_slug = "-".join(args.prompt.split(" ")[-3:])
    prompt_slug = re.sub(r'[^a-zA-Z0-9\-]', '', prompt_slug).lower()

    for index, item in enumerate(output):
        file_id = uuid.uuid4().hex[:5]
        output_path = os.path.join(output_dir, f"{prompt_slug}-{file_id}.webp")
        with open(output_path, "wb") as file:
            file.write(item.read())
            print(f"Saved photo {output_path}")
if __name__ == "__main__":
    main()
