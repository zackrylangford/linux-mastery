# Problem: Managing Directories

## What problem does this solve?

You need to create, organize, move, copy, or delete directories to keep your files organized. This is essential for maintaining a clean project structure and organizing your work.

## When do you encounter this?

- Starting a new project and need to create a directory structure
- Organizing files into logical groups
- Cleaning up old directories you no longer need
- Copying a directory structure to another location
- Renaming directories to better reflect their contents
- Need to create multiple nested directories at once

## Available approaches

### 1. **mkdir (Make Directory)**
   - **Best for**: Creating new directories
   - **Tradeoffs**: Basic version only creates one level at a time
   - **Recognition**: `mkdir dirname` creates a directory; `mkdir -p path/to/dir` creates nested directories
   - **AI prompt template**: "Show me how to create a directory structure for [describe structure]"

### 2. **rmdir (Remove Directory)**
   - **Best for**: Removing empty directories safely
   - **Tradeoffs**: Only works on empty directories; safer but less flexible
   - **Recognition**: `rmdir dirname` removes an empty directory
   - **AI prompt template**: "Show me how to safely remove an empty directory"

### 3. **rm -r (Remove Recursively)**
   - **Best for**: Removing directories with contents
   - **Tradeoffs**: Dangerous - can delete everything; no undo
   - **Recognition**: `rm -r dirname` deletes directory and all contents; `rm -rf` forces deletion
   - **AI prompt template**: "Show me how to safely delete a directory and its contents"

### 4. **cp -r (Copy Recursively)**
   - **Best for**: Copying entire directory structures
   - **Tradeoffs**: Can take time with large directories
   - **Recognition**: `cp -r source dest` copies directory and all contents
   - **AI prompt template**: "Show me how to copy a directory and all its files to [location]"

### 5. **mv (Move/Rename)**
   - **Best for**: Moving or renaming directories
   - **Tradeoffs**: Moving across filesystems can be slow
   - **Recognition**: `mv oldname newname` renames; `mv dir /path/` moves
   - **AI prompt template**: "Show me how to rename/move a directory to [new location]"

## Decision tree

```
Need to manage directories?
├─ Create new directory?
│  ├─ Single directory? → Use `mkdir dirname`
│  ├─ Nested directories? → Use `mkdir -p path/to/nested/dir`
│  └─ Multiple directories? → Use `mkdir dir1 dir2 dir3`
├─ Delete directory?
│  ├─ Empty directory? → Use `rmdir dirname` (safest)
│  ├─ Directory with contents? → Use `rm -r dirname` (careful!)
│  └─ Force delete everything? → Use `rm -rf dirname` (VERY dangerous!)
├─ Copy directory?
│  └─ With all contents? → Use `cp -r source destination`
└─ Move or rename?
   ├─ Rename in same location? → Use `mv oldname newname`
   └─ Move to different location? → Use `mv dirname /new/path/`
```

## Examples to recognize

### Example 1: Creating a single directory
```bash
mkdir projects
ls
# Output: projects/
```
**What it does**: Creates a new directory called "projects" in the current location.
**When to use**: When you need a new folder for organizing files.

### Example 2: Creating nested directories
```bash
mkdir -p projects/myapp/src/components
tree projects
# Output:
# projects/
# └── myapp/
#     └── src/
#         └── components/
```
**What it does**: Creates the entire directory path, including all parent directories that don't exist.
**When to use**: When you need to create a deep directory structure quickly.

### Example 3: Creating multiple directories at once
```bash
mkdir docs tests src
ls
# Output: docs/  src/  tests/
```
**What it does**: Creates three directories in one command.
**When to use**: When setting up a project structure with multiple top-level folders.

### Example 4: Removing an empty directory
```bash
rmdir old-project
# Success if empty, error if not
```
**What it does**: Safely removes a directory only if it's empty.
**When to use**: When you want to clean up but ensure you don't accidentally delete files.

### Example 5: Removing a directory with contents
```bash
rm -r old-project
# Deletes directory and everything inside
```
**What it does**: Removes the directory and all files/subdirectories inside it.
**When to use**: When you're sure you want to delete everything in that directory.
**Warning**: This is permanent! No undo!

### Example 6: Copying a directory
```bash
cp -r myproject myproject-backup
ls
# Output: myproject/  myproject-backup/
```
**What it does**: Creates a complete copy of the directory and all its contents.
**When to use**: When you want to backup or duplicate a project structure.

