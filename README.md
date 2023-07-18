# BotMan
Quick setup for BotManServer and BotManClient

Prerequisites
- Git
- Python 3.9 or higher

When you have the required dependencies, run the main.py script.


```bash
# Run this script in the directory you want to set up 
# the Server-Client combo.

cd YourPreferredFolder
python3 main.py
```
This script creates the directories BotManClient and BotManServer in the file's directory.


Here are a few things to remember.
- After cloning, fill in the required fields in the `config.json` files in the Client and Server directories. (You may need to do this twice.)
- Then, run the script again, and it will run the server in the background and the client in the foreground.
- If you want to close the server, kill the Python process.
- If you want to shut down the client, exit the script by pressing Ctrl+C.
