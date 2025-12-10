# LPIC-1 Syntax Recognition Guide

## Purpose

This guide contains syntax you need to **recognize** for the LPIC-1 exam, not necessarily memorize. When you see these patterns in exam questions, you should be able to identify what they do.

**Learning approach:**
- Read through examples
- Practice identifying what code does
- Don't stress about memorizing exact syntax
- Focus on recognizing patterns and understanding purpose

---

## File System Navigation & Management

### Directory Operations

**Recognize these patterns:**

```bash
# Creating directories
mkdir dirname                    # Create single directory
mkdir -p path/to/nested/dir     # Create nested directories (parents too)
mkdir -m 755 dirname            # Create with specific permissions

# Removing directories
rmdir dirname                   # Remove empty directory only
rm -r dirname                   # Remove directory and contents recursively
rm -rf dirname                  # Force remove without prompts

# Listing contents
ls -l                          # Long format with details
ls -a                          # Show hidden files (starting with .)
ls -lh                         # Human-readable sizes
ls -R                          # Recursive listing
ls -ld dirname                 # List directory itself, not contents
```

**What to recognize:** The `-p` flag creates parent directories, `-r` means recursive, `-f` means force.

### File Operations

**Recognize these patterns:**

```bash
# Copying
cp source dest                 # Copy file
cp -r source dest             # Copy directory recursively
cp -p source dest             # Preserve permissions/timestamps
cp -a source dest             # Archive mode (preserve everything)

# Moving/Renaming
mv source dest                # Move or rename
mv -i source dest             # Interactive (prompt before overwrite)

# Removing
rm filename                   # Remove file
rm -i filename               # Interactive removal
rm -f filename               # Force removal

# Creating files
touch filename               # Create empty file or update timestamp
touch -t 202512101200 file  # Set specific timestamp
```

**What to recognize:** `-i` means interactive (prompts), `-p` preserves attributes, `-a` is archive mode.

---

## File Permissions & Ownership

### Permission Syntax

**Recognize these patterns:**

```bash
# Symbolic mode
chmod u+x file               # Add execute for user
chmod g-w file               # Remove write for group
chmod o=r file               # Set other to read only
chmod a+r file               # Add read for all
chmod u+x,g-w file          # Multiple changes

# Numeric mode
chmod 755 file               # rwxr-xr-x
chmod 644 file               # rw-r--r--
chmod 600 file               # rw-------
chmod 777 file               # rwxrwxrwx

# Recursive
chmod -R 755 directory       # Apply to directory and contents

# Special permissions
chmod u+s file               # Set SUID
chmod g+s directory          # Set SGID
chmod +t directory           # Set sticky bit
chmod 4755 file              # SUID with numeric (4=SUID, 2=SGID, 1=sticky)
```

**What to recognize:** 
- First digit in 4-digit mode: special permissions (4=SUID, 2=SGID, 1=sticky)
- Three digits: user, group, other (4=read, 2=write, 1=execute)
- Letters: u=user, g=group, o=other, a=all

### Ownership

**Recognize these patterns:**

```bash
# Change owner
chown user file              # Change owner only
chown user:group file        # Change owner and group
chown -R user directory      # Recursive

# Change group
chgrp group file             # Change group only
chgrp -R group directory     # Recursive

# Default permissions
umask                        # Show current umask
umask 022                    # Set umask (subtracts from 666 for files, 777 for dirs)
```

**What to recognize:** umask subtracts from default permissions (666 for files, 777 for directories).

---

## Finding Files

### find Command

**Recognize these patterns:**

