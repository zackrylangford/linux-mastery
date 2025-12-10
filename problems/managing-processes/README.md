# Problem: Managing Processes

## What problem does this solve?

You need to view, monitor, control, or terminate programs (processes) running on your Linux system. Every program that runs is a process, and sometimes you need to see what's running, stop misbehaving programs, or understand what's consuming system resources.

## When do you encounter this?

**Real-world scenarios:**
- A program is frozen and you need to force it to quit
- Your system is slow and you want to see what's using CPU/memory
- You need to find and stop a specific running program
- A background process needs to be terminated
- You want to monitor system resource usage in real-time
- You need to change a process's priority to make it run faster or slower
- A service is stuck and needs to be restarted

## Available approaches

### 1. `ps` - The Process Snapshot
- **Best for:** Getting a snapshot of running processes, finding specific processes, scripting
- **Tradeoffs:** 
  - ✅ Pros: Fast, scriptable, shows detailed process info, standard on all systems
  - ❌ Cons: Static snapshot (not real-time), syntax can be confusing (BSD vs Unix style)
- **How to recognize it:** Look for `ps aux`, `ps -ef`, or `ps` with various flags
- **AI prompt template:** 
  ```
  Show me how to list all processes and find the one running [program name]
  ```

### 2. `top` / `htop` - The Real-Time Monitor
- **Best for:** Interactive monitoring, seeing what's using resources right now, quick overview
- **Tradeoffs:**
  - ✅ Pros: Real-time updates, interactive, shows CPU/memory usage, can kill processes from within
  - ❌ Cons: Takes over terminal, `htop` not always installed by default
- **How to recognize it:** Commands that launch interactive displays: `top`, `htop`
- **AI prompt template:**
  ```
  Show me how to monitor system processes in real-time and see what's using the most [CPU/memory]
  ```

### 3. `kill` / `killall` / `pkill` - The Process Terminators
- **Best for:** Stopping specific processes, force-quitting frozen programs
- **Tradeoffs:**
  - ✅ Pros: Precise control, can send different signals, works on any process
  - ❌ Cons: Need to know process ID or name, can accidentally kill wrong process
- **How to recognize it:** Look for `kill`, `killall`, or `pkill` followed by process ID or name
- **AI prompt template:**
  ```
  Show me how to stop a process called [program name] that's not responding
  ```

### 4. `nice` / `renice` - The Priority Adjusters
- **Best for:** Controlling how much CPU time a process gets, running low-priority background tasks
- **Tradeoffs:**
  - ✅ Pros: Prevents background tasks from slowing down system, can prioritize important work
  - ❌ Cons: Doesn't affect memory usage, requires understanding of priority values
- **How to recognize it:** Look for `nice -n` when starting programs, or `renice` for running processes
- **AI prompt template:**
  ```
  Show me how to run [command] with low priority so it doesn't slow down my system
  ```

### 5. `pgrep` / `pidof` - The Process Finders
- **Best for:** Finding process IDs by name for use in scripts
- **Tradeoffs:**
  - ✅ Pros: Simple, returns just the PID, perfect for scripting
  - ❌ Cons: Limited information, just finds processes
- **How to recognize it:** Simple commands: `pgrep firefox`, `pidof nginx`
- **AI prompt template:**
  ```
  Show me how to find the process ID of [program name]
  ```

## Decision tree

**Choose your approach:**
1. If you need to **see what's running right now** → Use `top` or `htop` (interactive)
2. If you need to **find a specific process** → Use `ps aux | grep name` or `pgrep name`
3. If you need to **stop a process** → Use `kill PID` or `killall name`
4. If a process **won't stop** → Use `kill -9 PID` (force kill)
5. If you need to **run something with low priority** → Use `nice -n 19 command`
6. If you need **process info for a script** → Use `ps` or `pgrep`

## Examples to recognize

### Example 1: Viewing all processes
```bash
ps aux
```

**What's happening here:**
- `ps` - Process status command
- `aux` - Show all processes (a), user-oriented format (u), including processes without terminals (x)
- This is the most common way to see all running processes
- Output: List of all processes with CPU%, memory%, user, command, etc.
- **Pattern to remember:** `aux` is like "show me everything"

### Example 2: Finding a specific process
```bash
ps aux | grep firefox
```

**What's happening here:**
- `ps aux` - List all processes
- `|` - Pipe the output to next command
- `grep firefox` - Filter for lines containing "firefox"
- Common pattern for finding if a program is running
- Output: Lines showing firefox processes (and the grep command itself)

### Example 3: Real-time monitoring with top
```bash
top
```

**What's happening here:**
- Launches interactive real-time process monitor
- Updates every few seconds
- Shows processes sorted by CPU usage by default
- Press `q` to quit, `M` to sort by memory, `k` to kill a process
- Essential for diagnosing performance issues

