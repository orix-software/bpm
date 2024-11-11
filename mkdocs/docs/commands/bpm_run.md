# bpm run

If AUTOBOOT is already in etc/autoboot. bpm saves it and restore it.

If there is no autoboot before "bpm run starts", sur autoboot from bpm will be removed.

For autoexecute AUTOBOOT, 'submit' binary must bin in sdcard/bin/

Orix kernel must be greater than 2023.3

Specify command to launch : bpm run --bin hello

To specify args :

bpm run --bin "hello -y"

