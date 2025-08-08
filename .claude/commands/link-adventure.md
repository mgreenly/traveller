---
description: Add missing entity links to an adventure folder
argument-hint: [adventure number]
---

I'll use a specialized sub-agent to systematically add missing entity links to adventure-$ARGUMENTS.

This will ensure all first references to characters, ships, systems, and factions have proper markdown links for better navigation and cross-referencing.

```function_calls
function_name: Task
parameters:
  subagent_type: general-purpose
  description: Link adventure entities
  prompt: |
    Systematically add entity links to adventure-$ARGUMENTS. This is a comprehensive task to ensure all first references to characters, ships, systems, and factions have proper markdown links. This operates from a clean slate - existing links will be replaced/updated as needed.

    ## Your Task:

    1. **Survey Adventure Structure**: Use LS tool to identify all files in /workspace/adventure-$ARGUMENTS/

    2. **Generate Complete Entity Database**: Create a comprehensive master list of ALL available entities by scanning the entire project:
       - Characters: Use Glob to find /workspace/characters/**/*.md and extract entity names and paths
       - Ships: Use Glob to find /workspace/ships/*.md and extract ship names and paths  
       - Systems: Use Glob to find /workspace/systems/*.md and extract system names and paths
       - Factions: Use Glob to find /workspace/factions/*.md and extract faction names and paths
       
       For each entity, record:
       - The exact name/title as it appears in filenames
       - Common variations (with/without quotes, nicknames, full vs short names)
       - The correct relative path from adventure files (../category/filename.md)

    3. **Use TodoWrite Tool**: Create a systematic checklist to track progress through each adventure file

    4. **Process Each File**: For each file in adventure-$ARGUMENTS/, systematically:
       - Read the file content completely
       - Search for ALL mentions of entities from your master list
       - Add markdown links for FIRST mentions only (subsequent mentions in same file remain unlinked)
       - Work from clean slate - replace any existing entity links with correct ones
       - Use MultiEdit tool for efficient batch updates

    5. **Entity Link Format**:
       - Characters: `[Full Name](../characters/path/filename.md)` 
       - Ships: `[*Ship Name*](../ships/ship-name.md)` (preserve italics for ship names)
       - Systems: `[System Name](../systems/system-name.md)` 
       - Factions: `[Faction Name](../factions/faction-name.md)`

    6. **Verification**: Use bash ls commands to verify all added links point to existing files

    ## Key Rules:
    - Generate complete entity list FIRST before processing any files
    - Only link the FIRST mention of each entity per file
    - Work from clean slate - don't preserve existing links, update them as needed
    - Use proper markdown link syntax
    - Verify all target files exist before creating links
    - Be systematic and thorough - process every single adventure file
    - Handle entity name variations (nicknames, quotes, etc.)
    - Report a comprehensive summary of all changes made

    ## Expected Output:
    Provide a detailed summary of:
    - Complete entity database generated (count by type)
    - Total files processed
    - Total links added/updated
    - Breakdown by entity type (characters/ships/systems/factions)
    - List of any entity name variations handled
    - Any issues encountered
    - Verification that all links are working

    Process adventure-$ARGUMENTS completely and systematically, starting with the complete entity database generation.
```