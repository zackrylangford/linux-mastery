# Problem: Text Processing

## What problem does this solve?

You need to search, filter, transform, extract, or analyze text data from files or command output. Text processing is fundamental in Linux - from analyzing log files to extracting data from CSV files to transforming configuration files.

## When do you encounter this?

**Real-world scenarios:**
- Searching log files for error messages
- Extracting specific columns from CSV or tabular data
- Finding and replacing text in configuration files
- Filtering command output to show only relevant lines
- Counting occurrences of words or patterns
- Sorting and removing duplicate lines
- Extracting email addresses or URLs from text
- Reformatting data from one structure to another

## Available approaches

### 1. `grep` - The Pattern Searcher
- **Best for:** Finding lines that match a pattern, filtering output, searching for text
- **Tradeoffs:** 
  - ✅ Pros: Fast, simple for basic searches, supports regex, ubiquitous
  - ❌ Cons: Only searches/filters, doesn't transform, can be slow on huge files
- **How to recognize it:** Look for `grep "pattern"` or `| grep something`
- **AI prompt template:** 
  ```
  Show me how to find all lines in [file] that contain [pattern]
  ```

### 2. `sed` - The Stream Editor
- **Best for:** Find and replace, deleting lines, simple transformations
- **Tradeoffs:**
  - ✅ Pros: Great for substitutions, can edit in-place, works in pipelines
  - ❌ Cons: Syntax can be cryptic, not ideal for complex logic
- **How to recognize it:** Look for `sed 's/old/new/'` or `sed '/pattern/d'`
- **AI prompt template:**
  ```
  Show me how to replace all occurrences of [old text] with [new text] in [file]
  ```

### 3. `awk` - The Data Processor
- **Best for:** Column-based data, calculations, complex text processing, reports
- **Tradeoffs:**
  - ✅ Pros: Powerful for structured data, can do math, has programming features
  - ❌ Cons: Steeper learning curve, overkill for simple tasks
- **How to recognize it:** Look for `awk '{print $1}'` or `awk -F',' '{...}'`
- **AI prompt template:**
  ```
  Show me how to extract column [N] from [file] and [do something with it]
  ```

### 4. `cut` - The Column Extractor
- **Best for:** Extracting specific columns or character ranges, simple and fast
- **Tradeoffs:**
  - ✅ Pros: Simple syntax, fast, perfect for basic column extraction
  - ❌ Cons: Limited to extraction, can't do transformations or calculations
- **How to recognize it:** Look for `cut -d',' -f1` or `cut -c1-10`
- **AI prompt template:**
  ```
  Show me how to extract the [Nth] column from [file] that's delimited by [character]
  ```

### 5. `sort` - The Line Sorter
- **Best for:** Sorting lines alphabetically or numerically, preparing data for `uniq`
- **Tradeoffs:**
  - ✅ Pros: Fast, handles large files, many sorting options
  - ❌ Cons: Only sorts, doesn't transform
- **How to recognize it:** Look for `sort`, `sort -n` (numeric), `sort -r` (reverse)
- **AI prompt template:**
  ```
  Show me how to sort [file] by [criteria: alphabetically, numerically, by column N]
  ```

### 6. `uniq` - The Duplicate Remover
- **Best for:** Removing or counting duplicate lines (requires sorted input)
- **Tradeoffs:**
  - ✅ Pros: Simple, can count occurrences, removes duplicates
  - ❌ Cons: Only works on adjacent lines (must sort first)
- **How to recognize it:** Look for `sort | uniq` or `uniq -c`
- **AI prompt template:**
  ```
  Show me how to find unique lines in [file] or count how many times each line appears
  ```

## Decision tree

**Choose your approach:**
1. If you need to **find lines matching a pattern** → Use `grep`
2. If you need to **replace text** → Use `sed 's/old/new/'`
3. If you need to **extract columns from structured data** → Use `cut` (simple) or `awk` (complex)
4. If you need to **do calculations or complex logic** → Use `awk`
5. If you need to **sort lines** → Use `sort`
6. If you need to **remove duplicates** → Use `sort | uniq`
7. If you need to **count occurrences** → Use `sort | uniq -c`

## Examples to recognize

### Example 1: Finding lines with a pattern
```bash
grep "error" /var/log/syslog
```

