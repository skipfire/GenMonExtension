echo "Setup timezone"
sudo timedatectl set-timezone America/New_York

echo "Setup hostname"
sudo sed -i "s/raspberrypi/genmon/g" /etc/hostname
sudo sed -i "s/raspberrypi/genmon/g" /etc/hosts

echo "Create user pitemp"
echo "Enter a password of pitemp"
sudo adduser pitemp

echo "Add to sudoers"
echo 'pitemp ALL=(ALL:ALL) ALL' | sudo EDITOR='tee -a' visudo

echo "Rebooting..."
echo "Login with user pitemp and run Step1-RenamePiUser.sh"
sudo reboot
