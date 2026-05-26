# MOBILE

## Preparation : 

```bash
sudo apt update
sudo apt install -y git zip unzip openjdk-17-jdk python3-pip autoconf libtool pkg-config zlib1g-dev libncurses5-dev libssl-dev cmake libffi-dev libgstreamer1.0-dev glib-2.0-dev libgstreamer-plugins-base1.0-dev


pip3 install --user buildozer

buildozer init
```
configuration du fichier buildozer§.spec

```
buildozer -v android debug deploy run
```
