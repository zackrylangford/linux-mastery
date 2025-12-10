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

### Beginner prompts
- "Show me how to check what directory I'm currently in"
- "How do I move to my home directory?"
- "Show me how to list all files in the current directory"

### Intermediate prompts
- "Show me how to navigate to /var/log and list all files with details"
- "How do I go up two directory levels?"
- "Show me how to list all files including hidden ones, sorted by modification time"

### Advanced prompts
- "Show me how to navigate to a directory and create a backup of all .txt files"
- "How do I find my current location and save it to return later?"

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
