# Problem: Checking System Resources

## What problem does this solve?

You need to monitor your system's resource usage - CPU, memory, disk space, and I/O performance. This helps you understand if your system is running out of resources, identify performance bottlenecks, find processes consuming too much CPU or memory, and know when you need to free up disk space or upgrade hardware.

## When do you encounter this?

**Real-world scenarios:**
- Your system is running slow and you need to find out why
- You're getting "disk full" errors and need to see what's using space
- An application is using too much memory and you need to identify it
- You need to check if you have enough free memory before starting a task
- You're monitoring server health and need to check resource usage
- A process seems stuck and you need to see if it's actually doing work
- You need to verify if disk I/O is causing performance issues

## Available approaches

### 1. `top` / `htop` - Real-time Process Monitor
- **Best for:** Interactive monitoring of CPU and memory usage by process
- **Tradeoffs:** 
  - ✅ Pros: Real-time updates, shows all processes, interactive (can kill processes), widely available
  - ❌ Cons: Can be overwhelming, htop not always installed by default, requires terminal
- **How to recognize it:** Look for `top` or `htop` commands, often run without arguments
- **AI prompt template:** 
  ```
  Show me how to see which processes are using the most CPU and memory
  ```

### 2. `free` - Memory Usage
- **Best for:** Quick check of available memory and swap usage
- **Tradeoffs:**
  - ✅ Pros: Simple, fast, easy to read with -h flag, shows memory and swap
  - ❌ Cons: Only shows memory, not other resources, snapshot only (not continuous)
- **How to recognize it:** Look for `free -h` or `free -m`
- **AI prompt template:**
  ```
  Show me how to check how much free memory I have
  ```

### 3. `df` - Disk Space Usage
- **Best for:** Checking available disk space on filesystems
- **Tradeoffs:**
  - ✅ Pros: Simple, shows all mounted filesystems, easy to read with -h
  - ❌ Cons: Doesn't show which files/directories use space (use du for that)
- **How to recognize it:** Look for `df -h` or `df -T`
- **AI prompt template:**
  ```
  Show me how to check how much disk space is available
  ```

### 4. `du` - Disk Usage by Directory
- **Best for:** Finding which directories/files are using disk space
- **Tradeoffs:**
  - ✅ Pros: Shows space usage by directory, can sort by size, helps find space hogs
  - ❌ Cons: Can be slow on large directories, doesn't show filesystem totals (use df for that)
- **How to recognize it:** Look for `du -sh` or `du -h` with sorting
- **AI prompt template:**
  ```
  Show me how to find which directories are using the most disk space
  ```

### 5. `iostat` - I/O Statistics
- **Best for:** Monitoring disk I/O performance and identifying I/O bottlenecks
- **Tradeoffs:**
  - ✅ Pros: Shows detailed I/O stats, can monitor over time, identifies slow disks
  - ❌ Cons: Not always installed by default (part of sysstat package), output can be complex
- **How to recognize it:** Look for `iostat` with options like `-x`, `-d`
- **AI prompt template:**
  ```
  Show me how to check if disk I/O is causing performance issues
  ```

### 6. `ps` - Process Status
- **Best for:** Getting detailed information about specific processes
- **Tradeoffs:**
  - ✅ Pros: Very flexible, can filter and format output, shows process details
  - ❌ Cons: Snapshot only (not real-time), complex options, less intuitive than top
- **How to recognize it:** Look for `ps aux` or `ps -ef`
- **AI prompt template:**
  ```
  Show me how to list all running processes with their resource usage
  ```

### 7. `uptime` - System Load Average
- **Best for:** Quick check of system load and how long system has been running
- **Tradeoffs:**
  - ✅ Pros: Very simple, shows load average (system stress), shows uptime
  - ❌ Cons: Limited information, load average can be hard to interpret
- **How to recognize it:** Simple command: `uptime`
- **AI prompt template:**
  ```
  Show me how to check system load and uptime
  ```

## Decision tree

**Choose your approach:**
1. If you need to **see what's using CPU/memory right now** → Use `top` or `htop`
2. If you need to **check available memory** → Use `free -h`
3. If you need to **check available disk space** → Use `df -h`
4. If you need to **find what's using disk space** → Use `du -sh * | sort -h`
5. If you need to **check if disk I/O is slow** → Use `iostat -x 1`
6. If you need to **find a specific process** → Use `ps aux | grep processname`
7. If you need to **quick system health check** → Use `uptime` and `free -h`

## Understanding System Resources

### The Mental Model: Four Key Resources

