# These and other macros are documented in dhd/droid-hal-device.inc
%define device d855
%define vendor lge
%define vendor_pretty LG
%define device_pretty G3 d855
%define installable_zip 1
%define __provides_exclude_from ^/system/.*$
%define __requires_exclude ^/system/bin/.*$
%define __find_provides %{nil}
%define __find_requires %{nil}
%include rpm/dhd/droid-hal-device.inc
