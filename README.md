# 📁 ChatGPT File Uploader Automation (Local Script)

This Python script automates the process of uploading a file to ChatGPT via the browser using Selenium and PyAutoGUI. It simulates the process of a user clicking the "+" button, selecting a file, entering a prompt, and sending it.

---

## Features

- Automatically connects to a pre-launched Chrome browser in debugging mode
- Uploads a file (e.g., Excel, image, PDF) to ChatGPT
- Sends a message like "explain this"
- Verifies if the file was uploaded successfully

---

## Important Notes

**This will NOT work on a cloud server or headless environment** because:
- It interacts with the actual Chrome GUI
- Uses `pyautogui` to handle OS-level file upload dialogs
- Requires an already logged-in ChatGPT session
- Needs manual Chrome launch in debugging mode

---

## 🛠 Requirements

- Python 3.7+
- Google Chrome
- ChromeDriver (matching your Chrome version)
- Installed Python packages:
  - `selenium`
  - `pyautogui`

Install packages:

```bash
pip install -r requirements.txt


## Setup Instructions

### 1. Launch Chrome with Remote Debugging (Windows)

Before running the script, you must start Chrome in remote debugging mode:

1. Close all running Chrome instances.

2. Open **Command Prompt**.

3. Run this command (adjust paths if needed):

```powershell
& "C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222 --user-data-dir="C:\ChromeSeleniumProfile"