# Traveller Campaign: The Long Haul

> A ship you can't afford. A debt you can't pay. A secret you can't escape.

Welcome to the campaign notes for **"The Long Haul"**, a high-stakes adventure set in the Spinward Marches of the Traveller universe. This repository contains all the necessary documents, characters, and lore for the campaign.

## The Adventure So Far...

The campaign begins with **Adventure 001: The Inheritance**, where the players receive an unexpected bequest: the advanced lab ship *Stardust Drifter*. The only catch is the ship is abandoned in the **Djinni** system, a quarantined Red Zone. To recover their prize, the players must plunge into a world of predatory financiers, ruthless mercenaries, and shadowy megacorporations, all of whom want the ship and the dangerous secrets locked in its data core.

---

## Campaign Resources

This project is organized into the following sections for easy reference:

### [Adventure 001: The Inheritance](./adventure-001.md)
The full adventure module, detailing the plot, scenes, encounters, and key decision points for the players.

### [Dramatis Personae](./characters/README.md)
A complete index of all Non-Player Characters (NPCs), from helpful allies and crucial contacts to dangerous rivals and implacable villains.

### [Player Characters](./players/README.md)
The heroes (or scoundrels) of our story.

### [Starships of the Sector](./ships/README.md)
Details and statistics for all key starships featured in the campaign, including the players' prize, their ride, and the vessels of their enemies.

### [Subsector Systems & Maps](./systems/README.md)
Descriptions, maps, and key data for all star systems the players will visit, from the gleaming core worlds to the lawless fringe.

### [Factions & Powers](./factions/README.md)
An overview of the major factions and organizations whose influence shapes the events of the campaign, from the Imperial Navy to the secretive Cultivators.

### [Lore & Setting Details](./misc/README.md)
Supplementary documents covering important game rules and setting details, such as Imperial Law Levels and the dangers of Red Zones.

---

## Technical Notes

This campaign repository is managed using Claude AI running in a Docker container for enhanced workflow and sandboxing capabilities.

### Docker Setup
- **Dockerfile**: [`Dockerfile`](./Dockerfile)
- **Build Script**: [`bin/build`](./bin/build) - Builds the Docker container
- **Claude Runner**: [`bin/claude`](./bin/claude) - Launches Claude Code CLI in the container

This setup uses Vim for editing and Claude Code CLI for AI assistance - no IDE required.

### Why Docker?
We run Claude in a containerized environment to:
- **Sandbox operations** - Provides a safe, isolated workspace for file manipulation
- **Skip permissions checks** - Uses `--dangerously-skip-permissions` flag for faster operations in our sandboxed environment
- **Consistent environment** - Ensures the same tooling and file system across sessions
- **Complete isolation** - Nothing outside the project folder can be changed, protecting the host system

### Workflow Safety Net
The human operator commits changes to git between Claude interactions, ensuring:
- **Version control** - Every change is tracked and documented
- **Easy rollback** - Previous state is always just one `git reset` away
- **Audit trail** - Complete history of all campaign development
- **Risk-free experimentation** - Can try bold changes knowing we can always revert

This combination of Docker sandboxing and git version control allows for rapid, fearless campaign development while maintaining complete safety and reversibility.

## Git Stuff

How I'm using Git

- git checkout -b wip              # Create feature branch
- # work with the AI, a commit per prompt
- git checkout main                # Switch to target branch
- git merge --squash wip           # Merge feature into main
- git commit -m "Your message"     # Create the squashed commit
- git branch -d wip                # Delete feature branch


