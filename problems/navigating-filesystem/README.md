# Problem: Navigating the Filesystem

## What problem does this solve?

You need to move around the Linux filesystem to access files and directories in different locations. This is like navigating through folders on your computer, but using the command line instead of clicking through a graphical interface.

## When do you encounter this?

- You need to access files in different directories
- You're following instructions that say "go to the /etc directory"
- You're lost and don't know where you are in the filesystem
- You need to see what files and directories are in your current location
- You want to quickly jump to your home directory or a specific location

## Available approaches

### 1. **pwd (Print Working Directory)**
   - **Best for**: Finding out where you currently are
   - **Tradeoffs**: Only shows current location, doesn't move you anywhere
   - **Recognition**: When you see `pwd` alone, it's checking the current location
   - **AI prompt template**: "Show me how to check my current directory location"

### 2. **cd (Change Directory)**
   - **Best for**: Moving to a different directory
   - **Tradeoffs**: Need to know where you want to go
   - **Recognition**: `cd` followed by a path means moving to that location
   - **AI prompt template**: "Show me how to navigate to [directory path]"

### 3. **ls (List)**
   - **Best for**: Seeing what's in a directory
   - **Tradeoffs**: Can be overwhelming with many files; need flags for details
   - **Recognition**: `ls` shows contents; `ls -l` shows detailed info; `ls -a` shows hidden files
   - **AI prompt template**: "Show me how to list all files including hidden ones with details"

### 4. **tree**
   - **Best for**: Visualizing directory structure hierarchically
   - **Tradeoffs**: Can be overwhelming for large directories; may need to install
   - **Recognition**: `tree` shows a visual tree structure of directories
   - **AI prompt template**: "Show me how to display a directory tree structure"

## Decision tree

```
Need to navigate the filesystem?
├─ Don't know where you are? → Use `pwd`
├─ Want to see what's here? → Use `ls` (add -la for details and hidden files)
├─ Want to move somewhere?
│  ├─ Go home? → Use `cd` or `cd ~`
│  ├─ Go up one level? → Use `cd ..`
│  ├─ Go to specific path? → Use `cd /path/to/directory`
│  └─ Go to previous directory? → Use `cd -`
└─ Want to see directory structure? → Use `tree` or `ls -R`
```

## Examples to recognize

### Example 1: Finding your location
```bash
pwd
# Output: /home/username/projects
```
**What it does**: Shows you're currently in the projects directory inside your home folder.
**When to use**: When you're lost or need to confirm your location.

### Example 2: Moving to a specific directory
```bash
cd /etc
pwd
# Output: /etc
```
**What it does**: Changes to the /etc directory (system configuration files).
**When to use**: When you need to access files in a specific location.

### Example 3: Going home
```bash
cd
pwd
# Output: /home/username
```
**What it does**: Takes you to your home directory (shortcut for `cd ~`).
**When to use**: Quick way to get back to your home directory from anywhere.

### Example 4: Moving up one level
```bash
pwd
# Output: /home/username/projects/myapp
cd ..
pwd
# Output: /home/username/projects
```
**What it does**: Moves up one directory level in the hierarchy.
**When to use**: When you want to go to the parent directory.

### Example 5: Listing directory contents
```bash
ls
# Output: file1.txt  file2.txt  mydir/

ls -la
# Output: 
# drwxr-xr-x 2 user user 4096 Dec 10 10:00 .
# drwxr-xr-x 5 user user 4096 Dec 10 09:00 ..
# -rw-r--r-- 1 user user  123 Dec 10 10:00 file1.txt
# -rw-r--r-- 1 user user  456 Dec 10 10:00 file2.txt
# drwxr-xr-x 2 user user 4096 Dec 10 10:00 mydir
```
**What it does**: First shows simple list; second shows detailed info including permissions, owner, size, and hidden files.
**When to use**: When you need to see what's in a directory or get file details.

### Example 6: Going back to previous directory
```bash
cd /var/log
cd /etc
cd -
pwd
# Output: /var/log
```
**What it does**: Returns to the previous directory you were in.
**When to use**: When you need to quickly switch between two directories.

## Common patterns to recognize

### Pattern: Checking location before doing something
```bash
pwd
ls
# Then do some operation
```
**Why**: Good practice to confirm you're in the right place before running commands.

### Pattern: Navigate and list in one go
```bash
cd /some/path && ls
```
**Why**: Combines moving to a directory and seeing what's there.

### Pattern: Relative navigation
```bash
cd ../../../
```
**Why**: Moving up multiple directory levels at once.

## Try with AI

**New to AI collaboration?** Check out the [AI Prompting Guide](../../references/ai-prompting-guide.md) for detailed tips on working effectively with AI.

### How to Use AI for This Problem

**Step 1: Understand what you need**
Before asking AI, be clear about:
- Do you need to know where you are?
- Do you need to see what's in a directory?
- Do you need to move to a different location?
- Do you know the path or just the general direction?

**Step 2: Use a good prompt template**