**What's happening here:**
- `grep "error"` - Search for the word "error"
- `/var/log/syslog` - In this log file
- Shows all lines containing "error"
- Case-sensitive by default
- Output: Lines from the file that match

### Example 2: Case-insensitive search
```bash
grep -i "warning" logfile.txt
```

**What's happening here:**
- `grep -i` - Case-insensitive search
- Matches "warning", "Warning", "WARNING", etc.
- Common for log analysis where case varies
- Output: All matching lines regardless of case

### Example 3: Counting matches
```bash
grep -c "failed" auth.log
```

**What's happening here:**
- `grep -c` - Count matching lines (don't show them)
- Returns just a number
- Quick way to see how many times something appears
- Output: Just a count, like "42"

### Example 4: Find and replace with sed
```bash
sed 's/old/new/g' file.txt
```

**What's happening here:**
- `sed` - Stream editor
- `s/old/new/g` - Substitute "old" with "new" globally
  - `s` = substitute
  - `g` = global (all occurrences on each line)
- Prints to stdout (doesn't change file)
- To edit file: add `-i` flag
- Output: File content with replacements

### Example 5: Deleting lines with sed
```bash
sed '/pattern/d' file.txt
```

**What's happening here:**
- `sed '/pattern/d'` - Delete lines matching pattern
- Useful for filtering out unwanted lines
- Doesn't modify original file (unless using `-i`)
- Output: File content without matching lines

### Example 6: Extracting first column with cut
```bash
cut -d',' -f1 data.csv
```

**What's happening here:**
- `cut` - Extract columns
- `-d','` - Delimiter is comma
- `-f1` - Field 1 (first column)
- Perfect for CSV files
- Output: Just the first column

### Example 7: Extracting multiple columns with awk
```bash
awk -F',' '{print $1, $3}' data.csv
```

**What's happening here:**
- `awk` - Pattern scanning and processing
- `-F','` - Field separator is comma
- `'{print $1, $3}'` - Print columns 1 and 3
- More flexible than `cut`
- Output: Two columns separated by space

### Example 8: Summing numbers with awk
```bash
awk '{sum += $1} END {print sum}' numbers.txt
```

**What's happening here:**
- `awk '{sum += $1}'` - Add first column to sum variable
- `END {print sum}` - After all lines, print total
- Shows awk's programming capabilities
- Great for calculating totals from data
- Output: Single number (the sum)

### Example 9: Sorting lines
```bash
sort names.txt
```

**What's happening here:**
- `sort` - Sort lines alphabetically
- Default is alphabetical, ascending
- Use `-n` for numeric sort
- Use `-r` for reverse order
- Output: Sorted lines

### Example 10: Removing duplicate lines
```bash
sort file.txt | uniq
```

**What's happening here:**
- `sort file.txt` - Sort the file first (required!)
- `|` - Pipe to next command
- `uniq` - Remove adjacent duplicate lines
- Must sort first because `uniq` only removes adjacent duplicates
- Output: Unique lines only

### Example 11: Counting occurrences
```bash
sort file.txt | uniq -c | sort -rn
```

**What's happening here:**
- `sort file.txt` - Sort the data
- `uniq -c` - Count occurrences of each unique line
- `sort -rn` - Sort by count, reverse numeric (highest first)
- Common pattern for "top N" analysis
- Output: Lines with counts, sorted by frequency

### Example 12: Filtering command output
```bash
ps aux | grep python | grep -v grep
```

**What's happening here:**
- `ps aux` - List all processes
- `| grep python` - Filter for lines with "python"
- `| grep -v grep` - Exclude lines with "grep" (removes the grep command itself)
- Common pattern for finding processes
- Output: Python processes only

### Example 13: Extracting specific pattern with grep
```bash
grep -oE '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}' logfile.txt
```

**What's happening here:**
- `grep -oE` - Only show matching part, extended regex
- `[0-9]{1,3}\.` - Pattern for IP addresses
- Extracts just the IPs, not whole lines
- Useful for extracting specific data
- Output: Just the IP addresses

### Example 14: Processing CSV with awk
```bash
awk -F',' '$3 > 100 {print $1, $2}' sales.csv
```

**What's happening here:**
- `awk -F','` - Comma-separated fields
- `$3 > 100` - Condition: third column greater than 100
- `{print $1, $2}` - If true, print columns 1 and 2
- Shows awk's filtering and logic capabilities
- Output: Rows where column 3 > 100, showing columns 1 and 2

## Try with AI

**New to AI collaboration?** Check out the [AI Prompting Guide](../../references/ai-prompting-guide.md) for detailed tips on working effectively with AI.

### How to Use AI for This Problem

**Step 1: Understand what you need**
Before asking AI, be clear about:
- What are you searching for? (pattern, column, line range?)
- What transformation do you need? (replace, extract, filter, count?)
- What's the input format? (CSV, log file, plain text?)
- What should the output look like?

**Step 2: Use a good prompt template**

Choose based on your need:

```
Searching/filtering:
"Show me how to find all lines in [file] that contain [pattern]"

Extracting columns:
"Show me how to extract column [N] from [file] that's delimited by [character]"

Find and replace:
"Show me how to replace all occurrences of [old] with [new] in [file]"

Counting/analyzing:
"Show me how to count how many times [pattern] appears in [file]"

Sorting/deduplicating:
"Show me how to sort [file] by [criteria] and remove duplicates"

Complex processing:
"I have a [format] file with [structure]. Extract [what] where [criteria] and [output format]"
```

**Step 3: Verify the AI's solution**

Before running the command, check:
- [ ] Does it read from the right file?
- [ ] Will it modify the original file? (look for `-i` flag with sed)
- [ ] Are the delimiters correct for your data format?
- [ ] Does the output format match what you need?
- [ ] Can you test it safely first? (without `-i`, redirect to new file)

**Step 4: Test safely**

```bash
# SAFE: Output to screen (doesn't modify files)
grep "error" logfile.txt                    # Safe - just displays
sed 's/old/new/g' file.txt                  # Safe - shows result
awk '{print $1}' data.csv                   # Safe - displays column

# SAFE: Output to new file
sed 's/old/new/g' file.txt > file_new.txt   # Safe - creates new file
grep "pattern" input.txt > output.txt       # Safe - saves to new file

# CAUTION: Modifies original file
sed -i 's/old/new/g' file.txt               # Modifies file in place!

# BEST PRACTICE: Test without -i first, then add it
sed 's/old/new/g' file.txt                  # 1. Check output looks right
sed -i 's/old/new/g' file.txt               # 2. Then modify if good
```

**Step 5: Understand the result**

Ask AI to explain if you don't understand:
- "What does the 'g' flag do in sed?"
- "Why do I need to sort before using uniq?"
- "What's the difference between $1 and $NF in awk?"

### Practice Exercises with AI

**Exercise 1: Search for patterns**
- **Prompt**: "Show me how to find all lines containing 'error' in /var/log/syslog and show the line numbers"
- **Verify**: Check for `grep` with `-n` flag
- **Test**: Run it and see if output makes sense
- **Document**: Note this pattern for log analysis

**Exercise 2: Extract columns**
- **Prompt**: "Show me how to extract the first column from a comma-separated file called data.csv"
- **Verify**: Check for `cut -d',' -f1` or `awk -F',' '{print $1}'`
- **Test**: Try on a sample CSV file
- **Document**: Save both approaches and when to use each

**Exercise 3: Count occurrences**
- **Prompt**: "Show me how to count how many times each unique line appears in a file and sort by frequency"
- **Verify**: Check for `sort | uniq -c | sort -rn` pattern
- **Test**: Try on a simple text file
- **Document**: Note this pattern for frequency analysis

**Exercise 4: Find and replace (safe)**
- **Prompt**: "Show me how to replace all occurrences of 'foo' with 'bar' in test.txt and save to a new file"
- **Verify**: Check for `sed 's/foo/bar/g'` with output redirection
- **Test**: Create a test file first
- **Document**: Note the difference between with and without `-i`

**Exercise 5: Filter and extract**
- **Prompt**: "I have a CSV with columns name,age,city. Show me how to extract names of people older than 25"
- **Verify**: Check for `awk` with condition and field extraction
- **Test**: Create a sample CSV to test
- **Document**: Note this pattern for conditional extraction

**Exercise 6: Complex pipeline**
- **Prompt**: "Show me how to find all unique IP addresses in access.log and count how many times each appears, sorted by frequency"
- **Verify**: Check for grep/awk to extract IPs, then sort | uniq -c | sort -rn
- **Test**: Try on a sample log file
- **Document**: Break down each step of the pipeline

### Common AI Collaboration Patterns

**Pattern 1: Building up complexity**
```
You: "Show me how to find lines with 'error' in log.txt"
AI: [gives basic grep]
You: "Now show me how to also include the line number and filename"
AI: [adds -n and -H flags]
You: "And make it case-insensitive"
AI: [adds -i flag]
```

**Pattern 2: Testing before modifying**
```
You: "Show me how to replace 'old' with 'new' in config.txt"
AI: [gives sed with -i]
You: "Show me how to test this first without modifying the file"
AI: [gives sed without -i, or with output redirection]
```

**Pattern 3: Understanding the pipeline**
```
You: [gets complex pipeline from AI]
You: "Can you explain what each part of this pipeline does?"
AI: [breaks down each command]
You: "Why do we need to sort before uniq?"
AI: [explains uniq only works on adjacent lines]
```

### Working with Different Data Formats

**CSV files:**
```
Prompt: "I have a CSV with headers. Show me how to extract column 2 skipping the header"
Tools: awk, cut, tail
```

**Log files:**
```
Prompt: "Show me how to extract timestamps and error messages from syslog format"
Tools: grep, awk, sed
```

**Configuration files:**
```
Prompt: "Show me how to find all uncommented lines in a config file"
Tools: grep -v '^#', sed
```

**JSON/structured data:**
```
Prompt: "Show me how to extract specific fields from JSON using command-line tools"
Tools: grep, awk, or suggest jq
```

### Verification Checklist

After getting a solution from AI:
- [ ] I understand what each command in the pipeline does
- [ ] I know what the input format is
- [ ] I know what the output format will be
- [ ] I've tested it without modifying files (no `-i` flag)
- [ ] The results match what I expected
- [ ] I understand when to use this tool vs alternatives
- [ ] I've documented the working solution

### Next Steps

1. Pick one exercise and try it with AI
2. Test the solution on sample data first
3. Understand each part of the command/pipeline
4. Document the pattern in `my-knowledge/problems-i-solve.md`
5. Try variations to deepen understanding

**Remember**: Text processing is about combining simple tools (grep, sed, awk, sort, uniq) into powerful pipelines. Focus on understanding what each tool does, not memorizing all the flags.

## Related problems

- [Finding files](../finding-files/) - Often combined with text processing
- [System monitoring](../system-monitoring/) - Processing system command output
- [Managing processes](../managing-processes/) - Filtering process lists

## What to memorize vs look up

**Memorize (high-value knowledge):**
- `grep` for searching/filtering
- `sed` for find and replace
- `awk` for column-based data
- `cut` for simple column extraction
- `sort` for sorting
- `uniq` for removing duplicates (after sort)
- Concept: pipes (`|`) chain commands together
- Concept: each tool does one thing well

**Look up as needed (low-value to memorize):**
- Specific `grep` flags like `-E`, `-o`, `-v`
- `sed` substitution syntax details
- `awk` programming syntax
- Complex regex patterns
- All the `sort` options
- Exact `cut` delimiter syntax

## For certification prep

**LPIC-1 / CompTIA Linux+ relevant syntax to recognize:**
- `grep "pattern" file` - Search for pattern
- `grep -i` - Case-insensitive search
- `grep -v` - Invert match (exclude)
- `grep -r` - Recursive search
- `sed 's/old/new/g'` - Global substitution
- `sed -i` - In-place editing
- `awk '{print $1}'` - Print first field
- `awk -F':'` - Set field separator
- `cut -d':' -f1` - Extract field with delimiter
- `sort` - Sort lines
- `sort -n` - Numeric sort
- `sort -r` - Reverse sort
- `uniq` - Remove adjacent duplicates
- `uniq -c` - Count occurrences
- `wc -l` - Count lines
- `tr` - Translate/delete characters
- `head -n 10` - First 10 lines
- `tail -n 10` - Last 10 lines

*Note: You don't need to memorize these, but you should be able to recognize what they do when you see them on an exam.*
