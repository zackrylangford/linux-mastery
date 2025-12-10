# Daily Practice Routine

A simple, sustainable 20-30 minute daily routine for learning Linux in the AI age.

## The Simple Daily Flow (20-30 minutes)

### 1. Pick One Problem (2 minutes)

Browse `problems/` and choose something you want to learn:
- Finding files
- Managing processes
- Text processing
- Understanding permissions
- Network troubleshooting
- System monitoring

**Tip**: Start with problems you encounter in real life.

### 2. Learn What's Possible (10 minutes)

Open the problem guide and read:
- What problem does this solve?
- When do you encounter this?
- What tools are available?
- Look at 2-3 examples - what do they do?

**Focus on understanding**, not memorizing:
- Why would I use this tool?
- What's the difference between these approaches?
- When would I choose one over another?

### 3. Try It With AI (10 minutes)

Now practice collaborating with AI:

1. **Ask AI for help**:
   - "Show me how to find files larger than 100MB"
   - "How do I check which process is using the most CPU?"
   - "Display the 10 largest directories in my home folder"

2. **Run the command** AI gives you

3. **Verify it works** - Does it do what you expected?

4. **Understand why** - Look at the command. Can you recognize what each part does?

**This is the key skill**: Directing AI and verifying results.

### 4. Document What You Learned (5 minutes)

Add to `my-knowledge/problems-i-solve.md`:

```markdown
## [Problem Name]
- Problem: [What you were trying to do]
- Solution: [Tool/approach that works]
- AI prompt that worked: "[The prompt you used]"
- When I use this: [Real scenarios]
```

**Keep it simple**. Just capture:
- What problem you can now solve
- What tool/approach works
- The AI prompt that worked

Optional: Add to `my-knowledge/daily-log.md` if you want to track your journey.

## That's It!

No complex tracking. No elaborate exercises. Just:
1. Pick a problem
2. Learn what's possible
3. Try it with AI
4. Document it

Repeat tomorrow with a different problem.

## Example: Your First Day

**Problem**: Find large files taking up disk space

**Learn** (10 min):
- Read `problems/finding-files/README.md`
- See that `find` and `du` are the main tools
- Look at examples:
  ```bash
  find /home -size +100M  # Files over 100MB
  du -sh * | sort -h      # Directory sizes, sorted
  ```

**Try with AI** (10 min):
- Ask: "Show me how to find all files larger than 500MB in my home directory"
- AI gives: `find ~ -type f -size +500M`
- Run it, see the results
- Understand: `~` is home, `-type f` is files only, `-size +500M` is over 500MB

**Document** (5 min):
```markdown
## Finding Large Files
- Problem: Need to free up disk space
- Solution: Use find with -size flag
- AI prompt: "Show me how to find files larger than X in directory Y"
- When I use this: When disk is full, need to clean up
```

**Total time**: 25 minutes. Done for the day!

## Weekly Pattern (Optional)

If you want more structure, follow this pattern:

- **Mon/Wed/Fri**: Learn new problems from `problems/`
- **Tue/Thu**: Revisit and practice problems you've learned
- **Weekend**: Try a small project combining multiple problems

But honestly? Just doing one problem per day is enough.

## Tips for Success

### Keep It Sustainable
- 20-30 minutes is better than skipping days
- One problem per day builds up fast
- Don't try to learn everything at once

### Focus on Understanding
- Why does this approach work?
- When would I use this vs. that?
- What problem is this solving?

### Practice AI Collaboration
- Get good at asking AI for help
- Learn to verify AI's answers
- Refine your prompts when needed

### Build Your Knowledge Base
- `my-knowledge/problems-i-solve.md` becomes your personal reference
- You'll quickly build a list of problems you can solve
- This is more valuable than memorizing commands

## What About Certification?

If you're preparing for LPIC-1 or similar exams:

**Daily routine stays the same**, but add:
- 5 minutes reviewing `cert-prep/syntax-to-recognize.md`
- Practice recognition exercises from `cert-prep/recognition-exercises.md`
- Focus on recognizing syntax, not writing from memory

**Total time**: 30-35 minutes daily.

## Tracking Progress (Optional)

If you want to track your progress:

**Simple approach**:
- Keep a streak counter in `my-knowledge/daily-log.md`
- Count problems you can solve in `my-knowledge/problems-i-solve.md`

**That's enough**. Don't over-complicate tracking.

## Common Questions

**Q: What if I miss a day?**
A: Just start again tomorrow. Consistency matters more than perfection.

**Q: Should I memorize commands?**
A: No. Focus on understanding problems and recognizing patterns. AI handles syntax.

**Q: What if AI gives me a wrong answer?**
A: Great learning opportunity! Figure out why it's wrong. Refine your prompt. This is a key skill.

**Q: How long until I'm "good" at Linux?**
A: After 30 days of daily practice, you'll be comfortable with common problems. After 90 days, you'll be confident.

**Q: Do I need to do everything in this repository?**
A: No! Just `problems/` and `my-knowledge/` are enough. Use the rest as needed.

## Start Simple

Don't overthink it:
1. Pick a problem
2. Learn about it
3. Try it with AI
4. Write it down

Do this daily. You'll be amazed at your progress in a month.

See [GETTING-STARTED.md](GETTING-STARTED.md) for your first week's problems.