### Example 7: Renaming a directory
```bash
mv old-name new-name
ls
# Output: new-name/
```
**What it does**: Renames the directory from "old-name" to "new-name".
**When to use**: When you want to give a directory a better name.

### Example 8: Moving a directory
```bash
mv myproject /home/username/projects/
ls /home/username/projects/
# Output: myproject/
```
**What it does**: Moves the directory to a different location.
**When to use**: When you want to reorganize your filesystem structure.

## Common patterns to recognize

### Pattern: Create project structure
```bash
mkdir -p myproject/{src,tests,docs,config}
```
**Why**: Creates a standard project layout with multiple directories in one command.
**What it does**: Uses brace expansion to create multiple subdirectories.

### Pattern: Safe deletion check
```bash
ls dirname
rm -r dirname
```
**Why**: List contents first to verify what you're about to delete.

### Pattern: Backup before modifying
```bash
cp -r important-dir important-dir.backup
# Then modify important-dir
```
**Why**: Create a safety copy before making changes.

### Pattern: Conditional directory creation
```bash
mkdir -p logs
# Creates logs/ if it doesn't exist, does nothing if it does
```
**Why**: Safe way to ensure a directory exists without errors.

## Try with AI

**New to AI collaboration?** Check out the [AI Prompting Guide](../../references/ai-prompting-guide.md) for detailed tips on working effectively with AI.

### How to Use AI for This Problem

**Step 1: Understand what you need**
Before asking AI, be clear about:
- Are you creating, deleting, copying, or moving directories?
- Do you need a single directory or a nested structure?
- Does the directory have contents or is it empty?
- Do you need to preserve permissions or timestamps?

**Step 2: Use a good prompt template**

```
Creating directories:
"Show me how to create a directory called [name]"
"Show me how to create a nested directory structure [path/to/nested/dir]"
"Show me how to create multiple directories [list] at once"

Deleting directories:
"Show me how to safely remove an empty directory called [name]"
"Show me how to delete a directory and all its contents called [name]"

Copying directories:
"Show me how to copy directory [source] to [destination] with all its contents"

Moving/renaming:
"Show me how to rename directory [old] to [new]"
"Show me how to move directory [source] to [destination]"
```

**Step 3: Verify the AI's solution**

Before running the command, check:
- [ ] Are the directory names/paths correct?
- [ ] Will it delete anything? (look for `rm`, `rmdir`)
- [ ] If deleting, do you have a backup?
- [ ] If creating nested dirs, does it use `-p` flag?
- [ ] Can you test it safely first?

**Step 4: Test safely**

```bash
# SAFE: Creating directories
mkdir test-dir                    # Safe - creates directory
mkdir -p path/to/nested/dir       # Safe - creates nested structure

# SAFE: Listing to verify
ls -la                            # Check what you created

# CAUTION: Deleting empty directories
rmdir test-dir                    # Safe - only works if empty

# DANGEROUS: Deleting with contents
rm -r test-dir                    # Deletes everything inside!
rm -rf test-dir                   # Force deletes - VERY dangerous!

# BEST PRACTICE: Check before deleting
ls -la dirname                    # 1. See what's inside
rmdir dirname                     # 2. Try safe removal first
rm -r dirname                     # 3. Only if you're sure
```

**Step 5: Understand the result**

Ask AI to explain if you don't understand:
- "What's the difference between mkdir and mkdir -p?"
- "Why did rmdir give an error?"
- "What does rm -rf do and why is it dangerous?"

### Practice Exercises with AI

**Exercise 1: Create a single directory (SAFE)**
- **Prompt**: "Show me how to create a new directory called 'my-project'"
- **Verify**: Should suggest `mkdir my-project`
- **Test**: Run it and verify with `ls`
- **Document**: Note this basic pattern

**Exercise 2: Create nested structure (SAFE)**
- **Prompt**: "Show me how to create a nested directory structure projects/myapp/src in one command"
- **Verify**: Should suggest `mkdir -p projects/myapp/src`
- **Test**: Run it and verify with `tree` or `ls -R`
- **Document**: Note the -p flag for nested creation

**Exercise 3: Create multiple directories (SAFE)**
- **Prompt**: "Show me how to create three directories called src, tests, and docs in one command"
- **Verify**: Should suggest `mkdir src tests docs`
- **Test**: Run it and verify with `ls`
- **Document**: Note you can create multiple at once

**Exercise 4: Copy a directory (SAFE)**
- **Prompt**: "Show me how to copy a directory called 'project' to 'project-backup' with all its contents"
- **Verify**: Should suggest `cp -r project project-backup`
- **Test**: Create a test directory first, add some files, then copy
- **Document**: Note the -r flag for recursive copy

