import replicate


import argparse

def get_input(detail):
    return {
        "prompt": f"a photo of CZUE, a 40-year-old man, {detail}",
        "hf_lora": "czue/me-v1"
    }

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("detail", help="Additional details for the prompt")
    args = parser.parse_args()

    input = get_input(args.detail)
    output = replicate.run(
        "lucataco/flux-dev-lora:091495765fa5ef2725a175a57b276ec30dc9d39c22d30410f2ede68a3eab66b3",
        input=input
    )
    for index, item in enumerate(output):
        with open(f"output_{index}.webp", "wb") as file:
            file.write(item.read())


if __name__ == "__main__":
    main()
