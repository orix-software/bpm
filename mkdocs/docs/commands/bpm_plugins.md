# bpm plugins - Manage plugins

A plugin is a tool in order to manage some part of the development. Each day, bpm will try to update plugins, and will ask if plugin must be installed

## bpm plugins

Usage : bpm plugins

## bpm plugins install

Usage : bpm plugins install [plugin_name] [--replace-for-new-project]

--replace-for-new-project option will set this plugin version for next project but it does not update it for current project (it needs to be changed in bpm.tml of the project)

## bpm plugins update

Update all plugins :

```bash
bpm plugins update
```

## bpm plugins -h

Usage : bpm plugins install -h


## Displays installed plugins

```bash
~$ bpm plugins
Use 'bpm plugins -h' for 'plugins' help
md2hlp: Build markdown into hlp file (text mode) [Installed]
orixsdk: Useful ca65 macro for Orix and reloc binary (Mandatory for Orix projects)  (Available versions : ['2023.3.0']) [Installed]
asm_bin_tpl: Assembly binary template for Orix  (Available versions : ['alpha']) [Installed]
asm_rom_tpl: Assembly rom template for Orix  (Available versions : ['2024.4', 'alpha']) [Installed]
github_action: Template for github action  (Available versions : ['2024.4']) [Installed]
generatedoc: Tool to comment source code and generate markdown  (Available versions : ['2025.1', '2024.4']) [Installed]
```
