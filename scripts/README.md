# Content Transformation Scripts

This directory contains scripts to help migrate from command-focused to problem-focused learning structure.

## transform-content.py

Analyzes existing command-focused content and generates problem-focused guide templates.

### Features

- **Analyze existing content** - Scans markdown files to identify commands and problem domains
- **Generate problem guides** - Creates structured problem guide templates
- **Smart categorization** - Maps commands to appropriate problem domains
- **Preserves examples** - Extracts code examples from existing content

### Usage

#### 1. Analyze Existing Content

See what problems your existing content addresses:

```bash
python3 scripts/transform-content.py --analyze
```

This will:
- Scan all markdown files in `topics/` directory
- Identify commands and their descriptions
- Group commands by problem domain
- Show a summary report

#### 2. Generate Problem Guides

Create problem guide templates from existing content:

```bash
python3 scripts/transform-content.py --generate
```

This will:
- Analyze existing content
- Generate problem guide templates in `problems/` directory
- Preserve command descriptions and examples
- Create structured guides ready for enhancement

#### 3. Custom Directories

Specify custom source and output directories:

```bash
python3 scripts/transform-content.py --analyze --source topics/ --output problems/
python3 scripts/transform-content.py --generate --source topics/ --output problems/
```

### Command Mappings

The script automatically maps commands to problem domains:

| Problem Domain | Commands |
|----------------|----------|
| **navigating-filesystem** | cd, pwd, ls, tree |
| **managing-directories** | mkdir, rmdir, rm |
| **finding-files** | find, locate, which, whereis |
| **file-operations** | cp, mv, touch, ln |
| **text-processing** | grep, sed, awk, cut, sort, uniq, wc, tr |
| **managing-processes** | ps, top, htop, kill, killall, nice, renice, bg, fg, jobs |
| **permissions** | chmod, chown, chgrp, umask |
| **networking** | ping, netstat, ss, ip, ifconfig, curl, wget |
| **system-monitoring** | df, du, free, uptime, iostat, vmstat |

### Generated Guide Structure

Each generated guide includes:

```markdown
# Problem: [Title]

## What problem does this solve?
[Description of the problem]

## When do you encounter this?
[Real-world scenarios - needs enhancement]

## Available approaches
[Tools and commands with descriptions]

## Decision tree
[Guidance on which tool to use when]

## Examples to recognize
[Code examples with explanations]

## Try with AI
[AI prompt templates]

## Related problems
[Links to related guides]
```

### After Generation

Generated guides are **templates** that need enhancement:

1. **Review accuracy** - Verify command descriptions are correct
2. **Add scenarios** - Include real-world use cases
3. **Enhance examples** - Add explanations for code examples
4. **Improve AI prompts** - Create specific, effective prompt templates
5. **Add decision guidance** - Help users choose the right tool
6. **Link related problems** - Connect to other problem guides

### Example Workflow

```bash
# 1. Analyze what you have
python3 scripts/transform-content.py --analyze

# Output shows:
# - 15 commands found
# - 5 problem domains identified
# - Source files analyzed

# 2. Generate problem guides
python3 scripts/transform-content.py --generate

# Output:
# Generated: problems/navigating-filesystem/README.md
# Generated: problems/managing-directories/README.md
# Generated: problems/finding-files/README.md
# ...

# 3. Review and enhance generated guides
# Open each guide and:
# - Add real-world scenarios
# - Enhance examples with explanations
# - Improve AI prompt templates
# - Add decision guidance
```

### Limitations

- **Template only** - Generated guides need manual enhancement
- **Basic extraction** - May miss complex command relationships
- **No overwrite** - Won't replace existing guides (safety feature)
- **Markdown only** - Only processes .md files

### Extending the Script

To add new problem domains or command mappings:

1. Edit `COMMAND_TO_PROBLEM` dictionary in the script
2. Add problem descriptions to `PROBLEM_DESCRIPTIONS`
3. Run the script to regenerate guides

### Troubleshooting

**No content found:**
- Check that `topics/` directory exists
- Verify markdown files contain command descriptions
- Use `--source` to specify different directory

**Guides not generated:**
- Check if guides already exist (script won't overwrite)
- Verify write permissions on output directory
- Check console output for errors

**Missing commands:**
- Add command mappings to `COMMAND_TO_PROBLEM`
- Commands not in mapping go to 'other' category
- Review analysis report to see what was found

## Future Scripts

Planned scripts for this directory:

- **validate-guides.py** - Check problem guides for completeness
- **link-checker.py** - Verify all internal links work
- **progress-migrator.py** - Convert old progress logs to new format
- **quiz-generator.py** - Generate recognition quizzes from guides

## Contributing

When adding new scripts:

1. Follow Python best practices
2. Include docstrings and comments
3. Add usage examples to this README
4. Make scripts executable: `chmod +x script.py`
5. Use argparse for command-line options
