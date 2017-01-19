#!/usr/bin/env python

#cat /sys/class/drm/card0/device/pp_dpm_sclk
#echo manual > /sys/class/drm/card0/device/power_dpm_force_performance_level
#echo 6 > /sys/class/drm/card0/device/pp_dpm_sclk
#cat /sys/class/drm/card0/device/pp_dpm_sclk


import subprocess
import time

def run_command_shell(cmd):
    the_process = subprocess.Popen(['/bin/bash', '-c', cmd])
    the_process.wait()

run_command_shell('cat /sys/class/drm/card0/device/pp_dpm_sclk')
print('Please enter the desired core power state')
core_index = raw_input()

run_command_shell('cat /sys/class/drm/card0/device/pp_dpm_mclk')
print('Please enter the desired memory power state')
mem_index = raw_input()

while True:
    print('')
    run_command_shell('echo manual > /sys/class/drm/card0/device/power_dpm_force_performance_level')
    run_command_shell('echo {} > /sys/class/drm/card0/device/pp_dpm_sclk'.format(core_index))
    run_command_shell('echo {} > /sys/class/drm/card0/device/pp_dpm_mclk'.format(mem_index))
    print('=== Core clocks ===')
    run_command_shell('cat /sys/class/drm/card0/device/pp_dpm_sclk')
    print('=== Memory clocks ===')
    run_command_shell('cat /sys/class/drm/card0/device/pp_dpm_mclk')
    time.sleep(10)

