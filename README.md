# retronas_check_systems
support script for retronas_systems.yml

will check supported systems against retronas data when `--system` is passed

```
./check_systems.py --system mister
```

output example

```
[      main] INFO Check Systems 0.01            
[    mister] INFO Initiated mister module       
[  retronas] INFO Initiated retronas module     
[       url] INFO Processing direct download mode
[       url] INFO Getting data from https://raw.githubusercontent.com/danmons/retronas/main/ansible/retronas_systems.yml
[       url] INFO Processing github tree download mode
[       url] INFO Getting data from https://api.github.com/repos/MiSTer-devel/Distribution_MiSTer/git/trees/main?recursive=1
[       url] INFO Processing github tree download mode
[       url] INFO Getting data from https://api.github.com/repos/MiSTer-DB9/Distribution_MiSTer/git/trees/main?recursive=1
[     tools] INFO Running left (mister) > right (retronas) compare
[     tools] INFO Checking for mister systems not in retronas
[     tools] INFO No missing mister systems found
[     tools] INFO Running right (retronas) > left (mister) compare
[     tools] INFO Checking for retronas systems not in mister
                  [M] Apple-I
                  [M] ATARI2600
                  [M] Zet98
                  [M] TeleStrat
                  [M] Arduboy
                  [M] Saturn
                  [M] zx48
```


where the `[M]` in the output is the first letter of the system the item is missing from