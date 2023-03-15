# Poneglyph

In One Piece, Poneglyphs are ancient stones with cryptic inscriptions revealing the location of an ultimate treasure. In real world is a microservice that helps your project to manage authentication and authorization in a easy way.

## How to run it on your machine

First, you will need to clone the repository.

```
$ git clone https://github.com/raissonsouto/Poneglyph.git && cd Poneglyph
```
After downloading and navigate to the directory, build the image using:
```
$ docker build -t Poneglyph .
```
---
Or get the image at dockerhub and run it.

```
$ docker pull raissonsouto/Poneglyph:<version>
```

**Option 1:** Run as docker-compose.
```
version: 3.6

services:
  bifrost:
    image: raissonsouto/Poneglyph:<version>
    port: 5757:5757
```

**Option 2:** run in command line:
```
$ docker run -p 5757:5757 --name Poneglyph raissonsouto/Poneglyph<version>
```

## Contribute
- Report bugs
- Create test cases
- Help us to write the documentation
- Translate already created documentation
