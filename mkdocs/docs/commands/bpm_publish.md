# bpm publish - publish package

This command can publish package to repo.orix.oric.org. It requires to get have a key in environnement variable "BPM_PUBLISH_KEY"

In order to have one, post an issue [here](https://github.com/orix-software/bpm/issues).

* For Unix-based systems

printenv | grep BPM

* For Windows

echo %BPM_PUBLISH_KEY%

## bpm publish --official

Publish package into official repo (depending of the version).

## bpm publish --personnal

Publish into personnal repo

## bpm publish --alpha

Publish into alpha repo

