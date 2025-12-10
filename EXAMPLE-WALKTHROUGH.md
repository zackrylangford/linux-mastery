# Complete Example: Learning to Find Large Files

This is a complete walkthrough showing how to learn one problem domain from start to finish using the AI-age learning approach. Follow along to see the entire process in action.

## The Scenario

**Your situation**: Your disk is running low on space. You need to find and clean up large files, but you don't know the Linux commands for this.

**Traditional approach**: Look up `find` command syntax, memorize flags, practice writing commands from memory.

**AI-age approach**: Understand the problem, learn what's possible, collaborate with AI, verify results.

Let's walk through the AI-age approach step by step.

---

## Step 1: Identify the Problem (2 minutes)

**What you're thinking**: "My disk is almost full. I need to find what's taking up space so I can clean it up."

**Action**: Browse the `problems/` directory to find relevant problem guides.

You see:
- `problems/finding-files/` - This looks relevant!
- `problems/system-monitoring/` - Might have disk space info

**Decision**: Start with `problems/finding-files/` since that's the core problem.

---

## Step 2: Read the Problem Guide (10 minutes)

**Action**: Open `problems/finding-files/README.md`

### What You Learn

**The problem this solves**:
- Locating files by name, size, type, or modification date
- Finding what's taking up disk space
- Searching for specific file types

**Available tools**:
1. **find** - Flexible search by any criteria
   - Best for: Complex searches, finding by size/date/type
   - Example: `find /home -size +100M` (files over 100MB)

2. **du** - Disk usage by directory
   - Best for: Seeing which directories are largest
   - Example: `du -sh * | sort -h` (directory sizes, sorted)

3. **locate** - Fast name-based search
   - Best for: Quick filename searches
   - Example: `locate large-file.zip`

**When to use each**:
- Use `find` when you need to search by size, date, or type
- Use `du` when you want to see directory sizes
- Use `locate` when you know the filename

### Recognition Examples

You see these examples and practice identifying what they do:

```bash
find /home -size +100M
```
**What does this do?** Find all files in /home larger than 100MB

```bash
du -sh */ | sort -h
```
**What does this do?** Show size of each directory, sorted from smallest to largest

```bash
find . -type f -size +500M -exec ls -lh {} \;
```
**What does this do?** Find files over 500MB in current directory and show details

**Key insight**: You don't need to memorize these. You just need to recognize the pattern:
- `find` with `-size` = searching by file size
- `du` with `sort` = showing directory sizes sorted
- Numbers with M/G = megabytes/gigabytes

---

## Step 3: Try It With AI (10 minutes)

Now you practice collaborating with AI to solve your actual problem.

### First Attempt: Basic Prompt

**You ask AI**:
> "How do I find large files on Linux?"

**AI responds**:
```bash
find / -type f -size +100M
```

**You think**: "Okay, but this searches the entire system. I just want my home directory."

### Second Attempt: Refined Prompt

**You ask AI**:
> "Show me how to find files larger than 500MB in my home directory"

**AI responds**:
```bash
find ~ -type f -size +500M
```

**You think**: "Better! Let me try this."

### Running the Command

**You run**:
```bash
find ~ -type f -size +500M
```

**Output**:
```
/home/you/Downloads/ubuntu-22.04.iso
/home/you/Videos/vacation-2024.mp4
/home/you/.cache/some-app/huge-cache-file.dat
```

**Success!** You found three large files.

### Understanding the Result

You look at the command and recognize:
- `~` = your home directory
- `-type f` = files only (not directories)
- `-size +500M` = larger than 500 megabytes

**Key skill**: You didn't memorize this syntax. You directed AI, ran the command, and now you understand what it does.

### Verifying It Works

**You verify** by checking one file:
```bash
ls -lh ~/Downloads/ubuntu-22.04.iso
```

**Output**:
```
-rw-r--r-- 1 you you 3.6G Dec 1 10:30 /home/you/Downloads/ubuntu-22.04.iso
```

**Confirmed**: The file is indeed large (3.6GB). The command works correctly.

---

## Step 4: Try a Related Problem (5 minutes)

Now you want to see which directories are taking up the most space.

**You ask AI**:
> "Show me which directories in my home folder are using the most disk space"

**AI responds**:
```bash
du -sh ~/* | sort -h
```

**You run it**:
```bash
du -sh ~/* | sort -h
```

**Output**:
```
4.0K    /home/you/Documents
156M    /home/you/Pictures
2.1G    /home/you/.cache
5.4G    /home/you/Downloads
8.2G    /home/you/Videos
```

**Insight**: Now you see that Videos (8.2G) and Downloads (5.4G) are your biggest directories.

### Understanding This Command

You recognize:
- `du -sh` = disk usage, summary, human-readable
- `~/*` = all items in home directory
- `sort -h` = sort by human-readable sizes

