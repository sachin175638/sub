#!/bin/bash
apt-get update
apt-get upgrade -y
apt-get install figlet -y
apt-get install python2 -y
cd $HOME/sub
chmod +x main.py
chmod +x dss.py
chmod +x dessign.py
chmod +x steel.py
chmod +x design2.py
chmod +x zig.py
rm -rf /data/data/com.termux/files/usr/bin/dss
cd $HOME
rm -rf dss.sh
touch dss.sh
chmod +x dss.sh
echo "#!/bin/bash" >> dss.sh
echo "cd $HOME/sub " >> dss.sh
echo "python2 steel.py" >> dss.sh
ln -s $HOME/dss.sh /data/data/com.termux/files/usr/bin/dss
echo
echo "execute ----dss----"
