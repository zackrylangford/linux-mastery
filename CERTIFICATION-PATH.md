# Linux Certification Path

Goal-oriented learning path aligned with industry certifications.

## 🎯 Recommended Path

### Phase 1: LPIC-1 (3-4 months)
**Target**: Linux Professional Institute Certification Level 1
**Cost**: ~$200 per exam ($400 total)
**Format**: Multiple choice, 60 questions each, 90 minutes
**Passing**: 500/800 points

### Phase 2: RHCSA (3-4 months after LPIC-1)
**Target**: Red Hat Certified System Administrator
**Cost**: ~$400
**Format**: 100% hands-on practical exam, 2.5 hours
**Passing**: 210/300 points (70%)

## 📋 LPIC-1 Exam Breakdown

### Exam 101-500 Topics (Weight %)

**Topic 101: System Architecture (8%)**
- Determine and configure hardware settings
- Boot the system
- Change runlevels/boot targets and shutdown/reboot

**Topic 102: Linux Installation and Package Management (10%)**
- Design hard disk layout
- Install a boot manager
- Manage shared libraries
- Use Debian/RPM package management

**Topic 103: GNU and Unix Commands (26%)**
- Work on the command line
- Process text streams using filters
- Perform basic file management
- Use streams, pipes and redirects
- Create, monitor and kill processes
- Modify process execution priorities
- Search text files using regular expressions
- Basic file editing

**Topic 104: Devices, Linux Filesystems, FHS (15%)**
- Create partitions and filesystems
- Maintain filesystem integrity
- Control mounting and unmounting
- Manage disk quotas
- Manage file permissions and ownership
- Create and change hard/symbolic links
- Find system files and place files in correct location

### Exam 102-500 Topics (Weight %)

**Topic 105: Shells and Shell Scripting (8%)**
- Customize and use the shell environment
- Customize or write simple scripts

**Topic 106: User Interfaces and Desktops (3%)**
- Install and configure X11
- Graphical desktops
- Accessibility

**Topic 107: Administrative Tasks (10%)**
- Manage user and group accounts
- Automate system administration with cron/at
- Localization and internationalization

**Topic 108: Essential System Services (10%)**
- Maintain system time
- System logging
- Mail Transfer Agent (MTA) basics
- Manage printers and printing

**Topic 109: Networking Fundamentals (13%)**
- Fundamentals of internet protocols
- Persistent network configuration
- Basic network troubleshooting
- Configure client side DNS

**Topic 110: Security (10%)**
- Perform security administration tasks
- Setup host security
- Securing data with encryption

## 📚 Free LPIC-1 Study Resources

### Video Courses
- **Jadi's LPIC-1 Course** (YouTube) - Complete free course
  - URL: https://www.youtube.com/watch?v=AKkNUvEHXhk
  - 100+ videos covering all objectives

### Practice Exams
- **LPI Learning Materials** - Official free resources
  - URL: https://learning.lpi.org/en/learning-materials/101-500/
  - URL: https://learning.lpi.org/en/learning-materials/102-500/

### Books (Free Online)
- **LPIC-1 Study Guide** - Available through various sources
- **Linux Command Line** by William Shotts

## 🗓️ 16-Week LPIC-1 Study Plan

### Weeks 1-8: Exam 101-500

**Week 1-2: System Architecture & Installation**
- Hardware settings and boot process
- Package management (apt/rpm)
- Shared libraries

**Week 3-5: GNU and Unix Commands** (Largest section)
- Command line mastery
- Text processing (grep, sed, awk)
- File management
- Process management
- Regular expressions
- Vi/Vim editing

**Week 6-8: Devices & Filesystems**
- Partitioning (fdisk, parted)
- Filesystem creation (ext4, xfs)
- Mounting and fstab
- Permissions and ownership
- Links and file locations

### Weeks 9-14: Exam 102-500

**Week 9-10: Shells & Administrative Tasks**
- Bash scripting
- Environment customization
- User/group management
- Cron and at scheduling

**Week 11-12: System Services**
- System time (NTP, chrony)
- Logging (rsyslog, journald)
- Email basics
- Printing

**Week 13-14: Networking & Security**
- TCP/IP fundamentals
- Network configuration
- DNS client setup
- Firewall basics
- SSH and encryption
- Security administration

### Weeks 15-16: Review & Practice Exams
- Take full practice exams
- Review weak areas
- Hands-on lab practice
- Schedule and take exams

## 📊 Certification-Aligned Achievement System

### LPIC-1 Exam 101 Achievements

**System Architecture Master**
- [ ] Identify hardware devices and modules
- [ ] Understand BIOS/UEFI boot process
- [ ] Configure GRUB2 bootloader
- [ ] Manage systemd targets
- [ ] Shutdown and reboot safely

**Package Management Expert**
- [ ] Install packages with apt/dpkg
- [ ] Install packages with yum/rpm
- [ ] Query package information
- [ ] Manage shared libraries
- [ ] Understand dependency resolution

**Command Line Ninja** (Critical - 26% of exam)
- [ ] Master 50+ essential commands
- [ ] Use pipes and redirects fluently
- [ ] Process text with grep/sed/awk
- [ ] Manage processes (ps, top, kill, nice)
- [ ] Write complex regular expressions
- [ ] Edit files efficiently in vim

**Filesystem Architect**
- [ ] Create partitions with fdisk/parted
- [ ] Format filesystems (ext4, xfs, btrfs)
- [ ] Configure /etc/fstab
- [ ] Manage permissions (chmod, chown, umask)
- [ ] Create hard and symbolic links
- [ ] Understand FHS (Filesystem Hierarchy Standard)

