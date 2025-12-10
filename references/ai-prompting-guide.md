# AI Prompting Guide for Linux Learning

## Overview

This guide teaches you how to effectively collaborate with AI when learning and using Linux. In the AI age, your job isn't to memorize syntax—it's to understand problems, direct AI effectively, and verify solutions.

**Key principle**: You need to know WHAT you want to accomplish and WHY, then AI can help with the HOW.

## Table of Contents

1. [The AI Collaboration Mindset](#the-ai-collaboration-mindset)
2. [Anatomy of a Good Prompt](#anatomy-of-a-good-prompt)
3. [Examples of Good vs Bad Prompts](#examples-of-good-vs-bad-prompts)
4. [How to Verify AI Solutions](#how-to-verify-ai-solutions)
5. [How to Refine Prompts](#how-to-refine-prompts)
6. [Common Pitfalls](#common-pitfalls)
7. [Prompt Templates by Problem Type](#prompt-templates-by-problem-type)

---

## The AI Collaboration Mindset

### What You Need to Know

**Before asking AI, you should understand:**
- What problem you're trying to solve
- What category of problem it is (filesystem, process, network, etc.)
- What constraints you have (permissions, system type, available tools)
- What the expected outcome looks like

**You DON'T need to know:**
- Exact command syntax
- All the flags and options
- The precise order of arguments

### The Collaboration Flow

```
1. Identify the problem
   ↓
2. Understand what's possible (read problem guides)
   ↓
3. Ask AI for specific solution
   ↓
4. Verify the solution makes sense
   ↓
5. Test it safely
   ↓
6. Document what worked
```

---

## Anatomy of a Good Prompt

### The Formula

A good Linux prompt has these components:

```
[CONTEXT] + [PROBLEM] + [CONSTRAINTS] + [EXPECTED OUTPUT]
```

### Breaking It Down

**CONTEXT**: What's your situation?
- "I'm on Ubuntu 22.04"
- "I'm working in a directory with 1000+ files"
- "I have sudo access"
- "I'm writing a backup script"

**PROBLEM**: What do you need to accomplish?
- "Find all log files larger than 100MB"
- "Kill a process that's using too much memory"
- "Extract specific columns from a CSV file"

**CONSTRAINTS**: What limitations exist?
- "Without deleting anything"
- "Only in the current directory, not subdirectories"
- "Preserve file permissions"
- "Must work on systems without tool X"

**EXPECTED OUTPUT**: What should the result look like?
- "Show me the file paths"
- "Just the process ID"
- "Output as a sorted list"
- "Save to a new file"

### Example

**Good prompt:**
```
I'm on Ubuntu and need to find all .log files in /var/log that are larger 
than 100MB and haven't been modified in 30 days. Show me the file paths 
and their sizes, sorted by size.
```

This includes:
- Context: Ubuntu, /var/log directory
- Problem: Find specific log files
- Constraints: Size > 100MB, age > 30 days, .log extension
- Expected output: Paths and sizes, sorted

---

## Examples of Good vs Bad Prompts

### Finding Files

❌ **Bad**: "How do I find files?"
- Too vague - what files? where? why?

✅ **Good**: "Show me how to find all PDF files in my home directory that are larger than 10MB"
- Specific file type, location, and criteria

---

❌ **Bad**: "find command"
- Not a question, no context

✅ **Good**: "I need to locate all files modified in the last 24 hours in /home/user/projects. Show me the command."
- Clear timeframe, location, and purpose

---

### Managing Processes

❌ **Bad**: "Kill process"
- Which process? How to identify it?

✅ **Good**: "Show me how to find and kill a process named 'firefox' that's using more than 2GB of memory"
- Specific process name and criteria for identification

---

❌ **Bad**: "What's using my CPU?"
- Unclear what information you need

✅ **Good**: "Show me the top 5 processes using the most CPU right now, with their process IDs and CPU percentages"
- Specific number, specific metrics, clear output format

---

### Text Processing

❌ **Bad**: "Parse this file"
- What kind of parsing? What's the goal?

✅ **Good**: "I have a CSV file with columns: name, age, city. Extract all rows where age > 30 and save to a new file"
- File format, structure, specific criteria, desired action

---

❌ **Bad**: "grep help"
- Not specific enough

✅ **Good**: "Search all .txt files in the current directory for lines containing 'ERROR' and show the filename and line number for each match"
- File type, search term, desired output format

---

### File Operations

❌ **Bad**: "Copy files"
- Which files? Where? With what options?

✅ **Good**: "Copy all .jpg files from /source to /backup, preserving timestamps and permissions, and show progress"
- Specific file type, source, destination, requirements

---

❌ **Bad**: "Change permissions"
- On what? To what?

✅ **Good**: "Make all .sh files in the current directory executable by the owner only, without changing other permissions"
- Specific files, specific permission change, constraints

---

## How to Verify AI Solutions

### Step 1: Read and Understand

Before running ANY command, ask yourself:

1. **Does this make sense?**
   - Does it address my actual problem?
   - Are the file paths correct?
   - Are the flags reasonable?

2. **Is it safe?**
   - Will it delete or modify files?
   - Does it need sudo (and should it)?
   - Will it affect system files?

3. **Can I test it safely?**
   - Can I try it on a small subset first?
   - Can I use a test directory?
   - Can I add a "dry run" flag?

### Step 2: Break Down the Command

**Example AI gives you:**
```bash
find /var/log -name "*.log" -size +100M -mtime +30 -exec ls -lh {} \;
```

**Break it down:**
- `find /var/log` - Search in /var/log directory
- `-name "*.log"` - Files ending in .log
- `-size +100M` - Larger than 100MB
- `-mtime +30` - Modified more than 30 days ago
- `-exec ls -lh {} \;` - For each file, show detailed info

**Verify each part matches your requirements.**

### Step 3: Test Safely

**Strategies for safe testing:**

1. **Use echo first**
   ```bash
   # Instead of deleting, echo what would be deleted
   find . -name "*.tmp" -exec echo "Would delete: {}" \;
   ```

2. **Test on a small subset**
   ```bash
   # Add -maxdepth 1 to limit to current directory
   find . -maxdepth 1 -name "*.log"
   ```

3. **Use dry-run flags when available**
   ```bash
   rsync -av --dry-run source/ dest/
   ```

4. **Redirect to a file instead of modifying**
   ```bash
   # Instead of modifying in place, save to new file
   sed 's/old/new/g' file.txt > file_new.txt
   ```

### Step 4: Verify the Output

After running the command:

1. **Check the results**
   - Did it do what you expected?
   - Are the numbers reasonable?
   - Any error messages?

2. **Spot check**
   - Manually verify a few results
   - Check edge cases
   - Look for unexpected behavior

3. **Document what worked**
   - Save the command that worked
   - Note any modifications you made
   - Record any gotchas

---

## How to Refine Prompts

### When AI Doesn't Give You What You Need

**Problem**: AI's solution is too complex

**Refinement**: "Can you simplify this? I just need the basic version without error handling"

---

**Problem**: AI's solution doesn't match your system

**Refinement**: "I'm on Ubuntu 20.04 and don't have tool X. What's an alternative?"

---

**Problem**: AI's solution is too vague

**Refinement**: "Can you show me the exact command with my specific paths: /home/user/documents"

---

**Problem**: AI's solution doesn't handle edge cases

**Refinement**: "What if the filename has spaces? How do I handle that?"

---

**Problem**: You don't understand the solution

**Refinement**: "Can you explain what each part of this command does?"

---

### The Iterative Approach

```
First prompt: "Find large files in my home directory"
   ↓
AI gives generic answer
   ↓
Refine: "Show me files larger than 500MB, modified in the last week"
   ↓
AI gives better answer but uses unfamiliar tool
   ↓
Refine: "Can you do this with find instead of du?"
   ↓
AI gives exactly what you need
```

**Key insight**: It's okay to refine! Each refinement teaches you more about the problem space.

---

## Common Pitfalls

### Pitfall 1: Trusting AI Blindly

❌ **Don't**: Copy-paste and run without understanding

✅ **Do**: Read the command, understand what it does, test safely

---

### Pitfall 2: Being Too Vague

❌ **Don't**: "Help me with files"

✅ **Do**: "Show me how to find all files larger than 1GB in /home"

---

### Pitfall 3: Not Providing Context

❌ **Don't**: "This command doesn't work"

✅ **Do**: "I'm on CentOS 7 and this command gives error X. Here's what I tried..."

---

### Pitfall 4: Ignoring Error Messages

❌ **Don't**: Keep trying random variations

✅ **Do**: Share the error message with AI and ask for explanation

---

### Pitfall 5: Not Testing Safely

❌ **Don't**: Run destructive commands on production data

✅ **Do**: Test on copies, use dry-run flags, start small

---

## Prompt Templates by Problem Type

### Finding Files

```
Template:
"Show me how to find all [FILE_TYPE] files in [DIRECTORY] that 
[CRITERIA] and [ACTION]"

Example:
"Show me how to find all .log files in /var/log that are larger 
than 100MB and list them with their sizes"
```

### Managing Processes

```
Template:
"Show me how to [ACTION] processes that [CRITERIA]"

Example:
"Show me how to list all processes using more than 1GB of memory 
with their process IDs and memory usage"
```

### Text Processing

```
Template:
"I have a [FILE_TYPE] with [STRUCTURE]. Extract/modify [WHAT] 
where [CRITERIA] and [OUTPUT_FORMAT]"

Example:
"I have a CSV with columns name,age,city. Extract all rows where 
age > 25 and save to a new file sorted by name"
```

### File Operations

```
Template:
"Copy/move/modify [WHAT] from [SOURCE] to [DESTINATION] with 
[REQUIREMENTS]"

Example:
"Copy all .jpg files from /photos to /backup preserving timestamps 
and show progress"
```

### Permissions

```
Template:
"Change permissions on [WHAT] to [PERMISSIONS] [CONSTRAINTS]"

Example:
"Make all .sh files in /scripts executable by owner and group, 
readable by others"
```

### System Monitoring

```
Template:
"Show me [WHAT_METRIC] for [WHAT_RESOURCE] [TIME_PERIOD]"

Example:
"Show me disk usage for all mounted filesystems, sorted by usage 
percentage"
```

### Networking

```
Template:
"Show me/test [WHAT] for [TARGET] [CONSTRAINTS]"

Example:
"Show me all active network connections on port 80 with the process 
names"
```

---

## Practice Exercise

Try improving these prompts:

1. **Vague**: "Delete old files"
   - **Your improved version**: _______________

2. **No context**: "Process is stuck"
   - **Your improved version**: _______________

3. **Unclear output**: "Show me logs"
   - **Your improved version**: _______________

**Answers** (examples):

1. "Show me how to find and delete all .tmp files in /home/user/temp that haven't been accessed in 90 days"

2. "I have a Python process named 'data_processor.py' that's been running for 6 hours and isn't responding. Show me how to find its PID and kill it gracefully"

3. "Show me the last 50 lines of /var/log/syslog that contain the word 'error', with timestamps"

---

## Quick Reference Card

### Before You Ask AI

- [ ] Do I understand what problem I'm trying to solve?
- [ ] Do I know what category this falls into?
- [ ] Have I read the relevant problem guide?
- [ ] Do I know what constraints I have?

### When AI Responds

- [ ] Do I understand what this command does?
- [ ] Is it safe to run?
- [ ] Can I test it safely first?
- [ ] Does it match my requirements?

### After Running the Command

- [ ] Did it work as expected?
- [ ] Should I document this for later?
- [ ] What did I learn about this problem type?

---

## Remember

**You're not trying to become a human command-line reference manual.** You're learning to:

1. Recognize what problems Linux can solve
2. Understand what's possible
3. Direct AI effectively to generate solutions
4. Verify that solutions are correct and safe
5. Build your personal knowledge of problems you can solve

**The goal**: Become an effective problem-solver who knows how to leverage AI, not someone who memorizes syntax.

---

## Next Steps

1. Pick a problem from the `problems/` directory
2. Read the problem guide
3. Try asking AI for a solution using these techniques
4. Verify and test the solution
5. Document what worked in `my-knowledge/good-prompts.md`

**Related Resources:**
- [Good Prompts Collection](../my-knowledge/good-prompts.md) - Your personal collection
- [Problem Guides](../problems/) - Learn what's possible
- [Quick Reference](quick-reference.md) - Fast lookup by problem type
