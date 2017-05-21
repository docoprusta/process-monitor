import argparse
import psutil
import time
import os

from app.monitor import Monitor
from app.monitor import CpuMonitor
from app.monitor import MemoryMonitor


def add_cli_args():
    parser = argparse.ArgumentParser(description=None)
    parser.add_argument('-p', '--pid', type=int, required=True,
                        help="Process id of the process")
    parser.add_argument('-f', '--frequency', type=int,
                        help="Measure frequency", default=10)
    parser.add_argument('-l', '--length', type=int,
                        help="When the length of the array reach this number "\
                                "create a log and empty the array", default=6)

    return parser


def get_cli_args():
    parser = add_cli_args()
    args = parser.parse_args()
    return args.pid, args.frequency, args.length


def start_monitor():
    cpu_monitor.start()
    memory_monitor.start()


if __name__ == '__main__':
    try:
        pid, frequency, length = get_cli_args()

        Monitor.process_id = pid
        Monitor.frequency = frequency
        Monitor.length = length

        cpu_monitor = CpuMonitor()
        memory_monitor = MemoryMonitor()

        cpu_monitor.print_process_name()

        start_monitor()

        while True:
            time.sleep(.001)
    except psutil.NoSuchProcess:
        print("There is no process with {} pid".format(pid))
    except KeyboardInterrupt:
        os._exit(0)
        print('KeyboardInterrupt')
    except Exception as e:
        print (e.message)
