# bpm package

Build package

"src/include/*.s" will be added into "/usr/include"

"src/include/*.inc" will be added into "/usr/include/asm"

In that case, if a binary calls theses include, "bpm build" will include theses paths automaticly

```bash
bpm package
```