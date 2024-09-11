# URL Ping CLI Tool

This is a simple Python-based command-line tool that continuously pings a specified URL and returns its HTTP status code every 5 minutes. The tool provides a visually appealing output using the `rich` library for colored and styled terminal text.

## Features:
- Pings a given URL and returns the HTTP status code.
- Automatically retries every 5 minutes, with a friendly wait message.
- Color-coded output based on the HTTP status code:
  - **Green** for 2xx (success).
  - **Yellow** for 4xx (client errors).
  - **Red** for 5xx (server errors).
- Easy to run on Mac (iTerm2, zsh) or any terminal that supports Python 3.

## Prerequisites
- Python 3.x
- Install required packages via pip:
    ```bash
    pip3 install requests rich
    ```

## Usage:
```bash
./ping_url.py <URL>
```

<img width="1512" alt="Skärmavbild 2024-09-11 kl  12 49 47" src="https://github.com/user-attachments/assets/488dcfb6-beaa-48fd-935b-b6f5599d01a6">

