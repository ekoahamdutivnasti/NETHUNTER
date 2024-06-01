#!/bin/bash

# Display personalized message
echo "SUN BHAI ❤️ MAI INSTALL KARDUNGA TERE LIYE 'EKOAHAMDUTIVNASTI'"

# Update and upgrade Termux packages
pkg update -y
pkg upgrade -y

# Install dependencies
pkg install -y wget curl proot tar

# Download and install Kali NetHunter
wget -O install-nethunter-termux https://offs.ec/2MceZWr
chmod +x install-nethunter-termux
./install-nethunter-termux

# Cleanup
rm -f install-nethunter-termux

echo "Kali NetHunter installation completed."
