```bash
mkdir ~/bin/
curl -o ~/bin/bpm https://raw.githubusercontent.com/orix-software/bpm/refs/heads/main/src/bpm
export PATH=$PATH:~/bin/
chmod +x ~/bin/bpm
curl -o /tmp/bpm.txt https://raw.githubusercontent.com/orix-software/bpm/refs/heads/main/requirements.txt
sudo apt install python3-pip
pip install -r /tmp/bpm.txt
```

