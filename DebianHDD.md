### Disk volumes LVM

https://wiki.debian.org/LVM

### How to create a volume and mount it

#### To create a volume 

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

#### Format the volume with ext4
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

#### Mounting the volume
```
root@host01:/opt# echo "/dev/mapper/host01--vg-virtualmachines /opt/virtualmachines            ext4    defaults        0       0" >> /etc/fstab
root@host01:/opt# mount /opt/virtualmachines
```

### How to expand a volume

#### Check disks and file system
Let's say in the following example that we want to add 2Gb from sdb to /home --host01--vg-home file system
```
nardison@host01:/sbin$ lsblk
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
  └─host01--vg-virtualmachines 254:6    0   300G  0 lvm  /opt/virtualmachines
sdb                              8:16   0 931.5G  0 disk
nardison@host01:/sbin$ df -h
Filesystem                              Size  Used Avail Use% Mounted on
udev                                    3.9G     0  3.9G   0% /dev
tmpfs                                   790M   50M  740M   7% /run
/dev/mapper/host01--vg-root              23G  4.4G   18G  20% /
tmpfs                                   3.9G  9.0M  3.9G   1% /dev/shm
tmpfs                                   5.0M  8.0K  5.0M   1% /run/lock
tmpfs                                   3.9G     0  3.9G   0% /sys/fs/cgroup
/dev/sda1                               236M   58M  166M  26% /boot
/dev/mapper/host01--vg-var              9.2G  1.2G  7.5G  14% /var
/dev/mapper/host01--vg-tmp              1.8G  6.3M  1.7G   1% /tmp
/dev/mapper/host01--vg-home             141G  115G   19G  87% /home
tmpfs                                   790M  7.7M  782M   1% /run/user/1000
/dev/mapper/host01--vg-virtualmachines  295G  120G  160G  43% /opt/virtualmachines
```
#### Create a partition table in the new disk 

```
root@host01:/sbin# ./fdisk /dev/sdb

Welcome to fdisk (util-linux 2.33.1).
Changes will remain in memory only, until you decide to write them.
Be careful before using the write command.

Device does not contain a recognized partition table.
Created a new DOS disklabel with disk identifier 0xc5560150.

Command (m for help): n
Partition type
   p   primary (0 primary, 0 extended, 4 free)
   e   extended (container for logical partitions)
Select (default p): p
Partition number (1-4, default 1): 1
First sector (2048-1953525167, default 2048):
Last sector, +/-sectors or +/-size{K,M,G,T,P} (2048-1953525167, default 1953525167):

Created a new partition 1 of type 'Linux' and of size 931.5 GiB.

Command (m for help): t
Selected partition 1
Hex code (type L to list all codes): 8e
Changed type of partition 'Linux' to 'Linux LVM'.

Command (m for help): w
The partition table has been altered.
Calling ioctl() to re-read partition table.
Syncing disks.
```

```
root@host01:/sbin# lsblk
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
  └─host01--vg-virtualmachines 254:6    0   300G  0 lvm  /opt/virtualmachines
sdb                              8:16   0 931.5G  0 disk
└─sdb1                           8:17   0 931.5G  0 part
```

#### Create a physical volume
```
root@host01:/sbin# ./pvcreate /dev/sdb1
  Physical volume "/dev/sdb1" successfully created.
```

#### Extend the volume group
```
root@host01:/sbin# ./vgextend host01-vg /dev/sdb1
  Volume group "host01-vg" successfully extended
```
#### Extend the logical volume
```
root@host01:/sbin# ./lvresize -l +20%free /dev/host01-vg/home
  Size of logical volume host01-vg/home changed from 143.89 GiB (36836 extents) to <379.20 GiB (97074 extents).
  Logical volume host01-vg/home successfully resized.
root@host01:/sbin# ./resize2fs /dev/host01-vg/home
resize2fs 1.44.5 (15-Dec-2018)
Filesystem at /dev/host01-vg/home is mounted on /home; on-line resizing required
old_desc_blocks = 18, new_desc_blocks = 48
The filesystem on /dev/host01-vg/home is now 99403776 (4k) blocks long.
```

#### Check new size of the filesystem
```
root@host01:/sbin# df -h
Filesystem                              Size  Used Avail Use% Mounted on
udev                                    3.9G     0  3.9G   0% /dev
tmpfs                                   790M   50M  740M   7% /run
/dev/mapper/host01--vg-root              23G  4.4G   18G  20% /
tmpfs                                   3.9G  9.0M  3.9G   1% /dev/shm
tmpfs                                   5.0M  8.0K  5.0M   1% /run/lock
tmpfs                                   3.9G     0  3.9G   0% /sys/fs/cgroup
/dev/sda1                               236M   58M  166M  26% /boot
/dev/mapper/host01--vg-var              9.2G  1.2G  7.5G  14% /var
/dev/mapper/host01--vg-tmp              1.8G  6.3M  1.7G   1% /tmp
/dev/mapper/host01--vg-home             373G  115G  241G  33% /home
tmpfs                                   790M  7.7M  782M   1% /run/user/1000
/dev/mapper/host01--vg-virtualmachines  295G  120G  160G  43% /opt/virtualmachines
```

### Raid

https://wiki.debian.org/SoftwareRAID
