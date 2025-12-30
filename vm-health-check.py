#!/usr/bin/env python3
"""
VM Health Check Script
Monitors system health metrics and generates alerts
Author: Evan Jania
Date: 2025
"""

import psutil
import datetime
import platform

# Configuration - Set your threshold values here
THRESHOLDS = {
    'cpu_percent': 80,      # Alert if CPU usage exceeds 80%
    'memory_percent': 85,   # Alert if memory usage exceeds 85%
    'disk_percent': 90      # Alert if disk usage exceeds 90%
}

def get_system_info():
    """Get basic system information"""
    print("=" * 60)
    print("VM HEALTH CHECK REPORT")
    print("=" * 60)
    print(f"Hostname: {platform.node()}")
    print(f"OS: {platform.system()} {platform.release()}")
    print(f"Scan Time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)
    print()

def check_cpu():
    """Check CPU usage"""
    cpu_percent = psutil.cpu_percent(interval=1)
    cpu_count = psutil.cpu_count()
    
    print(f"[CPU USAGE]")
    print(f"  Current Usage: {cpu_percent}%")
    print(f"  CPU Cores: {cpu_count}")
    
    if cpu_percent > THRESHOLDS['cpu_percent']:
        print(f"  ⚠️  ALERT: CPU usage is HIGH (>{THRESHOLDS['cpu_percent']}%)")
        return False
    else:
        print(f"  ✓ Status: Normal")
    print()
    return True

def check_memory():
    """Check memory usage"""
    mem = psutil.virtual_memory()
    
    print(f"[MEMORY USAGE]")
    print(f"  Total: {mem.total / (1024**3):.2f} GB")
    print(f"  Used: {mem.used / (1024**3):.2f} GB")
    print(f"  Available: {mem.available / (1024**3):.2f} GB")
    print(f"  Usage Percentage: {mem.percent}%")
    
    if mem.percent > THRESHOLDS['memory_percent']:
        print(f"  ⚠️  ALERT: Memory usage is HIGH (>{THRESHOLDS['memory_percent']}%)")
        return False
    else:
        print(f"  ✓ Status: Normal")
    print()
    return True

def check_disk():
    """Check disk usage for all partitions"""
    print(f"[DISK USAGE]")
    partitions = psutil.disk_partitions()
    all_normal = True
    
    for partition in partitions:
        try:
            usage = psutil.disk_usage(partition.mountpoint)
            print(f"  Drive: {partition.device}")
            print(f"    Mount Point: {partition.mountpoint}")
            print(f"    Total: {usage.total / (1024**3):.2f} GB")
            print(f"    Used: {usage.used / (1024**3):.2f} GB")
            print(f"    Free: {usage.free / (1024**3):.2f} GB")
            print(f"    Usage: {usage.percent}%")
            
            if usage.percent > THRESHOLDS['disk_percent']:
                print(f"    ⚠️  ALERT: Disk usage is HIGH (>{THRESHOLDS['disk_percent']}%)")
                all_normal = False
            else:
                print(f"    ✓ Status: Normal")
            print()
        except PermissionError:
            # Skip partitions we can't access
            continue
    
    return all_normal

def check_uptime():
    """Check system uptime"""
    boot_time = datetime.datetime.fromtimestamp(psutil.boot_time())
    uptime = datetime.datetime.now() - boot_time
    
    days = uptime.days
    hours, remainder = divmod(uptime.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    print(f"[SYSTEM UPTIME]")
    print(f"  Boot Time: {boot_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"  Uptime: {days} days, {hours} hours, {minutes} minutes")
    print(f"  ✓ Status: System is running")
    print()

def generate_summary(cpu_ok, mem_ok, disk_ok):
    """Generate summary report"""
    print("=" * 60)
    print("SUMMARY")
    print("=" * 60)
    
    issues = []
    if not cpu_ok:
        issues.append("High CPU usage detected")
    if not mem_ok:
        issues.append("High memory usage detected")
    if not disk_ok:
        issues.append("High disk usage detected")
    
    if issues:
        print("⚠️  ISSUES DETECTED:")
        for issue in issues:
            print(f"  - {issue}")
        print("\nRecommendation: Investigate resource usage and consider cleanup/optimization")
    else:
        print("✓ All systems normal - No issues detected")
    
    print("=" * 60)

def save_report():
    """Ask user if they want to save the report"""
    print("\nWould you like to save this report? (y/n): ", end="")
    choice = input().strip().lower()
    
    if choice == 'y':
        filename = f"health_check_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        print(f"Report saved as: {filename}")
        print("(Note: To actually save, redirect output: python script.py > report.txt)")

def main():
    """Main function to run all health checks"""
    try:
        get_system_info()
        
        cpu_ok = check_cpu()
        mem_ok = check_memory()
        disk_ok = check_disk()
        check_uptime()
        
        generate_summary(cpu_ok, mem_ok, disk_ok)
        save_report()
        
    except KeyboardInterrupt:
        print("\n\nHealth check interrupted by user.")
    except Exception as e:
        print(f"\n❌ Error during health check: {e}")

if __name__ == "__main__":
    main()
