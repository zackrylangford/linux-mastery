# Linux Pattern Recognition Guide

This guide helps you recognize common Linux patterns and idioms when you see them in scripts, documentation, or on exams. You don't need to memorize the exact syntax - just understand what each pattern does and when it's used.

## What is a Pattern?

A **pattern** is a common way of combining commands or using syntax that you'll see repeatedly in Linux. Recognizing these patterns helps you:
- Understand what a script does without running it
- Know what to ask AI for when solving problems
- Pass certification exams that test recognition
- Read documentation and examples more quickly

---

## Table of Contents

- [Pipes and Chaining](#pipes-and-chaining)
- [Redirection Patterns](#redirection-patterns)
- [Wildcards and Globbing](#wildcards-and-globbing)
- [Command Substitution](#command-substitution)
- [Quoting Patterns](#quoting-patterns)
- [Conditional Execution](#conditional-execution)
- [Looping Patterns](#looping-patterns)
- [Common Idioms](#common-idioms)

---

## Pipes and Chaining

### Pattern: Basic Pipe

**What it looks like:**
```bash
command1 | command2
```

**What it does:**
- Takes output from `command1` and feeds it as input to `command2`
- The pipe (`|`) connects commands together
- Data flows left to right

**When you see it:**
- Filtering output: `ps aux | grep firefox`
- Processing data: `cat file.txt | sort | uniq`
- Counting results: `ls | wc -l`

**Examples:**

```bash
# Find and count processes
ps aux | grep python | wc -l
```
**Reading this:** List all processes → filter for "python" → count the lines

```bash
# Sort and remove duplicates
cat names.txt | sort | uniq
```
**Reading this:** Show file → sort lines → remove duplicates

```bash
# Find largest directories
du -sh * | sort -h | tail -5
```
**Reading this:** Show sizes → sort by size → show last 5 (largest)

### Pattern: Multi-Stage Pipeline

**What it looks like:**
```bash
command1 | command2 | command3 | command4
```

**What it does:**
- Chains multiple transformations together
- Each command processes the output of the previous one
- Common in data processing and analysis

**When you see it:**
- Complex filtering and sorting
- Data transformation pipelines
- Log analysis

**Examples:**

```bash
# Top 10 most common lines in a file
cat file.txt | sort | uniq -c | sort -rn | head -10
```
**Reading this:** Show file → sort → count occurrences → sort by count (descending) → show top 10

```bash
# Find processes using most memory
ps aux | awk '{print $4, $11}' | sort -rn | head -5
```
**Reading this:** List processes → extract memory% and command → sort by memory → show top 5

---

## Redirection Patterns

### Pattern: Output to File (Overwrite)

**What it looks like:**
```bash
command > file.txt
```

**What it does:**
- Sends command output to a file
- **Overwrites** the file if it exists
- Creates the file if it doesn't exist

**When you see it:**
- Saving command output
- Creating files from command results
- Logging (but usually append is better)

**Examples:**

```bash
# Save process list to file
ps aux > processes.txt
```

```bash
# Save error messages
find / -name "*.conf" 2> errors.txt
```
**Note:** `2>` redirects error output (stderr)

### Pattern: Output to File (Append)

**What it looks like:**
```bash
command >> file.txt
```

**What it does:**
- Adds command output to end of file
- **Doesn't overwrite** existing content
- Creates the file if it doesn't exist

**When you see it:**
- Logging over time
- Building up results
- Adding to existing files

**Examples:**

```bash
# Append to log file
echo "$(date): Backup completed" >> backup.log
```

```bash
# Collect results over time
find /home -name "*.tmp" >> temp-files.txt
```

### Pattern: Redirect Both Output and Errors

**What it looks like:**
```bash
command > file.txt 2>&1
# or modern syntax:
command &> file.txt
```

**What it does:**
- Redirects both standard output and error output to same file
- `2>&1` means "send stderr (2) to wherever stdout (1) is going"
- `&>` is shorthand for the same thing

**When you see it:**
- Capturing all output for debugging
- Logging everything from a command
- Suppressing all output: `command &> /dev/null`

**Examples:**

```bash
# Save all output from a script
./backup-script.sh &> backup.log
```

```bash
# Suppress all output
find / -name "*.conf" 2> /dev/null
```
**Reading this:** Find files, but throw away error messages

### Pattern: Input from File

**What it looks like:**
```bash
command < input.txt
```

**What it does:**
- Feeds file contents as input to command
- Less common than pipes, but useful for some commands

**When you see it:**
- Feeding data to commands that expect stdin
- Batch processing

**Examples:**

```bash
# Sort contents of file
sort < unsorted.txt > sorted.txt
```

```bash
# Count lines in file
wc -l < file.txt
```

---

## Wildcards and Globbing

### Pattern: Match Any Characters (*)

**What it looks like:**
```bash
*.txt
file*
*backup*
```

**What it does:**
- `*` matches zero or more characters
- Used for matching multiple files
- Shell expands it before running command

**When you see it:**
- Operating on multiple files
- Finding files by pattern
- Batch operations

**Examples:**

```bash
# List all text files
ls *.txt
```

```bash
# Delete all backup files
rm *backup*
```

```bash
# Copy all log files
cp /var/log/*.log ~/logs/
```

### Pattern: Match Single Character (?)

**What it looks like:**
```bash
file?.txt
test-?.log
```

**What it does:**
- `?` matches exactly one character
- More specific than `*`
- Useful for numbered files

**When you see it:**
- Matching files with single-character variations
- Numbered sequences

**Examples:**

```bash
# Match file1.txt, file2.txt, but not file10.txt
ls file?.txt
```

```bash
# Match test-a.log, test-b.log, etc.
cat test-?.log
```

### Pattern: Match Character Range ([])

**What it looks like:**
```bash
file[1-5].txt
[a-z]*.log
[0-9][0-9].txt
```

**What it does:**
- `[...]` matches one character from the set
- Can specify ranges: `[a-z]`, `[0-9]`
- Can list specific characters: `[abc]`

**When you see it:**
- More precise matching than `*` or `?`
- Matching specific patterns

**Examples:**

```bash
# Match file1.txt through file5.txt
ls file[1-5].txt
```

```bash
# Match files starting with lowercase letter
ls [a-z]*.txt
```

---

## Command Substitution

### Pattern: Capture Command Output

**What it looks like:**
```bash
$(command)
# or older syntax:
`command`
```

**What it does:**
- Runs the command and replaces it with its output
- The output becomes part of another command
- Modern syntax uses `$(...)`, old syntax uses backticks

**When you see it:**
- Using command output as arguments
- Dynamic values in commands
- Scripting

**Examples:**

```bash
# Kill process by name
kill $(pgrep firefox)
```
**Reading this:** Run `pgrep firefox` to get PID, then kill that PID

```bash
# Create dated backup
cp file.txt backup-$(date +%Y%m%d).txt
```
**Reading this:** Copy file with today's date in the name

```bash
# Count files in directory
echo "There are $(ls | wc -l) files here"
```

```bash
# Use current directory name
tar -czf $(basename $(pwd)).tar.gz .
```
**Reading this:** Create archive named after current directory

---

## Quoting Patterns

### Pattern: Double Quotes (Variable Expansion)

**What it looks like:**
```bash
"$variable"
"text with $variable in it"
```

**What it does:**
- Preserves spaces and special characters
- **Allows** variable expansion (`$variable` is replaced)
- **Allows** command substitution (`$(command)` is executed)

**When you see it:**
- Protecting spaces in filenames
- Using variables in strings
- Most common quoting pattern

**Examples:**

```bash
# Handle filename with spaces
cp "$filename" /backup/
```

```bash
# Use variable in string
echo "Hello, $USER! Today is $(date)"
```

### Pattern: Single Quotes (Literal)

**What it looks like:**
```bash
'$variable'
'text with $variable in it'
```

**What it does:**
- Everything is literal - no expansion
- `$variable` stays as literal text
- Use when you want exact text

**When you see it:**
- Preventing variable expansion
- Literal strings with special characters
- Passing arguments to other programs

**Examples:**

```bash
# Print literal text
echo 'The variable $HOME is not expanded'
```

```bash
# Search for literal dollar sign
grep '$' file.txt
```

### Pattern: No Quotes (Word Splitting)

**What it looks like:**
```bash
$variable
$(command)
```

**What it does:**
- Variables and commands are expanded
- Spaces cause word splitting
- Wildcards are expanded
- **Dangerous** with filenames containing spaces

**When you see it:**
- Simple cases without spaces
- Intentional word splitting
- Often a mistake in scripts

**Examples:**

```bash
# Safe: no spaces expected
cd $HOME
```

```bash
# Dangerous: filename might have spaces
cp $file /backup/  # WRONG
cp "$file" /backup/  # RIGHT
```

---

## Conditional Execution

### Pattern: AND Operator (&&)

**What it looks like:**
```bash
command1 && command2
```

**What it does:**
- Runs `command2` **only if** `command1` succeeds
- "Do this AND then do that"
- Stops if any command fails

**When you see it:**
- Chaining dependent operations
- "Only continue if previous step worked"
- Error handling

**Examples:**

```bash
# Only compile if make succeeds
make && ./program
```

```bash
# Create directory and enter it
mkdir mydir && cd mydir
```

```bash
# Chain multiple dependent steps
./configure && make && make install
```

### Pattern: OR Operator (||)

**What it looks like:**
```bash
command1 || command2
```

**What it does:**
- Runs `command2` **only if** `command1` fails
- "Do this OR do that"
- Provides fallback behavior

**When you see it:**
- Fallback operations
- Error handling
- "Try this, if it fails try that"

**Examples:**

```bash
# Try to use htop, fall back to top
htop || top
```

```bash
# Create directory if it doesn't exist
cd mydir || mkdir mydir
```

```bash
# Exit with error message if command fails
command || { echo "Failed!"; exit 1; }
```

### Pattern: Combining AND and OR

**What it looks like:**
```bash
command1 && command2 || command3
```

**What it does:**
- If `command1` succeeds, run `command2`
- If either fails, run `command3`
- Common for "try this, or handle error"

**When you see it:**
- Error handling in one line
- Success/failure branching

**Examples:**

```bash
# Compile and run, or show error
make && ./program || echo "Build failed"
```

```bash
# Try to start service, report status
systemctl start nginx && echo "Started" || echo "Failed to start"
```

---

## Looping Patterns

### Pattern: For Loop Over Files

**What it looks like:**
```bash
for file in *.txt; do
    command "$file"
done
```

**What it does:**
- Loops over each matching file
- Runs commands for each one
- `$file` contains current filename

**When you see it:**
- Batch processing files
- Applying same operation to multiple files

**Examples:**

```bash
# Convert all .txt to .bak
for file in *.txt; do
    mv "$file" "${file%.txt}.bak"
done
```

```bash
# Process all log files
for log in /var/log/*.log; do
    grep "ERROR" "$log" >> errors.txt
done
```

### Pattern: For Loop Over List

**What it looks like:**
```bash
for item in item1 item2 item3; do
    command "$item"
done
```

**What it does:**
- Loops over specified items
- Can be literal values or command output

**When you see it:**
- Processing a known list
- Iterating over command results

**Examples:**

```bash
# Check multiple servers
for server in web1 web2 web3; do
    ping -c 1 "$server"
done
```

```bash
# Process each line from command
for user in $(cat users.txt); do
    echo "Processing $user"
done
```

### Pattern: While Loop

**What it looks like:**
```bash
while condition; do
    commands
done
```

**What it does:**
- Repeats while condition is true
- Often used with reading files line by line

**When you see it:**
- Reading files line by line
- Waiting for conditions
- Continuous monitoring

**Examples:**

```bash
# Read file line by line
while read line; do
    echo "Line: $line"
done < file.txt
```

```bash
# Wait for file to appear
while [ ! -f /tmp/ready ]; do
    sleep 1
done
```

---

## Common Idioms

### Idiom: Find and Process Files

**Pattern:**
```bash
find /path -type f -name "*.txt" -exec command {} \;
```

**What it does:**
- Finds files matching criteria
- Executes command on each file
- `{}` is replaced with filename
- `\;` marks end of command

**Examples:**

```bash
# Delete all .tmp files
find /tmp -name "*.tmp" -exec rm {} \;
```

```bash
# Change permissions on all scripts
find . -name "*.sh" -exec chmod +x {} \;
```

### Idiom: Process Substitution

**Pattern:**
```bash
command <(other-command)
```

**What it does:**
- Runs `other-command` and makes output appear as a file
- Useful for commands that need file arguments

**Examples:**

```bash
# Compare output of two commands
diff <(ls dir1) <(ls dir2)
```

```bash
# Sort and compare
diff <(sort file1.txt) <(sort file2.txt)
```

### Idiom: Here Document

**Pattern:**
```bash
command << EOF
multiple lines
of input
EOF
```

**What it does:**
- Provides multi-line input to command
- Everything between `EOF` markers is input
- `EOF` can be any word

**Examples:**

```bash
# Create file with multiple lines
cat > file.txt << EOF
Line 1
Line 2
Line 3
EOF
```

```bash
# Send multi-line input to command
mysql -u root << EOF
CREATE DATABASE mydb;
USE mydb;
CREATE TABLE users (id INT, name VARCHAR(50));
EOF
```

### Idiom: Background Job

**Pattern:**
```bash
command &
```

**What it does:**
- Runs command in background
- Returns control to shell immediately
- Process continues running

**Examples:**

```bash
# Start long-running process in background
./long-process.sh &
```

```bash
# Run multiple processes in parallel
process1 &
process2 &
process3 &
wait  # Wait for all to complete
```

### Idiom: Suppress Output

**Pattern:**
```bash
command > /dev/null 2>&1
# or:
command &> /dev/null
```

**What it does:**
- Throws away all output
- `/dev/null` is a "black hole" for data
- Useful for silent operation

**Examples:**

```bash
# Run command silently
find / -name "*.conf" 2> /dev/null
```

```bash
# Check if command succeeds without output
if command &> /dev/null; then
    echo "Success"
fi
```

### Idiom: Test File Existence

**Pattern:**
```bash
[ -f file ] && command
[ -d directory ] && command
```

**What it does:**
- Tests if file/directory exists
- Runs command only if test succeeds
- Common in scripts

**Examples:**

```bash
# Only process if file exists
[ -f config.txt ] && source config.txt
```

```bash
# Create directory if it doesn't exist
[ -d backup ] || mkdir backup
```

### Idiom: Default Value

**Pattern:**
```bash
${variable:-default}
```

**What it does:**
- Uses variable value if set
- Uses default if variable is empty or unset

**Examples:**

```bash
# Use PORT if set, otherwise use 8080
PORT=${PORT:-8080}
```

```bash
# Use provided filename or default
filename=${1:-"output.txt"}
```

### Idiom: String Manipulation

**Pattern:**
```bash
${variable#pattern}   # Remove shortest match from start
${variable##pattern}  # Remove longest match from start
${variable%pattern}   # Remove shortest match from end
${variable%%pattern}  # Remove longest match from end
```

**What it does:**
- Manipulates strings without external commands
- Useful for filename manipulation

**Examples:**

```bash
# Remove extension
filename="document.txt"
basename="${filename%.txt}"  # Result: "document"
```

```bash
# Get extension
extension="${filename##*.}"  # Result: "txt"
```

```bash
# Remove path, keep filename
fullpath="/home/user/file.txt"
filename="${fullpath##*/}"  # Result: "file.txt"
```

---

## Pattern Recognition Practice

### Exercise 1: What does this do?

```bash
ps aux | grep python | grep -v grep | awk '{print $2}' | xargs kill
```

<details>
<summary>Answer</summary>

**Reading left to right:**
1. `ps aux` - List all processes
2. `| grep python` - Filter for lines with "python"
3. `| grep -v grep` - Exclude the grep command itself
4. `| awk '{print $2}'` - Extract column 2 (the PID)
5. `| xargs kill` - Pass each PID to kill command

**What it does:** Kills all Python processes
</details>

### Exercise 2: What does this do?

```bash
find . -name "*.log" -mtime +30 -exec gzip {} \;
```

<details>
<summary>Answer</summary>

**Breaking it down:**
- `find .` - Search current directory
- `-name "*.log"` - Files ending in .log
- `-mtime +30` - Modified more than 30 days ago
- `-exec gzip {} \;` - Compress each file

**What it does:** Compresses all log files older than 30 days
</details>

### Exercise 3: What does this do?

```bash
cat access.log | awk '{print $1}' | sort | uniq -c | sort -rn | head -10
```

<details>
<summary>Answer</summary>

**Reading the pipeline:**
1. `cat access.log` - Show log file
2. `| awk '{print $1}'` - Extract first column (IP addresses)
3. `| sort` - Sort the IPs
4. `| uniq -c` - Count occurrences of each unique IP
5. `| sort -rn` - Sort by count, descending
6. `| head -10` - Show top 10

**What it does:** Shows the 10 IP addresses that appear most in the log
</details>

---

## Tips for Pattern Recognition

1. **Read left to right** - Follow the data flow through pipes
2. **Identify the pattern** - Is it a pipe? Redirection? Loop?
3. **Break it down** - Understand each piece separately
4. **Look for idioms** - Common combinations you've seen before
5. **Practice reading** - The more you see, the easier it gets

### When You See Unfamiliar Syntax

1. **Identify the pattern type** - Pipe? Redirection? Substitution?
2. **Look up the specific command** - Use this guide or ask AI
3. **Test safely** - Try on sample data first
4. **Document it** - Add to your personal notes

### For Certification Exams

**Focus on recognizing:**
- Pipes and redirection
- Common command combinations
- File test operators (`-f`, `-d`, etc.)
- Basic loops and conditionals
- Wildcards and globbing

**Don't worry about:**
- Obscure syntax variations
- Complex regex patterns
- Advanced shell scripting
- Memorizing all options

---

## Summary

**Key Takeaways:**

1. **Patterns are reusable** - Same patterns appear everywhere
2. **Recognition > Memorization** - Know what it does, not exact syntax
3. **Context matters** - Same pattern used differently in different situations
4. **Practice reading** - The more you see, the better you get
5. **Use AI** - When you see something unfamiliar, ask AI to explain it

**Most Important Patterns to Recognize:**

- Pipes (`|`) - Chaining commands
- Redirection (`>`, `>>`, `2>`) - Saving output
- Command substitution (`$(...)`) - Using command output
- Wildcards (`*`, `?`, `[...]`) - Matching files
- Conditional execution (`&&`, `||`) - Error handling
- Loops (`for`, `while`) - Batch processing

**Remember:** You don't need to memorize these patterns. You just need to recognize them when you see them and understand what they're doing. Keep this guide handy for quick reference!
