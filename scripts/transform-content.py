#!/usr/bin/env python3
"""
Content Transformation Script

This script helps reorganize existing command-focused content into problem-focused guides.
It analyzes existing content and generates problem guide templates.

Usage:
    python3 scripts/transform-content.py [options]

Options:
    --analyze           Analyze existing content and show what problems it addresses
    --generate          Generate problem guide templates from existing content
    --output DIR        Output directory for generated guides (default: problems/)
    --source DIR        Source directory to analyze (default: topics/)
"""

import os
import re
import argparse
from pathlib import Path
from typing import List, Dict, Set, Tuple
from dataclasses import dataclass, field


@dataclass
class Command:
    """Represents a Linux command found in content"""
    name: str
    description: str = ""
    examples: List[str] = field(default_factory=list)
    source_file: str = ""


@dataclass
class Problem:
    """Represents a problem domain extracted from content"""
    name: str
    description: str
    commands: List[Command] = field(default_factory=list)
    examples: List[str] = field(default_factory=list)
    source_files: Set[str] = field(default_factory=set)


class ContentAnalyzer:
    """Analyzes existing command-focused content"""
    
    # Common command patterns
    COMMAND_PATTERNS = [
        r'`([a-z][a-z0-9\-]+)`',  # Commands in backticks
        r'^\s*-\s*`([a-z][a-z0-9\-]+)`',  # List items with commands
        r'##\s*Commands?\s*(?:to\s*(?:Master|Learn|Know))?',  # Command sections
    ]
    
    # Problem domain mappings
    COMMAND_TO_PROBLEM = {
        # Filesystem navigation
        'cd': 'navigating-filesystem',
        'pwd': 'navigating-filesystem',
        'ls': 'navigating-filesystem',
        'tree': 'navigating-filesystem',
        
        # Directory management
        'mkdir': 'managing-directories',
        'rmdir': 'managing-directories',
        'rm': 'managing-directories',
        
        # File finding
        'find': 'finding-files',
        'locate': 'finding-files',
        'which': 'finding-files',
        'whereis': 'finding-files',
        
        # File operations
        'cp': 'file-operations',
        'mv': 'file-operations',
        'touch': 'file-operations',
        'ln': 'file-operations',
        
        # Text processing
        'grep': 'text-processing',
        'sed': 'text-processing',
        'awk': 'text-processing',
        'cut': 'text-processing',
        'sort': 'text-processing',
        'uniq': 'text-processing',
        'wc': 'text-processing',
        'tr': 'text-processing',
        
        # Process management
        'ps': 'managing-processes',
        'top': 'managing-processes',
        'htop': 'managing-processes',
        'kill': 'managing-processes',
        'killall': 'managing-processes',
        'nice': 'managing-processes',
        'renice': 'managing-processes',
        'bg': 'managing-processes',
        'fg': 'managing-processes',
        'jobs': 'managing-processes',
        
        # Permissions
        'chmod': 'permissions',
        'chown': 'permissions',
        'chgrp': 'permissions',
        'umask': 'permissions',
        
        # Networking
        'ping': 'networking',
        'netstat': 'networking',
        'ss': 'networking',
        'ip': 'networking',
        'ifconfig': 'networking',
        'curl': 'networking',
        'wget': 'networking',
        
        # System monitoring
        'df': 'system-monitoring',
        'du': 'system-monitoring',
        'free': 'system-monitoring',
        'uptime': 'system-monitoring',
        'iostat': 'system-monitoring',
        'vmstat': 'system-monitoring',
    }
    
    PROBLEM_DESCRIPTIONS = {
        'navigating-filesystem': 'Moving between directories and understanding filesystem structure',
        'managing-directories': 'Creating, organizing, and removing directory structures',
        'finding-files': 'Locating files by name, size, date, or other criteria',
        'file-operations': 'Copying, moving, and manipulating files',
        'text-processing': 'Searching, filtering, and transforming text data',
        'managing-processes': 'Viewing, controlling, and managing running processes',
        'permissions': 'Understanding and modifying file permissions and ownership',
        'networking': 'Network connectivity, troubleshooting, and data transfer',
        'system-monitoring': 'Checking system resources and performance',
    }
    
    def __init__(self, source_dir: str = "topics"):
        self.source_dir = Path(source_dir)
        self.commands: Dict[str, Command] = {}
        self.problems: Dict[str, Problem] = {}
    
    def analyze(self) -> Dict[str, Problem]:
        """Analyze all markdown files in source directory"""
        if not self.source_dir.exists():
            print(f"Warning: Source directory '{self.source_dir}' does not exist")
            return {}
        
        for md_file in self.source_dir.rglob("*.md"):
            self._analyze_file(md_file)
        
        self._group_by_problems()
        return self.problems
    
    def _analyze_file(self, filepath: Path):
        """Analyze a single markdown file"""
        try:
            content = filepath.read_text()
            
            # Extract commands
            commands = self._extract_commands(content, str(filepath))
            for cmd in commands:
                if cmd.name not in self.commands:
                    self.commands[cmd.name] = cmd
                else:
                    # Merge information
                    existing = self.commands[cmd.name]
                    if cmd.description and not existing.description:
                        existing.description = cmd.description
                    existing.examples.extend(cmd.examples)
            
            # Extract code examples
            examples = self._extract_code_examples(content)
            for cmd_name in self.commands:
                if cmd_name in content:
                    self.commands[cmd_name].examples.extend(
                        [ex for ex in examples if cmd_name in ex]
                    )
        
        except Exception as e:
            print(f"Error analyzing {filepath}: {e}")
    
    def _extract_commands(self, content: str, source_file: str) -> List[Command]:
        """Extract commands from markdown content"""
        commands = []
        lines = content.split('\n')
        
        for i, line in enumerate(lines):
            # Look for command list items: - `command` - description
            match = re.match(r'^\s*-\s*`([a-z][a-z0-9\-]+)`\s*-\s*(.+)$', line)
            if match:
                cmd_name = match.group(1)
                description = match.group(2).strip()
                commands.append(Command(
                    name=cmd_name,
                    description=description,
                    source_file=source_file
                ))
        
        return commands
    
    def _extract_code_examples(self, content: str) -> List[str]:
        """Extract code blocks from markdown"""
        examples = []
        in_code_block = False
        current_example = []
        
        for line in content.split('\n'):
            if line.strip().startswith('```'):
                if in_code_block:
                    # End of code block
                    if current_example:
                        examples.append('\n'.join(current_example))
                        current_example = []
                    in_code_block = False
                else:
                    # Start of code block
                    in_code_block = True
            elif in_code_block:
                current_example.append(line)
        
        return examples
    
    def _group_by_problems(self):
        """Group commands by problem domains"""
        for cmd_name, cmd in self.commands.items():
            problem_key = self.COMMAND_TO_PROBLEM.get(cmd_name, 'other')
            
            if problem_key not in self.problems:
                self.problems[problem_key] = Problem(
                    name=problem_key,
                    description=self.PROBLEM_DESCRIPTIONS.get(
                        problem_key,
                        f"Problems related to {problem_key}"
                    )
                )
            
            self.problems[problem_key].commands.append(cmd)
            self.problems[problem_key].source_files.add(cmd.source_file)


