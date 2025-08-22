# bpm doc

'bpm doc' generate several docs, depending of the plugins installed.

## Generate docs

```bash
bpm doc
```

## md2hlp plugin

All docs/{name}.md will be generated into .hlp (for man orix command) and inserted in "build/usr/share/man/".
md2hlp.cfg into project will be modifyed in order to modify title of .hlp (part Heading1, property : Head)

## generatedoc plugin

Generate docs from source code see [asm.md](https://github.com/orix-software/generatedoc/blob/main/docs/asm.md) and [c.md](https://github.com/orix-software/generatedoc/blob/main/docs/c.md)

## Change docs target folder

use docsfolder param in package section.

Default : docs/

ex:

```bash
[package]
...
docsfolder = "mkdocs/docs/"
...
```

## Folder

Docsfolder is always formatted with version of the program like 

docs/2025.2/


