# Lazy Enter + Shutdown Script

## Overview
This two-script setup allows you to:
1. **Automatically press the Enter key** at a fixed interval to prevent inactivity.
2. **Schedule an automatic shutdown** after a set time.

Designed for use in **WSL (Windows Subsystem for Linux)** or Linux environments with access to Windows shutdown commands.

---

## File Descriptions

### `lazy_enter.py`
- Presses the Enter key periodically using `xdotool`.
- Accepts:
  - **Interval (seconds)** between presses.
  - **Shutdown time (minutes)** before initiating shutdown.
- If shutdown is enabled, it will trigger a shutdown through Windows (`shutdown.exe`) or can be configured to call `shutdown.sh`.

### `shutdown.sh`
- Executes a Windows shutdown after a given number of seconds.
- Usage:  
  ```bash
  ./shutdown.sh <seconds>
  ```
  

# Requirements
- Linux / WSL environment with:
  - Python 3
  - xdotool (for keypress simulation)

- Windows for the shutdown command (shutdown.exe).

- Permission to install packages and run shutdown commands.

## Installation
- Clone or copy both scripts into the same folder.

- Make shutdown.sh executable:

```bash
chmod +x shutdown.sh
```

- Install xdotool (if not already installed):

```bash
sudo apt update
sudo apt install xdotool
```

## Usage

### Basic: Just Press Enter
- Run:

```bash
python3 lazy_enter.py
```

- Enter an interval in seconds when prompted (default: 42).

- Leave shutdown time blank if you do not want to shutdown.

### With Shutdown Timer (using Windows shutdown.exe)
Run:

```bash
python3 lazy_enter.py
```
- Enter interval in seconds.
- Enter shutdown time in minutes.

The script will press Enter periodically and shut down the system when time expires.


### Example
Scenario: Press Enter every 60 seconds and shutdown after 30 minutes.

```bash
python3 lazy_enter.py
```
- Enter key interval in seconds (default 42): 60
- Shutdown after how many minutes (leave blank to skip): 30

Output:
```yaml
Script started at 2025-08-11 10:00:00
• Enter key every: 60 seconds
• System will shutdown at: 2025-08-11 10:30:00
  (in 30 minutes)
Press Ctrl+C to stop
```

## Notes
- Focus your target window before the first Enter press — xdotool sends keystrokes to the active window.

- Press Ctrl+C to stop the script manually.

- Shutdown delay with shutdown.exe defaults to 60 seconds before power-off.

