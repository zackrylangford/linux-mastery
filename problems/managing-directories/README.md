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

### Beginner prompts
- "Show me how to create a new directory called 'my-project'"
- "How do I delete an empty directory?"
- "Show me how to rename a directory"

### Intermediate prompts
- "Show me how to create a project structure with src, tests, and docs folders"
- "How do I copy a directory and all its files to a backup location?"
- "Show me how to safely delete a directory that has files in it"

### Advanced prompts
- "Show me how to create a nested directory structure for a web app with frontend and backend folders"
- "How do I move all directories matching a pattern to a different location?"
- "Show me how to create a directory structure from a list in a file"

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
