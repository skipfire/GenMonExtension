echo "Setup hostname"
sudo sed -i "s/raspberrypi/genmon/g" /etc/hostname
sudo sed -i "s/raspberrypi/genmon/g" /etc/hosts

echo "Create user pitemp"
echo "Enter a password of pitemp"
sudo adduser pitemp

echo "Setup locale"
sudo apt-get install -y locales-all git
sudo sed -i "s/en_GB/en_US/g" /etc/default/locale

echo "Setup keyboard"
sudo sed -i "s/gb/us/g" /etc/default/keyboard

echo "Setup timezone"
sudo timedatectl set-timezone America/New_York

echo "Add to sudoers"
echo 'pitemp ALL=(ALL:ALL) ALL' | sudo EDITOR='tee -a' visudo

echo "Updating apt"
sudo apt-get update
sudo apt-get upgrade

echo "Rebooting..."
echo "Login with user pitemp and run Step1-RenamePiUser.sh"
sudo reboot
