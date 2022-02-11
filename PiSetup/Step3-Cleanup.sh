echo "Removing pitemp user and setup scripts"
sudo userdel -r pitemp
sudo rm -r /boot/Step*.sh

echo "Cleanup complete."