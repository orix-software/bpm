# bpm doc

bpm doc generate several docs, depending of the plugins installed.

## Generate docs

## md2hlp plugin

bpm doc

All docs/{name}.md will be generated into .hlp (for man orix command) and inserted in "build/usr/share/man/".
md2hlp.cfg into project will be modifyed in order to modify title of .hlp (part Heading1, property : Head)

## generatedoc pluginn

Generate docs from source code see [asm.md](https://github.com/orix-software/generatedoc/blob/main/docs/asm.md) and [c.md](https://github.com/orix-software/generatedoc/blob/main/docs/c.md)

