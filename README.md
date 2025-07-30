# Build and package manager for Orix

## First install

```bash
mkdir ~/bin/
curl -o ~/bin/bpm https://raw.githubusercontent.com/orix-software/bpm/refs/heads/main/src/bpm
export PATH=$PATH:~/bin/
chmod +x ~/bin/bpm
curl -o /tmp/bpm.txt https://raw.githubusercontent.com/orix-software/bpm/refs/heads/main/requirements.txt
sudo apt install python3-pip
pip install -r /tmp/bpm.txt
```


pip install -r requirements.txt

## First launch

bpm plugins

bpm plugins install md2hlp

bpm plugins install orixsdk

bpm plugins install asm_bin_tpl

bpm plugins

Create an empty folder with the name of the program ex : "hello"

In this folder : 

bpm init

Ensuite, créer un folder avec le nom du programme à coder. ex : "ftp"

Dans ce folder "ftp", lancer "bpm init"

Cela va créer plusieurs fichiers avec un src/ftp.c

En faisant un "bpm build", cela va builder ftp.c. Si on renomme ftp.c en ftp.s, cela buildera avec ca65.

Cela ne gère pas encore les links.

Cela gère le build de lib, mais il faut changer dans le fichier .tml le codetype à "lib"

Le "bpm run" lance oricutron si son chemin est correctement spécifié en faisant : "bpm config set oricutron mon_path"