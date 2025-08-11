import time
import subprocess
import os
from datetime import datetime, timedelta

def press_enter_periodically(interval_seconds=42, shutdown_minutes=None):
    """
    Presses Enter key periodically with optional shutdown timer
    
    Args:
        interval_seconds: Time between Enter presses (default 74)
        shutdown_minutes: System shutdown after this many minutes (optional)
    """
    shutdown_seconds = shutdown_minutes * 60 if shutdown_minutes else None
    start_time = time.time()
    
    try:
        print(f"\nScript started at {time.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"• Enter key every: {interval_seconds} seconds")
        if shutdown_seconds:
            shutdown_time = datetime.now() + timedelta(minutes=shutdown_minutes)
            print(f"• System will shutdown at: {shutdown_time.strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"  (in {shutdown_minutes} minutes)")
        print("Press Ctrl+C to stop\n")

        while True:
            # Use xdotool to press Enter (works in WSL with X forwarding)
            subprocess.run(['xdotool', 'key', 'Return'])
            
            current_time = time.strftime('%H:%M:%S')
            print(f"[{current_time}] Enter pressed")
            print(f"Another {interval_seconds} seconds wasted...")

            # Check for shutdown time
            if shutdown_seconds:
                elapsed = time.time() - start_time
                remaining_time = max(0, shutdown_seconds - elapsed)
                if remaining_time <= 0:
                    print("\nShutdown time reached! Initiating system shutdown...")
                    subprocess.run(['shutdown.exe', '/s', '/t', '60'])
                    return
                else:
                    mins, secs = divmod(remaining_time, 60)
                    print(f"  Shutdown in: {int(mins)}m {int(secs)}s")
            
            time.sleep(interval_seconds)
            
    except KeyboardInterrupt:
        print("\nScript stopped by user")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    try:
        # Get user inputs
        interval = int(input("Enter key interval in seconds (default 42): ") or 42)
        shutdown_input = input("Shutdown after how many minutes (leave blank to skip): ")
        shutdown_mins = int(shutdown_input) if shutdown_input else None

        # Install xdotool if not exists
        if subprocess.run(['which', 'xdotool'], capture_output=True).returncode != 0:
            print("Installing xdotool...")
            subprocess.run(['sudo', 'apt', 'install', '-y', 'xdotool'])
        
        print("\nStarting in 3 seconds... Focus your target window")
        time.sleep(3)
        
        press_enter_periodically(interval, shutdown_mins)
        
    except ValueError:
        print("Error: Please enter valid numbers")
