import os
import pyautogui
import time

print(os.getcwd())

pyautogui.FAILSAFE = False

# Image file paths
launcher_download_path = "launcher.PNG"
website_download_path = "website.PNG"
staging_download_path = "staging.PNG"
threshold = 0.9

while True:
    try:
        print("Checking for Launcher Download Button")
        launcher_location = pyautogui.locateOnScreen(launcher_download_path, confidence=threshold)

        if launcher_location is not None:
            # Click on the launcher download button if found
            pyautogui.click(launcher_location.left + 5, launcher_location.top + 5)

        # Introduce a delay before taking the screenshot
        time.sleep(1)
    
    except pyautogui.ImageNotFoundException:
        # Handle the exception (e.g., print a message)
        print("Image not found. Waiting for the element to appear.")
        time.sleep(1)  # Add a delay before retrying

    try:
        print("Checking for Website Download Button")
        website_location = pyautogui.locateOnScreen(website_download_path, confidence=threshold)

        if website_location is not None:
            # Click on the website download button if found
            pyautogui.click(website_location.left + 5, website_location.top + 5)

        time.sleep(1)
        print("Waiting for 5 seconds...")
    except pyautogui.ImageNotFoundException:
        # Handle the exception (e.g., print a message)
        print("Image not found. Waiting for the element to appear.")
        time.sleep(1)  # Add a delay before retrying
    
    try:
        print("Checking for Staging Button")
        staging_location = pyautogui.locateOnScreen(staging_download_path, confidence=threshold)

        if staging_location is not None:
            pyautogui.click(staging_location.left + 5, staging_location.top + 5)

        # Introduce a delay before taking the screenshot
        time.sleep(1)
    
    except pyautogui.ImageNotFoundException:
        # Handle the exception (e.g., print a message)
        print("Image not found. Waiting for the element to appear.")
        time.sleep(1)  # Add a delay before retrying