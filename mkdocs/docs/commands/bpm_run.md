# bpm run

Build an run program.

The Oricutron path must be set in main config file or local config file (manifest).

add a oricutron path for main config :

```bash
bpm config set main oricutron_path /mnt/c/Users/mypath/oric/oricutron_plugins/oricutron
```

for current manifest :

```bash
bpm config set project oricutron_path /mnt/c/Users/mypath/oric/oricutron_plugins/oricutron
```

## Behavior for 'bpm run'

oricutron_path is missing, it will read oricutron_path from main config.

## Behavior in oricutron sdcard/ folder

If AUTOBOOT is already in etc/autoboot. bpm saves it and restore it.

If there is no autoboot before "bpm run starts", sur autoboot from bpm will be removed.

For autoexecute AUTOBOOT, 'submit' binary must bin in sdcard/bin/

Orix kernel must be greater than 2023.3

Specify command to launch : bpm run --bin hello

To specify args :

bpm run --bin "hello -y"

## Specify extra args

bpm run -- arg1 arg2

## Launch a command before the project program (only for bin program)

```bash
$ mkdir scripts/
$ echo "netchk" > scripts/network.sub
$ bpm config set project orix_run_pre_script scripts/network.sub
$ bpm run
```

It will start scripts/network.sub and the main project binary
