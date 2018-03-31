#
# Title:create_raid.sh
#
# Description:
#
# Author:
#   G.S. Cole (guycole at gmail dot com)
#
# Maintenance History:
#   $Id$
#
#   $Log$
#
PATH=/bin:/usr/bin:/etc:/usr/local/bin; export PATH
#
/sbin/mdadm --create --verbose /dev/md0 --level=0 --name=RAID0 --raid-devices=2 /dev/nvme1n1 /dev/nvme2n1
#
/sbin/mkfs.ext4 -L RAID0 /dev/md0
#
/sbin/mdadm --detail --scan | sudo tee -a /etc/mdadm.conf
#
/sbin/dracut -H -f /boot/initramfs-$(uname -r).img $(uname -r)
#
mkdir -p /mnt/raid0
#
mount LABEL=RAID0 /mnt/raid0
#
cp /etc/fstab /etc/fstab.orig
#
echo "LABEL=RAID0 /mnt/raid0 ext4 defaults,nofail 0 2" >> /etc/fstab
#
mount -a
#
