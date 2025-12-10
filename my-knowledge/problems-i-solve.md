# Problems I Can Solve

This is your personal reference of Linux problems you've learned to solve. Keep it simple and practical - just add entries as you learn new capabilities.

**How to use this:**
- Add a new entry whenever you learn to solve a problem
- Keep descriptions short and actionable
- Focus on WHAT you can do, not memorizing exact syntax
- Use this to quickly remember "can I solve X with Linux?"

---

## Finding Files

### Find large files taking up disk space
- **Problem**: Need to free up disk space, don't know what's using it
- **Solution**: Use `find` with `-size` flag or `du` to show directory sizes
- **When to use**: Disk is full, need to identify large files to delete
- **AI prompt that works**: "Show me how to find all files larger than [size] in [directory]"
- **Related**: Can combine with `sort` to order by size

### Locate files by name quickly
- **Problem**: Know a filename but not where it is
- **Solution**: Use `locate` for fast searching (uses database) or `find` for real-time search
- **When to use**: Looking for config files, documents, or any file by name
- **AI prompt that works**: "How do I find all files named [pattern] on my system?"
- **Related**: `locate` is faster but needs updated database (`updatedb`)

---

## Managing Processes

### Find what's using CPU/memory
- **Problem**: System is slow, need to identify resource-hungry processes
- **Solution**: Use `top` or `htop` for interactive view, `ps aux` for snapshot
- **When to use**: System performance issues, investigating what's running
- **AI prompt that works**: "Show me how to find processes using the most [CPU/memory]"
- **Related**: Can sort by different columns, filter by user

### Stop a misbehaving process
- **Problem**: Program is frozen or needs to be terminated
- **Solution**: Use `kill` with process ID, or `killall` with process name
- **When to use**: Application not responding, need to force quit
- **AI prompt that works**: "How do I stop a process called [name] or with PID [number]?"
- **Related**: Different signal types (-9 for force kill, -15 for graceful)

---

## Text Processing

### Extract specific columns from text
- **Problem**: Have structured text, need only certain fields
- **Solution**: Use `cut` for simple delimiters, `awk` for complex patterns
- **When to use**: Processing CSV, log files, command output
- **AI prompt that works**: "Extract column [N] from [file] where delimiter is [char]"
- **Related**: Can combine with `grep` to filter rows first

### Search for patterns in files
- **Problem**: Need to find text across multiple files
- **Solution**: Use `grep` with patterns, `-r` for recursive search
- **When to use**: Searching code, logs, configuration files
- **AI prompt that works**: "Search for [pattern] in all [file types] under [directory]"
- **Related**: Can use regex patterns, show context with `-A/-B/-C`

---

## Template for New Entries

### [Short problem description]
- **Problem**: [What situation triggers needing this?]
- **Solution**: [Which tool/approach solves it?]
- **When to use**: [Specific scenarios where this applies]
- **AI prompt that works**: [Prompt template that gets good results]
- **Related**: [Connected problems or alternative approaches]

---

## Tips for Building This

- **Start small**: Add one entry each time you learn something new
- **Be specific**: "Find large files" is better than "file management"
- **Test your prompts**: Only add AI prompts that actually worked for you
- **Link related problems**: Note when solutions connect to each other
- **Update as you learn**: Come back and refine entries with new insights

**Remember**: This isn't about memorizing syntax - it's about knowing what's possible and how to get AI to help you do it!
