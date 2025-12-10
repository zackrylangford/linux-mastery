# Mental Model: Understanding the Linux Filesystem

## The Big Idea: Everything is a File

The most important concept in Linux is: **Everything is a file**.

This isn't literally true, but it's how Linux *thinks* about the world. Understanding this mental model will help you reason about Linux systems even when you encounter something new.

### What does "everything is a file" mean?

In Linux, almost everything you interact with is treated as a file:
- Regular files (documents, images, programs) → files
- Directories → special files that contain other files
- Devices (keyboard, mouse, hard drive) → files in `/dev/`
- Network connections → can be treated as files
- Running processes → have file-like interfaces in `/proc/`
- System information → files in `/sys/`

**Why this matters**: Once you understand how to work with files, you understand how to work with almost everything in Linux. The same tools and concepts apply everywhere.

### Example: Reading from a device like a file

```bash
# Your hard drive is a file
cat /dev/sda  # Don't actually do this! But it shows the concept

# System information is in files
cat /proc/cpuinfo  # Read CPU information like a text file
cat /sys/class/net/eth0/address  # Read network MAC address
```

## Mental Model 1: The Directory Tree

### The Core Concept

Linux organizes everything as a **single tree structure** starting from the root (`/`). There are no drive letters like Windows (C:, D:). Everything branches from one root.

```
/                           ← The root (top of everything)
├── home/                   ← User home directories
│   ├── alice/              ← Alice's personal space
│   │   ├── documents/
│   │   ├── downloads/
│   │   └── projects/
│   └── bob/                ← Bob's personal space
│       └── documents/
├── etc/                    ← System configuration files
│   ├── hostname
│   ├── passwd
│   └── ssh/
├── var/                    ← Variable data (logs, caches)
│   ├── log/
│   └── tmp/
├── usr/                    ← User programs and libraries
│   ├── bin/                ← User commands
│   └── lib/                ← Shared libraries
├── bin/                    ← Essential system commands
├── tmp/                    ← Temporary files
└── dev/                    ← Device files
```

### Key Insights

1. **Single root**: Everything starts from `/`. When you plug in a USB drive, it doesn't become "D:" - it gets mounted somewhere in the tree (like `/media/usb`).

2. **Hierarchical**: Directories contain other directories and files, forming a tree. You navigate by going up (toward root) or down (into subdirectories).

3. **Paths describe location**: A path is just directions through the tree:
   - `/home/alice/documents/report.txt` means: start at root, go to home, then alice, then documents, then report.txt

4. **Everything has a place**: The filesystem hierarchy has conventions:
   - `/home/` - user files
   - `/etc/` - configuration
   - `/var/log/` - log files
   - `/tmp/` - temporary files
   - `/usr/bin/` - programs

### Why This Matters

When you understand the tree structure:
- You know that `..` means "go up one branch"
- You understand why `/home/alice/file.txt` and `/home/bob/file.txt` are different files
- You can reason about where things should be located
- You understand what "mounting" means (attaching a new branch to the tree)

## Mental Model 2: Absolute vs Relative Paths

### The Core Concept

There are two ways to describe a location in the tree:

1. **Absolute path**: Directions from the root
   - Always starts with `/`
   - Always the same, no matter where you are
   - Like a street address: "123 Main St, Springfield"

2. **Relative path**: Directions from where you are now
   - Doesn't start with `/`
   - Changes based on your current location
   - Like directions: "two blocks north, then left"

### Visualizing the Difference

Imagine you're at `/home/alice/projects/myapp/`:

```
/                                    ← Root
└── home/
    └── alice/                       ← Alice's home
        ├── documents/
        │   └── report.txt
        └── projects/
            ├── myapp/               ← YOU ARE HERE
            │   ├── src/
            │   └── README.md
            └── other-app/
                └── config.json
```

**To access report.txt:**
- Absolute: `/home/alice/documents/report.txt` (from root)
- Relative: `../../documents/report.txt` (up 2, then down)
- Home: `~/documents/report.txt` (from home directory)

**To access README.md:**
- Absolute: `/home/alice/projects/myapp/README.md`
- Relative: `./README.md` or just `README.md` (in current directory)