```bash
# By name
find /path -name "*.txt"           # Find by exact name pattern
find /path -iname "*.TXT"          # Case-insensitive name
find /path -name "file*"           # Wildcard patterns

# By type
find /path -type f                 # Files only
find /path -type d                 # Directories only
find /path -type l                 # Symbolic links only

# By size
find /path -size +100M             # Larger than 100MB
find /path -size -1k               # Smaller than 1KB
find /path -size 50M               # Exactly 50MB

# By time
find /path -mtime -7               # Modified in last 7 days
find /path -mtime +30              # Modified more than 30 days ago
find /path -atime -1               # Accessed in last day

# By permissions
find /path -perm 644               # Exactly 644
find /path -perm -644              # At least 644
find /path -perm /u+x              # User executable

# Execute actions
find /path -name "*.tmp" -delete   # Delete matches
find /path -type f -exec chmod 644 {} \;  # Execute command on each
find /path -type f -exec ls -l {} +       # Execute with multiple files
```

**What to recognize:**
- `-mtime -7` means "less than 7 days ago" (minus = recent)
- `-mtime +30` means "more than 30 days ago" (plus = older)
- `{}` is placeholder for found file
- `\;` executes command once per file
- `+` executes command with multiple files at once

### locate Command

**Recognize these patterns:**

```bash
locate filename              # Search database for filename
locate -i filename          # Case-insensitive search
updatedb                    # Update the locate database
```

**What to recognize:** locate uses a database (faster but may be outdated), updatedb refreshes it.

---

## Text Processing

### grep

**Recognize these patterns:**

```bash
# Basic search
grep "pattern" file              # Search for pattern
grep -i "pattern" file           # Case-insensitive
grep -v "pattern" file           # Invert match (lines NOT matching)
grep -r "pattern" directory      # Recursive search
grep -n "pattern" file           # Show line numbers
grep -c "pattern" file           # Count matches
grep -l "pattern" files*         # List filenames with matches
grep -w "word" file              # Match whole word only

# Extended regex
grep -E "pattern1|pattern2" file # Extended regex (OR)
egrep "pattern1|pattern2" file   # Same as grep -E

# Multiple files
grep "pattern" file1 file2       # Search multiple files
grep "pattern" *.txt             # Search all .txt files
```

**What to recognize:** `-v` inverts (shows non-matches), `-r` is recursive, `-E` enables extended regex.

### sed

**Recognize these patterns:**

```bash
# Substitution
sed 's/old/new/' file            # Replace first occurrence per line
sed 's/old/new/g' file           # Replace all occurrences (global)
sed 's/old/new/2' file           # Replace second occurrence per line
sed -i 's/old/new/g' file        # Edit file in-place

# Deletion
sed '/pattern/d' file            # Delete lines matching pattern
sed '5d' file                    # Delete line 5
sed '1,3d' file                  # Delete lines 1-3

# Printing
sed -n '5p' file                 # Print only line 5
sed -n '/pattern/p' file         # Print only matching lines
```

**What to recognize:** `s/old/new/` is substitution, `g` means global, `-i` edits in-place, `d` deletes, `p` prints.

### awk

**Recognize these patterns:**

```bash
# Print columns
awk '{print $1}' file            # Print first column
awk '{print $1, $3}' file        # Print columns 1 and 3
awk '{print $NF}' file           # Print last column

# Pattern matching
awk '/pattern/ {print $1}' file  # Print first column of matching lines
awk '$3 > 100' file              # Print lines where column 3 > 100

# Field separator
awk -F: '{print $1}' /etc/passwd # Use : as separator
awk -F',' '{print $2}' file      # Use comma as separator
```

**What to recognize:** `$1`, `$2` are columns, `$NF` is last column, `-F` sets field separator.

### cut

**Recognize these patterns:**

```bash
cut -d: -f1 /etc/passwd          # Cut field 1 using : delimiter
cut -d, -f1,3 file               # Cut fields 1 and 3 using comma
cut -c1-10 file                  # Cut characters 1-10
```

**What to recognize:** `-d` sets delimiter, `-f` selects fields, `-c` selects characters.

### sort

**Recognize these patterns:**

```bash
sort file                        # Sort alphabetically
sort -n file                     # Sort numerically
sort -r file                     # Reverse sort
sort -k2 file                    # Sort by column 2
sort -u file                     # Sort and remove duplicates
sort -t: -k3 -n /etc/passwd      # Sort by field 3 numerically, : delimiter
```

