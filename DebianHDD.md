### Disk volumes LVM

https://wiki.debian.org/LVM

####To create a volume 

```
root@host01:/home/nardison# /sbin/vgs
  VG        #PV #LV #SN Attr   VSize    VFree
  host01-vg   1   6   0 wz--n- <931.27g 545.01g
root@host01:/home/nardison# /sbin/lvcreate -L 300G -n virtualmachines host01-vg
  Logical volume "virtualmachines" created.
root@host01:/home/nardison# lsblk
NAME                           MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT
sda                              8:0    0 931.5G  0 disk
├─sda1                           8:1    0   243M  0 part /boot
├─sda2                           8:2    0     1K  0 part
└─sda5                           8:5    0 931.3G  0 part
  ├─host01--vg-root            254:0    0  23.3G  0 lvm  /
  ├─host01--vg-swap_1          254:1    0   7.9G  0 lvm  [SWAP]
  ├─host01--vg-var             254:2    0   9.3G  0 lvm  /var
  ├─host01--vg-tmp             254:3    0   1.9G  0 lvm  /tmp
  ├─host01--vg-home            254:4    0 143.9G  0 lvm  /home
  ├─host01--vg-opt             254:5    0   200G  0 lvm
  └─host01--vg-virtualmachines 254:6    0   300G  0 lvm
sdb                              8:16   0 931.5G  0 disk

```


### Raid

https://wiki.debian.org/SoftwareRAID
