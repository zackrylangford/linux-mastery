# Problem: Finding Files

## What problem does this solve?

You need to locate files or directories on your system based on various criteria like name, size, modification time, or content. This is one of the most common tasks in Linux - whether you're looking for a specific configuration file, finding large files eating up disk space, or searching for files containing certain text.

## When do you encounter this?

**Real-world scenarios:**
- Your disk is full and you need to find large files to delete
- You know a file's name but not where it's located
- You need to find all files modified in the last 24 hours
- You're looking for files containing specific text or code
- You need to find all files with certain permissions or ownership
- You want to locate all files of a certain type (e.g., all .log files)

## Available approaches

### 1. `find` - The Swiss Army Knife
- **Best for:** Complex searches with multiple criteria, finding files by attributes (size, time, permissions)
- **Tradeoffs:** 
  - ✅ Pros: Extremely powerful, can search by almost any attribute, can execute commands on results
  - ❌ Cons: Slower on large directories (searches in real-time), syntax can be complex
- **How to recognize it:** Look for `find` followed by a path, then options like `-name`, `-size`, `-type`, `-mtime`
- **AI prompt template:** 
  ```
  Show me how to find files in [directory] that are [criteria: larger than X, modified in last Y days, named Z, etc.]
  ```

### 2. `locate` - The Speed Demon
- **Best for:** Quick searches by filename when you don't need real-time results
- **Tradeoffs:**
  - ✅ Pros: Extremely fast (uses pre-built database), simple syntax
  - ❌ Cons: Database may be outdated, only searches by name, needs to be installed/updated
- **How to recognize it:** Simple command: `locate filename`
- **AI prompt template:**
  ```
  Show me how to quickly find all files named [pattern] anywhere on my system
  ```

### 3. `grep` - The Content Hunter
- **Best for:** Finding files that contain specific text or patterns
- **Tradeoffs:**
  - ✅ Pros: Searches file contents, supports regex, shows matching lines
  - ❌ Cons: Slower on large directories, primarily for text files
- **How to recognize it:** Look for `grep -r` or `grep -R` (recursive search)
- **AI prompt template:**
  ```
  Show me how to find all files in [directory] that contain the text "[search term]"
  ```

### 4. `du` - The Disk Usage Analyzer
- **Best for:** Finding which files/directories are using the most disk space
- **Tradeoffs:**
  - ✅ Pros: Shows sizes clearly, can sort by size, good for disk cleanup
  - ❌ Cons: Not for finding specific files, focuses on size analysis
- **How to recognize it:** Look for `du -sh` or `du -h` with sorting
- **AI prompt template:**
  ```
  Show me how to find the largest files/directories in [path] to free up disk space
  ```

## Decision tree

**Choose your approach:**
1. If you need to find files by **content** → Use `grep -r`
2. If you need to find files by **name only** and want **speed** → Use `locate`
3. If you need to find files by **size, time, permissions, or complex criteria** → Use `find`
4. If you need to find **what's using disk space** → Use `du`
5. If `locate` doesn't find recent files → Update database with `sudo updatedb` or use `find`

## Examples to recognize

### Example 1: Finding large files
```bash
find /home -type f -size +100M
```

**What's happening here:**
- `find /home` - Search starting from /home directory
- `-type f` - Only find files (not directories)
- `-size +100M` - Larger than 100 megabytes
- This helps you identify files eating up disk space
- Output: Full paths to files over 100MB

### Example 2: Finding recently modified files
```bash
find . -type f -mtime -7
```

**What's happening here:**
- `find .` - Search in current directory and subdirectories
- `-type f` - Files only
- `-mtime -7` - Modified in the last 7 days (the minus means "less than")
- Useful for finding what changed recently
- Output: Paths to files modified in the past week

### Example 3: Finding files by name pattern
```bash
find /var/log -name "*.log" -mtime +30
```

**What's happening here:**
- `find /var/log` - Search in log directory
- `-name "*.log"` - Files ending in .log
- `-mtime +30` - Modified more than 30 days ago (plus means "more than")
- Great for finding old log files to clean up
- Output: Old log files you might want to archive or delete

### Example 4: Quick filename search with locate
```bash
locate nginx.conf
```

**What's happening here:**
- `locate` searches a pre-built database (very fast)
- Finds any file with "nginx.conf" in the path
- Much faster than `find` but may not show very recent files
- Output: All paths containing "nginx.conf"

### Example 5: Finding files containing text
```bash
grep -r "error" /var/log --include="*.log"
```

**What's happening here:**
- `grep -r` - Recursive search through directories
- `"error"` - The text to search for
- `/var/log` - Where to search
- `--include="*.log"` - Only search .log files
- Perfect for finding which log files contain errors
- Output: Lines containing "error" with filenames

### Example 6: Finding largest directories
```bash
du -sh /home/* | sort -h | tail -10
```

