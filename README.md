# Altic MCP - macOS Automation Server

A Model Context Protocol (MCP) server providing macOS automation tools including system control, Safari automation, messaging, calendar, notes, reminders, and AI-powered image generation.

## Features

### 🎨 Image Generation (Gemini AI)
- **Generate Image**: Create new images from text prompts using Google's Gemini 2.5 Flash Image model
- **Update Image**: Edit existing images based on text descriptions

### 📱 Messages & Contacts
- Send iMessages
- Search contacts
- Read recent message history

### 📅 Calendar & Reminders
- Create calendar events
- List events for specific days
- Set reminders

### 📝 Notes
- Create notes
- Search notes

### 🌐 Safari Automation
- Open/close tabs and windows
- Navigate, reload, go back/forward
- Execute JavaScript in tabs
- Get page information
- List all open tabs

### ⚙️ System Control
- Adjust screen brightness
- Control system volume
- Open applications
- Visual feedback (screen glow) for automation actions

## Setup

### 1. Install Dependencies

```bash
uv sync
```

### 2. Configure API Keys

For image generation features, you need a Google Gemini API key:

1. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```

2. Get your API key from [Google AI Studio](https://aistudio.google.com/apikey)

3. Edit `.env` and add your API key:
   ```
   GOOGLE_API_KEY=your_actual_api_key_here
   ```

### 3. Run the Server

```bash
python server.py
```

## Image Generation Usage

### Generate New Images

```python
# The LLM can call this tool to create new images
generate_image("A nano banana dish in a fancy restaurant with a Gemini theme")
```

The generated image will be:
- Saved to your `~/Downloads` folder with a timestamp
- Automatically opened in your default image viewer

### Update Existing Images

```python
# The LLM can call this tool to edit existing images
update_image(
    "Add a Gemini constellation in the background",
    "/path/to/existing/image.png"
)
```

The updated image will be:
- Saved as a new file in `~/Downloads` with a timestamp
- Automatically opened in your default image viewer

## Requirements

- macOS (tested on macOS Sonoma and later)
- Python 3.13+
- Google Gemini API key (for image generation features)

## Dependencies

- `fastmcp` - MCP server framework
- `google-genai` - Google Gemini API client
- `pillow` - Image processing
- `python-dotenv` - Environment variable management
- `rapidfuzz` - Fuzzy string matching

## License

See LICENSE file for details.

