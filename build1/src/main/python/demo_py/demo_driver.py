#! /usr/bin/python
#
# Title:demo_driver.py
# Description:
# Development Environment:OS X 10.13.3/Python 2.7.7
# Author:G.S. Cole (guycole at gmail dot com)
#
import sys
import syslog
import time
import yaml

from target import Target

class DemoDriver:

    def write_log_info(self, message):
        print message
        syslog.syslog(syslog.LOG_INFO, message)

    def execute(self):
        start_time = time.time()

        self.write_log_info('start demo driver')

        target = Target()
        target.adder(2, 3)

        stop_time = time.time()
        duration = stop_time - start_time

        self.write_log_info('stop demo driver')

        return duration

print 'start'

#
# argv[1] = configuration filename
#
if __name__ == '__main__':
    syslog.openlog(logoption=syslog.LOG_PID, facility=syslog.LOG_LOCAL4)

    if len(sys.argv) > 1:
        yaml_file_name = sys.argv[1]
    else:
        yaml_file_name = 'config.test'

    configuration = yaml.load(file(yaml_file_name))

    driver = DemoDriver()
    duration = driver.execute()

    syslog.closelog()

print 'stop'