# DontpadWard

It's just a little code I did to monitor and register all changes made to a given _dontpad.com/_ URL.

*I wrote it on Linux, but _maybe_ it also runs on Windows, if that's not the case feel free to read and modify the code :)

### Thanks
  _First of all thanks for @VGasparini and @lucianowayand, two more experienced programmers who did some codes that were the bases for this program_ <3

## Getting Started  
### Dependencies

DontpadWard requires the libraries:
```
requests
bs4
os
time
```


### How to use it

Execute the ```place-a-ward.py``` script:
```
Python3 place-a-ward.py
```
Then just type the _dontpad.com/_ URL you wish to ward and press _Enter_.


### How the program works

In resume the script ```place-a-ward.py``` creates a folder and place a copy of ```dontpadWard.py``` with a temporary text file containing the URL you entered. Then the script set ```dontpadWard.py``` to run on the background of the system with _**nohup_.

While ```dontpadWard.py``` is running on the background, it will write the last time a access on the _dontpad.com/_ URL as performed and if a change was registered it will create a new file named " \[URL]\_\[TIME-DATE].txt" where "URL" is the _dontpad.com/_ you warded and "TIME-DATE" is the time and date of when a change on the page was registered.

  **sorry, but for now, the only way to kill the program is through the system monitor, I might change it later.
  
### Disclaimers

English is not my native language, sorry for any misspelling.

I will refactor and properly comment the codes in the future ;) _Even though probably no one will ever runs this other than me..._
