bash <(curl -L https://github.com/balena-io/wifi-connect/raw/master/scripts/raspbian-install.sh)
copy /home/pi/WiFiConnect/wificonnect.service /lib/systemd/system/wificonnect.service
sudo chmod 644 /lib/systemd/system/WiFiConnect/wificonnect.service
chmod +x /home/pi/WiFiConnect/wificonnect.py
sudo systemctl daemon-reload
sudo systemctl enable wificonnect.service
sudo systemctl start wificonnect.service
