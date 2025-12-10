# Getting Started: Your First Week

A step-by-step guide to learning Linux the AI-age way. Follow this for your first week, then continue at your own pace.

## Before You Start (5 minutes)

### What You'll Need
- A Linux terminal (WSL, Mac terminal, or Linux machine)
- Access to an AI assistant (ChatGPT, Claude, etc.)
- This repository open in your editor

### Set Up Your Knowledge Base
1. Open `my-knowledge/problems-i-solve.md`
2. Open `my-knowledge/good-prompts.md`
3. Keep these files open - you'll update them daily

**That's it!** You're ready to start.

## Your First Week

Each day follows the same pattern:
1. Pick the day's problem (2 min)
2. Learn what's possible (10 min)
3. Try it with AI (10 min)
4. Document what you learned (5 min)

**Total: 20-30 minutes per day**

---

## Day 1: Understanding the Filesystem

**Goal**: Learn how Linux organizes files and directories

### What to Do

1. **Read** `problems/filesystem-mental-model/README.md` (10 min)
   - Understand "everything is a file"
   - Learn about the directory tree
   - See how paths work

2. **Try with AI** (10 min)
   - Ask AI: "Explain the Linux filesystem hierarchy. Where are user files stored?"
   - Ask AI: "Show me how to see the directory tree structure"
   - Run the commands AI suggests
   - Explore your own filesystem

3. **Document** (5 min)
   Add to `my-knowledge/problems-i-solve.md`:
   ```markdown
   ## Understanding Filesystem Structure
   - Problem: Need to know where files are located
   - Solution: Everything is organized in a tree from /
   - Key locations: /home (user files), /etc (config), /var (logs)
   - AI prompt: "Explain the Linux filesystem hierarchy"
   ```

### What You Learned
- How Linux organizes files
- The concept of "everything is a file"
- Where different types of files live

---

## Day 2: Navigating Directories

**Goal**: Move around the filesystem confidently

### What to Do

1. **Read** `problems/navigating-filesystem/README.md` (10 min)
   - Learn about pwd, cd, ls
   - Understand current directory concept
   - See navigation examples

2. **Try with AI** (10 min)
   - Ask AI: "Show me how to navigate to my Documents folder and list its contents"
   - Ask AI: "How do I go back to my home directory from anywhere?"
   - Practice moving around your filesystem
   - Try the commands yourself

3. **Document** (5 min)
   Add to `my-knowledge/problems-i-solve.md`:
   ```markdown
   ## Navigating Directories
   - Problem: Need to move around the filesystem
   - Solution: Use cd to change directories, pwd to see where I am
   - AI prompt: "Show me how to navigate to [directory] and list contents"
   - When I use this: Every time I work in terminal
   ```

### What You Learned
- How to move between directories
- How to see where you are
- How to list directory contents

---

## Day 3: Understanding Paths

**Goal**: Master absolute vs relative paths

### What to Do

1. **Read** `problems/understanding-paths/README.md` (10 min)
   - Learn absolute paths (start with /)
   - Learn relative paths (from current location)
   - Understand . and .. and ~
   - See path examples

2. **Try with AI** (10 min)
   - Ask AI: "Explain the difference between absolute and relative paths with examples"
   - Ask AI: "Show me how to reference a file in the parent directory"
   - Practice using both types of paths
   - Try using . and .. and ~

3. **Document** (5 min)
   Add to `my-knowledge/problems-i-solve.md`:
   ```markdown
   ## Working With Paths
   - Problem: Need to reference files and directories
   - Solution: Use absolute paths (/full/path) or relative paths (../nearby)
   - Shortcuts: ~ (home), . (current), .. (parent)
   - AI prompt: "Show me how to reference [file] using relative path"
   ```

### What You Learned
- Difference between absolute and relative paths
- When to use each type
- Useful shortcuts (., .., ~)

---

## Day 4: Managing Directories

**Goal**: Create, organize, and remove directories

### What to Do

1. **Read** `problems/managing-directories/README.md` (10 min)
   - Learn about mkdir, rmdir, rm -r
   - Understand directory operations
   - See organization examples

2. **Try with AI** (10 min)
   - Ask AI: "Show me how to create a new directory called 'test-project' with subdirectories"
   - Ask AI: "How do I safely remove a directory and its contents?"
   - Create a test directory structure
   - Practice organizing files

3. **Document** (5 min)
   Add to `my-knowledge/problems-i-solve.md`:
   ```markdown
   ## Managing Directories
   - Problem: Need to organize files into folders
   - Solution: Use mkdir to create, rm -r to remove directories
   - AI prompt: "Show me how to create/remove directory structure for [purpose]"
   - When I use this: Setting up projects, organizing files
   ```

### What You Learned
- How to create directory structures
- How to safely remove directories
- How to organize files effectively

---

## Day 5: Finding Files

**Goal**: Locate files on your system

### What to Do

1. **Read** `problems/finding-files/README.md` (10 min)
   - Learn about find, locate, grep
   - Understand search strategies
   - See finding examples

2. **Try with AI** (10 min)
   - Ask AI: "Show me how to find all .txt files in my home directory"
   - Ask AI: "How do I find files larger than 100MB?"
   - Practice finding files by name, size, type
   - Try different search criteria

3. **Document** (5 min)
   Add to `my-knowledge/problems-i-solve.md`:
   ```markdown
   ## Finding Files
   - Problem: Need to locate files on my system
   - Solution: Use find for flexible searches, locate for quick name searches
   - AI prompt: "Show me how to find files by [criteria] in [location]"
   - When I use this: Looking for files, cleaning up disk space
   ```

### What You Learned
- How to search for files by various criteria
- Difference between find and locate
- How to find large files

