from abc import abstractmethod

import psutil
import time
import threading
import os


class Monitor(object):    
    def __init__(self):
        self.min_usage = 0.0
        self.max_usage = 0.0
        self.avg_usage = 0.0
        self.measured_values = []
        self.process = psutil.Process(self.process_id)
        self.process_name = self.process.name()

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def measure_usage(self):
        pass

    @abstractmethod
    def print_values(self):
        pass

    def get_max_usage(self):
        if max(self.measured_values) > self.max_usage or self.max_usage == 0:
            return max(self.measured_values)
        return self.max_usage

    def get_min_usage(self):
        min_measured_value = min(self.measured_values)
        if min_measured_value < self.min_usage or (self.min_usage == 0.0 and min_measured_value != 0.0):
            return min(self.measured_values)
        return self.min_usage

    def print_process_name(self):
        print("-------------------------")
        print("Process name: {}".format(self.process_name))
        print("-------------------------")

    def print_date(self):
        print("\n-------------------------")
        print("{}".format(time.strftime('%c')))
        print("-------------------------")

    def set_values(self):
        self.avg_usage = (sum(self.measured_values) /
                          len(self.measured_values))
        self.min_usage = self.get_min_usage()
        self.max_usage = self.get_max_usage()

    def length_reached(self):
        self.set_values()
        self.print_values()
        del self.measured_values[:]
        self.measured_values.append(self.avg_usage)


class CpuMonitor(Monitor):
    def __init__(self):
        super(CpuMonitor, self).__init__()

    def start(self):
        threading.Thread(target=self.measure_usage).start()

    def print_values(self):
        self.print_date()
        print("        Total CPU")
        print("-------------------------")
        print("minimum usage:   {0:.2f} %".format(self.min_usage/psutil.cpu_count()))
        print("maximum usage:   {0:.2f} %".format(self.max_usage/psutil.cpu_count()))
        print("avarage usage:   {0:.2f} %".format(self.avg_usage/psutil.cpu_count()))
        print("-------------------------")

    def set_measured_values(self):
        for _ in range(self.length+1):
            cpu_percentage = self.process.cpu_percent(interval=self.frequency)
            self.measured_values.append(cpu_percentage)

    def measure_usage(self):
        try:
            while True:
                self.set_measured_values()
                self.length_reached()
        except psutil.NoSuchProcess:
            print ("Process {} stopped".format(self.process_name))
            os._exit(0)


class MemoryMonitor(Monitor):
    def __init__(self):
        super(MemoryMonitor, self).__init__()

    @staticmethod
    def byte_to_mb(value):
        return value/1000000

    def print_values(self):
        self.print_date()
        print("         Memory")
        print("-------------------------")
        print("minimum usage:   {} MB".format(self.byte_to_mb(self.min_usage)))
        print("maximum usage:   {} MB".format(self.byte_to_mb(self.max_usage)))
        print("avarage usage:   {} MB".format(self.byte_to_mb(self.avg_usage)))
        print("-------------------------")

    def start(self):
        threading.Thread(target=self.measure_usage).start()

    def measure_usage(self):
        try:
            start_time = time.time()
            while True:
                if len(self.measured_values) > self.length:
                    self.length_reached()
                    
                if time.time() - start_time >= self.frequency:
                    self.measured_values.append(
                        self.process.memory_info()[0])
                    start_time = time.time()

                time.sleep(.001)
        except psutil.NoSuchProcess:
            print ("Process {} stopped".format(self.process_name))
            os._exit(0)
