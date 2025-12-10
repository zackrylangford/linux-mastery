# LPIC-1 Recognition Practice Exercises

## How to Use This Guide

For each code snippet below:
1. **Don't run it** - just read it
2. **Ask yourself:** "What does this do?"
3. **Try to explain** the purpose in plain English
4. **Check your answer** against the explanation

This builds recognition skills for the LPIC-1 exam.

---

## Exercise Set 1: File System Operations

### Exercise 1.1

```bash
find /var/log -name "*.log" -mtime +30 -delete
```

**What does this do?**

<details>
<summary>Click to see answer</summary>

**Answer:** Finds all files in `/var/log` with names ending in `.log` that were modified more than 30 days ago, and deletes them.

**Key points:**
- `find /var/log` - searches in /var/log directory
- `-name "*.log"` - matches files ending in .log
- `-mtime +30` - modified MORE than 30 days ago (+ means older)
- `-delete` - deletes the matched files

**When you'd use this:** Cleaning up old log files to free disk space.
</details>

---

### Exercise 1.2

```bash
mkdir -p /opt/myapp/{bin,lib,conf,logs}
```

**What does this do?**

<details>
<summary>Click to see answer</summary>

**Answer:** Creates a directory structure `/opt/myapp/` with four subdirectories: `bin`, `lib`, `conf`, and `logs`. Creates parent directories if they don't exist.

**Key points:**
- `mkdir -p` - creates parent directories as needed
- `{bin,lib,conf,logs}` - brace expansion creates multiple directories
- Results in: `/opt/myapp/bin`, `/opt/myapp/lib`, `/opt/myapp/conf`, `/opt/myapp/logs`

**When you'd use this:** Setting up a standard application directory structure.
</details>

---

### Exercise 1.3

```bash
cp -a /home/user/project /backup/
```

**What does this do?**

<details>
<summary>Click to see answer</summary>

**Answer:** Copies the entire `/home/user/project` directory to `/backup/`, preserving all attributes (permissions, timestamps, ownership, symbolic links).

