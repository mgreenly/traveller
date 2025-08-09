# Combat Reference

## Table of Contents
- [Combat Overview](#combat-overview)
- [Initiative and Turn Order](#initiative-and-turn-order)
- [Combat Actions](#combat-actions)
- [Attack Resolution](#attack-resolution)
- [Damage and Armor](#damage-and-armor)
- [Special Situations](#special-situations)
- [Quick Reference Tables](#quick-reference-tables)

## Combat Overview

Combat is divided into **6-second rounds**. Each participant acts once per round in initiative order.

### Basic Combat Sequence
1. Determine surprise (if applicable)
2. Roll initiative
3. Participants act in initiative order
4. Repeat steps 3 until combat ends

## Initiative and Turn Order

### Rolling Initiative
**2D + DEX DM** (or INT DM if ambushing/tactical advantage)

### Turn Order
1. Highest initiative acts first
2. Ties act simultaneously
3. Continue in descending order
4. Repeat each round

### Surprise
- Surprised combatants cannot act in first round
- Attackers get one free round of actions

## Combat Actions

Each turn, a combatant can perform:
- **1 Significant Action** + **1 Minor Action**, OR
- **3 Minor Actions**

### Significant Actions
- **Attack:** Make one attack
- **Coup de Grace:** Auto-kill helpless opponent
- **Full Throttle:** Move up to 6x speed (requires Athletics check)
- **Sprint:** Move up to 4x normal speed

### Minor Actions
- **Aim:** +1 DM to next attack (max +6)
- **Change Stance:** Stand/crouch/prone
- **Draw/Sheathe:** Ready or stow a weapon
- **Leadership:** INT or SOC + Leadership to grant ally +2 to next check
- **Movement:** Move up to 6m (or 10m if Athletics (dexterity) or Athletics (endurance) skill 1+)
- **Miscellaneous:** Open door, operate device, take cover, etc.
- **Reload:** Reload a weapon

### Reactions (Not an Action)
**You get ONE reaction per combat round** - choose between:
- **Dodge:** Impose -1 DM on one incoming attack
- **Parry:** Use Melee skill to oppose one melee attack

Note: You must choose which attack to react to when it happens. Once used, you cannot react again until your next turn.

### Extended Actions
- **Automatic Fire:** Full-auto weapons only
  - Spend minor actions for extra attacks (max 3 total)
  - Each extra attack at cumulative -2 DM
- **Battlefield Medicine:** INT + Medic (1D minutes)

## Attack Resolution

### Basic Attack Roll
**2D + Skill + Characteristic DM ≥ 8**

### Gun Combat Attack
1. **Roll:** 2D + DEX DM + Gun Combat
2. **Modifiers:**
   - Range (see Range Bands below)
   - Aim bonus (+1 per aim, max +6)
   - Cover (-2 partial, -4 full)
   - Target stance (-1 crouching, -2 prone)
3. **Success:** Roll damage

### Melee Attack
1. **Roll:** 2D + STR or DEX DM + Melee
2. **Modifiers:**
   - Opponent can parry (opposed Melee check)
   - Size difference modifiers
3. **Success:** Roll damage

### Range Bands (Gun Combat)
- **Personal (0-5m):** +1 DM
- **Close (5-10m):** +0 DM
- **Short (10-50m):** +0 DM
- **Medium (50-250m):** -2 DM
- **Long (250-500m):** -4 DM
- **Very Long (500m+):** -6 DM

## Damage and Armor

### Applying Damage
1. Roll weapon damage
2. Apply Effect from attack roll:
   - **Effect 0-5:** Normal damage
   - **Effect 6+:** +1 damage per point of Effect above 5
3. Subtract armor protection
4. Apply to characteristics

### Damage Allocation
**For each attack that causes damage:**
1. All damage is initially applied to END
2. If END reaches 0, excess damage goes to either STR or DEX (target's choice)
3. If two characteristics reach 0, remaining damage goes to the last characteristic
4. If all three physical characteristics reach 0, character dies

Example: Taking 7 damage with END 4, STR 8, DEX 6:
- 4 damage reduces END to 0
- 3 excess damage goes to STR or DEX (target chooses)
- If target chooses DEX: DEX becomes 3

### Characteristic Damage Effects
- **First characteristic at 0:** Wounded but functional
- **Two characteristics at 0:** Unconscious
- **Three characteristics at 0:** Dead

### Armor
- Reduces damage by protection value
- Does not stack (use highest value)
- May have DM penalties to DEX

## Special Situations

### Cover
- **Partial Cover (-2 to hit):** Half body exposed
- **Full Cover (-4 to hit):** Only small part exposed
- **Total Cover:** Cannot be targeted directly

### Suppression Fire
1. Declare suppression (automatic weapon required)
2. Target area (up to 10m wide)
3. Anyone in area must make **8+ Morale check** (2D + lowest of INT/SOC) or:
   - Duck for cover (no actions this round)
   - May move to cover as reaction

### Grenades
1. **Throw:** DEX + Athletics, range = STR × 3 meters
2. **Miss:** Scatters 1D meters in random direction
3. **Damage:** All within blast radius

### Grappling
1. **Initiate:** Opposed Melee (unarmed) checks
2. **While Grappled:**
   - -2 DM to all physical actions
   - Can attempt to break free (opposed STR + Melee)
   - Can attack grappler only

### Battlefield Conditions
- **Darkness:** -2 to -4 DM to attacks
- **Smoke/Fog:** -1 to -2 DM
- **Zero-G:** -2 DM without Vacc Suit skill
- **Moving Platform:** -1 to -2 DM

## Quick Reference Tables

### Attack DM Summary
| Condition | DM |
|-----------|-----|
| Aiming | +1 per minor action (max +6) |
| Personal range (≤5m) | +1 |
| Medium range | -2 |
| Long range | -4 |
| Very Long range | -6 |
| Target dodging | -1 |
| Target crouching | -1 |
| Target prone | -2 |
| Partial cover | -2 |
| Full cover | -4 |
| Darkness | -2 to -4 |
| Auto-fire (2nd attack) | -2 |
| Auto-fire (3rd attack) | -4 |

### Common Weapon Damages
| Weapon | Damage | Special |
|--------|--------|---------|
| Unarmed | 1D | |
| Blade | 2D | |
| Stunner | 2D+3 | Stun only |
| Body Pistol | 2D | |
| Autopistol | 3D-3 | |
| Revolver | 3D | |
| Rifle | 3D | |
| Assault Rifle | 3D | Auto 2 |
| Shotgun | 4D | Bulky |
| Laser Rifle | 5D | |

### Armor Protection
| Armor Type | Protection | DEX Penalty |
|------------|------------|-------------|
| Jack | 1 | - |
| Mesh | 2 | - |
| Cloth | 5 | - |
| Flak Jacket | 6 | -2 |
| Combat Armor | 13 | -2 |
| Battle Dress | 22 | - (powered) |

### Combat Example: Gunfight
1. **Surprise?** Ambushers roll Stealth vs Recon
2. **Initiative:** Everyone rolls 2D + DEX DM
3. **Round 1:**
   - Highest initiative: Minor action (aim), Significant action (attack)
   - Roll: 2D + DEX + Gun Combat + 1 (aim) ≥ 8
   - If hit: Roll damage, subtract armor, apply to target
4. **Continue** until one side surrenders/flees/falls

### Combat Example: Melee
1. **Close Distance:** May require movement/sprint actions
2. **Attack:** 2D + STR/DEX + Melee ≥ 8
3. **Defender Reaction:** Can dodge (-1) or parry (opposed Melee)
4. **Damage:** If hit, roll damage + Effect bonus
5. **Grapple Option:** Opposed Melee to initiate