Every system has four main resources to monitor:
1. **CPU**: Processing power - how busy is the processor?
2. **Memory (RAM)**: Working space - do you have enough free memory?
3. **Disk Space**: Storage capacity - are filesystems full?
4. **Disk I/O**: Storage speed - is disk reading/writing fast enough?

**Performance issues usually come from one of these being maxed out.**

### Understanding Load Average

Load average shows system stress over 1, 5, and 15 minutes:
- **Below CPU count**: System is fine (e.g., 2.0 on 4-core system)
- **Equal to CPU count**: System is fully utilized
- **Above CPU count**: System is overloaded (processes waiting)

Example: `load average: 1.5, 2.0, 1.8` on a 4-core system = healthy

### Understanding Memory

Linux memory can be confusing:
- **Total**: All RAM in system
- **Used**: Memory in use (but includes cache!)
- **Free**: Completely unused memory
- **Available**: Memory available for new applications (includes reclaimable cache)

**Look at "available", not "free"** - Linux uses free memory for cache, which is good!

## Examples to recognize

### Example 1: Checking what's using CPU
```bash
top
```

**What's happening here:**
- `top` - Interactive process viewer
- Shows processes sorted by CPU usage (by default)
- Updates every few seconds
- Press 'q' to quit, 'M' to sort by memory, 'k' to kill a process
- Look at the top processes to see what's using CPU
- Also shows overall CPU, memory, and load average at the top

### Example 2: Better process viewer
```bash
htop
```

**What's happening here:**
- `htop` - Enhanced version of top (more user-friendly)
- Color-coded display, easier to read
- Shows CPU usage per core
- Mouse support, easier navigation
- Press F10 or 'q' to quit
- **Note**: May need to install first: `sudo apt install htop`

### Example 3: Checking free memory
```bash
free -h
```

**What's happening here:**
- `free` - Display memory usage
- `-h` - Human-readable format (GB, MB instead of bytes)
- Shows: total, used, free, shared, buff/cache, available
- **Look at "available"** - that's what matters for new programs
- Also shows swap usage (disk used as extra memory)

### Example 4: Checking disk space
```bash
df -h
```

**What's happening here:**
- `df` - Disk free (filesystem space)
- `-h` - Human-readable sizes
- Shows each filesystem with: size, used, available, use%, mount point
- Look for filesystems near 100% - those need attention
- Common mount points: `/` (root), `/home`, `/var`

### Example 5: Finding large directories
```bash
du -sh /home/* | sort -h | tail -10
```