**To access config.json:**
- Absolute: `/home/alice/projects/other-app/config.json`
- Relative: `../other-app/config.json` (up 1, then down)

### Key Insights

1. **Absolute paths are reliable**: They always point to the same place, regardless of where you are. Great for scripts and configuration files.

2. **Relative paths are convenient**: When working within a project, it's easier to type `../config.json` than `/home/alice/projects/other-app/config.json`.

3. **Current location matters**: With relative paths, you need to know where you are. Use `pwd` to check.

4. **Special symbols**:
   - `.` = current directory
   - `..` = parent directory (one level up)
   - `~` = your home directory
   - `/` = root directory

### Mental Model for Navigation

Think of the filesystem as a building:
- **Absolute path**: "Room 305, Building A, 123 Main St" - exact location
- **Relative path**: "Two floors up, third door on the left" - depends on where you start
- **Home path**: "My apartment" - your personal space

## Mental Model 3: Directories Are Containers

### The Core Concept

A directory is just a special file that contains a list of other files and directories. It's a container, not a location.

### Key Insights

1. **Directories contain references**: When you put a file "in" a directory, you're really just adding its name to the directory's list.

2. **Files don't "know" where they are**: A file doesn't store its own path. The directory structure creates the path.

3. **Moving is renaming**: When you move a file, you're just changing which directory lists it. The file data doesn't move (usually).

```bash
# These are the same operation internally:
mv file.txt newname.txt          # Rename in same directory
mv file.txt ../other/file.txt    # Move to different directory
```

4. **Deleting a directory**: You can't delete a directory that contains files because it's still "holding" references to them. You must either:
   - Remove all files first, then `rmdir` the directory
   - Use `rm -r` to remove the directory and all its contents

### Why This Matters

Understanding directories as containers helps you understand:
- Why you can't `rmdir` a non-empty directory
- Why moving files within the same filesystem is instant (just updating the directory list)
- Why hard links work (multiple directories can list the same file)
- Why you need `-r` (recursive) flag to copy/delete directories

## Mental Model 4: The Filesystem Hierarchy Standard (FHS)

### The Core Concept

Linux systems follow conventions about where different types of files go. This isn't enforced by the system, but everyone follows these conventions.

### The Main Branches

```
/
├── /home/          Your files live here
│   └── username/   Each user has their own space
│
├── /etc/           Configuration files
│                   "How should programs behave?"
│
├── /var/           Variable data (changes during operation)
│   ├── /var/log/   Log files
│   └── /var/tmp/   Temporary files that persist across reboots
│
├── /usr/           User programs (not "user files"!)
│   ├── /usr/bin/   Most programs you run
│   └── /usr/lib/   Shared libraries
│
├── /bin/           Essential system programs
│                   (needed to boot and repair the system)
│
├── /tmp/           Temporary files (deleted on reboot)
│
├── /dev/           Device files
│                   (your hardware appears here)
│
├── /proc/          Process information
│                   (running programs appear here)
│
└── /sys/           System information
                    (kernel and hardware info)
```

### Key Insights

1. **User files vs system files**:
   - Your stuff: `/home/username/`
   - System configuration: `/etc/`
   - Programs: `/usr/bin/` and `/bin/`

2. **Temporary vs permanent**:
   - `/tmp/` - deleted on reboot
   - `/var/tmp/` - persists across reboots
   - Your home directory - permanent (until you delete it)

3. **Configuration is in files**:
   - Most programs read configuration from `/etc/`
   - User-specific config is in `~/.config/` or `~/.programname`
   - This is why "everything is a file" is powerful