```
Finding your location:
"Show me how to check what directory I'm currently in"

Listing contents:
"Show me how to list all files in [directory] including [hidden files/details/sizes]"

Moving around:
"Show me how to navigate to [directory path]"
"Show me how to go to my home directory"
"Show me how to go up [N] directory levels"

Combining actions:
"Show me how to navigate to [path] and list all files with details"
```

**Step 3: Verify the AI's solution**

Before running the command, check:
- [ ] Does the path look correct?
- [ ] Will it just navigate/list, or modify anything?
- [ ] Do you have permission to access that directory?
- [ ] Is it using absolute or relative paths appropriately?

**Step 4: Test safely**

```bash
# All navigation commands are SAFE - they don't modify anything
pwd                    # Safe - just shows location
ls                     # Safe - just lists files
cd /some/path          # Safe - just moves you
cd ..                  # Safe - goes up one level

# You can always go back
cd /some/path          # Go somewhere
cd -                   # Go back to previous location
cd ~                   # Go home if you get lost
```

**Step 5: Understand the result**

Ask AI to explain if you don't understand:
- "What does the -la flag do in ls?"
- "What's the difference between cd ~ and cd /"
- "How do I know if a path is absolute or relative?"

### Practice Exercises with AI

**Exercise 1: Check your location (SAFE)**
- **Prompt**: "Show me how to check what directory I'm currently in"
- **Verify**: Should suggest `pwd`
- **Test**: Run it and see your current path
- **Document**: Note when you'd use this

**Exercise 2: List files with details (SAFE)**
- **Prompt**: "Show me how to list all files in the current directory including hidden files and details"
- **Verify**: Should suggest `ls -la` or similar
- **Test**: Run it and observe the output format
- **Document**: Note what each column means

**Exercise 3: Navigate to home (SAFE)**
- **Prompt**: "Show me how to quickly navigate to my home directory"
- **Verify**: Should suggest `cd` or `cd ~`
- **Test**: Try it from different locations
- **Document**: Note this shortcut

**Exercise 4: Navigate and list (SAFE)**
- **Prompt**: "Show me how to navigate to /etc and list all files with details"
- **Verify**: Should suggest `cd /etc && ls -la` or similar
- **Test**: Run it and explore the output
- **Document**: Note the && pattern for combining commands

**Exercise 5: Navigate relatively (SAFE)**
- **Prompt**: "Show me how to go up two directory levels"
- **Verify**: Should suggest `cd ../..`
- **Test**: Try from different locations
- **Document**: Note the .. pattern

**Exercise 6: Return to previous location (SAFE)**
- **Prompt**: "Show me how to go back to the directory I was just in"
- **Verify**: Should suggest `cd -`
- **Test**: Navigate somewhere, then somewhere else, then use cd -
- **Document**: Note this useful shortcut

### Common AI Collaboration Patterns

**Pattern 1: Exploring unfamiliar territory**
```
You: "Show me how to navigate to /var/log"
AI: [gives cd /var/log]
You: [runs it]
You: "Now show me how to list all files here sorted by size"
AI: [gives ls -lhS]
```

**Pattern 2: Understanding where you are**
```
You: [gets lost in filesystem]
You: "Show me how to check where I am and list what's here"
AI: [gives pwd and ls]
You: "How do I get back to my home directory?"
AI: [gives cd or cd ~]
```

**Pattern 3: Building navigation skills**
```
You: "Show me how to navigate to /etc"
AI: [gives cd /etc]
You: "Now how do I go up one level?"
AI: [gives cd ..]
You: "And how do I go back to /etc?"
AI: [gives cd - or cd /etc]
```

### Understanding the Output

**When you run `pwd`:**
```bash
/home/username/projects/myapp
```
This shows your full path from root (/) to your current location.

**When you run `ls -la`:**
```bash
drwxr-xr-x 2 user user 4096 Dec 10 10:00 mydir
-rw-r--r-- 1 user user  123 Dec 10 10:00 file.txt
```
- First column: permissions (d = directory, - = file)
- Numbers: links, owner, group, size
- Date/time: last modified
- Name: file or directory name

Ask AI: "Can you explain what each column means in ls -la output?"

### Verification Checklist

After getting a solution from AI:
- [ ] I understand what this command does
- [ ] I know where it will take me or what it will show
- [ ] I've tested it and the output makes sense
- [ ] I understand the difference between absolute and relative paths
- [ ] I know how to get back if I get lost (cd ~ or cd -)
- [ ] I've documented useful patterns

### Next Steps

1. Practice all the exercises above - they're all safe!
2. Explore different directories on your system
3. Practice using both absolute and relative paths
4. Document navigation patterns in `my-knowledge/problems-i-solve.md`

**Remember**: Navigation commands are safe - you can't break anything by moving around or listing files. Explore freely!

## What to memorize (for exams)

- `pwd` - shows current directory
- `cd` - changes directory
- `cd ~` or just `cd` - goes to home directory
- `cd ..` - goes up one level
- `cd -` - goes to previous directory
- `ls` - lists files
- `ls -l` - detailed list
- `ls -a` - shows hidden files
- `ls -la` - detailed list with hidden files

## Look up as needed

- Specific `ls` flags for sorting and formatting
- `tree` command options
- Complex path navigation patterns