**Exercise 5: Rename a directory (SAFE)**
- **Prompt**: "Show me how to rename a directory from 'old-name' to 'new-name'"
- **Verify**: Should suggest `mv old-name new-name`
- **Test**: Create a test directory and rename it
- **Document**: Note that mv is used for renaming

**Exercise 6: Remove empty directory (SAFE)**
- **Prompt**: "Show me how to safely remove an empty directory"
- **Verify**: Should suggest `rmdir dirname`
- **Test**: Create an empty test directory and remove it
- **Document**: Note this only works on empty directories

**⚠️ DANGEROUS EXERCISE - Only try with test data:**

**Exercise 7: Remove directory with contents (CAUTION)**
- **Prompt**: "Show me how to remove a directory and all its contents, but let me verify first"
- **Verify**: Should suggest listing first, then `rm -r`
- **Test**: Create a test directory with some test files
- **Document**: Note the danger and verification steps

### Common AI Collaboration Patterns

**Pattern 1: Building project structure**
```
You: "Show me how to create a project structure for a web app"
AI: [gives basic mkdir commands]
You: "Can you show me how to create src, tests, docs, and config directories all at once?"
AI: [gives mkdir src tests docs config]
You: "And how do I create subdirectories under src like components and utils?"
AI: [gives mkdir -p src/{components,utils}]
```

**Pattern 2: Safe deletion workflow**
```
You: "Show me how to delete a directory called old-project"
AI: [gives rm -r old-project]
You: "How can I check what's inside first before deleting?"
AI: [gives ls -la old-project or tree old-project]
You: [checks contents]
You: "OK, now show me how to delete it"
AI: [gives rm -r old-project]
```

**Pattern 3: Understanding errors**
```
You: [tries rmdir on non-empty directory]
You: "I got 'Directory not empty' error. What does this mean?"
AI: [explains rmdir only works on empty directories]
You: "How do I remove it if it has files?"
AI: [explains rm -r and warns about danger]
```

### Safety Guidelines

**⚠️ CRITICAL: Directory deletion is permanent!**

**DO:**
- ✅ Use `ls` to check contents before deleting
- ✅ Use `rmdir` for empty directories (safer)
- ✅ Create backups before deleting important directories
- ✅ Test commands on test directories first
- ✅ Double-check paths before running rm -r

**DON'T:**
- ❌ Use `rm -rf` without being absolutely sure
- ❌ Delete directories you don't understand
- ❌ Use wildcards with rm -r without testing
- ❌ Run rm -rf with sudo unless you know exactly why
- ❌ Delete system directories (/etc, /usr, /var, etc.)

**If unsure, ask AI:**
- "Is it safe to delete this directory?"
- "How can I check what's inside before deleting?"
- "Can I undo this if I make a mistake?" (Answer: No!)

### Verification Checklist

After getting a solution from AI:
- [ ] I understand what this command will do
- [ ] I know which directories it will affect
- [ ] If deleting, I've verified the contents first
- [ ] If deleting, I have a backup if needed
- [ ] I've tested on a safe test directory first
- [ ] I understand I cannot undo deletions
- [ ] I've documented the working solution

### Next Steps

1. Start with SAFE exercises (creating, copying, renaming)
2. Practice on test directories, not real projects
3. Only practice deletion on directories you created for testing
4. Document patterns in `my-knowledge/problems-i-solve.md`

**Remember**: Creating and copying directories is safe. Deleting is permanent - always verify first!

## What to memorize (for exams)

- `mkdir dirname` - creates a directory
- `mkdir -p path/to/dir` - creates nested directories
- `rmdir dirname` - removes empty directory
- `rm -r dirname` - removes directory and contents
- `rm -rf dirname` - force removes directory (dangerous!)
- `cp -r source dest` - copies directory recursively
- `mv oldname newname` - renames/moves directory

## Look up as needed

- Specific flags for preserving permissions when copying
- Advanced brace expansion patterns
- Options for handling symbolic links
- Flags for verbose output or interactive prompts

## Safety tips

⚠️ **DANGER ZONE**: `rm -rf` is extremely dangerous!
- It deletes everything without asking
- It can delete your entire system if you're not careful
- Always double-check the path before running
- Consider using `rm -ri` for interactive deletion (asks before each file)

💡 **Best practices**:
- Use `ls` to verify what you're about to delete
- Use `rmdir` instead of `rm -r` when possible (safer)
- Create backups before deleting important directories
- Use tab completion to avoid typos in paths
