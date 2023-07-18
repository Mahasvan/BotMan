import os
import subprocess
import sys
import time

client = r"https://github.com/Mahas1/BotManClient"
server = r"https://github.com/Mahas1/BotManServer"


def get_project_root():
    """Returns the absolute path to the project's root directory."""
    return os.path.abspath(os.path.dirname(__file__))


root = get_project_root()

os.chdir(root)

if not os.path.exists("BotManClient"):
    print("Cloning Client...")
    try:
        x = subprocess.call(["git", "clone", client])
        if x != 0:
            print("Clone failed. Please try again.")
            sys.exit(1)
    except FileNotFoundError:
        print("It seems git is not installed. Please install Git and try again.")
        sys.exit(1)
    finally:
        print("Client has been cloned. Configure `config.json` and run this script again.")
else:
    os.chdir("BotManClient")
    print("Updating Client...")
    try:
        x = subprocess.call(["git", "pull"])
        if x != 0:
            print("Update failed. Please try again.")
            sys.exit(1)
    except FileNotFoundError:
        print("It seems git is not installed. Please install Git and try again.")
    finally:
        os.chdir(root)

if not os.path.exists("BotManServer"):
    print("Cloning Server...")
    try:
        x = subprocess.call(["git", "clone", server])
        if x != 0:
            print("Clone failed. Please try again.")
            sys.exit(1)
    except FileNotFoundError:
        print("It seems git is not installed. Please install Git and try again.")
    finally:
        print("Server has been cloned. Configure `config.json` and run this script again.")
else:
    print("Updating Server...")
    os.chdir("BotManServer")
    try:
        x = subprocess.call(["git", "pull"])
        if x != 0:
            print("Update failed. Please try again.")
            sys.exit(1)
    except FileNotFoundError:
        print("It seems git is not installed. Please install Git and try again.")
    finally:
        os.chdir(root)

print("Done!")

print("Starting Server...")
os.chdir("BotManServer")  # FastAPI Server
subprocess.Popen([sys.executable, 'app.py'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
print("Server is now on!")

print("Waiting for 1 second")
time.sleep(1)
os.chdir("..")

print("Starting Client...")
os.chdir("BotManClient")  # Discord.py client
process = subprocess.call([sys.executable, 'main.py'])
