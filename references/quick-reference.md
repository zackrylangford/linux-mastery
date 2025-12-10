# Quick Reference Guide

This is your fast-lookup guide organized by **problems you want to solve**, not alphabetically by command. When you face a problem, find it here and get the solution quickly.

## How to use this guide

1. **Find your problem** in the table of contents
2. **Look up the solution** - we show the most common approach
3. **Memorize vs Look Up** - we mark what's worth remembering
4. **AI Prompt** - use these templates to get AI help

---

## Table of Contents

- [Finding Files](#finding-files)
- [Managing Processes](#managing-processes)
- [Text Processing](#text-processing)
- [Navigating Filesystem](#navigating-filesystem)
- [Managing Directories](#managing-directories)
- [Understanding Paths](#understanding-paths)

---

## Finding Files

### Common Scenarios

| Problem | Solution | When to Use |
|---------|----------|-------------|
| Find files by name | `find /path -name "filename"` | You know the name but not location |
| Find large files | `find /path -type f -size +100M` | Disk is full, need to clean up |
| Find recently modified files | `find /path -mtime -7` | See what changed in last 7 days |
| Find files containing text | `grep -r "text" /path` | Search file contents |
| Find what's using disk space | `du -sh * \| sort -h` | Identify space hogs |
| Quick filename search | `locate filename` | Fast search by name only |

### Recognition Patterns

**If you see this** → **It's doing this**
- `find ... -name` → Searching by filename
- `find ... -size` → Searching by file size
- `find ... -mtime` → Searching by modification time
- `grep -r` → Searching file contents recursively
- `du -sh` → Showing directory sizes
- `locate` → Fast database search

### AI Prompt Templates

```
Show me how to find files in [directory] that are [larger than X / modified in last Y days / named Z]
```

```
Show me how to find all files containing the text "[search term]" in [directory]
```

```
Show me the largest files/directories in [path] to free up disk space
```

### Memorize (High Value)

✅ **DO memorize:**
- `find` is for complex searches by attributes
- `locate` is for fast name-only searches
- `grep -r` is for searching file contents
- `du` is for analyzing disk usage
- Different tools for different search criteria

❌ **DON'T memorize:**
- Specific `find` flags like `-mtime`, `-size`, `-perm`
- Exact syntax for size units (M, G, K)
- Complex `find` expressions
- All the `du` and `grep` options

---

## Managing Processes

### Common Scenarios

| Problem | Solution | When to Use |
|---------|----------|-------------|
| See all running processes | `ps aux` | Get snapshot of what's running |
| Monitor processes in real-time | `top` or `htop` | See what's using CPU/memory now |
| Find a specific process | `ps aux \| grep name` or `pgrep name` | Locate a running program |
| Stop a process | `kill PID` | Terminate a process normally |
| Force stop frozen process | `kill -9 PID` | When normal kill doesn't work |
| Stop all processes by name | `killall name` | Kill multiple instances at once |
| Run with low priority | `nice -n 19 command` | Background task shouldn't slow system |
| Find process ID | `pgrep name` or `pidof name` | Get PID for scripting |

### Recognition Patterns

**If you see this** → **It's doing this**
- `ps aux` → Listing all processes
- `top` or `htop` → Real-time process monitoring
- `kill PID` → Terminating process (polite)
- `kill -9 PID` → Force killing process
- `killall name` → Killing all processes with that name
- `nice -n` → Running with adjusted priority
- `pgrep` → Finding process ID by name

### AI Prompt Templates

```
Show me how to see all running processes and find the one running [program name]
```

```
Show me how to monitor which processes are using the most [CPU/memory]
```

```
Show me how to stop a process called [program name] that's not responding
```

```
Show me how to run [command] with low priority so it doesn't slow down my system
```

### Memorize (High Value)

✅ **DO memorize:**
- `ps aux` shows all processes
- `top` for real-time monitoring
- `kill PID` to stop a process
- `kill -9 PID` to force stop
- Every running program is a process with a PID
- Processes can be politely asked to quit (SIGTERM) or force killed (SIGKILL)

❌ **DON'T memorize:**
- All the `ps` flag combinations
- Different signal numbers for `kill`
- Exact niceness value ranges
- Specific `top` keyboard shortcuts
- Complex `ps` output formatting

---

## Text Processing

### Common Scenarios

| Problem | Solution | When to Use |
|---------|----------|-------------|
| Find lines matching pattern | `grep "pattern" file` | Search for text in files |
| Case-insensitive search | `grep -i "pattern" file` | When case doesn't matter |
| Count matches | `grep -c "pattern" file` | How many times does it appear? |
| Find and replace | `sed 's/old/new/g' file` | Replace text |
| Extract first column | `cut -d',' -f1 file.csv` | Get one column from CSV |
| Extract multiple columns | `awk -F',' '{print $1, $3}' file` | Get specific columns |
| Sort lines | `sort file` | Alphabetical sorting |
| Remove duplicates | `sort file \| uniq` | Get unique lines only |
| Count occurrences | `sort file \| uniq -c \| sort -rn` | Frequency analysis |
| Sum numbers | `awk '{sum += $1} END {print sum}' file` | Calculate totals |

### Recognition Patterns

**If you see this** → **It's doing this**
- `grep "pattern"` → Searching for text
- `grep -v` → Excluding matches (inverse)
- `sed 's/old/new/'` → Find and replace
- `sed '/pattern/d'` → Deleting lines
- `awk '{print $N}'` → Extracting column N
- `cut -d'X' -fN` → Extracting field N with delimiter X
- `sort` → Sorting lines
- `uniq` → Removing adjacent duplicates
- `| uniq -c` → Counting occurrences

### AI Prompt Templates

```
Show me how to find all lines in [file] that contain [pattern]
```

```
Show me how to replace all occurrences of [old text] with [new text] in [file]
```

```
Show me how to extract column [N] from [file] that's delimited by [character]
```

```
Show me how to count how many times each line appears in [file]
```

### Memorize (High Value)

✅ **DO memorize:**
- `grep` for searching/filtering
- `sed` for find and replace
- `awk` for column-based data
- `cut` for simple column extraction
- `sort` for sorting
- `uniq` for removing duplicates (after sort)
- Pipes (`|`) chain commands together
- Each tool does one thing well

❌ **DON'T memorize:**
- Specific `grep` flags like `-E`, `-o`, `-v`
- `sed` substitution syntax details
- `awk` programming syntax
- Complex regex patterns
- All the `sort` options
- Exact `cut` delimiter syntax

---

## Navigating Filesystem

### Common Scenarios

| Problem | Solution | When to Use |
|---------|----------|-------------|
| See current directory | `pwd` | Where am I? |
| Change directory | `cd /path/to/dir` | Move to another location |
| Go to home directory | `cd` or `cd ~` | Return home |
| Go up one level | `cd ..` | Move to parent directory |
| Go to previous directory | `cd -` | Toggle between two locations |
| List files | `ls` | See what's here |
| List with details | `ls -la` | See permissions, sizes, hidden files |
| List by modification time | `ls -lt` | See newest files first |

### Recognition Patterns

**If you see this** → **It's doing this**
- `pwd` → Printing working directory
- `cd /path` → Changing to absolute path
- `cd ../..` → Going up two levels
- `cd ~` → Going to home directory
- `cd -` → Going to previous directory
- `ls -l` → Long listing with details
- `ls -a` → Showing hidden files (starting with .)
- `ls -h` → Human-readable sizes

### AI Prompt Templates

```
Show me how to navigate to [directory path]
```

```
Show me how to list all files in [directory] including hidden ones
```

```
Show me how to see the full path of my current directory
```

### Memorize (High Value)

✅ **DO memorize:**
- `pwd` shows where you are
- `cd` changes directory
- `ls` lists files
- `..` means parent directory
- `~` means home directory
- `.` means current directory
- `/` at start means absolute path from root

❌ **DON'T memorize:**
- All the `ls` flags
- Complex path combinations
- Specific directory structures

---

## Managing Directories

### Common Scenarios

| Problem | Solution | When to Use |
|---------|----------|-------------|
| Create directory | `mkdir dirname` | Make a new folder |
| Create nested directories | `mkdir -p path/to/nested/dir` | Create parent directories too |
| Remove empty directory | `rmdir dirname` | Delete empty folder |
| Remove directory with contents | `rm -r dirname` | Delete folder and everything in it |
| Copy directory | `cp -r source dest` | Duplicate a folder |
| Move/rename directory | `mv oldname newname` | Rename or relocate folder |
| See directory size | `du -sh dirname` | How much space does it use? |

### Recognition Patterns

**If you see this** → **It's doing this**
- `mkdir` → Creating directory
- `mkdir -p` → Creating nested directories (parents too)
- `rmdir` → Removing empty directory
- `rm -r` → Removing directory recursively
- `cp -r` → Copying directory recursively
- `mv` → Moving or renaming
- `du -sh` → Showing directory size

### AI Prompt Templates

```
Show me how to create a directory at [path]
```

```
Show me how to delete a directory and all its contents at [path]
```

```
Show me how to copy directory [source] to [destination]
```

### Memorize (High Value)

✅ **DO memorize:**
- `mkdir` creates directories
- `mkdir -p` creates parent directories
- `rm -r` removes directories recursively
- `cp -r` copies directories recursively
- `-r` means recursive (include contents)
- Be careful with `rm -r` - it's permanent!

❌ **DON'T memorize:**
- All the `mkdir` options
- Complex `rm` flag combinations
- All `cp` and `mv` options

---

## Understanding Paths

### Common Scenarios

| Problem | Solution | When to Use |
|---------|----------|-------------|
| Use absolute path | `/home/user/file.txt` | Specify exact location from root |
| Use relative path | `../other/file.txt` | Specify location relative to current |
| Reference home directory | `~/Documents` | Path in your home directory |
| Reference current directory | `./script.sh` | File in current location |
| Reference parent directory | `../file.txt` | File one level up |

### Recognition Patterns

**If you see this** → **It's doing this**
- `/` at start → Absolute path from root
- `./` at start → Relative to current directory
- `../` at start → Relative to parent directory
- `~/` at start → Relative to home directory
- No `/` at start → Relative to current directory

### AI Prompt Templates

```
Show me the difference between absolute and relative paths
```

```
Show me how to reference a file in [location] from [current location]
```

### Memorize (High Value)

✅ **DO memorize:**
- `/` at start = absolute path
- `./` = current directory
- `../` = parent directory
- `~/` = home directory
- Absolute paths work from anywhere
- Relative paths depend on current location

❌ **DON'T memorize:**
- Specific system directory paths
- Complex relative path combinations

---

## Quick Command Cheat Sheet

### Most Common Commands by Problem

**Finding Things:**
- `find` - Search for files by attributes
- `grep` - Search for text patterns
- `locate` - Fast filename search

**Managing Processes:**
- `ps aux` - List all processes
- `top` - Monitor processes
- `kill` - Stop processes

**Text Processing:**
- `grep` - Search text
- `sed` - Find and replace
- `awk` - Process columns
- `sort` - Sort lines
- `uniq` - Remove duplicates

**Files & Directories:**
- `ls` - List files
- `cd` - Change directory
- `pwd` - Show current directory
- `mkdir` - Create directory
- `rm` - Remove files/directories
- `cp` - Copy
- `mv` - Move/rename

### Common Patterns to Recognize

**Pipes** (`|`) - Chain commands together:
```bash
command1 | command2 | command3
```
Output of command1 goes into command2, then into command3

**Redirection** (`>`, `>>`) - Save output to file:
```bash
command > file.txt    # Overwrite file
command >> file.txt   # Append to file
```

**Wildcards** (`*`, `?`) - Match multiple files:
```bash
*.txt     # All files ending in .txt
file?.txt # file1.txt, file2.txt, etc.
```

**Command Substitution** (`$(...)`) - Use command output:
```bash
kill $(pgrep firefox)  # Kill process by name
```

---

## For Certification Prep

### Must Recognize (Not Memorize)

These are common on LPIC-1 and CompTIA Linux+ exams. You should be able to **recognize what they do**, not necessarily write them from memory:

**File Operations:**
- `ls -la`, `cd`, `pwd`, `mkdir -p`, `rm -rf`, `cp -r`, `mv`

**Finding:**
- `find / -name "file"`, `find . -type f -size +10M`, `locate`, `updatedb`

**Text Processing:**
- `grep -i`, `grep -r`, `sed 's/old/new/g'`, `awk '{print $1}'`, `cut -d':' -f1`
- `sort`, `sort -n`, `uniq`, `uniq -c`, `wc -l`

**Processes:**
- `ps aux`, `ps -ef`, `top`, `kill`, `kill -9`, `killall`, `pkill`, `nice`, `renice`

**Pipes & Redirection:**
- `|`, `>`, `>>`, `2>`, `&>`

### Study Strategy

1. **Don't memorize syntax** - Focus on recognizing what commands do
2. **Practice reading code** - Look at examples and explain what they do
3. **Use this guide** - Quick lookup when you forget
4. **Ask AI for help** - Use the prompt templates above
5. **Document what you learn** - Keep your own notes in `my-knowledge/`

---

## Tips for Using This Guide

1. **Bookmark common problems** - Mark the sections you use most
2. **Try before looking up** - Think about what you need, then verify here
3. **Use AI prompts** - The templates help you get better AI responses
4. **Build your own** - Add your own solutions to `my-knowledge/problems-i-solve.md`
5. **Focus on concepts** - Understand the "why" not just the "how"

**Remember:** This is a reference, not a textbook. Use it when you need quick answers, then go back to the problem guides for deeper understanding.
