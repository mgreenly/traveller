# Traveller Campaign: The Long Haul

> A ship you can't afford. A debt you can't pay. A secret you can't escape.

Welcome to **"The Long Haul"**, a high-stakes Traveller RPG campaign set in the Spinward Marches. This repository contains all campaign materials, from adventures and NPCs to starships and political factions.

## 🚀 Current Adventure

**[Adventure 001: The Inheritance](./adventure-001/README.md)** - The players inherit the advanced lab ship *Stardust Drifter*, abandoned in the quarantined Djinni system. To claim their prize, they must navigate predatory financiers, ruthless mercenaries, and shadowy megacorporations—all while uncovering dangerous secrets locked in the ship's data core.

---

## 📚 Campaign Resources

### Core Materials
- **[Adventures](./adventure-001/README.md)** - Complete adventure modules with scenes and encounters
- **[Traveller Characters](./travellers/README.md)** - The heroes (or scoundrels) of our story
- **[NPCs & Characters](./characters/README.md)** - Allies, contacts, rivals, and villains

### Setting & Equipment  
- **[Starships](./ships/README.md)** - Vessels from the players' prize to enemy fleets
- **[Star Systems](./systems/README.md)** - Worlds to explore from core systems to lawless frontiers
- **[Factions](./factions/README.md)** - Organizations shaping the campaign's politics

### Reference Materials
- **[Lore & Encounters](./lore/README.md)** - Locations, establishments, brands, and historical events
- **[Rules & Tables](./rules/README.md)** - Game mechanics, equipment, and reference materials
- **[Session Notes](./sessions/README.md)** - Campaign session narratives and records

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
wip              # Save all changes to wip branch
main "MESSAGE"   # Squash merge wip into main with message
```

**Available Commands** (via direnv):
- `wip` - Commits all changes to wip branch and pushes to GitHub
- `main "message"` - Squash merges wip to main, commits with message, and pushes to GitHub

### Safety Features
- **Docker Isolation** - Nothing outside project folder can be changed
- **Version Control** - Every change tracked, easy rollback with `git reset`
- **Audit Trail** - Complete development history
- **Risk-free Experimentation** - Try bold changes knowing you can revert

---

## 📂 Project Structure

### Key Files
- **[CLAUDE.md](./CLAUDE.md)** - AI assistant configuration and context
- **[Dockerfile](./Dockerfile)** - Container definition
- **[bin/](./bin/)** - Utility scripts for development

### Content Organization
- **adventures/** - Structured adventure modules with scenes and NPCs
- **characters/** - NPC data sheets organized by affiliation
- **ships/** - Detailed starship specifications
- **systems/** - Star system data and planetary information
- **factions/** - Political and corporate organizations
- **lore/** - Reusable locations, brands, and historical events
- **rules/** - Game mechanics quick references
- **travellers/** - Traveller character records
- **sessions/** - Campaign session narratives
- **books/** - Reference materials (Mongoose Traveller 2022)

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

