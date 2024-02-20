import requests
import json
from tqdm import tqdm
import time
import sys
import os

def clearConsole():
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Linux and Mac
        os.system('clear')

def fetchRawFile(url, filename):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status() # Cause an exception if there is a bad status code.

        d = []
        total_size = int(response.headers.get('content-length', 0))

        with open(filename, 'wb') as json_file:
            progress_bar = tqdm(total=total_size, unit='B', unit_scale=True, desc="Downloading", position=0)
            for data in response.iter_content(chunk_size=4096):
                json_file.write(data)
                progress_bar.update(len(data))
            progress_bar.close()

        print("File downloaded successfully.")

        with open(filename, 'r') as file:
            lines = file.readlines()
            progress_bar = tqdm(total=len(lines), desc="Saving", position=0)
            for line in lines:
                line = line.strip()
                if line and not line.startswith('#'):
                    d.append(line)

                    progress_bar.update(1)
                    progress_bar.set_postfix_str(f"{line} uploaded to file")

                    # time.sleep(0.001) # this delay isn't needed, uncomment this for the status bar to look cool though :D
            progress_bar.close()

        with open(filename, 'w') as json_file:
            json.dump(d, json_file, indent=4)

        print(f"\n{filename} saved successfully.")
    except requests.exceptions.RequestException as e:
        print(f"Failed to download: {e}")

if __name__ == "__main__":
    config = json.load(open("config.json"))

    # URL: MUST BE A RAW FILE (such as one from GithubUserContent)
    # FileName must end in .json

    if config["fileName"] != "" and config["downloadURL"] != "":
        if(config["fileName"].endswith(".json") and config["downloadURL"].startswith("http")):
            clearConsole() # Comment this out if you don't want to clear the console upon execution
            fetchRawFile(url=config["downloadURL"], filename=config["fileName"])
        else:
            print("Configuration values are not formatted correctly")
    else:
        print("Config values are not set")
    