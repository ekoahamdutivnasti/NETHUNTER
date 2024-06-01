#!/usr/bin/python

# This Python script automates the installation of Kali NetHunter on an Android device using Termux

# Print a greeting message
print("Hi bhai, mai aage dekh lunga mai hu ekolhamdutivnasti")

# Update the Termux package index
print("Updating Termux package index...")
os.system("termux-update")

# Install wget package
print("Installing wget package...")
os.system("pkg install wget")

# Download the NetHunter installer script
print("Downloading NetHunter installer script...")
os.system("wget -O install-nethunter-termux https://offs.ec/2MceZWr")

# Make the installer script executable
print("Making installer script executable...")
os.system("chmod +x install-nethunter-termux")

# Run the NetHunter installer script
print("Running NetHunter installer script...")
os.system("./install-nethunter-termux")

# Print a completion message
print("NetHunter installation complete!")
