#!/usr/bin/env python3
import os
import sys

def check_reboot():
    """Returns true if the computer has a pending reboot"""
    return os.path.exist("/run/reboot-required")


def check_disk_full(disk, min_gb, min_percent):
    """Returns Truw if there isn't enough disk space, False otherwise."""
    # Calculate the percent of free space
    percent_free = 100* du.free /du.total
    # Calculate how many fre gigabytes
    gigabytes_free = du.free / 2**30
    if percent _free < min_percent or gigabytes_free < min_gb:
        return True
    return False
def check_root_full():
    """Returs True if the root partition is full"""
    return check_disk_full(disk="/", min_gb=2,min_percent=10")

def main()
  if check_reboot():
      print("Pending Reboot.")
      sys.exit(1)
  if check_root_full():
     print("Root partition Full.")
     sys.exit(1)
 print("Everything ok.")
 sys.exit(0)
main()
