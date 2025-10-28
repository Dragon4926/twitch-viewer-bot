import requests
import warnings
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from colorama import Fore, init
from pystyle import Center, Colors, Colorate
import os
import time
import sys

init(autoreset=True)
warnings.filterwarnings("ignore", category=DeprecationWarning)

def check_for_updates():
    """Check for updates from GitHub repository"""
    try:
        r = requests.get(
            "https://raw.githubusercontent.com/Dragon4926/twitch-viewer-bot/main/version.txt",
            headers={"Cache-Control": "no-cache"},
            timeout=5
        )
        r.raise_for_status()
        remote_version = r.text.strip()
        
        with open('version.txt', 'r') as f:
            local_version = f.read().strip()
        
        print(f"Local version: {local_version}")
        print(f"Remote version: {remote_version}")
        
        if remote_version != local_version:
            print(Colors.yellow + Center.XCenter("\n⚠ A new version is available!"))
            print(Colors.cyan + Center.XCenter("Download: https://github.com/Dragon4926/twitch-viewer-bot\n"))
            time.sleep(3)
            return False
        return True
    except requests.RequestException as e:
        print(Colors.red + Center.XCenter(f"⚠ Could not check for updates: {e}"))
        print(Colors.yellow + Center.XCenter("Continuing with local version...\n"))
        time.sleep(2)
        return True
    except FileNotFoundError:
        print(Colors.red + Center.XCenter("⚠ version.txt not found!"))
        return True
    except Exception as e:
        print(Colors.red + Center.XCenter(f"⚠ Unexpected error: {e}"))
        return True