Again, you didn't memorize this. You asked AI, ran it, and now understand what it does.

---

## Step 5: Document What You Learned (5 minutes)

**Action**: Open `my-knowledge/problems-i-solve.md` and add your new knowledge.

### What You Add

```markdown
## Finding Large Files

**Problem**: Disk is running low on space, need to find what's taking up room

**Solution**: Use `find` command with `-size` flag to search by file size

**AI prompts that worked**:
- "Show me how to find files larger than 500MB in my home directory"
- "Show me which directories are using the most disk space"

**Commands I used**:
- `find ~ -type f -size +500M` - Find large files
- `du -sh ~/* | sort -h` - Show directory sizes sorted

**When I use this**:
- Disk space warnings
- Cleaning up old downloads
- Finding forgotten large files
- Before backing up to see what's big

**What I learned**:
- `find` is flexible - can search by size, date, name, type
- `du` shows directory sizes
- Combining with `sort -h` makes output more useful
- Don't need to memorize syntax - AI can generate it
- Important to verify results make sense

**Related problems**:
- Deleting files safely (need to learn this next)
- Understanding disk usage by file type
- Automating cleanup tasks
```

### What You Also Add to good-prompts.md

```markdown
## Finding Large Files

**Good prompts**:
- "Show me how to find files larger than [size] in [directory]"
- "Show me which directories are using the most disk space"
- "Find files modified in the last [timeframe] larger than [size]"

**Why these work**:
- Specific about what you want (size, location)
- Clear action (find, show)
- Includes constraints (larger than, in directory)

**Bad prompts** (what didn't work as well):
- "How do I find large files?" - Too vague, got generic answer
- "Linux disk space" - Too broad, got explanation not command
```

---

## Step 6: Practice Recognition (5 minutes)

To reinforce your learning, you look at some code examples and practice identifying what they do.

### Example 1
```bash
find /var/log -type f -size +10M -mtime +30
```

**What does this do?**
<details>
<summary>Your answer (click to reveal)</summary>

Find files in /var/log that are:
- Larger than 10MB
- Modified more than 30 days ago

This would be useful for finding old log files to clean up.
</details>

### Example 2
```bash
du -sh /home/*/Downloads | sort -h
```

**What does this do?**
<details>
<summary>Your answer (click to reveal)</summary>

Show the disk usage of the Downloads folder for all users, sorted by size.

This would help identify which user has the largest Downloads folder.
</details>

### Example 3
```bash
find . -type f -size +1G -exec du -h {} \; | sort -h
```

**What does this do?**
<details>
<summary>Your answer (click to reveal)</summary>

Find all files larger than 1GB in the current directory, show their sizes, and sort them.

This combines find with du to get detailed size information sorted.
</details>

**Key insight**: You can now recognize these patterns even though you didn't memorize the exact syntax. This is the goal!

---

## Step 7: Apply to Real Problem (10 minutes)

Now you use your new knowledge to actually clean up your disk.

### Your Process

1. **Find large files**:
   ```bash
   find ~ -type f -size +500M
   ```

2. **Identify what can be deleted**:
   - Old ISO file in Downloads (3.6GB) - can delete
   - Vacation video (2.1GB) - keep
   - Cache file (800MB) - can delete

3. **Ask AI how to delete safely**:
   > "Show me how to safely delete a file in Linux"
   
   AI gives you: `rm filename` (and warns to be careful)

4. **Delete the files**:
   ```bash
   rm ~/Downloads/ubuntu-22.04.iso
   rm ~/.cache/some-app/huge-cache-file.dat
   ```

5. **Verify space freed**:
   ```bash
   df -h ~
   ```

**Result**: You freed up 4.4GB of space!

---

## What You Accomplished (Total: ~45 minutes)

### Skills Gained

✅ **Problem identification**: Recognized this as a "finding files" problem

✅ **Tool awareness**: Learned that `find` and `du` solve this problem

✅ **AI collaboration**: Practiced asking effective questions and refining prompts

✅ **Verification**: Confirmed AI's solutions actually work

✅ **Recognition**: Can now identify what file-finding commands do

✅ **Documentation**: Built your personal knowledge base

✅ **Real-world application**: Actually solved your disk space problem

### What You DON'T Need to Remember

❌ Exact syntax of `find` command flags

❌ All the options for `du` command

❌ The order of arguments

❌ Complex one-liners

### What You DO Remember

✅ "I can find large files using `find` with size criteria"

✅ "I can see directory sizes using `du` and `sort`"

✅ "When I need this, I ask AI: 'Show me how to find files larger than X'"

✅ "I verify results make sense before taking action"

---

## The Learning Pattern (Reusable)

This same pattern works for ANY Linux problem:

1. **Identify the problem** - What are you trying to do?
2. **Find the problem guide** - Browse `problems/` directory
3. **Learn what's possible** - Read about available tools
4. **Practice recognition** - Look at examples, identify what they do
5. **Try with AI** - Ask AI to generate solutions
6. **Verify results** - Make sure it works correctly
7. **Document** - Add to your personal knowledge base
8. **Apply** - Use it to solve real problems

**Time investment**: 30-45 minutes per problem

**Long-term value**: You can now solve this problem forever

---

## Tomorrow: Pick a New Problem

Now that you've learned one problem domain, pick another:

**Suggestions**:
- `problems/managing-processes/` - Control running programs
- `problems/text-processing/` - Search and manipulate text
- `problems/permissions/` - Understand file permissions
- `problems/networking/` - Basic network troubleshooting

**The process is the same**:
1. Read the problem guide (10 min)
2. Try with AI (10 min)
3. Document what you learned (5 min)

**In 30 days**, you'll have 30 problems you can solve. That's real Linux competency!

---

## Key Takeaways

### What Makes This Approach Different

**Traditional learning**:
- Memorize: `find /path -name "*.txt" -type f -mtime -7`
- Problem: Forget syntax in a week
- Result: Constantly looking up commands

**AI-age learning**:
- Understand: "I need to find files by name, type, or date"
- Recognize: "This find command searches for recent text files"
- Direct AI: "Show me how to find text files from last week"
- Result: Solve problems without memorizing syntax

### Why This Works

1. **Cognitive load**: You focus on concepts, not syntax details
2. **Practical**: You solve real problems immediately
3. **Sustainable**: 30 minutes daily is manageable
4. **Cumulative**: Each problem builds your capability
5. **Modern**: Leverages AI as a tool, not a crutch

### Your Next Steps

1. **Pick your next problem** from `problems/` directory
2. **Follow this same pattern** - it works for any problem
3. **Build your knowledge base** - Keep updating `my-knowledge/`
4. **Practice daily** - Consistency beats intensity
5. **Apply to real work** - Use Linux for actual tasks

---

## Reflection Questions

After completing this walkthrough, ask yourself:

1. **Did I memorize the exact syntax?** (No, and that's okay!)
2. **Can I recognize what these commands do?** (Yes!)
3. **Could I ask AI to generate similar commands?** (Yes!)
4. **Did I solve a real problem?** (Yes - freed up disk space!)
5. **Can I do this again tomorrow with a new problem?** (Yes!)

If you answered yes to questions 2-5, you're learning effectively!

---

## Additional Examples

Want to see this pattern applied to other problems? Here are quick examples:

### Example: Managing Processes

**Problem**: Computer is slow, need to find what's using CPU

**Learn**: Read `problems/managing-processes/README.md`

**Try with AI**: "Show me which processes are using the most CPU"

**AI gives**: `top` or `ps aux --sort=-%cpu | head`

**Document**: "I can monitor processes using top or ps"

**Time**: 30 minutes

### Example: Text Processing

**Problem**: Need to find all occurrences of "error" in log files

**Learn**: Read `problems/text-processing/README.md`

**Try with AI**: "Show me how to search for 'error' in all log files"

**AI gives**: `grep -r "error" /var/log/`

**Document**: "I can search text using grep"

**Time**: 30 minutes

### Example: Understanding Permissions

**Problem**: Can't edit a file, getting "permission denied"

**Learn**: Read `problems/permissions/README.md`

**Try with AI**: "Show me how to check and fix file permissions"

**AI gives**: `ls -l filename` and `chmod` commands

**Document**: "I can manage permissions using chmod"

**Time**: 30 minutes

**Pattern**: Same every time. Learn, try, document, apply.

---

## Conclusion

You've now seen the complete AI-age learning process from start to finish. This isn't theory - it's a practical approach that works.

**The key insight**: In 2025, you don't need to memorize Linux commands. You need to:
- Understand what problems Linux can solve
- Recognize patterns when you see them
- Collaborate effectively with AI
- Verify solutions work correctly
- Build your personal knowledge base

**Start today**: Pick a problem from `problems/`, follow this pattern, and solve something real.

One problem at a time, you'll build genuine Linux competency. 🚀

---

## Related Resources

- **[GETTING-STARTED.md](GETTING-STARTED.md)** - Your first week's problems in order
- **[DAILY-PRACTICE.md](DAILY-PRACTICE.md)** - The simple daily routine
- **[README.md](README.md)** - Overview of the entire learning system
- **[MIGRATION-GUIDE.md](MIGRATION-GUIDE.md)** - Transitioning from old structure

**Next**: See [GETTING-STARTED.md](GETTING-STARTED.md) for your first week's problems, or browse `problems/` to pick what interests you.
