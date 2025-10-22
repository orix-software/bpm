# bpm config

'bpm config' modify behavior of bpm

It can modify main configuration and project configuration.

Main parameters are :

```bash
    oricutron_path                  Set Oricutron path for main (general behavior), value must be path of Oricutron binary with filename binary in the path
    oricutron_replace_autoboot_run  Set False or True. False will not modify /etc/autoboot in Oricutron
    default_rom_oricutron_for_code  Default rom when code type is rom : the .rom will be inserted into this slot
```

Project parameters are :

```bash
    name                            Name of the project
    version                         Version of the project
    codetype                        Code type of the project (lib is a library, bin a command line [lib|bin])
    oricutron_replace_autoboot_run  Set False or True. False will not modify /etc/autoboot in Oricutron when bpm run is executed
    oricutron_path                  Set Oricutron path for current project
    default_rom_oricutron_for_code  Default rom when code type is rom : the .rom will be inserted into this slot
    orix_run_pre_script             Pre submit script : will be added before project command
    md2hlp                          Activate md2hlp : enable set to yer, disabled set to no
```

## bpm config set

"config set" can be used to set any parameter in global configuration (main) or project configuration

### bpm config add project binary : add a source code to build during build stage

For example, we want to add curl.c into build stage with the output name called "curl"

Add a "curl" binary into bin list to generate :

```bash
bpm config add project binary curl tests/curl.c
```

Add args :

```bash
bpm config add project binary curl tests/curl.c "arg1 arg2"
```

In that case, "bpm run --bin curl" will launch "curl" compiled from tests/curl.c

## Add a 'pre' script before main command is launched

```bash
~$ mkdir scripts/
~$ echo "netchk" > scripts/network.sub
~$ bpm config set project orix_run_pre_script scripts/network.sub
```
