import subprocess
import time

while True:
  subprocess.call('./radeonfreq.sh', shell=True)
  time.sleep(0.5)

