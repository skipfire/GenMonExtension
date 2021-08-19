echo "this must be run when not logged in as pi"
echo "must be in boot to console without autologin for this to work"
usermod -l genmonpi -d /home/genmonpi -m pi
groupmod --new-name genmonpi pi
ls -al /home/
echo "If the above has a line with genmonpi for both group and owner then it was successful"
echo "Rebooting..."
echo "Login with user genmonpi and run Step2-SetupGenMon.sh from home directory."
sudo reboot
