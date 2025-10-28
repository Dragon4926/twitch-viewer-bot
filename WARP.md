# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Project Overview

This is a Python-based Twitch viewer bot that uses Selenium WebDriver and proxy servers to simulate multiple viewers on a Twitch channel. The project is educational in nature and violates Twitch's terms of service.

**Key Warning**: This tool is for educational purposes only. Using it violates Twitch's terms of service and can result in account suspension.

## Commands

### Environment Setup
```powershell
# Install dependencies (standard installation)
pip install -r requirements.txt

# Or use the virtual environment (recommended)
.\twitch\Scripts\Activate.ps1
pip install -r requirements.txt
```

### Running the Bot
```powershell
# Run the main bot script
python main.py
```

### Dependencies Management
The project uses `requirements.txt` (not `req.txt` as mentioned in README):
- colorama (terminal color output)
- pystyle (styled terminal output)
- selenium (web automation)
- requests (HTTP requests for update checking)

### ChromeDriver Setup
- Download ChromeDriver compatible with your Chrome browser version
- Place `chromedriver.exe` in the project root directory
- Run chromedriver.exe as administrator before running the bot
- Default Chrome path is hardcoded: `C:\Program Files\Google\Chrome\Application\chrome.exe`

## Architecture

### Single-File Design
The entire bot logic is contained in `main.py` with no modular architecture. The script follows a procedural flow:

1. **Update Check** (`check_for_updates()`): Compares local `version.txt` with remote GitHub version
2. **Proxy Selection**: User selects from 5 hardcoded proxy servers (blockaway.net, croxy.network, etc.)
3. **Target Configuration**: User inputs Twitch username and viewer count
4. **Selenium Automation**: Creates multiple Chrome browser tabs, each accessing the Twitch channel through the selected proxy

### Key Components

**Proxy Servers** (lines 35-41):
- Hardcoded dictionary of 5 proxy server URLs
- Used to bypass detection by appearing as different viewers
- If a server is unreachable, it needs manual updating in the code

**Browser Configuration** (lines 84-96):
- Headless Chrome with logging disabled
- Audio muted, extensions disabled
- Hardcoded Chrome binary path (Windows-specific)
- Uses local `chromedriver.exe`

**Core Workflow** (lines 100-108):
- Opens multiple browser windows (one per desired viewer)
- Each window navigates to the proxy server
- Finds the URL input field by ID 'url'
- Submits the Twitch channel URL through the proxy
- Keeps windows open until user presses ENTER

### Critical Assumptions
- Chrome installed at `C:\Program Files\Google\Chrome\Application\chrome.exe`
- `chromedriver.exe` exists in project root
- Proxy servers use an input field with ID 'url'
- Windows OS (uses `os.system("cls")` and `title` command)

### Version Management
- Local version stored in `version.txt` (currently 2.0.25)
- Remote version checked from GitHub raw URL
- No automatic updates, just notification

## Code Editing Guidelines

### When Modifying Proxy Servers
The proxy server dictionary is at lines 35-41. Ensure new servers:
- Have a URL input field with ID 'url'
- Support Twitch.tv access
- Are active and reachable

### When Modifying Browser Options
Chrome options are configured at lines 87-95. Critical flags:
- `--headless`: Required for background operation
- `--mute-audio`: Prevents audio from multiple streams
- `excludeSwitches: ['enable-logging']`: Reduces console spam

### Path Modifications
If changing file paths, update:
- `chrome_path` (line 84): Chrome browser location
- `driver_path` (line 85): ChromeDriver location
- Version check URL (line 15): For update checking

### Platform Compatibility
The code is Windows-specific:
- Line 32: `os.system(f"title ...")` (Windows-only)
- Line 75, 110: `os.system("cls")` (Windows-only)
- Line 84: Hardcoded Windows Chrome path

For Linux/Mac support, these need conditional logic based on `platform.system()`.

## Virtual Environment

A Python virtual environment exists in the `twitch/` directory. To use it:

```powershell
# Activate
.\twitch\Scripts\Activate.ps1

# Deactivate
deactivate
```
