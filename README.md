# Bifrost

In Norse mythology, Bifrost, is a burning rainbow bridge that reaches
between Midgard (Earth) and Asgard, the realm of the gods. In real
world Bifrost is a microservice that helps your project to manage
authentication and authorization in a easy way.

## How to run it on your machine

First, you will need to ...

```
$ git clone
```
```
$ cd bifrost
```
```
$ docker build -t bifrost .
```
Or get the image at dockerhub and run it:

```
$ docker pull raissonsouto/bifrost:<version>
```

1. Run as dockerfile:
```
version: 3.6

services:
  bifrost:
    image: raissonsouto/bifrost:<version>
    port: 5757:5757
```

2. run in command line:
```
$ docker run -p 5757:5757 --name bifrost raissonsouto/bifrost<version>
```

## Contribute
- Report bugs
- Create test cases
- Help us writing the documentation
- Translate already created documentation