def main():
    """Main bot execution function"""
    if not check_for_updates():
        return

    # Set window title (Windows only)
    if sys.platform == 'win32':
        os.system("title Twitch View Bot 3.0 by dragon4926")
    
    # Updated proxy URLs
    proxy_servers = {
        1: "https://www.blockaway.net",
        2: "https://www.croxy.network",
        3: "https://www.croxy.org",
        4: "https://www.youtubeunblocked.live",
        5: "https://www.croxyproxy.net",
    }

    # Selecting proxy server
    print(Colors.orange, Center.XCenter("╔════════════════════════════════════════════════════════════════════════════╗"))
    print(Colors.red, Center.XCenter("If a server is not reachable, please let me know. I will update it then."))
    print(Colors.red, Center.XCenter("Select a server. Enter the Server number and press Enter."))
    print(Colorate.Vertical(Colors.green_to_blue,"  "))
    for i in range(1, 6):
        print(Colors.cyan, Center.XCenter(f"Server {i}: {proxy_servers[i]}"))
    print(Colors.orange, Center.XCenter("╚════════════════════════════════════════════════════════════════════════════╝"))
    
    while True:
        try:
            proxy_choice = int(input(Colorate.Vertical(Colors.cyan_to_blue, ">> ")))
            if proxy_choice in proxy_servers:
                proxy_url = proxy_servers[proxy_choice]
                break
            else:
                print(Colors.red + Center.XCenter("Invalid choice! Please select 1-5."))
        except ValueError:
            print(Colors.red + Center.XCenter("Please enter a valid number!"))
    
    # Select Twitch Account
    print(Colorate.Vertical(Colors.green_to_blue,"  "))
    print(Colorate.Vertical(Colors.green_to_blue,"  "))
    print(Colorate.Vertical(Colors.green_to_blue,"  "))
    print(Colors.orange, Center.XCenter("╔════════════════════════════════════════════════════════════════════════════╗"))
    print(Colors.cyan, Center.XCenter("Target Twitch account? Please provide only the username!"))
    print(Colors.cyan, Center.XCenter("Example: o7_streams  (NOT: www.twitch.tv/o7_streams)"))
    print(Colors.orange, Center.XCenter("╚════════════════════════════════════════════════════════════════════════════╝"))
    twitch_username = input(Colorate.Vertical(Colors.cyan_to_blue, ">>"))
    
    # Select viewer count
    print(Colorate.Vertical(Colors.green_to_blue,"  "))
    print(Colorate.Vertical(Colors.green_to_blue,"  "))
    print(Colorate.Vertical(Colors.green_to_blue,"  "))
    print(Colors.orange, Center.XCenter("╔════════════════════════════════════════════════════════════════════════════╗"))
    print(Colors.cyan, Center.XCenter("How many viewers should be sent?"))
    print(Colors.cyan, Center.XCenter("(Recommended: 5-20. Higher numbers may cause issues!)"))
    print(Colors.orange, Center.XCenter("╚════════════════════════════════════════════════════════════════════════════╝"))
    
    while True:
        try:
            proxy_count = int(input(Colorate.Vertical(Colors.cyan_to_blue, ">> ")))
            if 1 <= proxy_count <= 100:
                break
            else:
                print(Colors.red + Center.XCenter("Please enter a number between 1 and 100."))
        except ValueError:
            print(Colors.red + Center.XCenter("Please enter a valid number!"))
    
    # Clear screen
    if sys.platform == 'win32':
        os.system("cls")
    else:
        os.system("clear")

    print('')
    print(Colors.orange, Center.XCenter("╔════════════════════════════════════════════════════════════════════════════╗"))
    print(Colors.cyan, Center.XCenter("⚙ Initializing browser..."))
    print(Colors.cyan, Center.XCenter("The bot will start sending viewers."))
    print(Colors.cyan, Center.XCenter("If not all viewers arrive or it doesn't work,"))
    print(Colors.cyan, Center.XCenter("restart the bot or try a different proxy server."))
    print(Colors.orange, Center.XCenter("╚════════════════════════════════════════════════════════════════════════════╝"))

    # Chrome configuration
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
    chrome_options.add_argument('--disable-logging')
    chrome_options.add_argument('--log-level=3')
    chrome_options.add_argument('--disable-extensions')
    chrome_options.add_argument('--headless=new')  # Updated headless mode
    chrome_options.add_argument('--mute-audio')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--no-sandbox')  # Additional stability
    chrome_options.add_argument('--disable-gpu')  # Better compatibility
    chrome_options.add_argument('--window-size=1920,1080')
    
    # Try to initialize Chrome driver
    driver = None
    try:
        print(Colors.yellow + Center.XCenter("Starting Chrome WebDriver..."))
        driver = webdriver.Chrome(options=chrome_options)
        print(Colors.green + Center.XCenter("✓ WebDriver started successfully!"))
    except Exception as e:
        print(Colors.red + Center.XCenter(f"✘ Failed to start Chrome: {e}"))
        print(Colors.yellow + Center.XCenter("Make sure Chrome and chromedriver.exe are properly installed."))
        input("Press ENTER to exit...")
        return

    try:
        # Navigate to proxy in first window
        print(Colors.cyan + Center.XCenter(f"Loading proxy server: {proxy_url}"))
        driver.get(proxy_url)
        time.sleep(2)
        
        # Create and configure viewer windows
        successful_viewers = 0
        failed_viewers = 0
        
        for i in range(proxy_count):
            try:
                print(Colors.yellow + Center.XCenter(f"Creating viewer {i+1}/{proxy_count}..."))
                
                # Open new tab
                driver.execute_script(f"window.open('{proxy_url}', '_blank');")
                driver.switch_to.window(driver.window_handles[-1])
                
                # Wait for page to load
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.ID, 'url'))
                )
                
                # Enter Twitch URL
                text_box = driver.find_element(By.ID, 'url')
                text_box.clear()
                text_box.send_keys(f'www.twitch.tv/{twitch_username}')
                text_box.send_keys(Keys.RETURN)
                
                successful_viewers += 1
                time.sleep(0.5)  # Small delay between viewers
                
            except TimeoutException:
                print(Colors.red + Center.XCenter(f"Timeout creating viewer {i+1}"))
                failed_viewers += 1
            except NoSuchElementException:
                print(Colors.red + Center.XCenter(f"Could not find URL input for viewer {i+1}"))
                failed_viewers += 1
            except Exception as e:
                print(Colors.red + Center.XCenter(f"Error creating viewer {i+1}: {str(e)[:50]}"))
                failed_viewers += 1
                
    except Exception as e:
        print(Colors.red + Center.XCenter(f"Critical error: {e}"))
        if driver:
            driver.quit()
        input("Press ENTER to exit...")
        return

    # Display results
    if sys.platform == 'win32':
        os.system("cls")
    else:
        os.system("clear")

    print('')
    print(Colors.orange, Center.XCenter("╔════════════════════════════════════════════════════════════════════════════╗"))
    print(Colors.green, Center.XCenter("✓ Bot setup complete!"))
    print(Colors.cyan, Center.XCenter(""))
    print(Colors.cyan, Center.XCenter(f"Target channel: twitch.tv/{twitch_username}"))
    print(Colors.cyan, Center.XCenter(f"Successful viewers: {successful_viewers}"))
    if failed_viewers > 0:
        print(Colors.yellow, Center.XCenter(f"Failed viewers: {failed_viewers}"))
    print(Colors.cyan, Center.XCenter(""))
    print(Colors.cyan, Center.XCenter("If the viewer count decreases or the bot stops working,"))
    print(Colors.cyan, Center.XCenter("consider restarting the script or trying a different proxy server."))
    print(Colors.cyan, Center.XCenter(""))
    print(Colors.green, Center.XCenter("Keep this window open for as long as you want the viewers active."))
    print(Colors.yellow, Center.XCenter("Press ENTER to stop the bot and close all viewers."))
    print(Colors.orange, Center.XCenter("╚════════════════════════════════════════════════════════════════════════════╝"))
    
    try:
        input(Colorate.Vertical(Colors.cyan_to_blue, ">> "))
    except KeyboardInterrupt:
        print("\n" + Colors.yellow + Center.XCenter("Stopping bot..."))
    finally:
        print(Colors.cyan + Center.XCenter("Closing browser windows..."))
        if driver:
            driver.quit()
        print(Colors.green + Center.XCenter("✓ Bot stopped successfully!"))
        time.sleep(1)


if __name__ == '__main__':
    main()