**What's happening here:**
- `du -sh /home/*` - Show size of each item in /home
  - `-s` means summary (don't show subdirectories)
  - `-h` means human-readable (KB, MB, GB)
- `sort -h` - Sort by human-readable sizes
- `tail -10` - Show last 10 (the largest)
- Essential for disk cleanup
- Output: Top 10 largest items in /home

### Example 7: Finding and deleting old files
```bash
find /tmp -type f -mtime +7 -delete
```

**What's happening here:**
- `find /tmp` - Search temp directory
- `-type f` - Files only
- `-mtime +7` - Older than 7 days
- `-delete` - Delete them (be careful with this!)
- Common for cleanup scripts
- **Warning:** Always test without `-delete` first!

### Example 8: Finding files by permissions
```bash
find /var/www -type f -perm 0777
```

**What's happening here:**
- `find /var/www` - Search web directory
- `-type f` - Files only
- `-perm 0777` - Files with full permissions (security risk!)
- Important for security audits
- Output: Files that might be security vulnerabilities

## Try with AI

**New to AI collaboration?** Check out the [AI Prompting Guide](../../references/ai-prompting-guide.md) for detailed tips on working effectively with AI.

### How to Use AI for This Problem

**Step 1: Understand what you need**
Before asking AI, be clear about:
- What are you looking for? (files by name, size, content, time?)
- Where should it search? (specific directory or entire system?)
- What should the output look like? (just paths, or with details?)

**Step 2: Use a good prompt template**

Choose based on your need:

```
Finding by name:
"Show me how to find all [file type] files in [directory] that match [pattern]"

Finding by size:
"Show me how to find files in [directory] larger than [size] and list them with their sizes"

Finding by content:
"Show me how to search all [file types] in [directory] for lines containing [text]"

Finding by time:
"Show me how to find files in [directory] modified in the last [time period]"

Disk usage:
"Show me the largest [N] files/directories in [path] to help free up space"
```

**Step 3: Verify the AI's solution**

Before running the command, check:
- [ ] Does it search the right location?
- [ ] Are the search criteria correct (size, time, name)?
- [ ] Will it modify or delete anything? (look for `-delete`, `rm`, etc.)
- [ ] Can you test it safely first? (add `-maxdepth 1` to limit scope)

**Step 4: Test safely**

```bash
# If AI gives you something with -delete, test without it first:
find /tmp -name "*.tmp" -mtime +7        # Test: just list files
find /tmp -name "*.tmp" -mtime +7 -delete  # Then delete if list looks right

# If searching large areas, test on smaller scope first:
find . -maxdepth 1 -size +100M           # Test: current directory only
find . -size +100M                        # Then search recursively
```

**Step 5: Understand the result**

Ask AI to explain if you don't understand:
- "Can you explain what each part of this command does?"
- "Why did you use -type f instead of just searching?"
- "What does the + in +100M mean?"

### Practice Exercises with AI

**Exercise 1: Find large files**
- **Prompt**: "Show me how to find all files in my home directory larger than 50MB and display them sorted by size"
- **Verify**: Check that it uses `find`, has correct size syntax, includes sorting
- **Test**: Try with `-maxdepth 2` first to limit scope
- **Document**: Save the working command in `my-knowledge/good-prompts.md`

**Exercise 2: Find recent files**
- **Prompt**: "Show me how to find all .txt files in ~/documents modified in the last 3 days"
- **Verify**: Check for correct path, file extension, and time criteria
- **Test**: Run it and check if the results make sense
- **Document**: Note when you'd use this (finding recent work)

**Exercise 3: Find disk space hogs**
- **Prompt**: "Show me how to find the top 10 largest directories in /home to free up disk space"
- **Verify**: Check that it uses `du`, sorts by size, limits to 10 results
- **Test**: Run it and see if the output is readable
- **Document**: Save this for future disk cleanup

**Exercise 4: Find by content**
- **Prompt**: "Show me how to find all .log files in /var/log that contain the word 'error' and show the filename and line number"
- **Verify**: Check for `grep -r`, correct path, and output format
- **Test**: Try on a smaller directory first if /var/log is large
- **Document**: Note this pattern for log analysis

### Common AI Collaboration Patterns

**Pattern 1: Refining the search**
```
You: "Show me how to find large files"
AI: [gives generic answer]
You: "Show me files larger than 500MB in /home, modified in the last month, sorted by size"
AI: [gives specific answer]
```

**Pattern 2: Making it safer**
```
You: "Show me how to find and delete old temp files"
AI: [gives command with -delete]
You: "Show me the same command but just list the files first without deleting"
AI: [gives safer version]
```

**Pattern 3: Understanding the output**
```
You: [runs command, gets confusing output]
You: "I ran this command and got [output]. What does this mean?"
AI: [explains the output]
```

### Verification Checklist

After getting a solution from AI:
- [ ] I understand what problem this solves
- [ ] I can explain what each part of the command does
- [ ] I've tested it safely (limited scope or dry-run)
- [ ] The results match what I expected
- [ ] I know when to use this approach vs alternatives
- [ ] I've documented the working solution

### Next Steps

1. Pick one exercise above and try it with AI
2. Verify and test the solution safely
3. Document what worked in `my-knowledge/problems-i-solve.md`
4. Try a variation to deepen your understanding

**Remember**: The goal isn't to memorize the syntax, it's to understand what's possible and how to direct AI to generate the right solution for your specific need.

## Related problems

- [Managing disk space](../system-monitoring/) - Once you find large files, you need to manage them
- [File permissions](../permissions/) - Finding files with specific permissions
- [Text processing](../text-processing/) - Processing the files you find

## What to memorize vs look up

**Memorize (high-value knowledge):**
- `find` is for complex searches by attributes
- `locate` is for fast name-only searches
- `grep -r` is for searching file contents
- `du` is for analyzing disk usage
- The concept: different tools for different search criteria

**Look up as needed (low-value to memorize):**
- Specific `find` flags like `-mtime`, `-size`, `-perm`
- Exact syntax for size units (M, G, K)
- Complex `find` expressions with `-and`, `-or`
- All the `du` and `grep` options

## For certification prep

**LPIC-1 / CompTIA Linux+ relevant syntax to recognize:**
- `find / -name "filename"` - Find by name from root
- `find . -type f -size +10M` - Find files by size
- `find . -mtime -7` - Find by modification time
- `locate filename` - Quick database search
- `grep -r "pattern" /path` - Recursive content search
- `du -sh *` - Show directory sizes
- `updatedb` - Update locate database

*Note: You don't need to memorize these, but you should be able to recognize what they do when you see them on an exam.*
