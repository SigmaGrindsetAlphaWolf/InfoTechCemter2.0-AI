import time
import sys

def get_user_input(prompt, default):
    """
    Helper function to get user input with a default value.
    """
    user_input = input(prompt + f" [{default}]: ").strip()
    return user_input if user_input else default

def print_loading_screen(loading_message, loading_speed):
    """
    Function to print the loading screen animation.
    """
    ellipsis = 0
    # Loop to simulate loading
    for _ in range(20):
        # Construct loading message with increasing ellipsis
        sys.stdout.write(f"\r{loading_message}{'.' * ellipsis}")
        # Update ellipsis
        ellipsis = (ellipsis + 1) % 4
        # Sleep for specified loading speed
        time.sleep(loading_speed)
    # Print final message when loading completes
    print("\nOperating System Booted Up - Retina Scanned - Access Granted!")

def main():
    # Get user inputs
    welcome_message = get_user_input("Enter welcome message", "Welcome to InfoTech Center V1.0")
    time_to_sleep = float(get_user_input("Enter time to sleep before loading (in seconds)", "1"))
    loading_message = get_user_input("Enter loading message", "InfoTech Center Operating System Loading")
    loading_speed = float(get_user_input("Enter loading speed (in seconds)", "0.5"))

    # Print welcome message and sleep
    print(f"\n\n{welcome_message}\n")
    time.sleep(time_to_sleep)

    # Print loading screen
    print_loading_screen(loading_message, loading_speed)

if __name__ == "__main__":
    main()