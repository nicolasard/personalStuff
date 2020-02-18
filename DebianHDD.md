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

Format the volume with ext4
```
root@host01:/home/nardison# /sbin/mkfs.ext4 /dev/mapper/host01--vg-virtualmachines
mke2fs 1.44.5 (15-Dec-2018)
Creating filesystem with 78643200 4k blocks and 19660800 inodes
Filesystem UUID: faac267a-1759-4be6-a345-eb25478f4774
Superblock backups stored on blocks:
        32768, 98304, 163840, 229376, 294912, 819200, 884736, 1605632, 2654208,
        4096000, 7962624, 11239424, 20480000, 23887872, 71663616

Allocating group tables: done
Writing inode tables: done
Creating journal (262144 blocks): done
Writing superblocks and filesystem accounting information: done
```


### Raid

https://wiki.debian.org/SoftwareRAID
