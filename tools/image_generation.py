import os
import subprocess
from datetime import datetime
from io import BytesIO
from pathlib import Path
from google import genai
from PIL import Image
from dotenv import load_dotenv


def _get_api_key() -> str:
    env_file_path = os.getenv("ENV_FILE_PATH")
    load_dotenv(dotenv_path=env_file_path)
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError(
            "GOOGLE_API_KEY not found in environment variables. "
            "Please set it in your .env file."
        )
    return api_key


def _get_downloads_path() -> Path:
    return Path.home() / "Downloads"


def _save_and_open_image(image: Image.Image) -> str:
    downloads_path = _get_downloads_path()
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    image_path = downloads_path / f"generated_image_{timestamp}.png"

    image.save(image_path)

    subprocess.run(["open", str(image_path)], check=True)

    return str(image_path)


def generate_image(prompt: str) -> str:
    try:
        api_key = _get_api_key()
        client = genai.Client(api_key=api_key)

        response = client.models.generate_content(
            model="gemini-2.5-flash-image",
            contents=[prompt],
        )

        for part in response.candidates[0].content.parts:
            if part.inline_data is not None:
                image = Image.open(BytesIO(part.inline_data.data))
                image_path = _save_and_open_image(image)
                return f"Successfully generated image and saved to: {image_path}"

        return "Error: No image was generated in the response"

    except ValueError as e:
        return f"Configuration error: {str(e)}"
    except Exception as e:
        return f"Error generating image: {str(e)}"


def update_image(prompt: str, image_path: str) -> str:
    try:
        api_key = _get_api_key()
        client = genai.Client(api_key=api_key)

        if not os.path.exists(image_path):
            return f"Error: Image file not found at {image_path}"

        existing_image = Image.open(image_path)

        response = client.models.generate_content(
            model="gemini-2.5-flash-image",
            contents=[prompt, existing_image],
        )

        for part in response.candidates[0].content.parts:
            if part.inline_data is not None:
                image = Image.open(BytesIO(part.inline_data.data))
                new_image_path = _save_and_open_image(image)
                return f"Successfully updated image and saved to: {new_image_path}"

        return "Error: No image was generated in the response"

    except ValueError as e:
        return f"Configuration error: {str(e)}"
    except Exception as e:
        return f"Error updating image: {str(e)}"
