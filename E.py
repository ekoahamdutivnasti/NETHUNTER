import os
import subprocess

# Print the initial message
print("HI THIS IS EKOAHAMDUTIVNASTI MAI KARLETA HU NETHUNTER INSTALL TU CHILL KAR")

# Define the commands to be executed
commands = [
    "pkg update -y",

    "pkg install wget curl proot git -y",
    "wget -O install-nethunter-termux https://offs.ec/2MceZWr",
    "chmod +x install-nethunter-termux",
    "./install-nethunter-termux"
]

# Function to execute commands in Termux
def run_commands():
    for command in commands:
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        if process.returncode != 0:
            print(f"Error executing command: {command}")
            print(stderr.decode())
        else:
            print(stdout.decode())

# Run the commands
run_commands()

