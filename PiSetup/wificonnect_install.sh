sudo curl -L https://github.com/balena-io/wifi-connect/raw/master/scripts/raspbian-install.sh -o /boot/PiSetup/raspbian-install.sh
sudo bash /boot/PiSetup/raspbian-install.sh
#sudo bash <(curl -L https://github.com/balena-io/wifi-connect/raw/master/scripts/raspbian-install.sh)
sudo mkdir /home/genmonpi/WiFiConnect
sudo cp /boot/PiSetup/wificonnect.service /lib/systemd/system/wificonnect.service
sudo cp /boot/PiSetup/wificonnect.py /home/genmonpi/WiFiConnect/wificonnect.py
sudo chmod 644 /lib/systemd/system/wificonnect.service
sudo chmod +x /home/genmonpi/WiFiConnect/wificonnect.py
sudo systemctl daemon-reload
sudo systemctl enable wificonnect.service
sudo systemctl start wificonnect.service

#sudo nmcli device set wlan0 autoconnect yes
#sudo nmcli connection modify PintSize_HS connection.autoconnect yes|no
