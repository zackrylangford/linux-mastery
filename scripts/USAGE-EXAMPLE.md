# Content Transformation Script - Usage Example

This document shows a complete example of using the transformation script to migrate content.

## Scenario

You have existing content in `topics/filesystem/week-1-filesystem-basics.md` that looks like this:

```markdown
# Week 1: Filesystem Basics

## Commands to Master
- `pwd` - Print working directory
- `ls` - List directory contents
- `cd` - Change directory
- `mkdir` - Create directories
- `find` - Search for files
```

You want to transform this into problem-focused guides.

## Step 1: Analyze Existing Content

Run the analysis to see what problems your content addresses:

```bash
python3 scripts/transform-content.py --analyze
```

**Expected Output:**

```
============================================================
CONTENT ANALYSIS REPORT
============================================================

Total commands found: 11
Problem domains identified: 4

NAVIGATING-FILESYSTEM
----------------------------------------
Description: Moving between directories and understanding filesystem structure
Commands (3):
  • pwd - Print working directory
  • ls - List directory contents (with -l, -a, -h flags)
  • cd - Change directory
Source files: 1
  • topics/filesystem/week-1-filesystem-basics.md

MANAGING-DIRECTORIES
----------------------------------------
Description: Creating, organizing, and removing directory structures
Commands (3):
  • mkdir - Create directories
  • rmdir - Remove empty directories
  • rm - Remove files (careful with -rf)
Source files: 1
  • topics/filesystem/week-1-filesystem-basics.md

FINDING-FILES
----------------------------------------
Description: Locating files by name, size, date, or other criteria
Commands (1):
  • find - Search for files
Source files: 1
  • topics/filesystem/week-1-filesystem-basics.md

FILE-OPERATIONS
----------------------------------------
Description: Copying, moving, and manipulating files
Commands (4):
  • touch - Create files
  • cp - Copy files/directories
  • mv - Move/rename files
Source files: 1
  • topics/filesystem/week-1-filesystem-basics.md
```

## Step 2: Generate Problem Guides

Generate problem guide templates:

```bash
python3 scripts/transform-content.py --generate
```

**Expected Output:**

```
============================================================
GENERATING PROBLEM GUIDES
============================================================

Generated: problems/navigating-filesystem/README.md
Generated: problems/managing-directories/README.md
Generated: problems/finding-files/README.md
Generated: problems/file-operations/README.md

Guides generated in 'problems/' directory
Please review and enhance the generated guides with:
  • More specific real-world scenarios
  • Better decision guidance
  • Additional examples with explanations
  • Clearer AI prompt templates
```

## Step 3: Review Generated Guide

Open `problems/navigating-filesystem/README.md`:

```markdown
# Problem: Navigating Filesystem

## What problem does this solve?

Moving between directories and understanding filesystem structure

## When do you encounter this?

- *[Add specific scenario when you'd encounter this problem]*
- *[Add another real-world use case]*
- *[Add a third common scenario]*

## Available approaches

### 1. **pwd**
   - **Best for:** Print working directory
   - **Recognition:** `pwd [options] [arguments]`
   - **Tradeoffs:** *[Add tradeoffs and when to use]*

### 2. **ls**
   - **Best for:** List directory contents (with -l, -a, -h flags)
   - **Recognition:** `ls [options] [arguments]`
   - **Tradeoffs:** *[Add tradeoffs and when to use]*

### 3. **cd**
   - **Best for:** Change directory
   - **Recognition:** `cd [options] [arguments]`
   - **Tradeoffs:** *[Add tradeoffs and when to use]*

## Decision tree

**Which tool should I use?**

- Use `pwd` when: *[add condition]*
- Use `ls` when: *[add condition]*
- Use `cd` when: *[add condition]*

## Examples to recognize

```bash
# [Add example command]
# What does this do? [Add explanation]
```

## Try with AI

**Effective prompts to try:**

- "Show me how to [specific task related to this problem]"
- "What's the best way to [another task]?"
- "Explain what this command does: [paste command]"

**When asking AI:**
- Be specific about what you want to accomplish
- Mention any constraints (file types, size limits, etc.)
- Ask for explanations, not just commands

## Related problems

*[Add links to related problem guides]*

---

*This guide was generated from existing content. Please review and enhance with:*
- *More real-world scenarios*
- *Better decision guidance*
- *Additional examples*
- *Clearer AI prompt templates*
```