### Example 4: Killing a process by ID
```bash
kill 1234
```

**What's happening here:**
- `kill` - Send signal to process
- `1234` - The process ID (PID)
- By default sends SIGTERM (polite "please quit")
- Process has chance to clean up before exiting
- If this doesn't work, you might need `kill -9 1234`

### Example 5: Force killing a frozen process
```bash
kill -9 1234
```

**What's happening here:**
- `kill -9` - Send SIGKILL signal (force quit)
- `1234` - The process ID
- Process is immediately terminated, no cleanup
- Use this when normal `kill` doesn't work
- **Warning:** Process can't save data or clean up

### Example 6: Killing all processes by name
```bash
killall firefox
```

**What's happening here:**
- `killall` - Kill all processes with this name
- `firefox` - The program name
- Stops all firefox processes at once
- Useful when multiple instances are running
- **Warning:** Kills ALL processes with that name

### Example 7: Finding process ID by name
```bash
pgrep nginx
```

**What's happening here:**
- `pgrep` - Process grep (find by name)
- `nginx` - The program to find
- Returns just the process ID(s)
- Perfect for scripts: `kill $(pgrep nginx)`
- Output: Just numbers (PIDs)

### Example 8: Running with low priority
```bash
nice -n 19 ./backup-script.sh
```

**What's happening here:**
- `nice -n 19` - Run with niceness value 19 (lowest priority)
- `./backup-script.sh` - The command to run
- Process will use CPU only when nothing else needs it
- Great for background tasks that shouldn't slow down system
- Range: -20 (highest priority) to 19 (lowest priority)

### Example 9: Changing priority of running process
```bash
renice -n 10 -p 1234
```

**What's happening here:**
- `renice` - Change priority of running process
- `-n 10` - New niceness value
- `-p 1234` - Process ID to change
- Useful when you forgot to use `nice` when starting
- May need sudo for some priority changes

### Example 10: Viewing process tree
```bash
ps auxf
```

**What's happening here:**
- `ps aux` - All processes
- `f` - Forest mode (shows parent-child relationships)
- Displays processes in tree structure
- Helps understand which process started which
- Useful for finding related processes

### Example 11: Monitoring specific user's processes
```bash
top -u username
```

**What's happening here:**
- `top` - Real-time monitor
- `-u username` - Filter to specific user
- Shows only processes owned by that user
- Useful on multi-user systems
- Can also use `ps -u username`

## Try it yourself

**Practice with AI:**
1. Think of a specific version of this problem you want to solve
2. Use one of the AI prompt templates above
3. Ask AI to generate the solution
4. **Before running it:** Try to understand what the AI gave you
5. Run it and verify it works
6. Document what you learned in `my-knowledge/problems-i-solve.md`

**Verification checklist:**
- [ ] Does the solution match what you asked for?
- [ ] Can you explain what each part does?
- [ ] Did you test it safely (won't kill important processes)?
- [ ] Do you understand when to use this approach?

**Safe practice exercises:**
1. Ask AI: "Show me how to see all running processes on my system"
2. Ask AI: "Show me how to monitor which processes are using the most CPU"
3. Ask AI: "Show me how to find the process ID of a program called 'python'"
4. **Don't practice killing processes unless you know what you're doing!**

## Related problems

- [System monitoring](../system-monitoring/) - Broader system resource monitoring
- [Finding files](../finding-files/) - Finding process-related files like logs
- [Networking](../networking/) - Finding processes using network ports

## What to memorize vs look up

**Memorize (high-value knowledge):**
- `ps aux` shows all processes
- `top` for real-time monitoring
- `kill PID` to stop a process
- `kill -9 PID` to force stop
- Concept: every running program is a process with a PID
- Concept: processes can be politely asked to quit (SIGTERM) or force killed (SIGKILL)

**Look up as needed (low-value to memorize):**
- All the `ps` flag combinations
- Different signal numbers for `kill`
- Exact niceness value ranges
- Specific `top` keyboard shortcuts
- Complex `ps` output formatting

## For certification prep

**LPIC-1 / CompTIA Linux+ relevant syntax to recognize:**
- `ps aux` - List all processes
- `ps -ef` - Alternative format for all processes
- `top` - Interactive process viewer
- `kill PID` - Terminate process
- `kill -9 PID` - Force kill process
- `killall name` - Kill by process name
- `pkill name` - Kill by pattern matching
- `pgrep name` - Find process ID by name
- `nice -n value command` - Run with priority
- `renice -n value -p PID` - Change priority
- `jobs` - List background jobs in current shell
- `bg` / `fg` - Background/foreground jobs

*Note: You don't need to memorize these, but you should be able to recognize what they do when you see them on an exam.*
