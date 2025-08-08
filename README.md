# Traveller Campaign: The Long Haul

> A ship you can't afford. A debt you can't pay. A secret you can't escape.

Welcome to **"The Long Haul"**, a high-stakes Traveller RPG campaign set in the Spinward Marches. This repository contains all campaign materials, from adventures and NPCs to starships and political factions.

## 🚀 Current Adventure

**[Adventure 001: The Inheritance](./adventure-001/README.md)** - The players inherit the advanced lab ship *Stardust Drifter*, abandoned in the quarantined Djinni system. To claim their prize, they must navigate predatory financiers, ruthless mercenaries, and shadowy megacorporations—all while uncovering dangerous secrets locked in the ship's data core.

---

## 📚 Campaign Resources

### Core Materials
- **[Adventures](./adventure-001/README.md)** - Complete adventure modules with scenes and encounters
- **[Player Characters](./players/README.md)** - The heroes (or scoundrels) of our story
- **[NPCs & Characters](./characters/README.md)** - Allies, contacts, rivals, and villains

### Setting & Equipment  
- **[Starships](./ships/README.md)** - Vessels from the players' prize to enemy fleets
- **[Star Systems](./systems/README.md)** - Worlds to explore from core systems to lawless frontiers
- **[Factions](./factions/README.md)** - Organizations shaping the campaign's politics

### Reference Materials
- **[Lore & Encounters](./lore/README.md)** - Locations, establishments, and reusable encounters
- **[Rules & Tables](./misc/README.md)** - Game mechanics, equipment, and reference materials

---

## ⚙️ Development Workflow

This campaign uses Claude AI running in Docker for safe, sandboxed development with git version control.

### Quick Start
```bash
bin/build    # Build Docker container
bin/claude   # Launch Claude Code CLI
```

### Development Stack
- **Editor**: Vim
- **AI Assistant**: Claude Code CLI
- **Environment**: Docker (sandboxed operations)
- **Version Control**: Git with feature branches

### Git Workflow
```bash
gwip                    # Create feature branch
claude                  # Work with Claude AI
gmain                   # Switch to main
gsquash                 # Squash merge changes  
gcommit "description"   # Commit with message
gclean                  # Delete feature branch
```

**Available Commands** (via direnv):
- `gwip` - Create and switch to wip branch
- `gadd` - Stage and commit all changes with 'wip' message (wip branch only)
- `grollback` - Reset last commit (wip branch only)
- `gmain` - Switch to main branch
- `gsquash` - Squash merge wip → main
- `gcommit "msg"` - Commit with message and push to GitHub
- `gclean` - Delete wip branch

### Safety Features
- **Docker Isolation** - Nothing outside project folder can be changed
- **Version Control** - Every change tracked, easy rollback with `git reset`
- **Audit Trail** - Complete development history
- **Risk-free Experimentation** - Try bold changes knowing you can revert

---

## 🛠️ Technical Details

### Docker Configuration
- **[Dockerfile](./Dockerfile)** - Container definition
- **[bin/build](./bin/build)** - Container build script  
- **[bin/claude](./bin/claude)** - Claude Code launcher
- **[.envrc](./.envrc)** - Git workflow aliases via direnv

### Development Philosophy
This setup combines Docker sandboxing with git version control for rapid, fearless campaign development while maintaining complete safety and reversibility.

---

*Built with Claude Code CLI, Docker, and Vim*