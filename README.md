A script that monitors CPU usage, memory usage, disk space, and system uptime, then generates a simple report.
Checks CPU usage (alerts if >80%), checks memory usage (alerts if >85%), checks disk space on all drives (alerts if >90%), shows system uptime, and generates a summary with recommendations

Run it: python vm_health_check.py

To save the report to a file:
python vm_health_check.py > health_report.txt
