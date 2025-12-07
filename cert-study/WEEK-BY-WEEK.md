# LPIC-1 Week-by-Week Study Plan

Detailed daily breakdown for 16-week certification preparation.

## Week 1: System Architecture (Exam 101 - Topic 101)

### Monday: Hardware & Devices
- **Study**: `/sys`, `/proc`, `/dev` directories
- **Commands**: `lspci`, `lsusb`, `lsmod`, `modprobe`
- **Lab**: Identify all hardware on your system
- **Quiz**: Hardware identification

### Tuesday: Boot Process
- **Study**: BIOS/UEFI, bootloader, kernel, init
- **Commands**: `dmesg`, `journalctl -b`
- **Lab**: Trace boot process from power-on
- **Quiz**: Boot sequence order

### Wednesday: GRUB2 Bootloader
- **Study**: GRUB2 configuration
- **Files**: `/boot/grub/grub.cfg`, `/etc/default/grub`
- **Commands**: `grub2-mkconfig`, `update-grub`
- **Lab**: Modify GRUB timeout and default entry

### Thursday: Runlevels & Targets
- **Study**: systemd targets vs SysV runlevels
- **Commands**: `systemctl get-default`, `systemctl isolate`
- **Lab**: Change default target, boot to rescue mode
- **Quiz**: Target equivalents

### Friday: Shutdown & Reboot
- **Study**: Proper shutdown procedures
- **Commands**: `shutdown`, `reboot`, `halt`, `poweroff`, `systemctl`
- **Lab**: Schedule shutdowns, cancel shutdowns
- **Practice Exam**: Topic 101 questions

### Weekend: Review & Lab
- Complete all Week 1 exercises
- Build a boot troubleshooting guide
- Practice all commands without looking up syntax

---

## Week 2: Package Management (Exam 101 - Topic 102)

### Monday: Debian Package Management
- **Study**: dpkg and apt systems
- **Commands**: `dpkg -i`, `dpkg -l`, `dpkg -r`
- **Lab**: Install/remove packages with dpkg
- **Quiz**: dpkg options

### Tuesday: APT Advanced
- **Study**: apt, apt-get, apt-cache
- **Commands**: `apt update`, `apt install`, `apt search`
- **Lab**: Add PPA, install from repository
- **Quiz**: APT vs dpkg

### Wednesday: RPM Package Management
- **Study**: RPM and YUM/DNF systems
- **Commands**: `rpm -i`, `rpm -qa`, `rpm -e`
- **Lab**: Install/remove packages with rpm
- **Quiz**: RPM options

### Thursday: YUM/DNF Advanced
- **Study**: Repository management
- **Commands**: `yum install`, `yum update`, `dnf search`
- **Lab**: Add repository, install package groups
- **Quiz**: YUM/DNF operations

### Friday: Shared Libraries
- **Study**: Library dependencies and paths
- **Commands**: `ldd`, `ldconfig`
- **Files**: `/etc/ld.so.conf`, `/etc/ld.so.cache`
- **Lab**: Identify library dependencies
- **Practice Exam**: Topic 102 questions

### Weekend: Cross-Platform Practice
- Set up both Debian and RHEL-based VMs
- Practice same tasks on both systems
- Create package management cheat sheet

---

## Week 3-5: GNU and Unix Commands (Exam 101 - Topic 103)
*This is 26% of the exam - spend extra time here*

### Week 3: Command Line Basics

**Monday: Shell Basics**
- Commands: `bash`, `echo`, `type`, `which`, `man`, `info`
- Environment: `$PATH`, `$HOME`, `$SHELL`
- Lab: Customize prompt, understand command types

**Tuesday: File Management**
- Commands: `ls`, `cp`, `mv`, `rm`, `mkdir`, `rmdir`, `touch`
- Options: Master all important flags
- Lab: Complex file operations

**Wednesday: File Viewing**
- Commands: `cat`, `less`, `more`, `head`, `tail`, `tac`
- Lab: View logs, follow files with `tail -f`

**Thursday: File Finding**
- Commands: `find`, `locate`, `updatedb`, `whereis`, `which`
- Lab: Complex find operations with -exec

**Friday: Archives**
- Commands: `tar`, `gzip`, `bzip2`, `xz`, `zip`, `unzip`
- Lab: Create and extract various archive types
- Practice Exam: Command line basics

### Week 4: Text Processing

**Monday: Grep & Regular Expressions**
- Commands: `grep`, `egrep`, `fgrep`
- Regex: Basic and extended patterns
- Lab: Search log files for patterns

**Tuesday: Sed**
- Commands: `sed` substitution, deletion, insertion
- Lab: Batch text file modifications

**Wednesday: Awk**
- Commands: `awk` patterns and actions
- Lab: Process columnar data

**Thursday: Text Utilities**
- Commands: `cut`, `paste`, `join`, `sort`, `uniq`, `tr`, `wc`
- Lab: Complex text processing pipelines

**Friday: Streams & Pipes**
- Redirection: `>`, `>>`, `<`, `2>`, `&>`
- Pipes: `|`, `tee`, `xargs`
- Lab: Build complex command chains
- Practice Exam: Text processing

### Week 5: Processes & Vi

**Monday: Process Viewing**
- Commands: `ps`, `pstree`, `top`, `htop`
- Lab: Monitor system processes

**Tuesday: Process Control**
- Commands: `kill`, `killall`, `pkill`, `jobs`, `fg`, `bg`
- Signals: SIGTERM, SIGKILL, SIGHUP
- Lab: Manage background processes

