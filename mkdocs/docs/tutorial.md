# Tutorial

## Binary command (C language)

```bash
$ mkdir pong
$ cd pong
$ bpm new
This project is :
1) A binary program
2) A library
3) A rom
answer ? 1
Init bpm.tml
Init src folder
Init src/tmp.c
Init VERSION file
Add github action main.yml into project: y/N ?N
initialized
```

Set oricutron path (global)

```bash
~$ bpm config oricutron_path /mnt/c/Users/myfolder/OneDrive/oric/oricutron_plugins/oricutron
```

```bash
~$ bpm run
```

![alt text](images/helloworld.png)

## Library (Assembly language only)

```bash
~$ mkdir gizmo && cd gizmo
~$ bpm new
This project is :
1) A binary program
2) A library
3) A rom
answer ?2
Init .gitignore
Init bpm.tml
Init src folder
Init VERSION file
Add github action main.yml into project: y/N ?N
initialized
~$ tree
.
├── bpm.tml
├── docs
├── src
│   └── dynamic_lib
│       └── gizmo.s
└── VERSION

~$ bpm build
Creating build/etc/bpm/gizmo/2025.1
Generate gizmo.lib
Building gizmo.llo
No build done

~$ tree
.
├── bpm.tml
├── bpmtmp
│   └── gizmo.o
├── build
│   ├── etc
│   │   └── bpm
│   │       └── gizmo
│   │           └── 2025.1
│   │               └── bpm.tml
│   └── usr
│       ├── lib
│       │   └── gizmo
│       │       └── 2025.1
│       │           └── llo
│       │               └── gizmo.lib
│       └── share
│           └── gizmo
│               └── 2025.1
├── docs
├── src
│   └── dynamic_lib
│       ├── gizmo.s
│       ├── gizmo_so.o
│       └── gizmo_so.s
└── VERSION

```

## Publish

If this command, return an empty line : 


```bash
set | grep BPM
BPM_PUBLISH_KEY=yourKey
```

Set a key for publishing


```bash
~$ vi ~/.bashrc
```

add :

export BPM_PUBLISH_KEY=yourKey

```bash
bpm publish
```