class ProblemGuideGenerator:
    """Generates problem guide templates from analyzed content"""
    
    GUIDE_TEMPLATE = """# Problem: {title}

## What problem does this solve?

{description}

## When do you encounter this?

{scenarios}

## Available approaches

{tools}

## Decision tree

{decision_tree}

## Examples to recognize

{examples}

## Try with AI

{ai_prompts}

## Related problems

{related}

---

*This guide was generated from existing content. Please review and enhance with:*
- *More real-world scenarios*
- *Better decision guidance*
- *Additional examples*
- *Clearer AI prompt templates*
"""
    
    TOOL_TEMPLATE = """### {number}. **{name}**
   - **Best for:** {best_for}
   - **Recognition:** `{recognition}`
   - **Tradeoffs:** {tradeoffs}
"""
    
    def __init__(self, output_dir: str = "problems"):
        self.output_dir = Path(output_dir)
    
    def generate(self, problems: Dict[str, Problem]):
        """Generate problem guides for all problems"""
        self.output_dir.mkdir(exist_ok=True)
        
        for problem_key, problem in problems.items():
            if problem_key == 'other':
                continue  # Skip uncategorized
            
            self._generate_guide(problem_key, problem)
    
    def _generate_guide(self, problem_key: str, problem: Problem):
        """Generate a single problem guide"""
        problem_dir = self.output_dir / problem_key
        problem_dir.mkdir(exist_ok=True)
        
        guide_path = problem_dir / "README.md"
        
        # Don't overwrite existing guides
        if guide_path.exists():
            print(f"Skipping {problem_key} - guide already exists")
            return
        
        # Generate content
        title = self._format_title(problem_key)
        description = problem.description
        scenarios = self._generate_scenarios(problem)
        tools = self._generate_tools_section(problem)
        decision_tree = self._generate_decision_tree(problem)
        examples = self._generate_examples(problem)
        ai_prompts = self._generate_ai_prompts(problem)
        related = self._generate_related(problem_key)
        
        content = self.GUIDE_TEMPLATE.format(
            title=title,
            description=description,
            scenarios=scenarios,
            tools=tools,
            decision_tree=decision_tree,
            examples=examples,
            ai_prompts=ai_prompts,
            related=related
        )
        
        guide_path.write_text(content)
        print(f"Generated: {guide_path}")
    
    def _format_title(self, problem_key: str) -> str:
        """Convert problem-key to Title Case"""
        return problem_key.replace('-', ' ').title()
    
    def _generate_scenarios(self, problem: Problem) -> str:
        """Generate when-to-use scenarios"""
        # Generic scenarios based on problem type
        scenarios = [
            "- *[Add specific scenario when you'd encounter this problem]*",
            "- *[Add another real-world use case]*",
            "- *[Add a third common scenario]*"
        ]
        return '\n'.join(scenarios)
    
    def _generate_tools_section(self, problem: Problem) -> str:
        """Generate tools/approaches section"""
        if not problem.commands:
            return "*[No commands found - add tool descriptions]*"
        
        tools = []
        for i, cmd in enumerate(problem.commands, 1):
            tool_text = self.TOOL_TEMPLATE.format(
                number=i,
                name=cmd.name,
                best_for=cmd.description or "*[Add description]*",
                recognition=f"{cmd.name} [options] [arguments]",
                tradeoffs="*[Add tradeoffs and when to use]*"
            )
            tools.append(tool_text)
        
        return '\n'.join(tools)
    
    def _generate_decision_tree(self, problem: Problem) -> str:
        """Generate decision guidance"""
        if len(problem.commands) <= 1:
            return "*[Add guidance on when to use this approach]*"
        
        tree = ["**Which tool should I use?**\n"]
        for cmd in problem.commands:
            tree.append(f"- Use `{cmd.name}` when: *[add condition]*")
        
        return '\n'.join(tree)
    
    def _generate_examples(self, problem: Problem) -> str:
        """Generate example code blocks"""
        examples = []
        
        for cmd in problem.commands:
            if cmd.examples:
                for example in cmd.examples[:2]:  # Limit to 2 examples per command
                    examples.append(f"```bash\n{example}\n# What does this do? [Add explanation]\n```\n")
        
        if not examples:
            examples.append("```bash\n# [Add example command]\n# What does this do? [Add explanation]\n```\n")
        
        return '\n'.join(examples)
    
    def _generate_ai_prompts(self, problem: Problem) -> str:
        """Generate AI prompt templates"""
        prompts = [
            "**Effective prompts to try:**\n",
            "- \"Show me how to [specific task related to this problem]\"",
            "- \"What's the best way to [another task]?\"",
            "- \"Explain what this command does: [paste command]\"",
            "\n**When asking AI:**",
            "- Be specific about what you want to accomplish",
            "- Mention any constraints (file types, size limits, etc.)",
            "- Ask for explanations, not just commands"
        ]
        return '\n'.join(prompts)
    
    def _generate_related(self, problem_key: str) -> str:
        """Generate related problems section"""
        # This would ideally use actual relationships
        return "*[Add links to related problem guides]*"