**Wednesday: Process Priority**
- Commands: `nice`, `renice`
- Lab: Adjust process priorities

**Thursday: Vi/Vim Basics**
- Modes: Normal, Insert, Visual, Command
- Basic editing: i, a, o, x, dd, yy, p
- Lab: Edit configuration files

**Friday: Vi/Vim Advanced**
- Search: `/`, `?`, `n`, `N`
- Replace: `:s/old/new/g`
- Lab: Complex file editing tasks
- Practice Exam: Processes and Vi

### Weekend: Topic 103 Mastery
- Take full Topic 103 practice exam
- Review all weak areas
- Create command reference sheet

---

## Week 6-8: Filesystems (Exam 101 - Topic 104)

### Week 6: Partitions & Filesystems

**Monday: Disk Partitioning**
- Commands: `fdisk`, `parted`, `gdisk`
- Concepts: MBR vs GPT
- Lab: Create partitions (in VM!)

**Tuesday: Filesystem Creation**
- Commands: `mkfs.ext4`, `mkfs.xfs`, `mkfs.vfat`
- Lab: Format partitions with different filesystems

**Wednesday: Mounting**
- Commands: `mount`, `umount`
- Files: `/etc/fstab`
- Lab: Mount filesystems, configure fstab

**Thursday: Filesystem Maintenance**
- Commands: `fsck`, `e2fsck`, `xfs_repair`, `tune2fs`
- Lab: Check and repair filesystems

**Friday: Disk Usage**
- Commands: `df`, `du`, `lsblk`, `blkid`
- Lab: Monitor disk space
- Practice Exam: Partitions and filesystems

### Week 7: Permissions & Links

**Monday: File Permissions**
- Concepts: rwx, owner/group/other
- Commands: `chmod` (octal and symbolic)
- Lab: Set various permission combinations

**Tuesday: Ownership**
- Commands: `chown`, `chgrp`
- Lab: Change file ownership

**Wednesday: Special Permissions**
- Concepts: SUID, SGID, sticky bit
- Commands: `chmod u+s`, `chmod g+s`, `chmod +t`
- Lab: Set special permissions

**Thursday: Links**
- Concepts: Hard links vs symbolic links
- Commands: `ln`, `ln -s`
- Lab: Create and manage links

**Friday: Umask**
- Concepts: Default permissions
- Commands: `umask`
- Lab: Set umask values
- Practice Exam: Permissions

### Week 8: FHS & Review

**Monday: Filesystem Hierarchy Standard**
- Study: All major directories
- Lab: Explore and document each directory

**Tuesday: File Locations**
- Commands: `find`, `locate`, `which`, `whereis`
- Lab: Locate system files

**Wednesday: Disk Quotas**
- Commands: `quota`, `edquota`, `quotacheck`
- Lab: Set up user quotas

**Thursday: Review Topic 104**
- Review all filesystem concepts
- Practice all commands

**Friday: Practice Exam 101-500**
- Take full 60-question practice exam
- Time yourself (90 minutes)
- Review incorrect answers

### Weekend: Exam 101 Final Review
- Review all weak areas from practice exam
- Hands-on lab for all topics
- Create final study sheet

---

## Weeks 9-14: Exam 102-500 Topics

*Similar detailed breakdown for:*
- Week 9: Shells & Scripting (Topic 105)
- Week 10: Administrative Tasks (Topic 107)
- Week 11: System Services (Topic 108)
- Week 12: Networking (Topic 109)
- Week 13: Security (Topic 110)
- Week 14: Review & Practice

---

## Weeks 15-16: Final Preparation

### Week 15: Intensive Practice

**Daily Routine:**
- Morning: Practice exam (90 min)
- Afternoon: Review incorrect answers
- Evening: Hands-on lab for weak areas

**Goals:**
- Take 5+ full practice exams
- Score consistently above 75%
- Identify and eliminate weak areas

### Week 16: Exam Week

**Monday-Wednesday: Light Review**
- Review notes and cheat sheets
- Practice only comfortable topics
- No new material

**Thursday: Rest**
- No studying
- Relax and prepare mentally

**Friday: Exam Day**
- Arrive early
- Read questions carefully
- Manage time (90 min / 60 questions = 1.5 min per question)

---

## Daily Study Template

```
Date: ___________
Topic: ___________
Time Spent: ___________

What I Learned:
-
-
-

Commands Practiced:
-
-
-

Lab Exercises Completed:
-
-

Quiz Score: ___/___

Weak Areas to Review:
-
-

Tomorrow's Focus:
-
```

## Progress Tracking

- [ ] Week 1: System Architecture
- [ ] Week 2: Package Management
- [ ] Week 3: Command Line Basics
- [ ] Week 4: Text Processing
- [ ] Week 5: Processes & Vi
- [ ] Week 6: Partitions & Filesystems
- [ ] Week 7: Permissions & Links
- [ ] Week 8: FHS & Exam 101 Review
- [ ] Week 9: Shells & Scripting
- [ ] Week 10: Administrative Tasks
- [ ] Week 11: System Services
- [ ] Week 12: Networking
- [ ] Week 13: Security
- [ ] Week 14: Exam 102 Review
- [ ] Week 15: Practice Exams
- [ ] Week 16: Exam Week

**Exam 101-500 Scheduled**: ___________
**Exam 102-500 Scheduled**: ___________
