
# Over The Edge Radio

((very much a work in progress))

An endless stream of Over The Edge episodes, from
the [archive.org collection](https://archive.org/details/ote?tab=collection).

This is very much based on the
[noise-arch radio](https://github.com/breedx2/noise-arch-radio).

# About

tbd

# Prerequisites

We need to first fetch all the metadata for this collection.
It is basically assumed that this set is static once 
we are running...but a person could fetch it again later 
I guess.

```bash
$ virtualenv env
$ source env/bin/activate
$ pip install internetarchive
$ python3 fetch_meta.py
```

It takes a while to download all the metadata.

# Build the container images

There are two containers:

* icecast - responsible for streaming to clients
* ezstream - responsible for sending audio to icecast

The `ezstream` container has a custom playlist script that
will download the next item before it is needed, and then 
delete old stuff more than 8 hours old.