---

## Day 6: Managing Processes

**Goal**: See and control running programs

### What to Do

1. **Read** `problems/managing-processes/README.md` (10 min)
   - Learn about ps, top, kill
   - Understand process concept
   - See process management examples

2. **Try with AI** (10 min)
   - Ask AI: "Show me how to see all running processes"
   - Ask AI: "How do I find which process is using the most CPU?"
   - Practice viewing processes
   - Try finding specific processes

3. **Document** (5 min)
   Add to `my-knowledge/problems-i-solve.md`:
   ```markdown
   ## Managing Processes
   - Problem: Need to see or control running programs
   - Solution: Use ps to list, top to monitor, kill to stop processes
   - AI prompt: "Show me how to [view/stop] processes doing [task]"
   - When I use this: System is slow, need to stop stuck program
   ```

### What You Learned
- How to see running processes
- How to monitor system resources
- How to stop processes when needed

---

## Day 7: Text Processing Basics

**Goal**: Work with text files and data

### What to Do

1. **Read** `problems/text-processing/README.md` (10 min)
   - Learn about grep, cat, less, head, tail
   - Understand text manipulation
   - See text processing examples

2. **Try with AI** (10 min)
   - Ask AI: "Show me how to search for a word in all files in a directory"
   - Ask AI: "How do I view just the first 10 lines of a file?"
   - Practice searching and viewing text
   - Try different text operations

3. **Document** (5 min)
   Add to `my-knowledge/problems-i-solve.md`:
   ```markdown
   ## Text Processing
   - Problem: Need to search or view text files
   - Solution: Use grep to search, cat/less to view, head/tail for portions
   - AI prompt: "Show me how to [search/view/extract] text from [file]"
   - When I use this: Reading logs, searching code, viewing configs
   ```

### What You Learned
- How to search text files
- How to view file contents
- How to extract portions of files

---

## End of Week 1: Review (30 minutes)

### What You've Accomplished

After one week, you can now:
- ✅ Understand how Linux organizes files
- ✅ Navigate the filesystem confidently
- ✅ Work with paths (absolute and relative)
- ✅ Create and organize directories
- ✅ Find files on your system
- ✅ View and manage processes
- ✅ Search and view text files

### Review Your Knowledge Base

1. Open `my-knowledge/problems-i-solve.md`
2. You should have 7 problems documented
3. Review each one - can you still do them?

### Test Yourself

Try these without looking up the answer first:

1. "I need to find all PDF files in my Documents folder"
   - What tool would you use?
   - How would you ask AI for help?

2. "My computer is running slow"
   - What tool would you use to investigate?
   - How would you ask AI for help?

3. "I need to create a project folder with subdirectories"
   - What tool would you use?
   - How would you ask AI for help?

If you can identify the right tool and ask AI effectively, you're succeeding!

### Celebrate!

You've completed your first week of AI-age Linux learning. You now have:
- A foundation in core Linux concepts
- 7 problems you can solve
- Experience collaborating with AI
- Your own personal knowledge base

---

## What's Next?

### Week 2 and Beyond

Continue the same pattern with new problems:
- Permissions and ownership
- Network troubleshooting
- System monitoring
- Package management
- Shell scripting basics
- File compression
- User management

Browse `problems/` and pick what interests you or what you need for work.

### Keep Building Your Knowledge

Your `my-knowledge/problems-i-solve.md` file is your most valuable asset. Keep adding to it:
- New problems you learn to solve
- AI prompts that work well
- Patterns you recognize

After 30 days, you'll have a comprehensive personal reference.

### Optional: Certification Path

If you're preparing for LPIC-1:
- Start using `cert-prep/syntax-to-recognize.md`
- Practice with `cert-prep/recognition-exercises.md`
- Add 5-10 minutes daily for exam-specific syntax

See [CERTIFICATION-PATH.md](CERTIFICATION-PATH.md) for details.

---

## Tips for Continued Success

### Stay Consistent
- 20-30 minutes daily beats 3 hours on weekends
- One problem per day adds up fast
- Don't skip days - keep the momentum

### Focus on Understanding
- Why does this work?
- When would I use this?
- What problem does this solve?

### Practice AI Collaboration
- Get better at asking questions
- Learn to verify AI's answers
- Refine prompts when needed

### Build Your Reference
- Keep updating `my-knowledge/problems-i-solve.md`
- Document AI prompts that work
- Create your own examples

### Don't Memorize
- You don't need to remember exact syntax
- Focus on recognizing patterns
- Let AI handle the details

---

## Common First Week Questions

**Q: This seems too simple. Am I learning enough?**
A: Yes! Understanding problems and collaborating with AI is more valuable than memorizing commands. You're building the right skills.

**Q: Should I be taking more notes?**
A: Only if it helps you. The `problems-i-solve.md` file is usually enough. Don't over-document.

**Q: What if I don't understand something?**
A: Ask AI to explain it differently. Try the command yourself. Read the problem guide again. Understanding comes with practice.

**Q: Can I skip days or go faster?**
A: Go at your own pace. The week structure is a guide, not a rule. Consistency matters more than speed.

**Q: Do I need to memorize these commands?**
A: No! Focus on understanding what's possible and how to ask AI for help. Recognition over memorization.

---

## Ready to Start?

1. Go back to [Day 1](#day-1-understanding-the-filesystem)
2. Spend 20-30 minutes on today's problem
3. Update your `my-knowledge/problems-i-solve.md`
4. Come back tomorrow for Day 2

You've got this! One problem at a time, you'll build real Linux skills.

See [DAILY-PRACTICE.md](DAILY-PRACTICE.md) for the daily routine details.