4. **Logs are in /var/log/**:
   - When something goes wrong, look here
   - Each program typically has its own log file

### Why This Matters

When you know the conventions:
- You know where to look for configuration files (`/etc/`)
- You know where to look for logs (`/var/log/`)
- You know where your files should go (`/home/username/`)
- You can navigate any Linux system, even if you've never seen it before

## Putting It All Together

### Scenario: You want to edit a configuration file

1. **Everything is a file**: Configuration is stored in text files
2. **Directory tree**: Config files are in `/etc/`
3. **Absolute path**: `/etc/ssh/sshd_config` always refers to the same file
4. **Hierarchy**: You need to navigate to `/etc/ssh/` or use the full path

```bash
# Using absolute path (works from anywhere)
sudo vim /etc/ssh/sshd_config

# Using navigation
cd /etc/ssh
sudo vim sshd_config
```

### Scenario: You're working on a project

1. **Directory tree**: Your project is at `/home/alice/projects/myapp/`
2. **Relative paths**: Within the project, use relative paths for portability
3. **Directories as containers**: Organize code into subdirectories

```bash
cd ~/projects/myapp
./build.sh              # Relative path
vim src/main.py         # Relative path
cat README.md           # Relative path
```

### Scenario: You need to find where a program is installed

1. **Hierarchy conventions**: Programs are in `/usr/bin/` or `/bin/`
2. **Everything is a file**: Programs are just executable files

```bash
which python3
# Output: /usr/bin/python3

ls -l /usr/bin/python3
# Shows it's a file with execute permissions
```

## Common "Aha!" Moments

### "Why can't I just delete this directory?"
Because it's not empty! Directories are containers - you need to empty them first or use `rm -r`.

### "Why does my script work in one directory but not another?"
You're using relative paths! They depend on where you run the script from. Use absolute paths in scripts.

### "Where did my USB drive go?"
It's mounted somewhere in the tree, probably `/media/` or `/mnt/`. Use `lsblk` or `df` to find it.

### "Why are there so many 'bin' directories?"
- `/bin/` - essential system commands (needed to boot)
- `/usr/bin/` - regular user programs
- `~/bin/` - your personal scripts
They're organized by importance and who uses them.

### "What's the difference between /tmp and /var/tmp?"
- `/tmp/` - deleted on reboot, use for truly temporary stuff
- `/var/tmp/` - persists across reboots, use for temporary files you might need later

## Practice Thinking in These Models

### Exercise 1: Trace a path
Starting from `/home/alice/projects/app/src/`, trace these paths:
- `../../docs/README.md` → `/home/alice/projects/docs/README.md`
- `/etc/hostname` → `/etc/hostname` (absolute, doesn't change)
- `../tests/test.py` → `/home/alice/projects/app/tests/test.py`

### Exercise 2: Choose the right path type
For each scenario, decide: absolute, relative, or home path?
- Script that reads `/etc/config.conf` → Absolute (always the same)
- Accessing `../data/input.txt` in a project → Relative (portable)
- Opening `~/documents/notes.txt` → Home (your personal files)

### Exercise 3: Predict the location
Where would you expect to find:
- SSH configuration → `/etc/ssh/`
- System logs → `/var/log/`
- Your downloads → `~/Downloads/` or `/home/username/Downloads/`
- Temporary files → `/tmp/`

## Try with AI

**New to AI collaboration?** Check out the [AI Prompting Guide](../../references/ai-prompting-guide.md) for detailed tips on working effectively with AI.

### How to Use AI to Deepen Your Understanding

Mental models are about understanding concepts, not memorizing commands. AI can help you explore and test your understanding.

**Step 1: Ask for explanations**

```
"Explain the 'everything is a file' concept in Linux with examples"
"Why does Linux use a single tree structure instead of drive letters?"
"What's the practical difference between absolute and relative paths?"
```

**Step 2: Test your understanding**

```
"I'm in /home/user/projects/app/src. What does ../../docs/README.md resolve to?"
"Where would I find [type of file] in the Linux filesystem hierarchy?"
"Why can't I delete a directory that has files in it?"
```

**Step 3: Explore edge cases**

```
"What happens when I move a file between directories?"
"How does the filesystem handle symbolic links?"
"Why do some programs have config in /etc and others in ~/.config?"
```

### Practice Exercises with AI

**Exercise 1: Understanding "everything is a file"**
- **Prompt**: "Show me examples of how devices, processes, and network connections are treated as files in Linux"
- **Follow-up**: "Show me how to read system information from /proc/ as if it were a text file"
- **Document**: Note examples that help you remember this concept

**Exercise 2: Tracing paths**
- **Prompt**: "I'm in /home/alice/projects/myapp/src. Trace these paths for me: ../README.md, ../../other-app/config.json, ~/documents/notes.txt"
- **Follow-up**: "Explain step-by-step how each path resolves"
- **Document**: Note the pattern for resolving relative paths

**Exercise 3: Filesystem hierarchy**
- **Prompt**: "Where would I find [configuration files / log files / temporary files / user programs] in the Linux filesystem and why?"
- **Follow-up**: "Show me examples of actual files in each location"
- **Document**: Create your own mental map of important locations

**Exercise 4: Understanding directory operations**
- **Prompt**: "Explain why moving a file within the same filesystem is instant but copying takes time"
- **Follow-up**: "What's actually happening when I run mv vs cp?"
- **Document**: Note the mental model that helps you understand this

**Exercise 5: Absolute vs relative paths**
- **Prompt**: "I'm writing a script that needs to read a config file. Should I use an absolute or relative path? Why?"
- **Follow-up**: "Show me examples of when each type is appropriate"
- **Document**: Note your decision-making criteria

**Exercise 6: Exploring the tree structure**
- **Prompt**: "Show me how to visualize the directory tree structure starting from /home/user"
- **Follow-up**: "Explain how this tree structure affects navigation commands"
- **Document**: Draw your own tree diagram for your system

### Common AI Collaboration Patterns

**Pattern 1: Concept to practice**
```
You: "Explain the directory tree concept"
AI: [gives explanation]
You: "Show me commands to explore this tree structure on my system"
AI: [gives tree, ls -R, find commands]
You: [tries them]
You: "Now I see it! Can you show me how to navigate between branches?"
AI: [gives cd examples]
```

**Pattern 2: Testing understanding**
```
You: "I think relative paths are like directions from where you are. Is that right?"
AI: [confirms and elaborates]
You: "Give me a quiz question to test if I understand"
AI: [provides scenario]
You: [answers]
You: "How did I do?"
AI: [provides feedback]
```

**Pattern 3: Connecting concepts**
```
You: "How does the 'everything is a file' concept relate to the directory tree?"
AI: [explains connection]
You: "Show me a practical example where understanding both concepts helps"
AI: [provides real-world scenario]
```

### Deepening Your Mental Models

**Ask AI to help you visualize:**
- "Draw a diagram showing how /home/user/projects relates to the root"
- "Show me a visual representation of absolute vs relative paths"
- "Create a map of the most important directories in /etc"

**Ask AI to provide analogies:**
- "Explain the Linux filesystem using a real-world analogy"
- "Compare absolute and relative paths to something from everyday life"
- "What's a good analogy for understanding why directories can't be deleted when they have files?"

**Ask AI for real-world scenarios:**
- "Give me a scenario where understanding the filesystem hierarchy would help me troubleshoot"
- "Show me a real problem that's easier to solve when you understand 'everything is a file'"
- "What's a common mistake people make when they don't understand relative paths?"

### Verification Checklist

After working with AI on mental models:
- [ ] I can explain the concept in my own words
- [ ] I can provide my own examples
- [ ] I understand why this concept matters practically
- [ ] I can apply this mental model to solve problems
- [ ] I can predict what will happen in new situations
- [ ] I've tested my understanding with real commands

### Next Steps

1. Pick one mental model and explore it deeply with AI
2. Test your understanding by predicting outcomes
3. Apply the mental model to solve a real problem
4. Document your understanding in `my-knowledge/problems-i-solve.md`
5. Move to the next mental model

**Remember**: Mental models are about understanding WHY, not memorizing WHAT. Use AI to explore concepts until they click, then apply them to real situations.

## Key Takeaways

1. **Everything is a file** - This mental model unifies how you interact with Linux
2. **Single tree structure** - Everything branches from `/`, no drive letters
3. **Absolute vs relative** - Two ways to describe the same location
4. **Directories are containers** - They hold references to files
5. **Conventions matter** - The FHS tells you where things should be

When you internalize these mental models, Linux stops feeling arbitrary and starts making sense. You can reason about new situations because you understand the underlying principles.
