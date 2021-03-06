# process-monitor
Monitoring cpu and memory usage of a process.

Works in linux and windows.

**Requires:**
<a href="https://pythonhosted.org/psutil/">psutil</a>

**install psutil:**
`pip install psutil`

**How to get pid of running processes:**
**Windows:**
Task manager (ctrl+shif+esc) --> details page pid column

**Linux:**

`pidof <process name>`

i.e.: `pidof cinnamon`

or

`top | grep <process name>`

i.e.: `top | grep cinnamon`

the first column contains the pid

or

`ps a | grep <process name>`

i.e.: `ps a | grep cinnamon`

the first column contains the pid

**usage:**

`python processmonitor.py -p <pid> [-f <frequency>] [-l <length>]`

**alternative:**

`python processmonitor.py --pid <pid> [--frequency <frequency>] [--length <length>]`

**PID(required):** Process id of the process that we want to monitor

**Frequency(optional):** Checks the process cpu and memory usage in every < frequency >th sec. *default: 10*

**Length(optional):** The program adds the measured values to a list in every check. If the length of the list equals length the program creates a log, empty the array and put the avarage value to the array. *default: 6*

Technically the program create a log in every < freqency > * < length > second. If you use the default values the program creates log in every minute (because `frequency = 10` and `length = 6` so check the process in every 10 seconds and creates log after 10 checks)

**example output: **

`python processmonitor.py -p 3539`


```
-------------------------
Process name: cinnamon
-------------------------

-------------------------
Sun May 21 16:37:50 2017
-------------------------
         Memory
-------------------------
minimum usage:   226 MB
maximum usage:   231 MB
avarage usage:   230 MB
-------------------------

-------------------------
Sun May 21 16:37:50 2017
-------------------------
        Total CPU
-------------------------
minimum usage:   0.17 %
maximum usage:   1.75 %
avarage usage:   0.92 %
-------------------------

-------------------------
Sun May 21 16:38:50 2017
-------------------------
         Memory
-------------------------
minimum usage:   226 MB
maximum usage:   231 MB
avarage usage:   227 MB
-------------------------

-------------------------
Sun May 21 16:38:51 2017
-------------------------
        Total CPU
-------------------------
minimum usage:   0.17 %
maximum usage:   1.75 %
avarage usage:   0.57 %
-------------------------

-------------------------
Sun May 21 16:39:50 2017
-------------------------
         Memory
-------------------------
minimum usage:   226 MB
maximum usage:   231 MB
avarage usage:   226 MB
-------------------------

-------------------------
Sun May 21 16:39:51 2017
-------------------------
        Total CPU
-------------------------
minimum usage:   0.12 %
maximum usage:   1.75 %
avarage usage:   0.66 %
-------------------------

-------------------------
Sun May 21 16:40:50 2017
-------------------------
         Memory
-------------------------
minimum usage:   226 MB
maximum usage:   231 MB
avarage usage:   226 MB
-------------------------

-------------------------
Sun May 21 16:40:51 2017
-------------------------
        Total CPU
-------------------------
minimum usage:   0.03 %
maximum usage:   1.75 %
avarage usage:   0.50 %
-------------------------

```
