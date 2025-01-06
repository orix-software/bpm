# First steps

## First start

bpm needs *'Oricutron'* and *'cc65'* in order to work properly.

Theses binaries must be installed and cc65 (as ca65, ar65, ld65 must be in your PATH).

## Initialize bpm and install plugins

Each day "bpm" will check if a new version is available and will ask if you want to install this version

```bash
~$ bpm
```

it will install all plugins

```bash
~$ bpm plugins
Use 'bpm plugins -h' for 'plugins' help
md2hlp: Build markdown into hlp file (text mode) [Installed]
orixsdk: Useful ca65 macro for Orix and reloc binary (Mandatory for Orix projects)  (Available versions : ['2023.3.0']) [Installed]
asm_bin_tpl: Assembly binary template for Orix  (Available versions : ['2024.4']) [Installed]
asm_rom_tpl: Assembly rom template for Orix  (Available versions : ['2024.4']) [Installed]
github_action: Template for github action  (Available versions : ['2024.4']) [Installed]
generatedoc: Tool to comment source code and generate markdown  (Available versions : ['2025.1']) [Installed]
```

## First project

We create a binary from which will be loaded from /bin orix folder

```bash
~$ mkdir myprgm
~$ bpm new
This project is :
1) A binary program
2) A library
3) A rom
answer ?
```

Press 1

```bash
Init .gitignore
Init bpm.tml
Init src folder
Init src/myprgm.c
Init VERSION file
Add github action main.yml into project: y/N ?
```

Press N

```bash
initialized
```

```bash
~$ cat src/myprgm.c
#include <stdio.h>
int main() {
  printf("Hello word");
  return 0;
}
```

Launch build

```bash
~$ bpm build
Creating build/etc/bpm/myprgm/2025.1
Format 2 overhead:  304 304 1 2424 303
Generate file ...
-Generate file version: 2
-Truncate reloc table from 304 to 303 (-0.33%)
Built : build/bin/myprogram
```