**What to recognize:** `-n` is numeric sort, `-r` reverses, `-k` specifies column, `-u` removes duplicates.

---

## Process Management

### Viewing Processes

**Recognize these patterns:**

```bash
# ps command
ps                               # Show processes in current shell
ps aux                           # All processes, detailed (BSD style)
ps -ef                           # All processes (Unix style)
ps -u username                   # Processes for specific user
ps -p 1234                       # Process with specific PID

# top/htop
top                              # Interactive process viewer
top -u username                  # Show user's processes
htop                             # Enhanced interactive viewer
```

**What to recognize:** `ps aux` shows all processes with details, `top` is interactive and updates.

### Managing Processes

**Recognize these patterns:**

```bash
# Signals
kill 1234                        # Send TERM signal to PID 1234
kill -9 1234                     # Send KILL signal (force kill)
kill -15 1234                    # Send TERM signal (graceful)
kill -HUP 1234                   # Send HUP signal (reload config)
killall processname              # Kill all processes by name
pkill pattern                    # Kill processes matching pattern

# Background/Foreground
command &                        # Run in background
jobs                             # List background jobs
fg %1                            # Bring job 1 to foreground
bg %1                            # Resume job 1 in background
Ctrl+Z                           # Suspend current process

# Priority
nice -n 10 command               # Start with priority 10
renice 5 -p 1234                 # Change priority of PID 1234
```

**What to recognize:** 
- Signal 9 (KILL) cannot be caught, signal 15 (TERM) is graceful
- Lower nice values = higher priority
- `&` runs in background

---

## Archiving & Compression

### tar

**Recognize these patterns:**

```bash
# Creating archives
tar -cf archive.tar files        # Create tar archive
tar -czf archive.tar.gz files    # Create and gzip compress
tar -cjf archive.tar.bz2 files   # Create and bzip2 compress
tar -cJf archive.tar.xz files    # Create and xz compress

# Extracting archives
tar -xf archive.tar              # Extract tar archive
tar -xzf archive.tar.gz          # Extract gzipped tar
tar -xjf archive.tar.bz2         # Extract bzip2 tar
tar -xf archive.tar -C /path     # Extract to specific directory

# Listing contents
tar -tf archive.tar              # List contents
tar -tzf archive.tar.gz          # List gzipped tar contents

# Verbose mode
tar -cvf archive.tar files       # Create with verbose output
tar -xvf archive.tar             # Extract with verbose output
```

**What to recognize:**
- `c` = create, `x` = extract, `t` = list, `f` = file
- `z` = gzip, `j` = bzip2, `J` = xz
- `v` = verbose

### Compression Tools

**Recognize these patterns:**

```bash
# gzip
gzip file                        # Compress (creates file.gz, removes original)
gzip -d file.gz                  # Decompress
gunzip file.gz                   # Decompress (same as gzip -d)
gzip -k file                     # Keep original file

# bzip2
bzip2 file                       # Compress (creates file.bz2)
bzip2 -d file.bz2                # Decompress
bunzip2 file.bz2                 # Decompress

# xz
xz file                          # Compress (creates file.xz)
xz -d file.xz                    # Decompress
unxz file.xz                     # Decompress
```

**What to recognize:** These tools replace the original file by default, use `-k` to keep it.

---

## Package Management

### Debian/Ubuntu (apt/dpkg)

**Recognize these patterns:**

```bash
# apt
apt update                       # Update package lists
apt upgrade                      # Upgrade installed packages
apt install package              # Install package
apt remove package               # Remove package (keep config)
apt purge package                # Remove package and config
apt search keyword               # Search for packages
apt show package                 # Show package details

# dpkg
dpkg -i package.deb              # Install .deb package
dpkg -r package                  # Remove package
dpkg -l                          # List installed packages
dpkg -L package                  # List files in package
dpkg -S /path/to/file            # Find package owning file
```

