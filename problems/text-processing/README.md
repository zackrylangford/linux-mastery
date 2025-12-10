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

## Try it yourself

**Practice with AI:**
1. Think of a specific version of this problem you want to solve
2. Use one of the AI prompt templates above
3. Ask AI to generate the solution
4. **Before running it:** Try to understand what the AI gave you
5. Run it and verify it works
6. Document what you learned in `my-knowledge/problems-i-solve.md`

**Verification checklist:**
- [ ] Does the solution match what you asked for?
- [ ] Can you explain what each part does?
- [ ] Did you test it safely (won't modify important files)?
- [ ] Do you understand when to use this approach?

**Safe practice exercises:**
1. Ask AI: "Show me how to find all lines containing 'error' in a log file"
2. Ask AI: "Show me how to extract the first column from a comma-separated file"
3. Ask AI: "Show me how to count how many times each word appears in a file"
4. Ask AI: "Show me how to replace all occurrences of 'foo' with 'bar' in a file"

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