**What's happening here:**
- `du -sh /home/*` - Disk usage of each item in /home
  - `-s` - Summary (don't show subdirectories)
  - `-h` - Human-readable
- `sort -h` - Sort by human-readable sizes
- `tail -10` - Show last 10 (the largest)
- Helps you find what's eating disk space
- **Warning**: Can be slow on large directories

### Example 6: Monitoring disk I/O
```bash
iostat -x 1
```

**What's happening here:**
- `iostat` - I/O statistics
- `-x` - Extended statistics
- `1` - Update every 1 second
- Shows read/write speeds and utilization per disk
- Look at `%util` column - high values (>80%) indicate I/O bottleneck
- Press Ctrl+C to stop
- **Note**: Part of sysstat package, may need to install

### Example 7: Listing all processes
```bash
ps aux
```

**What's happening here:**
- `ps` - Process status
- `a` - Show processes from all users
- `u` - User-oriented format (shows user, CPU%, MEM%)
- `x` - Include processes without a terminal
- Shows snapshot of all running processes
- Columns: USER, PID, %CPU, %MEM, COMMAND
- Often piped to grep: `ps aux | grep nginx`

### Example 8: Finding memory-hungry processes
```bash
ps aux --sort=-%mem | head -10
```

**What's happening here:**
- `ps aux` - All processes with details
- `--sort=-%mem` - Sort by memory usage (descending)
- `head -10` - Show top 10
- Quickly identifies which processes use most memory
- Useful when system is running out of memory

### Example 9: Checking system load
```bash
uptime
```

**What's happening here:**
- `uptime` - Show how long system has been running
- Also shows: current time, number of users, load average
- Load average shows 1, 5, and 15 minute averages
- Compare to number of CPU cores to assess if system is overloaded
- Very quick health check

### Example 10: Watching disk space in real-time
```bash
watch -n 5 df -h
```

**What's happening here:**
- `watch` - Run command repeatedly
- `-n 5` - Every 5 seconds
- `df -h` - The command to run
- Shows disk space updating every 5 seconds
- Useful for monitoring during large file operations
- Press Ctrl+C to stop

### Example 11: Checking specific filesystem
```bash
df -h /var
```

**What's happening here:**
- `df -h` - Disk free, human-readable
- `/var` - Check only this filesystem
- Shows space for the filesystem containing /var
- Useful when you care about specific location
- `/var` often fills up with logs

### Example 12: Finding processes by name
```bash
ps aux | grep nginx
```

**What's happening here:**
- `ps aux` - All processes
- `grep nginx` - Filter for lines containing "nginx"
- Shows all nginx processes with their resource usage
- Common pattern for checking if a service is running
- **Note**: grep itself will appear in results (can ignore it)

### Example 13: Checking CPU info
```bash
lscpu
```

**What's happening here:**
- `lscpu` - List CPU information
- Shows: number of CPUs, cores per socket, architecture, speed
- Useful for understanding your system's CPU capacity
- Helps interpret load average (compare to CPU count)

### Example 14: Memory usage by process
```bash
top -o %MEM
```

**What's happening here:**
- `top` - Process viewer
- `-o %MEM` - Sort by memory usage
- Shows which processes use most memory
- Alternative to `ps aux --sort=-%mem`
- Updates in real-time

### Example 15: Disk usage of current directory
```bash
du -h --max-depth=1 | sort -h
```

**What's happening here:**
- `du -h` - Disk usage, human-readable
- `--max-depth=1` - Only show immediate subdirectories (don't recurse)
- `sort -h` - Sort by size
- Shows size of each subdirectory in current location
- Helps drill down to find large directories

## Try with AI

**New to AI collaboration?** Check out the [AI Prompting Guide](../../references/ai-prompting-guide.md) for detailed tips on working effectively with AI.

### How to Use AI for This Problem

**Step 1: Understand what you need**
Before asking AI, be clear about:
- What resource are you checking? (CPU, memory, disk, I/O?)
- Do you need real-time monitoring or a snapshot?
- Are you looking for overall usage or specific processes?
- Do you need to find what's using resources or just check availability?

**Step 2: Use a good prompt template**

Choose based on your need:

```
Checking overall resources:
"Show me how to check my system's CPU, memory, and disk usage"

Finding resource hogs:
"Show me how to find which processes are using the most [CPU/memory/disk]"

Checking specific resource:
"Show me how to check how much [memory/disk space] is available"

Monitoring over time:
"Show me how to monitor [resource] usage in real-time"

Finding disk space issues:
"Show me how to find which directories are using the most disk space in [path]"

Checking I/O performance:
"Show me how to check if disk I/O is causing slowness"
```

**Step 3: Verify the AI's solution**

Before running the command, check:
- [ ] Does it monitor the right resource?
- [ ] Will it run continuously? (know how to exit: usually Ctrl+C or 'q')
- [ ] Does it need sudo? (most monitoring commands don't)
- [ ] Is the output format readable? (look for -h flag)

**Step 4: Test and interpret results**

```bash
# For continuous monitoring, know how to exit:
top          # Press 'q' to quit
htop         # Press F10 or 'q'
iostat 1     # Press Ctrl+C

# For disk space, check the percentage:
df -h        # Look at "Use%" column
# Above 90% = need to free space soon
# At 100% = system may have issues

# For memory, look at "available":
free -h      # "available" is what matters, not "free"
```

**Step 5: Understand the result**

Ask AI to explain if you don't understand:
- "What does load average mean?"
- "Why does 'used' memory seem high but system is fine?"
- "What's a normal CPU usage percentage?"
- "How do I interpret iostat output?"

### Practice Exercises with AI

**Exercise 1: System health check**
- **Prompt**: "Show me how to quickly check my system's overall health - CPU, memory, and disk space"
- **Verify**: Check for commands like `uptime`, `free -h`, `df -h`
- **Test**: Run them and understand what "healthy" looks like
- **Document**: Save this as your go-to health check

**Exercise 2: Find memory hog**
- **Prompt**: "Show me how to find which process is using the most memory on my system"
- **Verify**: Check for `top`, `htop`, or `ps` with memory sorting
- **Test**: Run it and identify the top memory user
- **Document**: Note this for troubleshooting slow systems

**Exercise 3: Find disk space hogs**
- **Prompt**: "Show me how to find the largest directories in /home to free up disk space"
- **Verify**: Check for `du` with sorting
- **Test**: Run it and see what's using space
- **Document**: Save for disk cleanup tasks

**Exercise 4: Monitor CPU usage**
- **Prompt**: "Show me how to monitor CPU usage in real-time and identify which processes are using the most CPU"
- **Verify**: Check for `top` or `htop`
- **Test**: Run it, understand the display, practice exiting
- **Document**: Note when to use this

### Common AI Collaboration Patterns

**Pattern 1: Diagnosing slowness**
```
You: "My system is running slow"
AI: [suggests checking CPU and memory with top]
You: "CPU is at 5%, memory shows 90% used. Is that bad?"
AI: [explains to check 'available' memory, not 'used']
You: "Available shows 8GB. What else could cause slowness?"
AI: [suggests checking disk I/O with iostat]
```

**Pattern 2: Disk full troubleshooting**
```
You: "I'm getting disk full errors"
AI: [suggests df -h to check which filesystem is full]
You: "/home is at 98%. How do I find what's using space?"
AI: [provides du command to find large directories]
You: "Found a 50GB directory. How do I see what's in it?"
AI: [provides du command for that specific directory]
```

**Pattern 3: Understanding output**
```
You: [runs free -h, sees confusing output]
You: "I ran free -h and it shows 15GB used but only 2GB free. Do I need more RAM?"
AI: [explains Linux memory caching and to look at 'available']
You: "Available shows 10GB. So I'm actually fine?"
AI: [confirms and explains why]
```

### Verification Checklist

After getting a solution from AI:
- [ ] I understand what resource is being monitored
- [ ] I know how to read the output
- [ ] I know what values indicate problems
- [ ] I know how to exit if it's a continuous monitor
- [ ] I can explain when to use this tool

### Next Steps

1. Pick one exercise above and try it with AI
2. Run the command and understand the output
3. Check your system regularly to learn what's "normal"
4. Document useful commands in `my-knowledge/problems-i-solve.md`

**Remember**: Regular monitoring helps you understand what's normal for your system. Then when something is slow, you'll quickly spot what's different.

## Related problems

- [Managing processes](../managing-processes/) - Killing processes that use too much resources
- [Finding files](../finding-files/) - Finding large files to free disk space
- [Networking](../networking/) - Network usage is also a system resource

## What to memorize vs look up

**Memorize (high-value knowledge):**
- `top` or `htop` for CPU/memory monitoring
- `free -h` for memory check
- `df -h` for disk space check
- `du -sh` for directory sizes
- The concept: four key resources (CPU, memory, disk space, disk I/O)
- Look at "available" memory, not "free"
- Load average should be compared to CPU count

**Look up as needed (low-value to memorize):**
- Specific flags for ps command
- iostat output interpretation
- Advanced top commands and shortcuts
- Exact du options for different use cases
- All the different ways to format ps output

## For certification prep

**LPIC-1 / CompTIA Linux+ relevant syntax to recognize:**
- `top` - Interactive process viewer
- `htop` - Enhanced process viewer
- `ps aux` - List all processes
- `ps -ef` - Alternative process listing format
- `free -h` - Memory usage in human-readable format
- `df -h` - Disk space in human-readable format
- `du -sh directory` - Directory size summary
- `uptime` - System load and uptime
- `iostat` - I/O statistics
- `lscpu` - CPU information

*Note: You don't need to memorize exact syntax, but you should recognize what these commands do and understand how to interpret their output when you see them on an exam.*

## Common Monitoring Patterns

**Pattern 1: Quick health check**
```bash
uptime && free -h && df -h
```
Shows load, memory, and disk space in one command

**Pattern 2: Find top CPU users**
```bash
ps aux --sort=-%cpu | head -10
```
Lists top 10 CPU-consuming processes

**Pattern 3: Find top memory users**
```bash
ps aux --sort=-%mem | head -10
```
Lists top 10 memory-consuming processes

**Pattern 4: Find largest directories**
```bash
du -sh /* 2>/dev/null | sort -h | tail -10
```
Shows 10 largest directories from root (ignoring errors)

**Pattern 5: Monitor specific process**
```bash
watch -n 2 "ps aux | grep processname"
```
Updates every 2 seconds showing specific process

**Pattern 6: Continuous disk space monitoring**
```bash
watch -n 5 df -h
```
Updates disk space every 5 seconds

## Understanding "Normal" Values

**CPU Usage:**
- 0-30%: Light usage, system responsive
- 30-70%: Moderate usage, normal for active work
- 70-90%: Heavy usage, may feel slower
- 90-100%: Maxed out, system will be slow

**Memory:**
- Available > 20% of total: Healthy
- Available 10-20%: Getting tight
- Available < 10%: May need to close programs or add RAM

**Disk Space:**
- < 80% used: Healthy
- 80-90% used: Should clean up soon
- 90-95% used: Clean up now
- > 95% used: Critical, system may have issues

**Load Average (per CPU core):**
- < 0.7: Light load
- 0.7-1.0: Moderate load
- 1.0-1.5: Heavy load
- > 1.5: Overloaded
