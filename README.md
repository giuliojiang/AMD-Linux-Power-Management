# AMD Radeon Linux power management scripts

Tested on Linux Mint 18, 
with 
Sapphire Radeon R9 380X (AMDGPU),
Sapphire Radeon R7 260X (radeon)

## Use cases

* Crashes and freezes can be due to some GPU states being unstable under certain workloads. This might be especially evident when using desktop environments that cause a moderate GPU load for 3D effects, or modern browsers that use GPU acceleration for some kinds of content.

* You want to force the GPU into low power or high performance state

## Compatibility

This should work on recent systems with Radeon DPM support. Please do some more research to ensure that your system is supported.

An easy way to check is to run

```
cat /sys/class/drm/card0/device/power_dpm_force_performance_level
```
which will print out `high` `low` or `auto`. If the file does not exist, dpm is not enabled.

## The scripts

The scripts starting with `agpu` will set and read states for AMDGPU drivers, while those starting with `radeon` are for the radeon drivers.

`agpufreq` and `radeonfreq` will periodically print core and memory clocks.

`agpulow` and `agpuhigh` will set lowest and highest profiles.

`radeonset low` and `radeonset high` will do the same for radeon driver based cards.
