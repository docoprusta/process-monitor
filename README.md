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
Sun May 21 16:24:34 2017
-------------------------
         Memory
-------------------------
minimum usage:   227 MB
maximum usage:   227 MB
avarage usage:   227 MB
-------------------------

-------------------------
Sun May 21 16:24:34 2017
-------------------------
        Total CPU
-------------------------
minimum usage:   0.10 %
maximum usage:   0.55 %
avarage usage:   0.32 %
-------------------------

-------------------------
Sun May 21 16:25:24 2017
-------------------------
         Memory
-------------------------
minimum usage:   227 MB
maximum usage:   227 MB
avarage usage:   227 MB
-------------------------

-------------------------
Sun May 21 16:25:34 2017
-------------------------
        Total CPU
-------------------------
minimum usage:   0.10 %
maximum usage:   2.17 %
avarage usage:   1.16 %
-------------------------

-------------------------
Sun May 21 16:26:14 2017
-------------------------
         Memory
-------------------------
minimum usage:   227 MB
maximum usage:   227 MB
avarage usage:   227 MB
-------------------------

-------------------------
Sun May 21 16:26:34 2017
-------------------------
        Total CPU
-------------------------
minimum usage:   0.10 %
maximum usage:   2.17 %
avarage usage:   0.91 %
-------------------------

-------------------------
Sun May 21 16:27:04 2017
-------------------------
         Memory
-------------------------
minimum usage:   227 MB
maximum usage:   228 MB
avarage usage:   227 MB
-------------------------

-------------------------
Sun May 21 16:27:34 2017
-------------------------
        Total CPU
-------------------------
minimum usage:   0.10 %
maximum usage:   2.25 %
avarage usage:   1.17 %
-------------------------

-------------------------
Sun May 21 16:27:54 2017
-------------------------
         Memory
-------------------------
minimum usage:   227 MB
maximum usage:   230 MB
avarage usage:   230 MB
-------------------------

-------------------------
Sun May 21 16:28:34 2017
-------------------------
        Total CPU
-------------------------
minimum usage:   0.10 %
maximum usage:   2.25 %
avarage usage:   0.92 %
-------------------------

-------------------------
Sun May 21 16:28:44 2017
-------------------------
         Memory
-------------------------
minimum usage:   227 MB
maximum usage:   230 MB
avarage usage:   230 MB
-------------------------

-------------------------
Sun May 21 16:29:34 2017
-------------------------
         Memory
-------------------------
minimum usage:   227 MB
maximum usage:   230 MB
avarage usage:   230 MB
-------------------------

-------------------------
Sun May 21 16:29:34 2017
-------------------------
        Total CPU
-------------------------
minimum usage:   0.10 %
maximum usage:   2.25 %
avarage usage:   1.05 %
-------------------------

```