**Key points:**
- `cp -a` - archive mode (preserves everything)
- Equivalent to `cp -dpR` (preserve links, don't follow them, recursive)
- Maintains exact copy including metadata

**When you'd use this:** Creating backups that preserve all file attributes.
</details>

---

### Exercise 1.4

```bash
ls -lh | grep "^d" | wc -l
```

**What does this do?**

<details>
<summary>Click to see answer</summary>

**Answer:** Counts the number of directories in the current directory.

**Key points:**
- `ls -lh` - long format listing with human-readable sizes
- `grep "^d"` - filters lines starting with 'd' (directories in ls -l output)
- `wc -l` - counts the number of lines
- `|` pipes output from one command to the next

**When you'd use this:** Quickly counting subdirectories without listing them all.
</details>

---

## Exercise Set 2: Permissions & Ownership

### Exercise 2.1

```bash
chmod 4755 /usr/local/bin/myapp
```

**What does this do?**

<details>
<summary>Click to see answer</summary>

**Answer:** Sets permissions on `/usr/local/bin/myapp` to `rwxr-xr-x` with the SUID bit set.

**Key points:**
- `4755` - first digit (4) sets SUID bit
- `755` - owner: rwx (7), group: r-x (5), other: r-x (5)
- SUID means the file runs with owner's permissions, not executor's
- Common for programs that need elevated privileges

**When you'd use this:** Setting up programs that need to run with specific user privileges (like `passwd`).
</details>

---

### Exercise 2.2

```bash
find /var/www -type f -exec chmod 644 {} \;
find /var/www -type d -exec chmod 755 {} \;
```

**What does this do?**

<details>
<summary>Click to see answer</summary>

**Answer:** Sets standard web server permissions: files to `644` (rw-r--r--) and directories to `755` (rwxr-xr-x) in `/var/www`.

**Key points:**
- First command: finds all files (`-type f`) and sets them to 644
- Second command: finds all directories (`-type d`) and sets them to 755
- `{}` is placeholder for each found item
- `\;` executes chmod once per item
- Standard practice: files don't need execute, directories do

**When you'd use this:** Fixing permissions on a web directory after uploading files.
</details>

---

### Exercise 2.3

```bash
chown -R www-data:www-data /var/www/html
```

**What does this do?**

<details>
<summary>Click to see answer</summary>

**Answer:** Recursively changes the owner and group of `/var/www/html` and all its contents to `www-data`.

**Key points:**
- `chown -R` - recursive (applies to directory and all contents)
- `www-data:www-data` - sets both owner and group to www-data
- Common on Debian/Ubuntu web servers

**When you'd use this:** Ensuring web server has proper ownership of web files.
</details>

---

### Exercise 2.4

```bash
umask 027
touch newfile
```

**What does this do?**

<details>
<summary>Click to see answer</summary>

**Answer:** Sets umask to 027, then creates a file. The new file will have permissions `640` (rw-r-----).

**Key points:**
- `umask 027` - subtracts from default permissions
- Default for files: 666, minus 027 = 640 (rw-r-----)
- Default for directories: 777, minus 027 = 750 (rwxr-x---)
- Umask 027 means: owner full, group read, other nothing

**When you'd use this:** Setting restrictive default permissions for security.
</details>

---

## Exercise Set 3: Text Processing

### Exercise 3.1

```bash
grep -v "^#" /etc/ssh/sshd_config | grep -v "^$"
```

**What does this do?**

<details>
<summary>Click to see answer</summary>

**Answer:** Shows the active configuration lines from SSH config file, removing comments and blank lines.

**Key points:**
- `grep -v "^#"` - excludes lines starting with # (comments)
- `grep -v "^$"` - excludes empty lines
- `-v` inverts the match (shows lines that DON'T match)
- `^` means start of line, `$` means end of line
- Result: only actual configuration directives

**When you'd use this:** Reviewing active configuration without clutter.
</details>

---

### Exercise 3.2

```bash
awk -F: '$3 >= 1000 {print $1}' /etc/passwd
```

**What does this do?**

<details>
<summary>Click to see answer</summary>

**Answer:** Lists usernames of all regular users (UID >= 1000) from the password file.

**Key points:**
- `awk -F:` - uses colon as field separator
- `$3 >= 1000` - condition: third field (UID) is 1000 or greater
- `{print $1}` - prints first field (username)
- `/etc/passwd` format: username:x:UID:GID:...
- UIDs >= 1000 are typically regular users (not system accounts)

**When you'd use this:** Finding all regular user accounts on the system.
</details>

---

### Exercise 3.3

```bash
sed -i 's/SELINUX=enforcing/SELINUX=disabled/g' /etc/selinux/config
```

**What does this do?**

<details>
<summary>Click to see answer</summary>

**Answer:** Changes SELinux from enforcing mode to disabled mode in the config file, editing the file in-place.

**Key points:**
- `sed -i` - edit file in-place (modifies the actual file)
- `s/old/new/g` - substitute old with new, globally
- Replaces `SELINUX=enforcing` with `SELINUX=disabled`
- `g` flag means replace all occurrences on each line

**When you'd use this:** Disabling SELinux (though reboot required for effect).
</details>

---

### Exercise 3.4

```bash
cat access.log | cut -d' ' -f1 | sort | uniq -c | sort -rn | head -10
```

**What does this do?**

<details>
<summary>Click to see answer</summary>

**Answer:** Shows the top 10 IP addresses by request count from an access log.

**Key points:**
- `cut -d' ' -f1` - extracts first field (IP address) using space delimiter
- `sort` - sorts IP addresses
- `uniq -c` - counts consecutive duplicate lines
- `sort -rn` - sorts numerically in reverse (highest first)
- `head -10` - shows first 10 lines
- Pipeline processes: extract IPs → sort → count → sort by count → show top 10

**When you'd use this:** Analyzing web server logs to find most active IP addresses.
</details>

---

### Exercise 3.5

```bash
grep -r "error" /var/log/*.log 2>/dev/null | wc -l
```

**What does this do?**

<details>
<summary>Click to see answer</summary>

**Answer:** Counts how many lines contain "error" across all .log files in /var/log, suppressing error messages.

**Key points:**
- `grep -r "error"` - recursively searches for "error"
- `/var/log/*.log` - searches all files ending in .log
- `2>/dev/null` - redirects error messages (like permission denied) to nowhere
- `wc -l` - counts the lines
- Useful for getting a count without seeing permission errors

**When you'd use this:** Quickly checking how many errors are in log files.
</details>

---

## Exercise Set 4: Process Management

### Exercise 4.1

```bash
ps aux | grep httpd | grep -v grep | awk '{print $2}' | xargs kill -9
```

**What does this do?**

<details>
<summary>Click to see answer</summary>

**Answer:** Force kills all httpd processes.

**Key points:**
- `ps aux` - shows all processes with details
- `grep httpd` - filters for httpd processes
- `grep -v grep` - excludes the grep command itself from results
- `awk '{print $2}'` - extracts second column (PID)
- `xargs kill -9` - passes PIDs to kill command with signal 9 (force kill)
- Signal 9 (SIGKILL) cannot be caught or ignored

**When you'd use this:** Emergency shutdown of a misbehaving web server (though `killall httpd` is simpler).
</details>

---

### Exercise 4.2

```bash
nice -n 19 ./backup-script.sh &
```

**What does this do?**

<details>
<summary>Click to see answer</summary>

**Answer:** Runs the backup script in the background with the lowest priority.

**Key points:**
- `nice -n 19` - sets priority to 19 (lowest, least CPU priority)
- Nice values range from -20 (highest) to 19 (lowest)
- `&` - runs process in background
- Lower priority means it won't interfere with other processes
- Good for resource-intensive tasks that aren't urgent

**When you'd use this:** Running backups or batch jobs that shouldn't slow down the system.
</details>

---

### Exercise 4.3

```bash
nohup ./long-running-task.sh > output.log 2>&1 &
```

**What does this do?**

<details>
<summary>Click to see answer</summary>

**Answer:** Runs a script in the background that continues even after logout, with all output saved to a log file.

**Key points:**
- `nohup` - immune to hangup signal (continues after logout)
- `> output.log` - redirects stdout to output.log
- `2>&1` - redirects stderr to same place as stdout
- `&` - runs in background
- Process continues even if you close the terminal

**When you'd use this:** Starting long-running tasks that should survive terminal disconnection.
</details>

---

### Exercise 4.4

```bash
pgrep -u www-data | xargs renice 10
```

**What does this do?**

<details>
<summary>Click to see answer</summary>

**Answer:** Changes the priority of all processes owned by www-data user to 10.

**Key points:**
- `pgrep -u www-data` - finds PIDs of all processes owned by www-data
- `xargs renice 10` - changes priority of those PIDs to 10
- Priority 10 is lower than default (0), so less CPU priority
- Affects running processes

**When you'd use this:** Reducing priority of web server processes to favor other applications.
</details>

---

## Exercise Set 5: Archiving & Compression

### Exercise 5.1

```bash
tar -czf backup-$(date +%Y%m%d).tar.gz /home/user/documents
```

**What does this do?**

<details>
<summary>Click to see answer</summary>

**Answer:** Creates a compressed tar archive of the documents directory with today's date in the filename.

**Key points:**
- `tar -czf` - create, gzip compress, file
- `$(date +%Y%m%d)` - command substitution, inserts date like 20251210
- Results in filename like `backup-20251210.tar.gz`
- Archives entire `/home/user/documents` directory
- Compressed with gzip

**When you'd use this:** Creating dated backups automatically.
</details>

---

### Exercise 5.2

```bash
tar -xzf archive.tar.gz -C /tmp --strip-components=1
```

**What does this do?**

<details>
<summary>Click to see answer</summary>

**Answer:** Extracts a gzipped tar archive to /tmp, removing the top-level directory from the archive structure.

**Key points:**
- `tar -xzf` - extract, gunzip, file
- `-C /tmp` - extract to /tmp directory
- `--strip-components=1` - removes first directory level from paths
- If archive has `project/src/file.txt`, extracts as `/tmp/src/file.txt`
- Useful when archive has unnecessary wrapper directory

**When you'd use this:** Extracting archives that have an extra top-level directory you don't want.
</details>

---

### Exercise 5.3

```bash
find /var/log -name "*.log" -mtime +7 -exec gzip {} \;
```

**What does this do?**

<details>
<summary>Click to see answer</summary>

**Answer:** Compresses all log files older than 7 days in /var/log.

**Key points:**
- `find /var/log -name "*.log"` - finds all .log files
- `-mtime +7` - modified more than 7 days ago
- `-exec gzip {} \;` - compresses each found file
- Original files are replaced with .gz versions
- Saves disk space on old logs

**When you'd use this:** Log rotation and compression to save disk space.
</details>

---

## Exercise Set 6: Package Management

### Exercise 6.1 (Debian/Ubuntu)

```bash
dpkg -l | grep "^ii" | awk '{print $2}' > installed-packages.txt
```

**What does this do?**

<details>
<summary>Click to see answer</summary>

**Answer:** Creates a list of all installed package names and saves it to a file.

**Key points:**
- `dpkg -l` - lists all packages
- `grep "^ii"` - filters for installed packages (status "ii")
- `awk '{print $2}'` - extracts package name (second column)
- `> installed-packages.txt` - saves to file
- Useful for documenting or replicating system setup

**When you'd use this:** Creating a backup list of installed packages before system changes.
</details>

---

### Exercise 6.2 (Debian/Ubuntu)

```bash
apt-cache search web server | grep -i apache
```

**What does this do?**

<details>
<summary>Click to see answer</summary>

**Answer:** Searches for packages related to "web server" and filters results for those mentioning Apache (case-insensitive).

**Key points:**
- `apt-cache search` - searches package descriptions
- `web server` - search terms
- `grep -i apache` - case-insensitive filter for "apache"
- Doesn't require root privileges
- Shows available packages, not just installed ones

**When you'd use this:** Finding Apache-related packages before installation.
</details>

---

### Exercise 6.3 (Red Hat/CentOS)

```bash
rpm -qa --last | head -20
```

**What does this do?**

<details>
<summary>Click to see answer</summary>

**Answer:** Shows the 20 most recently installed packages.

**Key points:**
- `rpm -qa` - query all installed packages
- `--last` - sorts by installation date (newest first)
- `head -20` - shows first 20 lines
- Useful for troubleshooting recent changes

**When you'd use this:** Investigating what was recently installed after a problem appeared.
</details>

---

## Exercise Set 7: System Information & Monitoring

### Exercise 7.1

```bash
df -h | grep -v "tmpfs" | awk '$5+0 > 80 {print $0}'
```

**What does this do?**

<details>
<summary>Click to see answer</summary>

**Answer:** Shows filesystems that are more than 80% full, excluding temporary filesystems.

**Key points:**
- `df -h` - disk free space in human-readable format
- `grep -v "tmpfs"` - excludes tmpfs (temporary) filesystems
- `awk '$5+0 > 80'` - checks if 5th column (usage %) is greater than 80
- `$5+0` converts "85%" to number 85
- `{print $0}` prints entire line
- Useful for monitoring disk space

**When you'd use this:** Checking for filesystems that are running out of space.
</details>

---

### Exercise 7.2

```bash
du -sh /var/* 2>/dev/null | sort -h | tail -5
```

**What does this do?**

<details>
<summary>Click to see answer</summary>

**Answer:** Shows the 5 largest directories in /var.

**Key points:**
- `du -sh /var/*` - summary size of each item in /var
- `2>/dev/null` - suppresses permission denied errors
- `sort -h` - sorts by human-readable sizes (understands K, M, G)
- `tail -5` - shows last 5 lines (largest)
- Helps identify what's using disk space

**When you'd use this:** Finding which directories are consuming the most space.
</details>

---

### Exercise 7.3

```bash
ps aux --sort=-%mem | head -10
```

**What does this do?**

<details>
<summary>Click to see answer</summary>

**Answer:** Shows the top 10 processes using the most memory.

**Key points:**
- `ps aux` - all processes with details
- `--sort=-%mem` - sorts by memory usage, descending (- means reverse)
- `head -10` - shows first 10 lines
- Useful for identifying memory hogs

**When you'd use this:** Troubleshooting high memory usage.
</details>

---

### Exercise 7.4

```bash
free -h | grep "Mem:" | awk '{print "Used: "$3" / Total: "$2}'
```

**What does this do?**

<details>
<summary>Click to see answer</summary>

**Answer:** Shows memory usage in a simple "Used: X / Total: Y" format.

**Key points:**
- `free -h` - memory usage in human-readable format
- `grep "Mem:"` - extracts memory line (not swap)
- `awk '{print "Used: "$3" / Total: "$2}'` - formats output
- `$2` is total memory, `$3` is used memory
- Creates readable summary

**When you'd use this:** Quick memory status check in scripts or monitoring.
</details>

---

## Exercise Set 8: Networking

### Exercise 8.1

```bash
netstat -tuln | grep ":80 "
```

**What does this do?**

<details>
<summary>Click to see answer</summary>

**Answer:** Checks if anything is listening on port 80 (HTTP).

**Key points:**
- `netstat -tuln` - shows TCP/UDP listening ports, numeric
- `-t` = TCP, `-u` = UDP, `-l` = listening, `-n` = numeric (don't resolve names)
- `grep ":80 "` - filters for port 80 (space prevents matching 8080, 800, etc.)
- Shows if web server is running

**When you'd use this:** Verifying if a web server is listening on the HTTP port.
</details>

---

### Exercise 8.2

```bash
ss -s
```

**What does this do?**

<details>
<summary>Click to see answer</summary>

**Answer:** Shows summary statistics of all socket connections.

**Key points:**
- `ss` - socket statistics (modern replacement for netstat)
- `-s` - summary statistics
- Shows total TCP, UDP, and other socket counts
- Much faster than netstat
- Gives overview of network activity

**When you'd use this:** Quick overview of network connection statistics.
</details>

---

### Exercise 8.3

```bash
ping -c 4 -W 2 8.8.8.8 > /dev/null 2>&1 && echo "Online" || echo "Offline"
```

**What does this do?**

<details>
<summary>Click to see answer</summary>

**Answer:** Tests internet connectivity and prints "Online" or "Offline".

**Key points:**
- `ping -c 4` - send 4 packets
- `-W 2` - wait 2 seconds for response
- `8.8.8.8` - Google's DNS (reliable test target)
- `> /dev/null 2>&1` - suppresses all output
- `&&` - if ping succeeds, run next command
- `||` - if ping fails, run this command instead
- Simple connectivity test

**When you'd use this:** Scripts that need to check internet connectivity.
</details>

---

## Exercise Set 9: Redirection & Pipes

### Exercise 9.1

```bash
command 2>&1 | tee output.log
```

**What does this do?**

<details>
<summary>Click to see answer</summary>

**Answer:** Runs a command, showing output on screen AND saving it to a file, including error messages.

**Key points:**
- `2>&1` - redirects stderr (2) to stdout (1)
- `|` - pipes combined output
- `tee output.log` - writes to file AND displays on screen
- Both stdout and stderr are captured
- You see output in real-time and have a log

**When you'd use this:** Running commands where you want to see output immediately but also keep a log.
</details>

---

### Exercise 9.2

```bash
cat << EOF > /tmp/config.txt
server=localhost
port=8080
EOF
```

**What does this do?**

<details>
<summary>Click to see answer</summary>

**Answer:** Creates a file with multiple lines of content using a here document.

**Key points:**
- `<< EOF` - here document (reads until EOF marker)
- `> /tmp/config.txt` - redirects to file
- Everything between the EOF markers becomes file content
- Useful in scripts for creating config files
- No need for multiple echo commands

**When you'd use this:** Creating configuration files in shell scripts.
</details>

---

### Exercise 9.3

```bash
ls -la /nonexistent 2>&1 | grep "cannot access"
```

**What does this do?**

<details>
<summary>Click to see answer</summary>

**Answer:** Tries to list a nonexistent directory and searches the error message for "cannot access".

**Key points:**
- `ls -la /nonexistent` - will produce an error
- `2>&1` - redirects stderr to stdout so it can be piped
- `| grep "cannot access"` - searches error message
- Without `2>&1`, grep wouldn't see the error (errors go to stderr, not stdout)
- Demonstrates error handling in pipes

**When you'd use this:** Scripts that need to check for specific error conditions.
</details>

---

## Exercise Set 10: Shell Scripting

### Exercise 10.1

```bash
#!/bin/bash
if [ -f "$1" ]; then
    echo "File exists"
else
    echo "File not found"
fi
```

**What does this do?**

<details>
<summary>Click to see answer</summary>

**Answer:** Checks if the first command-line argument is an existing regular file.

**Key points:**
- `$1` - first positional parameter (command-line argument)
- `[ -f "$1" ]` - tests if it's a regular file
- Quotes around `$1` prevent errors if argument contains spaces
- `-f` specifically tests for regular files (not directories or special files)
- Basic file existence check

**When you'd use this:** Scripts that need to validate file arguments.
</details>

---

### Exercise 10.2

```bash
for file in *.txt; do
    mv "$file" "${file%.txt}.bak"
done
```

**What does this do?**

<details>
<summary>Click to see answer</summary>

**Answer:** Renames all .txt files to .bak files (changes extension).

**Key points:**
- `for file in *.txt` - loops through all .txt files
- `${file%.txt}` - removes .txt from end of filename
- `${file%.txt}.bak` - adds .bak to the trimmed name
- Example: `document.txt` becomes `document.bak`
- Parameter expansion for string manipulation

**When you'd use this:** Batch renaming files with different extensions.
</details>

---

### Exercise 10.3

```bash
#!/bin/bash
count=0
while [ $count -lt 5 ]; do
    echo "Count: $count"
    count=$((count + 1))
done
```

**What does this do?**

<details>
<summary>Click to see answer</summary>

**Answer:** Prints "Count: 0" through "Count: 4" using a while loop.

**Key points:**
- `count=0` - initializes counter
- `while [ $count -lt 5 ]` - continues while count less than 5
- `-lt` means "less than" (numeric comparison)
- `$((count + 1))` - arithmetic expansion (increments count)
- Loop runs 5 times (0, 1, 2, 3, 4)

**When you'd use this:** Scripts that need to repeat actions a specific number of times.
</details>

---

### Exercise 10.4

```bash
#!/bin/bash
result=$(grep "error" /var/log/app.log | wc -l)
if [ $result -gt 10 ]; then
    echo "Too many errors: $result" | mail -s "Alert" admin@example.com
fi
```

**What does this do?**

<details>
<summary>Click to see answer</summary>

**Answer:** Counts errors in a log file and sends an email alert if there are more than 10.

**Key points:**
- `$()` - command substitution (captures command output)
- `grep "error" ... | wc -l` - counts lines with "error"
- `[ $result -gt 10 ]` - checks if greater than 10
- `-gt` means "greater than"
- `mail -s "Alert"` - sends email with subject
- Basic monitoring script pattern

**When you'd use this:** Automated monitoring and alerting in cron jobs.
</details>

---

## Practice Tips

1. **Cover the answers** - Try to figure out what each command does before looking
2. **Focus on patterns** - Notice how similar flags work across different commands
3. **Understand the logic** - Don't just memorize, understand WHY commands are combined
4. **Practice regularly** - Review a few exercises each day
5. **Test yourself** - Can you explain it to someone else?

## Next Steps

- Review the [Syntax Recognition Guide](syntax-to-recognize.md) for detailed explanations
- Practice with real commands in a safe environment (VM or container)
- Create your own recognition exercises from man pages
- Time yourself - can you identify commands quickly?

Remember: **Recognition is faster than recall**. You're building the skill to read and understand Linux commands, which is exactly what you need for the LPIC-1 exam!