**What to recognize:** `apt` is high-level (handles dependencies), `dpkg` is low-level.

### Red Hat/CentOS (yum/rpm)

**Recognize these patterns:**

```bash
# yum
yum update                       # Update all packages
yum install package              # Install package
yum remove package               # Remove package
yum search keyword               # Search for packages
yum info package                 # Show package info
yum list installed               # List installed packages

# rpm
rpm -i package.rpm               # Install package
rpm -e package                   # Remove package
rpm -qa                          # Query all installed packages
rpm -ql package                  # List files in package
rpm -qf /path/to/file            # Find package owning file
rpm -V package                   # Verify package integrity
```

**What to recognize:** `yum` handles dependencies, `rpm` is low-level. `-q` is query, `-i` is install, `-e` is erase.

---

## System Information

### Disk Usage

**Recognize these patterns:**

```bash
# df - disk free space
df                               # Show disk usage
df -h                            # Human-readable sizes
df -i                            # Show inode usage
df -T                            # Show filesystem types

# du - disk usage
du directory                     # Show size of directory
du -h directory                  # Human-readable
du -s directory                  # Summary only (total)
du -sh *                         # Summary of each item
du -a directory                  # Include files, not just directories
```

**What to recognize:** `df` shows filesystem space, `du` shows directory/file sizes.

### System Resources

**Recognize these patterns:**

```bash
# Memory
free                             # Show memory usage
free -h                          # Human-readable
free -m                          # Show in megabytes

# CPU info
lscpu                            # Show CPU information
cat /proc/cpuinfo                # Detailed CPU info

# System info
uname -a                         # All system information
uname -r                         # Kernel version
uname -m                         # Machine architecture
hostname                         # Show hostname
uptime                           # Show uptime and load average
```

**What to recognize:** `/proc` contains system information files.

---

## Redirection & Pipes

### I/O Redirection

**Recognize these patterns:**

```bash
# Output redirection
command > file                   # Redirect stdout to file (overwrite)
command >> file                  # Redirect stdout to file (append)
command 2> file                  # Redirect stderr to file
command &> file                  # Redirect both stdout and stderr
command > file 2>&1              # Redirect both (older syntax)

# Input redirection
command < file                   # Read input from file
command << EOF                   # Here document
text
EOF

# Pipes
command1 | command2              # Pipe stdout of cmd1 to stdin of cmd2
command1 |& command2             # Pipe both stdout and stderr
```

**What to recognize:**
- `>` overwrites, `>>` appends
- `2>` redirects stderr (file descriptor 2)
- `&>` redirects both stdout and stderr
- `|` pipes output between commands

---

## Shell Scripting Basics

### Variables

**Recognize these patterns:**

```bash
# Variable assignment
VAR="value"                      # Set variable (no spaces around =)
VAR=$(command)                   # Command substitution
VAR=`command`                    # Command substitution (old style)

# Using variables
echo $VAR                        # Use variable
echo ${VAR}                      # Use variable (explicit)
echo "$VAR"                      # Use variable (preserves spaces)

# Special variables
$0                               # Script name
$1, $2, ...                      # Positional parameters
$#                               # Number of parameters
$@                               # All parameters as separate words
$*                               # All parameters as single word
$?                               # Exit status of last command
$$                               # Current process ID
```

**What to recognize:** No spaces around `=`, use `$` to access variables, `$?` is exit status.

### Conditionals

**Recognize these patterns:**

