A script that monitors CPU usage, memory usage, disk space, and system uptime, then generates a simple report.
Checks CPU usage (alerts if >80%), checks memory usage (alerts if >85%), checks disk space on all drives (alerts if >90%), shows system uptime, and generates a summary with recommendations

Run it: python vm_health_check.py

To save the report to a file:
python vm_health_check.py > health_report.txt

See example with UCF's Linux Server: 

============================================================
VM HEALTH CHECK REPORT
============================================================
Hostname: net1547.net.ucf.edu
OS: Linux 6.8.0-88-generic
Scan Time: 2025-12-29 19:47:35
============================================================

[CPU USAGE]
  Current Usage: 0.0%
  CPU Cores: 8
  ✓ Status: Normal

[MEMORY USAGE]
  Total: 31.34 GB
  Used: 4.58 GB
  Available: 26.28 GB
  Usage Percentage: 16.1%
  ✓ Status: Normal

[DISK USAGE]
  Drive: /dev/sda1
    Mount Point: /
    Total: 242.82 GB
    Used: 139.42 GB
    Free: 91.04 GB
    Usage: 60.5%
    ✓ Status: Normal

  Drive: /dev/sdb1
    Mount Point: /home/net
    Total: 930.54 GB
    Used: 186.59 GB
    Free: 743.95 GB
    Usage: 20.1%
    ✓ Status: Normal

[SYSTEM UPTIME]
  Boot Time: 2025-12-02 09:17:59
  Uptime: 27 days, 10 hours, 29 minutes
  ✓ Status: System is running

============================================================
SUMMARY
============================================================
✓ All systems normal - No issues detected
============================================================

Would you like to save this report? (y/n): y
Report saved as: health_check_20251229_194754.txt
(Note: To actually save, redirect output: python script.py > report.txt)
