#!/usr/bin/env python3
"""Generate an illustration using Nano Banana Pro (Gemini image generation API)."""

import argparse
import os
import sys


def load_api_key():
    """Load GEMINI_API_KEY from environment or .env file."""
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key:
        return api_key

    env_path = os.path.join(os.getcwd(), ".env")
    if os.path.exists(env_path):
        with open(env_path) as f:
            for line in f:
                line = line.strip()
                if line.startswith("GEMINI_API_KEY="):
                    return line.split("=", 1)[1]

    print("ERROR: GEMINI_API_KEY not found in environment or .env file", file=sys.stderr)
    sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="Generate or edit an image using Nano Banana Pro")
    parser.add_argument("--prompt", required=True, help="Image generation/editing prompt")
    parser.add_argument("--output", required=True, help="Output file path (PNG)")
    parser.add_argument("--input", action="append", default=[], help="Input image path(s) for editing (can be specified multiple times)")
    parser.add_argument("--aspect-ratio", default="16:9", help="Aspect ratio (default: 16:9)")
    parser.add_argument("--image-size", default="2K", help="Image size: 1K, 2K, or 4K (default: 2K)")
    args = parser.parse_args()

    try:
        from google import genai
        from google.genai import types
        from PIL import Image
    except ImportError:
        print("ERROR: google-genai package not installed. Run: pip install google-genai Pillow", file=sys.stderr)
        sys.exit(1)

    api_key = load_api_key()
    client = genai.Client(api_key=api_key)

    mode = "Editing" if args.input else "Generating"
    print(f"{mode} image with Nano Banana Pro (gemini-3-pro-image-preview)...")
    if args.input:
        for path in args.input:
            print(f"  Input: {path}")
    print(f"  Aspect ratio: {args.aspect_ratio}")
    print(f"  Image size: {args.image_size}")
    print(f"  Output: {args.output}")

    contents = []
    contents.append(args.prompt)
    for path in args.input:
        if not os.path.exists(path):
            print(f"ERROR: Input image not found: {path}", file=sys.stderr)
            sys.exit(1)
        contents.append(Image.open(path))

    response = client.models.generate_content(
        model="gemini-3-pro-image-preview",
        contents=contents,
        config=types.GenerateContentConfig(
            response_modalities=["IMAGE"],
            image_config=types.ImageConfig(
                aspect_ratio=args.aspect_ratio,
                image_size=args.image_size,
            ),
        ),
    )

    os.makedirs(os.path.dirname(os.path.abspath(args.output)), exist_ok=True)

    for part in response.parts:
        if part.text is not None:
            print(f"Model response: {part.text}")
        elif part.inline_data is not None:
            image = part.as_image()
            image.save(args.output)
            size = os.path.getsize(args.output)
            print(f"OK: Saved {size:,} bytes to {args.output}")
            return

    print("ERROR: No image data in response", file=sys.stderr)
    sys.exit(1)


if __name__ == "__main__":
    main()
