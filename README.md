# My system
![system.svg](./img/system.svg)

Commands:

```
# For clone with submodules
git clone --recurse-submodules git@github.com:VolokzhaninVadim/server

# Add submodule
git submodule add git@<repo>

# Update submodules
git pull --recurse-submodules
```
# Backup
For backup use [backup](./backup)<br>
For `part` use (example):
```bash
cat /mnt/backup/backup/backup/2023-08-12_17_51_54_dns_.zst.gpg.part_* > /mnt/backup/backup/backup/2023-08-12_17_51_54_dns_.zst.gpg
```