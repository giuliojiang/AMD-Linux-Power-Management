cat /sys/class/drm/card0/device/pp_dpm_sclk
echo manual > /sys/class/drm/card0/device/power_dpm_force_performance_level
echo 6 > /sys/class/drm/card0/device/pp_dpm_sclk
cat /sys/class/drm/card0/device/pp_dpm_sclk
