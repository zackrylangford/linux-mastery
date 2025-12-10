# AI Prompts That Work

This is your collection of effective prompts for getting Linux help from AI. Learn what makes prompts work well, and build your own library.

**Why this matters:**
- Good prompts get you accurate, usable solutions faster
- Bad prompts waste time with generic or wrong answers
- Learning to prompt well is a core skill in the AI age

---

## What Makes a Good Prompt?

### ✅ Good prompts are:
- **Specific**: Include exact details (file types, sizes, directories)
- **Contextual**: Explain what you're trying to accomplish
- **Constrained**: Mention limitations (no sudo, must preserve permissions, etc.)
- **Verifiable**: Ask for explanations so you can check if it's right

### ❌ Bad prompts are:
- **Vague**: "Help me with files"
- **Assumption-heavy**: Assuming AI knows your system setup
- **Syntax-only**: "What's the find command?" without context
- **Unverifiable**: No way to check if the answer is correct

---

## Finding Files

### ✅ Good Prompt
```
I need to find all PDF files larger than 10MB in my home directory and its subdirectories. 
Show me the command and explain what each part does.
```

**Why it works**: Specific file type, size, location. Asks for explanation.

### ❌ Bad Prompt
```
How do I find files?
```

**Why it fails**: Too vague - what files? Where? What criteria?

---

### ✅ Good Prompt
```
Show me how to locate all files modified in the last 7 days under /var/log, 
excluding any files in subdirectories named 'archive'. Explain the command.
```

**Why it works**: Specific timeframe, location, exclusion criteria, asks for explanation.

### ❌ Bad Prompt
```
Find recent files
```

**Why it fails**: "Recent" is ambiguous, no location specified.

---

## Managing Processes

### ✅ Good Prompt
```
I have a Python script running that I need to stop, but I don't know its PID. 
The script is called 'data_processor.py'. Show me how to find and kill it safely, 
and explain the difference between kill signals.
```

**Why it works**: Specific process name, asks for safe approach, wants to understand signals.

### ❌ Bad Prompt
```
How to kill a process?
```

**Why it fails**: No context about which process or how to identify it.

---

### ✅ Good Prompt
```
Show me how to list all processes owned by user 'webapp' that are using more than 
500MB of memory, sorted by memory usage. Explain what each part of the command does.
```

**Why it works**: Specific user, memory threshold, sorting requirement, asks for explanation.

### ❌ Bad Prompt
```
Show memory usage
```

**Why it fails**: Unclear if asking about system memory or process memory, no filtering criteria.

---

## Text Processing

### ✅ Good Prompt
```
I have a CSV file with comma-separated values. I need to extract the 3rd column 
and save it to a new file. The CSV has a header row that I want to skip. 
Show me how to do this and explain the command.
```

**Why it works**: Specific format, column number, header handling, asks for explanation.

### ❌ Bad Prompt
```
Extract column from file
```

**Why it fails**: No details about file format, which column, or what to do with output.

---

### ✅ Good Prompt
```
I need to search for the word 'ERROR' in all .log files under /var/app/logs, 
showing 2 lines of context before and after each match. The search should be 
case-insensitive. Show me the command and explain the flags.
```

**Why it works**: Specific pattern, file types, location, context lines, case handling.

### ❌ Bad Prompt
```
Search logs for errors
```

**Why it fails**: Vague about what "errors" means, where to search, what output format.

---

## File Permissions

### ✅ Good Prompt
```
I need to make a shell script executable for the owner only, while keeping it 
readable by the group. The file is called 'backup.sh'. Show me the chmod command 
and explain what the permissions mean.
```

**Why it works**: Specific permissions needed, file name, asks for explanation.

### ❌ Bad Prompt
```
Make file executable
```

**Why it fails**: Doesn't specify for whom, doesn't mention other permission requirements.

---

## Disk Usage

### ✅ Good Prompt
```
Show me how to find the top 10 largest directories under /home, displaying sizes 
in human-readable format (GB/MB), sorted from largest to smallest. Explain the command.
```

**Why it works**: Specific location, number of results, format preference, sorting.

### ❌ Bad Prompt
```
Check disk space
```

**Why it fails**: Unclear if asking about free space, directory sizes, or file sizes.

---

## Prompt Templates You Can Reuse

### For Finding Things
```
I need to find all [file type] that [criteria] in [location]. 
[Any exclusions or special requirements]. 
Show me the command and explain what each part does.
```

### For Processing Text
```
I have a [file format] with [structure]. I need to [action] and [output requirement]. 
[Any special handling needed]. 
Show me how to do this and explain the command.
```

### For Managing Processes
```
I need to [action] a process that [identification criteria]. 
[Any constraints or safety requirements]. 
Show me the command and explain the approach.
```

### For Understanding Code
```
Explain what this command does and when I would use it:
[paste command here]

Break down each part and explain the overall purpose.
```

### For Troubleshooting
```
I'm trying to [goal] but [what's going wrong]. 
My current approach is [what you tried]. 
[Relevant system details or constraints]. 
What's the correct way to do this?
```

---

## Tips for Better Prompts

1. **Always ask for explanations**: "Show me the command and explain what each part does"
2. **Mention constraints**: "without sudo", "must preserve timestamps", "case-insensitive"
3. **Specify output format**: "human-readable", "one per line", "sorted by size"
4. **Include context**: Why you need this, what you're trying to accomplish
5. **Request verification**: "How can I verify this worked correctly?"

---

## Your Prompt Collection

### [Problem Type]

#### ✅ Prompt that worked:
```
[Your effective prompt here]
```

**Why it worked**: [What made this prompt effective]

**Result**: [What you got back and how you used it]

---

## Learning from Bad Prompts

When a prompt doesn't work well:
1. **Identify what was missing**: Specificity? Context? Constraints?
2. **Refine and retry**: Add the missing information
3. **Document both versions**: Learn from the comparison
4. **Build your templates**: Turn good prompts into reusable patterns

**Remember**: Getting good at prompting is like learning any skill - you improve with practice and reflection!