### LPIC-1 Exam 102 Achievements

**Shell Scripting Pro**
- [ ] Write bash scripts with functions
- [ ] Use variables and conditionals
- [ ] Implement loops and case statements
- [ ] Customize shell environment
- [ ] Create useful automation scripts

**System Administrator**
- [ ] Manage users and groups
- [ ] Configure sudo access
- [ ] Schedule tasks with cron
- [ ] Use at for one-time tasks
- [ ] Manage system locale

**Service Manager**
- [ ] Configure system time (NTP)
- [ ] Manage systemd services
- [ ] Configure rsyslog/journald
- [ ] Understand mail basics
- [ ] Set up printing

**Network & Security Specialist**
- [ ] Configure network interfaces
- [ ] Troubleshoot connectivity
- [ ] Set up DNS resolution
- [ ] Configure SSH securely
- [ ] Use basic firewall rules
- [ ] Implement encryption (GPG)

## 🎓 After LPIC-1: RHCSA Path

### RHCSA Exam Objectives (RHEL 9)

**Understand and use essential tools**
- Access shell and run commands
- Use input-output redirection
- Use grep and regular expressions
- Access remote systems using SSH
- Log in and switch users
- Archive, compress, unpack files
- Create and edit text files
- Create, delete, copy, move files
- Create hard and soft links
- List, set, and change permissions
- Locate, read, and use system documentation

**Create simple shell scripts**
- Conditionally execute code
- Use looping constructs
- Process script inputs

**Operate running systems**
- Boot, reboot, shutdown systems
- Boot systems into different targets
- Interrupt boot process for recovery
- Identify CPU/memory intensive processes
- Adjust process scheduling
- Manage tuning profiles
- Locate and interpret system log files
- Preserve system journals
- Start, stop, and check status of services
- Transfer files securely

**Configure local storage**
- List, create, delete partitions
- Create and remove physical volumes
- Assign physical volumes to volume groups
- Create and delete logical volumes
- Configure systems to mount filesystems at boot
- Add new partitions and logical volumes
- Create and configure set-GID directories
- Configure disk compression
- Manage layered storage
- Diagnose and correct file permission problems

**Create and configure file systems**
- Create, mount, unmount, and use vfat, ext4, and xfs
- Mount and unmount network file systems using NFS
- Configure autofs
- Extend existing logical volumes
- Create and configure set-GID directories
- Diagnose and correct file permission problems

**Deploy, configure, and maintain systems**
- Schedule tasks using at and cron
- Start and stop services and configure services to start automatically
- Configure systems to boot into a specific target
- Configure time service clients
- Install and update software packages
- Modify the system bootloader

**Manage basic networking**
- Configure IPv4 and IPv6 addresses
- Configure hostname resolution
- Configure network services to start automatically
- Restrict network access using firewall-cmd/firewalld

**Manage users and groups**
- Create, delete, and modify local user accounts
- Change passwords and adjust password aging
- Create, delete, and modify local groups
- Configure superuser access

**Manage security**
- Configure firewall settings
- Manage default file permissions
- Configure key-based authentication for SSH
- Set enforcing and permissive modes for SELinux
- List and identify SELinux file and process context
- Restore default file contexts
- Manage SELinux port labels
- Use boolean settings to modify system SELinux settings
- Diagnose and address routine SELinux policy violations

**Manage containers**
- Find and retrieve container images
- Inspect container images
- Perform container management
- Perform basic container management
- Run services inside containers
- Configure a container to start automatically
- Attach persistent storage to a container

## 📅 Daily Practice for Certification

### Weekday Routine (60 min)
1. **Study** (30 min) - One exam objective
2. **Lab Practice** (20 min) - Hands-on with that objective
3. **Flashcards/Quiz** (10 min) - Test retention

### Weekend Routine (90 min)
1. **Review** (30 min) - Week's objectives
2. **Practice Exam** (45 min) - Timed section
3. **Document** (15 min) - Update notes and weak areas

**See also**: [DAILY-PRACTICE.md](DAILY-PRACTICE.md) for the general learning routine, and [EXAMPLE-WALKTHROUGH.md](EXAMPLE-WALKTHROUGH.md) for a complete example of the learning process.

## 🎯 Exam Preparation Timeline

### 2 Months Before
- Complete all study materials
- Start practice exams
- Identify weak areas

### 1 Month Before
- Focus on weak areas
- Take full practice exams weekly
- Hands-on labs daily

### 2 Weeks Before
- Practice exams every other day
- Review all notes
- Memorize key commands and concepts

### 1 Week Before
- Light review only
- Rest and prepare mentally
- Schedule exam if not already done

## 💰 Cost Breakdown

**LPIC-1**
- Exam 101-500: $200
- Exam 102-500: $200
- Study materials: $0 (all free)
- **Total: $400**

**RHCSA**
- Exam: $400
- Study materials: $0-50 (optional books)
- Practice environment: $0 (use free tier cloud)
- **Total: $400-450**

**Combined Investment: $800-850**

## 🏆 Career Impact

**With LPIC-1:**
- Junior Linux Administrator roles
- Entry-level DevOps positions
- Technical support (Linux focus)
- Salary boost: 10-20%

**With RHCSA:**
- Linux System Administrator
- DevOps Engineer
- Cloud Infrastructure roles
- Salary boost: 20-40%

**Both certifications:**
- Senior positions accessible
- Strong foundation for advanced certs
- Competitive advantage in job market
