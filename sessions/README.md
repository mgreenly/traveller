# Session Narratives

## Overview

This directory contains fictionalized narratives of our Traveller campaign sessions. Each session is transformed from gameplay notes into immersive stories told from the perspective of someone fifty years in the future, reminiscing about the legendary adventures of our crew.

## Directory Structure

- `src/` - Source directory containing raw session notes
  - Format: `YYYYMMDD-<kebab-case-title>.md`
  - Contains gameplay notes, dice rolls, and referee annotations
  
- Root directory - Fictionalized session narratives
  - Format: `YYYYMMDD-<kebab-case-title>.md`
  - Contains narrative retellings of the sessions

## The Narrative Framework

### The Narrator
Our stories are told by an unnamed individual, fifty years after the events occurred. This narrator:
- Is often found in bars, starports, or other gathering places
- Tells these tales to anyone who will listen
- Has imperfect memory, leading to embellishments and occasional inaccuracies
- Views "the Star Duster's crew" as legendary figures from a bygone era
- **Emphasizes the pre-war timing:** These events took place before the Fifth Frontier War, when no one quite realized what was coming
- Comments on the innocence of those days, before the war changed everything
- **Exaggerates the crew's abilities:** Remembers them as nearly superhuman - failed attempts become narrow escapes, successes become impossible feats
- May conflate events, exaggerate details, or add colorful flourishes
- Initially refers to the protagonists collectively as "the Star Duster's crew" - individual names may emerge over time
- May allude to them becoming known by other, more famous names in the future - hinting at greater legends yet to come

### Narrative Style
Each fictionalized session:
- **Length:** Approximately 2 pages of text (800-1000 words) per session
- Opens with 2-3 sentences establishing where the narrator is and who they're telling the story to
- Transforms mechanical game events into dramatic narrative moments
- Incorporates sensory details and atmospheric descriptions
- References the aesthetic characteristics defined in `lore/aesthetics.md`
- **World Consistency:** Uses established details from `characters/`, `lore/`, and `systems/` folders
- Maintains consistency with previous session narratives
- Prioritizes storytelling over strict accuracy to actual events
- Expands brief gameplay notes into fully realized scenes with dialogue and description
- **Scene Transitions:** Includes smooth narrative bridges between scenes that maintain flow
- **Dramatic Reordering:** Events may be rearranged from the source notes for better pacing

### Creative License
The fictionalization process embraces:
- **Embellishment:** Dice rolls become dramatic moments of tension
- **Hero-making:** The crew's abilities are consistently exaggerated - mundane piloting becomes death-defying stunts, basic repairs become engineering miracles
- **Characterization:** NPCs and PCs gain depth through the narrator's perspective
- **Atmosphere:** Technical descriptions transform into vivid sensory experiences
- **Unreliability:** The narrator's faulty memory adds charm and mystery
- **Legend-building:** Events are filtered through fifty years of retelling, with each retelling making the crew more legendary
- **Expansion:** Brief notes are elaborated into full scenes to reach the target length of 2 pages
- **Creative filling:** When source material is sparse, the narrator adds colorful details and subplots

## Using the /update-session Command

To create a fictionalized narrative from session notes:

```
/update-session YYYYMMDD
```

Example: `/update-session 20250810`

This command will:
1. Read up to 10 previous session narratives (if they exist) to maintain consistency
2. Consult relevant `characters/`, `lore/`, and `systems/` files for accurate world details
3. Read the source file from `sessions/src/20250810-<title>.md`
4. Transform it into a narrative with smooth scene transitions
5. Write the fictionalized version to `sessions/20250810-<title>.md`

## The Purpose

These narratives serve multiple functions:
- **Immersion:** Transform game mechanics into living stories
- **Documentation:** Preserve campaign history in an engaging format
- **World-building:** Add depth and texture to the game universe
- **Entertainment:** Create readable stories that capture the spirit of play
- **Legacy:** Build the mythology of the crew's adventures
- **Historical Context:** Capture the feel of the pre-Fifth Frontier War era, when the galaxy seemed more stable and the coming conflict was still unimaginable

## A Note on Truth

Remember: these are stories told in bars fifty years hence. The truth has been filtered through time, alcohol, and the natural tendency of tales to grow in the telling. What matters isn't perfect accuracy, but capturing the spirit of adventure that made these travelers legendary.