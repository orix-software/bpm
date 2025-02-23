# bpm config

## bpm config set

## bpm config add

### bpm config add project binary

Add a "curl" binary into bin list to generate :

"bpm config add project binary curl tests/curl.c"

In that case, "bpm run --bin curl" will launch "curl" compiled from tests/curl.c

## Add a pre script before main command is launched

```bash
$ mkdir scripts/
$ echo "netchk" > scripts/network.sub
$ bpm config set project orix_run_pre_script scripts/network.sub
```