def print_analysis_report(problems: Dict[str, Problem]):
    """Print a summary of analyzed content"""
    print("\n" + "="*60)
    print("CONTENT ANALYSIS REPORT")
    print("="*60 + "\n")
    
    total_commands = sum(len(p.commands) for p in problems.values())
    print(f"Total commands found: {total_commands}")
    print(f"Problem domains identified: {len(problems)}\n")
    
    for problem_key, problem in sorted(problems.items()):
        print(f"\n{problem.name.upper()}")
        print("-" * 40)
        print(f"Description: {problem.description}")
        print(f"Commands ({len(problem.commands)}):")
        for cmd in problem.commands:
            desc = f" - {cmd.description}" if cmd.description else ""
            print(f"  • {cmd.name}{desc}")
        print(f"Source files: {len(problem.source_files)}")
        for src in sorted(problem.source_files):
            print(f"  • {src}")


def main():
    parser = argparse.ArgumentParser(
        description="Transform command-focused content to problem-focused guides"
    )
    parser.add_argument(
        '--analyze',
        action='store_true',
        help='Analyze existing content and show what problems it addresses'
    )
    parser.add_argument(
        '--generate',
        action='store_true',
        help='Generate problem guide templates from existing content'
    )
    parser.add_argument(
        '--output',
        default='problems',
        help='Output directory for generated guides (default: problems/)'
    )
    parser.add_argument(
        '--source',
        default='topics',
        help='Source directory to analyze (default: topics/)'
    )
    
    args = parser.parse_args()
    
    # Default to analyze if no action specified
    if not args.analyze and not args.generate:
        args.analyze = True
    
    # Analyze content
    analyzer = ContentAnalyzer(args.source)
    problems = analyzer.analyze()
    
    if not problems:
        print(f"No content found in '{args.source}' directory")
        return
    
    # Print analysis
    if args.analyze:
        print_analysis_report(problems)
    
    # Generate guides
    if args.generate:
        print("\n" + "="*60)
        print("GENERATING PROBLEM GUIDES")
        print("="*60 + "\n")
        
        generator = ProblemGuideGenerator(args.output)
        generator.generate(problems)
        
        print(f"\nGuides generated in '{args.output}/' directory")
        print("Please review and enhance the generated guides with:")
        print("  • More specific real-world scenarios")
        print("  • Better decision guidance")
        print("  • Additional examples with explanations")
        print("  • Clearer AI prompt templates")


if __name__ == '__main__':
    main()
