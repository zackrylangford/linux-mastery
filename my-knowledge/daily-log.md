# Daily Learning Log

Quick daily notes to track your Linux learning progress. Keep it minimal - under 5 minutes per day!

**Purpose**: Build momentum and track what's working without creating overhead.

---

## How to Use This

**Each day, answer these 3 questions:**
1. What problem did I learn about today?
2. What worked well?
3. What should I try next?

**That's it!** Don't overthink it. Just capture the essentials and move on.

---

## December 2025

### Week of Dec 9-15

#### Monday, Dec 9
- **Problem learned**: Finding large files to free up disk space
- **What worked**: Used `find ~ -size +100M` and it showed me all big files. AI prompt "show me files larger than 100MB" worked perfectly.
- **Try next**: Learn how to sort the results by size, or maybe look into `du` for directory sizes

#### Tuesday, Dec 10
- **Problem learned**: Checking which processes use the most memory
- **What worked**: `top` command is interactive and easy to read. Pressing 'M' sorts by memory. Simple!
- **Try next**: Learn how to kill a process if needed

#### Wednesday, Dec 11
- **Problem learned**: [Your entry here]
- **What worked**: [What clicked for you today]
- **Try next**: [What to explore tomorrow]

---

## Template for Each Day

### [Day], [Date]
- **Problem learned**: [One sentence: what problem can you now solve?]
- **What worked**: [What approach/tool/prompt was effective?]
- **Try next**: [What's the logical next step?]

---

## Tips for Effective Daily Logging

### ✅ Do:
- **Keep it short**: 3-5 sentences total
- **Focus on problems**: What can you DO now that you couldn't before?
- **Note what worked**: Successful AI prompts, helpful examples, good resources
- **Plan next step**: What's the natural progression?

### ❌ Don't:
- **Write essays**: This isn't a journal, just quick notes
- **Copy syntax**: You don't need to memorize commands here
- **Track everything**: Just the highlights
- **Stress about gaps**: Missed a day? No problem, just continue

---

## Weekly Review (Optional)

At the end of each week, optionally spend 5 minutes reviewing:

### Week of [Date Range]
- **Problems I can now solve**: [List 3-5 new capabilities]
- **Most useful discovery**: [What had the biggest impact?]
- **Patterns I'm noticing**: [Any recurring themes or connections?]
- **Focus for next week**: [What area to explore next?]

---

## Example Week

### Week of Dec 2-8

#### Monday, Dec 2
- **Problem learned**: Finding files by name across the system
- **What worked**: `locate` is super fast for finding files. Had to run `updatedb` first though.
- **Try next**: Learn when to use `locate` vs `find`

#### Tuesday, Dec 3
- **Problem learned**: Difference between `locate` and `find`
- **What worked**: `locate` uses a database (fast but may be outdated), `find` searches in real-time (slower but current). Now I know which to use when!
- **Try next**: Practice with `find` using different criteria

#### Wednesday, Dec 4
- **Problem learned**: Using `find` with multiple criteria
- **What worked**: Can combine `-name`, `-size`, `-mtime` flags. AI helped me build: `find /home -name "*.pdf" -size +5M -mtime -7`
- **Try next**: Learn about `grep` for searching inside files

#### Thursday, Dec 5
- **Problem learned**: Searching for text patterns in files
- **What worked**: `grep -r "pattern" /path` searches recursively. The `-i` flag for case-insensitive is useful!
- **Try next**: Try combining `find` and `grep` together

#### Friday, Dec 6
- **Problem learned**: Piping commands together
- **What worked**: `find . -name "*.log" | xargs grep "ERROR"` - finds log files then searches them. Pipes are powerful!
- **Try next**: Learn more about text processing with `awk` or `sed`

**Week summary**: Learned the whole "finding things" problem domain - files by name, by size, by content. Can now locate what I need on a Linux system!

---

## Motivation Reminders

- **Consistency > Perfection**: 5 minutes daily beats 2 hours once a week
- **Progress compounds**: Each small problem you learn builds on the last
- **You're building capability**: Focus on what you CAN do, not what you don't know yet
- **AI is your partner**: You're learning to direct AI, not replace it

**Remember**: The goal isn't to memorize everything - it's to know what's possible and how to make it happen!