```bash
# if statement
if [ condition ]; then
    commands
fi

if [ condition ]; then
    commands
else
    commands
fi

# File tests
[ -f file ]                      # True if file exists and is regular file
[ -d directory ]                 # True if directory exists
[ -e path ]                      # True if path exists
[ -r file ]                      # True if file is readable
[ -w file ]                      # True if file is writable
[ -x file ]                      # True if file is executable

# String tests
[ -z "$string" ]                 # True if string is empty
[ -n "$string" ]                 # True if string is not empty
[ "$str1" = "$str2" ]            # True if strings are equal
[ "$str1" != "$str2" ]           # True if strings are not equal

# Numeric tests
[ $num1 -eq $num2 ]              # Equal
[ $num1 -ne $num2 ]              # Not equal
[ $num1 -lt $num2 ]              # Less than
[ $num1 -le $num2 ]              # Less than or equal
[ $num1 -gt $num2 ]              # Greater than
[ $num1 -ge $num2 ]              # Greater than or equal
```

**What to recognize:** 
- Spaces around brackets are required
- `-f`, `-d`, `-e` test file types
- `-eq`, `-ne`, `-lt`, `-gt` for numeric comparisons
- `=`, `!=` for string comparisons

### Loops

**Recognize these patterns:**

```bash
# for loop
for var in list; do
    commands
done

for file in *.txt; do
    echo $file
done

# while loop
while [ condition ]; do
    commands
done

# until loop
until [ condition ]; do
    commands
done
```

**What to recognize:** `for` iterates over list, `while` continues while true, `until` continues until true.

---

## Networking Basics

### Network Configuration

**Recognize these patterns:**

```bash
# ip command (modern)
ip addr show                     # Show IP addresses
ip link show                     # Show network interfaces
ip route show                    # Show routing table
ip addr add 192.168.1.10/24 dev eth0  # Add IP address

# ifconfig (legacy)
ifconfig                         # Show network interfaces
ifconfig eth0                    # Show specific interface
ifconfig eth0 up                 # Bring interface up
ifconfig eth0 down               # Bring interface down
```

**What to recognize:** `ip` is modern replacement for `ifconfig`.

### Network Testing

**Recognize these patterns:**

```bash
# Connectivity
ping host                        # Test connectivity
ping -c 4 host                   # Send 4 packets only
ping6 host                       # Ping IPv6

# DNS
host domain                      # DNS lookup
nslookup domain                  # DNS lookup (interactive)
dig domain                       # Detailed DNS lookup

# Ports and connections
netstat -tuln                    # Show listening ports
netstat -r                       # Show routing table
ss -tuln                         # Show listening ports (modern)
ss -s                            # Show socket statistics
```

**What to recognize:** `ss` is modern replacement for `netstat`.

---

## User & Group Management

### User Management

**Recognize these patterns:**

```bash
# Adding users
useradd username                 # Create user (minimal)
useradd -m username              # Create user with home directory
useradd -m -s /bin/bash username # Create with specific shell
adduser username                 # Interactive user creation (Debian)

# Modifying users
usermod -l newname oldname       # Rename user
usermod -L username              # Lock user account
usermod -U username              # Unlock user account
usermod -aG groupname username   # Add user to group

# Deleting users
userdel username                 # Delete user (keep home)
userdel -r username              # Delete user and home directory

# Password management
passwd username                  # Set/change password
passwd -l username               # Lock password
passwd -u username               # Unlock password
```

**What to recognize:** `-m` creates home directory, `-r` removes home directory, `-aG` adds to group.

### Group Management

**Recognize these patterns:**

```bash
# Adding groups
groupadd groupname               # Create group
groupadd -g 1500 groupname       # Create with specific GID

# Modifying groups
groupmod -n newname oldname      # Rename group

# Deleting groups
groupdel groupname               # Delete group

# Viewing groups
groups username                  # Show user's groups
id username                      # Show user ID and groups
```

**What to recognize:** `groups` shows group membership, `id` shows UID/GID.

---

## Study Tips

1. **Don't memorize everything** - Focus on recognizing patterns
2. **Practice reading code** - Look at examples and identify what they do
3. **Understand the logic** - Know why certain flags are used together
4. **Use the recognition exercises** - Practice with real exam-style questions
5. **Test yourself** - Cover the explanations and try to identify what code does

Remember: The goal is **recognition**, not recall. You should be able to look at a command and understand what it does, not necessarily write it from memory.
