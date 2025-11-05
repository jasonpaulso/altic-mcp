# Altic MCP

An MCP server that gives Claude hands-on control of your Mac, what Siri should've been 

## Features

20+ tools for macOS automation:
- 📱 **Messages & Contacts** - Send/read iMessages, search contacts
- 📝 **Notes & Reminders** - Create and search notes, set reminders  
- 📅 **Calendar** - Create and view events
- 🌐 **Safari** - Control tabs, navigate, execute JavaScript
- 🖥️ **System** - Open apps, adjust brightness/volume, visual effects

## Requirements

- macOS 10.13+
- Python 3.13+
- [UV package manager](https://docs.astral.sh/uv/getting-started/installation/)

## Quick Start

### Option 1: Install as UV Tool (Recommended)

```bash
# Install UV if needed
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install altic-mcp as a tool
git clone https://github.com/altic-dev/altic-mcp.git
cd altic-mcp
uv tool install .

# Test it works
altic-mcp-server
```

### Option 2: Local Development Setup

```bash
# Install UV if needed
curl -LsSf https://astral.sh/uv/install.sh | sh

# Clone and setup
git clone https://github.com/altic-dev/altic-mcp.git
cd altic-mcp
uv sync

# Test locally
uv run server.py
```

## Setup with Claude Desktop

### Using UV Tool Install (Recommended)

After installing as a UV tool, edit `~/Library/Application Support/Claude/claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "altic-mcp": {
      "command": "altic-mcp-server"
    }
  }
}
```

### Using Local Path

**1. Edit `~/Library/Application Support/Claude/claude_desktop_config.json`:**

```json
{
  "mcpServers": {
    "altic-mcp": {
      "command": "uv",
      "args": ["run", "/FULL/PATH/TO/altic-mcp/server.py"]
    }
  }
}
```

Replace `/FULL/PATH/TO/altic-mcp` with your actual path (e.g., `/Users/johndoe/Documents/altic-mcp`).

**2. Restart Claude Desktop** (Command + Q, then reopen)

**3. Look for the 🔨 hammer icon** in the chat interface to see available tools

## Permissions Required


### System Preferences → Privacy & Security:
- ✅ **Contacts** - For search_contacts
- ✅ **Calendars** - For calendar events
- ✅ **Reminders** - For creating reminders
- ✅ **Automation** - Allow Claude to control apps (Messages, Notes, Safari)
- ✅ **Accessibility** - For screen glow and system controls

### Safari Settings:
Safari → Develop → **Allow JavaScript from Apple Events** ✅ (Required for Safari tools)

*Note: If "Develop" menu is not visible, enable it in Safari → Settings → Advanced → Show Develop menu*

macOS will prompt for permissions when first used. Grant them to enable full functionality.
