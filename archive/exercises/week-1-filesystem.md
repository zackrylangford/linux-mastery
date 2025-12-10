# Week 1 Exercises: Filesystem Mastery

Complete these exercises to earn the "Filesystem Explorer" achievement.

## Exercise 1: System Exploration

**Goal**: Navigate and understand the Linux filesystem hierarchy

**Tasks**:
1. Navigate to each of these directories and note what they contain:
   - `/bin` - Essential command binaries
   - `/etc` - System configuration files
   - `/home` - User home directories
   - `/var` - Variable data (logs, caches)
   - `/tmp` - Temporary files
   - `/usr` - User programs and data
   - `/opt` - Optional software
   - `/dev` - Device files
   - `/proc` - Process information
   - `/sys` - System information

2. For each directory, run `ls -la` and note:
   - Who owns the directory
   - What permissions it has
   - Any interesting files

**Document**: Create `exercises/week-1-ex1-notes.md` with your findings

---

## Exercise 2: Directory Structure Creation

**Goal**: Practice creating complex directory structures

**Tasks**:
1. Create this structure in `/tmp/practice`:
```
project/
├── src/
│   ├── main/
│   └── test/
├── docs/
│   ├── api/
│   └── guides/
├── config/
└── logs/
```

2. Create empty files in appropriate locations:
   - `src/main/app.py`
   - `src/test/test_app.py`
   - `docs/README.md`
   - `config/settings.conf`

3. Use `tree` command to verify structure (install if needed: `sudo apt install tree`)

**Commands to use**: `mkdir -p`, `touch`, `tree`

**Document**: Save your commands in `exercises/week-1-ex2-solution.sh`

---

## Exercise 3: File Operations

**Goal**: Master copying, moving, and removing files

**Tasks**:
1. Copy the entire `/tmp/practice` directory to `/tmp/backup`
2. Move `src/main/app.py` to `src/main/application.py`
3. Copy all `.py` files to a new directory `/tmp/python-files`
4. Remove the `test/` directory
5. Remove all files in `logs/` but keep the directory

**Commands to use**: `cp -r`, `mv`, `rm`, `rm -r`, `find`

**Challenge**: Do task 3 using a single command with `find` and `cp`

**Document**: Save your commands in `exercises/week-1-ex3-solution.sh`

---

## Exercise 4: Links and Inodes

**Goal**: Understand hard links and symbolic links

**Tasks**:
1. Create a file: `echo "Original content" > /tmp/original.txt`
2. Create a hard link: `ln /tmp/original.txt /tmp/hardlink.txt`
3. Create a symbolic link: `ln -s /tmp/original.txt /tmp/symlink.txt`
4. Check inodes: `ls -li /tmp/original.txt /tmp/hardlink.txt /tmp/symlink.txt`
5. Modify the original file and check all three files
6. Delete the original file and check what happens to the links

**Questions to answer**:
- What's the inode number of the original and hard link?
- What happens to the hard link when you delete the original?
- What happens to the symbolic link when you delete the original?
- When would you use each type of link?

**Document**: Save your answers in `exercises/week-1-ex4-notes.md`

---

## Exercise 5: Find Command Mastery

**Goal**: Use `find` to locate files efficiently

**Tasks**:
1. Find all `.conf` files in `/etc`
2. Find all files modified in the last 24 hours in your home directory
3. Find all files larger than 100MB in `/var`
4. Find all empty files in `/tmp`
5. Find all files owned by your user in `/tmp`
6. Find and delete all `.log` files older than 7 days in `/tmp`

**Commands to use**: `find` with `-name`, `-mtime`, `-size`, `-empty`, `-user`, `-delete`

**Document**: Save your commands in `exercises/week-1-ex5-solution.sh`

---

## Bonus Challenge: Filesystem Scavenger Hunt

**Goal**: Combine all skills

**Tasks**:
1. Find the largest file in `/var/log`
2. Count how many configuration files (`.conf`) exist in `/etc`
3. Find all symbolic links in `/usr/bin`
4. Create a backup script that:
   - Creates a timestamped backup directory
   - Copies important files to it
   - Creates a log of what was backed up

**Document**: Save your script in `exercises/week-1-bonus-backup.sh`

---

## Completion Checklist

- [ ] Completed Exercise 1: System Exploration
- [ ] Completed Exercise 2: Directory Structure
- [ ] Completed Exercise 3: File Operations
- [ ] Completed Exercise 4: Links and Inodes
- [ ] Completed Exercise 5: Find Command
- [ ] Completed Bonus Challenge
- [ ] All solutions documented
- [ ] Committed to GitHub

**When complete**: Update ACHIEVEMENTS.md and unlock Week 2!
