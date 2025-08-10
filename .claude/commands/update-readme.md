---
description: Update README.md files in folders with summary and table of contents
argument-hint: [folder path, 'all', or 'help']
---

# Update README Command

**Usage:** `/update-readme [target]`

## Available Targets
- `all` - Process all major folders
- `characters` - Character files and subdirectories
- `ships` - Starship data sheets
- `systems` - Star system information
- `factions` - Faction and organization data
- `adventure-001` - Adventure 001 files
- `adventure-002` - Adventure 002 files (if exists)
- `lore` - In-universe locations and encounters
- `rules` - Rules references and tables
- `players` - Player character sheets

---

I'll update README.md files with brief summaries and table of contents for the specified target: $ARGUMENTS

To update a specific folder's README, I'll:
1. List all files in the directory
2. Create a brief summary of the folder's purpose
3. Generate a table of contents with file descriptions
4. Save the updated README.md