## Step 4: Enhance the Generated Guide

Now manually enhance the guide with real content:

```markdown
# Problem: Navigating Filesystem

## What problem does this solve?

You need to move between directories, understand where you are in the filesystem,
and explore the directory structure.

## When do you encounter this?

- Exploring a new system or server
- Finding configuration files in /etc
- Understanding a project's directory structure
- Troubleshooting issues by checking different directories
- Setting up your development environment

## Available approaches

### 1. **cd (change directory)**
   - **Best for:** Moving to a different directory
   - **Recognition:** `cd /path/to/dir`, `cd ..`, `cd ~`, `cd -`
   - **Tradeoffs:** Simple and fast, but you need to know where you're going

### 2. **pwd (print working directory)**
   - **Best for:** Finding out your current location
   - **Recognition:** `pwd` (no arguments needed)
   - **Tradeoffs:** Only shows current location, doesn't help you navigate

### 3. **ls (list)**
   - **Best for:** Seeing what's in a directory before or after navigating
   - **Recognition:** `ls`, `ls -la`, `ls /path`
   - **Tradeoffs:** Shows contents but doesn't move you there

## Decision tree

**Which tool should I use?**

- Use `cd` when: You want to move to a different directory
- Use `pwd` when: You're lost and need to know where you are
- Use `ls` when: You want to see what's in a directory without moving there
- Use all three together: `pwd` to check location, `ls` to see options, `cd` to move

## Examples to recognize

```bash
cd /etc/nginx
# What does this do? Navigate to the nginx configuration directory

pwd
# What does this do? Show the current directory path

ls -la ~/.config
# What does this do? List all files (including hidden) in the .config directory

cd ..
# What does this do? Move up one directory level

cd -
# What does this do? Go back to the previous directory
```

## Try with AI

**Effective prompts to try:**

- "Show me how to navigate to my home directory"
- "How do I see hidden files in the current directory?"
- "What command shows my current location in the filesystem?"
- "How do I go back to the previous directory I was in?"

**When asking AI:**
- Mention if you need to see hidden files
- Specify if you want detailed information (like file sizes)
- Ask for explanations of what each part of the command does

## Related problems

- [Understanding Paths](../understanding-paths/) - Learn about absolute vs relative paths
- [Finding Files](../finding-files/) - Locate files across the filesystem
- [Filesystem Mental Model](../filesystem-mental-model/) - Understand how Linux organizes files
```

## Step 5: Repeat for Other Guides

Enhance each generated guide:
- `problems/managing-directories/README.md`
- `problems/finding-files/README.md`
- `problems/file-operations/README.md`

## Step 6: Update Your Knowledge Base

Add to `my-knowledge/problems-i-solve.md`:

```markdown
## Navigating Filesystem
- Problem: Need to move between directories and know where I am
- Solution: Use cd to move, pwd to check location, ls to see contents
- AI prompt: "Show me how to navigate to X directory"
- When: Daily work, exploring systems, finding files

## Managing Directories
- Problem: Create and organize directory structures
- Solution: Use mkdir for creation, rmdir for removal
- AI prompt: "Create a directory structure for X project"
- When: Setting up projects, organizing files
```

## Complete Workflow Summary

```bash
# 1. Analyze existing content
python3 scripts/transform-content.py --analyze

# 2. Generate problem guides
python3 scripts/transform-content.py --generate

# 3. Review each generated guide
# 4. Enhance with real scenarios and examples
# 5. Update your personal knowledge base
# 6. Start using the new problem-focused structure
```

## Tips for Enhancement

**Good scenarios are specific:**
- ❌ "When working with files"
- ✅ "When you need to free up disk space by finding large files"

**Good examples explain WHY:**
- ❌ `find / -name "*.log"`
- ✅ `find / -name "*.log"  # Find all log files on the system for cleanup`

**Good AI prompts are actionable:**
- ❌ "Help me with files"
- ✅ "Show me how to find files larger than 100MB in my home directory"

**Good decision guidance is practical:**
- ❌ "Use find when you need to find files"
- ✅ "Use find when you know part of the filename or need to search by size/date. Use locate when you need fast results and have the full filename."

## Result

You've successfully transformed command-focused content into problem-focused guides that:
- Organize by problems, not commands
- Explain when and why to use each tool
- Include AI collaboration guidance
- Focus on recognition and understanding
- Support modern AI-assisted workflows
