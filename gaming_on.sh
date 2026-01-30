#!/system/bin/sh

# Governor CPU
for cpu in /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor; do
    echo schedutil > $cpu
done

# Batasi frekuensi (AMAN – Helio G95)
echo 2000000 > /sys/devices/system/cpu/cpu0/cpufreq/scaling_max_freq
echo 2200000 > /sys/devices/system/cpu/cpu4/cpufreq/scaling_max_freq

# Responsif tapi hemat
for cpu in /sys/devices/system/cpu/cpu*/cpufreq/schedutil/up_rate_limit_us; do
    echo 500 > $cpu
done

# I/O Scheduler
for blk in /sys/block/*/queue/scheduler; do
    echo noop > $blk
done
