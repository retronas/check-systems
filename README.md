# retronas_check_systems
support script for retronas_systems.yml

will check supported systems against retronas data when `--system` is passed

## running

```
./check_systems.py --system mister
```

### output example

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

## validate retronas yaml
supports filtering on a key
```
./check_systems.py --system mister --validate-only
```

### output example
```
RETRONAS SYSTEMS output, data is good, no data is :'(
----------------------------------------------------------------------------------------------------------------------------------
retronas_system                | romdir                                   | key:mister                    
----------------------------------------------------------------------------------------------------------------------------------
system_acorn                   | acorn/archimedes                         | ARCHIE                        
system_acorn                   | acorn/atom                               | AcornAtom                     
system_acorn                   | acorn/bbcmicro                           | BBCMicro                      
system_acorn                   | acorn/electron                           | AcornElectron                 
system_amstrad                 | amstrad/cpc                              | Amstrad                       
system_amstrad                 | amstrad/pcw                              | Amstrad PCW                   
system_amstrad                 | amstrad/gx4000                           |                               
system_antonic                 | antonic/galaksija                        | Galaksija                     
system_apf                     | apf/mp1000                               |                               
system_apple                   | apple/applei                             | Apple-I                       
system_apple                   | apple/appleii                            | Apple-II                      
system_apple                   | apple/appleiigs                          |                               
system_apple                   | apple/appleiii                           |                               
system_apple                   | apple/macintosh                          | MACPLUS                       
system_arcade                  | mame/hbmame                              | hbmame                        
system_arcade                  | mame/mame                                | mame                          

```

## modules
1. new systems are added under systems dir
1. import them into `check_systems.py`
1. whitelist them in `VALID_SYSTEMS`