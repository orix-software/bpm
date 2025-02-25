
# Installation Guide for bpmorix

bpm does not install Oricutron and cc65, bit are needed for bpm.

How to install for Linux

```bash
mkdir ~/bin/
curl -o ~/bin/bpm https://raw.githubusercontent.com/orix-software/bpm/refs/heads/main/src/bpm
export PATH=$PATH:~/bin/
chmod +x ~/bin/bpm
curl -o /tmp/bpm.txt https://raw.githubusercontent.com/orix-software/bpm/refs/heads/main/requirements.txt
sudo apt install python3-pip
pip install -r /tmp/bpm.txt
rm -f /tmp/bpm.txt
```
