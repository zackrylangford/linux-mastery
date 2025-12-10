# Quick Reference

Fast answers organized by problem type. Use this when you need a quick reminder.

---

## Finding Files

### Common Scenarios
- **Find files by name**: `find` command with `-name` flag
- **Find files by size**: `find` command with `-size` flag
- **Find files by date**: `find` command with `-mtime` flag
- **Search file contents**: `grep` command

### Recognition Patterns
- If you see `find ... -name` → It's searching for files by name
- If you see `find ... -size +100M` → It's finding files larger than 100MB
- If you see `grep -r "text"` → It's searching for text in files recursively

### AI Prompt Templates
- "Show me how to find files named [pattern] in [directory]"
- "How do I find files larger than [size] in [location]?"
- "Help me search for [text] in all files under [directory]"

---

## Managing Processes

### Common Scenarios
- **View running processes**: `ps`, `top`, `htop`
- **Kill a process**: `kill` command with process ID
- **Find process by name**: `pgrep` or `ps aux | grep`

### Recognition Patterns
- If you see `ps aux` → It's listing all running processes
- If you see `kill -9` → It's forcefully terminating a process
- If you see `top` → It's showing real-time process information

### AI Prompt Templates
- "Show me how to find and kill a process named [name]"
- "How do I see what's using the most CPU?"

---

## Text Processing

### Common Scenarios
- **Search in files**: `grep`
- **Replace text**: `sed`
- **Extract columns**: `awk` or `cut`
- **Sort lines**: `sort`

### Recognition Patterns
- If you see `grep "pattern"` → It's searching for text
- If you see `sed 's/old/new/'` → It's replacing text
- If you see `awk '{print $1}'` → It's extracting the first column
- If you see `| sort` → It's sorting the output

### AI Prompt Templates
- "Show me how to search for [pattern] in [files]"
- "How do I replace [old] with [new] in [file]?"

---

## What to Memorize vs Look Up

### Memorize (Core Concepts)
- Problem categories and which tools solve them
- Common patterns (pipes, redirects)
- Mental models (everything is a file, process lifecycle)

### Look Up (Syntax Details)
- Exact command flags and options
- Complex regular expressions
- Specific command combinations

