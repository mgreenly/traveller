# Ship Combat Reference

## Table of Contents (In Order of Use)
- [Pre-Combat Setup](#pre-combat-setup)
  - [Range Determination](#range-determination)
  - [Detection and Sensors](#detection-and-sensors)
  - [Crew Positions](#crew-positions)
- [Combat Sequence](#combat-sequence)
  - [Initiative](#initiative)
  - [Combat Round Structure](#combat-round-structure)
- [Maneuver Step](#maneuver-step)
  - [Movement](#movement)
  - [Combat Maneuvers](#combat-maneuvers)
- [Attack Step](#attack-step)
  - [Weapons and Attacks](#weapons-and-attacks)
  - [Missile Combat](#missile-combat)
  - [Reactions and Defensive Actions](#reactions-and-defensive-actions)
- [Actions Step](#actions-step)
  - [Actions by Position](#actions-by-position)
  - [Electronic Warfare](#electronic-warfare)
- [Damage Resolution](#damage-resolution)
  - [Damage and Critical Hits](#damage-and-critical-hits)
- [Special Situations](#special-situations)
  - [Boarding Actions](#boarding-actions)
  - [Dogfighting](#dogfighting)
- [Quick Reference Tables](#quick-reference-tables)

## Combat Overview

### Basic Sequence (Core Rules p.164)
Space combat uses **6-minute rounds** (not 6 seconds like personal combat)

**Combat Steps Each Round:**
1. **Maneuver Step:** Ships allocate Thrust for movement/maneuvers (Initiative order)
2. **Attack Step:** Ships fire weapons and launch missiles (Initiative order)  
3. **Actions Step:** Crew perform other actions like repairs, jumping (Initiative order)

### Combat Scales
- **Long Range Combat:** Thousands of kilometers, methodical submarine-like warfare
- **Dogfighting:** Close range (≤10km), uses vehicle combat rules (Core Rules p.174)

## Detection and Sensors

### Sensor Detection by Range Band

| Range Band | Distance | Detection Check | Information Available | Time Delay |
|------------|----------|-----------------|----------------------|-------------|
| **Adjacent** | ≤1km | Automatic | Full detail: hull markings, weapon status, damage | Instant |
| **Close** | 1-10km | Automatic | Ship class, configuration, active systems | Instant |
| **Short** | 11-1,250km | Easy (4+) | Ship type, size, basic configuration | Instant |
| **Medium** | 1,251-10,000km | Routine (6+) | Tonnage, general type, thrust signature | 0.03 seconds |
| **Long** | 10,001-25,000km | Average (8+) | Size category, drive emissions | 0.08 seconds |
| **Very Long** | 25,001-50,000km | Difficult (10+) | "Something ship-sized", heat signature | 0.17 seconds |
| **Distant** | 50,001-300,000km | Very Difficult (12+) | Large object presence, maybe artificial | 1 second |
| **Very Distant** | 300,001-5,000,000km | Formidable (14+) | Jump flash detection only | 17 seconds |
| **Far** | >5,000,000km | Impossible (16+) | Jump emergence signature | >17 seconds |

### Active vs Passive Sensors (Starship Operator's Manual p.68-69)
- **Passive Sensors:** Detect emissions, heat, reflected light
  - No detection risk to scanning ship
  - -2 DM at Long range and beyond
  - Cannot penetrate stealth systems
- **Active Sensors:** Send out "pings" to get returns
  - +2 DM to detection rolls
  - Reveals scanning ship's position (automatic detection by target)
  - Can penetrate basic stealth at closer ranges

### Sensor Checks
**Basic Roll:** 2D + Electronics (sensors) + INT or EDU DM ≥ Target Number

**Common Modifiers:**
| Condition | DM |
|-----------|----|
| Active sensors | +2 |
| Military/Scout sensors | +2 |
| Improved sensors | +4 |
| Target using active sensors | +4 |
| Target accelerating >2G | +2 |
| Target in asteroid field/debris | -4 |
| Target powered down | -4 |
| Target has stealth coating | -2 to -4 |
| Per 1,000 tons of target | +1 (max +6) |
| Passive sensors at Long+ range | -2 |

### Evading Detection

**Silent Running Options:**
| Action | DM to be Detected | Consequences |
|--------|-------------------|------------|
| Power down weapons | -1 | Cannot fire without startup (1 round) |
| Minimum life support | -1 | Crew DM-1 to all checks |
| Drift (no thrust) | -2 | No movement or evasion |
| Power down active sensors | -2 | Cannot make sensor checks |
| Total shutdown | -6 | No power, emergency life support only |
| Hide behind celestial body | -4 to -8 | Must maintain position |
| Inside asteroid field | -4 | Navigation hazards |

### Transponders and IFF (Traveller Companion p.165-166)
- **Standard Operations:** Ships broadcast ID continuously
- **Disabling Transponder:** Illegal in most systems (Law Level 2+)
- **False Transponder:** Requires Electronics (comms) check vs sensors
- **Military IFF:** Encrypted friend-or-foe identification

### Detecting Specific Events

**Jump Emergence:**
- Creates distinctive "jump flash"
- Automatic detection within 1,000,000km
- Routine (6+) at Very Distant range
- Average (8+) at Far range
- Stealth jump drives: -4 DM to detection

**Missile Launch (Core Rules p.173):**
- Routine (6+) if firing ship detected
- Average (8+) if firing ship undetected  
- +1 DM per 10 missiles (max +6)
- Can attempt detection each round after

**Weapons Fire:**
- Energy weapons: Automatic detection of firing ship
- Kinetic weapons: Difficult (10+) to detect launch
- Point defense: Reveals ship position

### Information Warfare
**Sensor Lock:** Successful check gives +2 to attacks
**Jamming:** Opposed Electronics check to break lock
**Spoofing:** Create false sensor returns (Deception or Electronics)

### Sensor Targeting Requirements

**Detection vs Targeting:**
- **Detection Required:** Cannot fire at undetected targets
- **Sensor Lock Needed:** For accurate fire beyond Close range
- **Identification Issues:** At Distant range, friendly fire risk due to poor target ID

**Targeting by Sensor Information Level:**
| Sensor Info | Range Typical | Can Target? | Notes |
|-------------|---------------|-------------|-------|
| **Full** | Adjacent-Close | Yes | Complete targeting data available |
| **Limited** | Short-Medium | Yes | Normal targeting, standard DMs apply |
| **Minimal** | Long-Very Long | Yes with -2 | Difficult targeting without lock |
| **None** | Beyond Distant | No | Cannot engage without detection |

**Practical Limits:**
- Energy weapons need line of sight (sensor contact)
- Missiles need target detection before launch
- Called shots only possible at Short range or less
- Point defense cannot engage missiles launched from Short range or closer

## Initiative and Combat Sequence

### Rolling Initiative (Core Rules p.165)
**2D + Pilot skill + Ship's Thrust score**

### Modifiers
- **Tactics (naval):** Commander makes check, Effect adds to ship/fleet Initiative (Core Rules p.165)
- **Surprise:** Surprised ships cannot act in first round (Core Rules p.165)
- **Ambush:** Aware side +6 Initiative, unaware side -6 Initiative (first round only)

## Crew Positions and Duties

### Essential Positions (Core Rules p.164)
| Position | Role | Limit |
|----------|------|-------|
| **Pilot** | Flies ship, evasive maneuvers | 1 per ship |
| **Captain** | Commands, uses Leadership/Tactics | 1 per ship |
| **Engineer** | Power plant, drives, damage control | Multiple allowed |
| **Sensor Operator** | Electronic warfare, tracking | Multiple allowed |
| **Turret Gunner** | Controls one turret | 1 per turret |
| **Bay Gunner** | Controls bay weapon | 1 per bay |
| **Marine** | Boarding/repelling boarders | Multiple allowed |
| **Passenger** | No combat duties | Unlimited |

### Automated Duties (Core Rules p.164-165)
- **Fire Control:** Acts as gunner or assists gunners
- **Auto-Repair:** Performs damage control (requires repair drones)
- **Intellect + Expert:** Can fill pilot, engineer, or sensor operator roles

## Range Bands

### Space Combat Ranges (Core Rules p.165)
| Range Band | Distance | Thrust to Cross |
|------------|----------|-----------------|
| **Adjacent** | ≤1km | 1 |
| **Close** | 1-10km | 1 |
| **Short** | 11-1,250km | 2 |
| **Medium** | 1,251-10,000km | 5 |
| **Long** | 10,001-25,000km | 10 |
| **Very Long** | 25,001-50,000km | 25 |
| **Distant** | >50,000km | 50 |

**Note:** At Close or Adjacent range, switch to Dogfighting rules (Core Rules p.174)

## Movement and Maneuvers

### Thrust Allocation (Core Rules p.165-166)
Pilot allocates ship's Thrust each round between:
1. **Movement:** Change range bands
2. **Combat Maneuvers:** Special actions

### Movement Rules (Core Rules p.166)
- Ships approaching: Add Thrust devoted to movement
- One escaping: Subtract lower from higher Thrust
- Can accumulate Thrust over multiple rounds

### Combat Maneuvers (1 Thrust each) (Core Rules p.166)
- **Aid Gunners:** Pilot check for task chain with gunners
- **Docking:** Pilot check (opposed if unwilling, -2 DM)
- **Evasive Action:** Reserve for dodging (see Reactions)

## Weapons and Attacks

### Attack Roll (Core Rules p.167)
**2D + Gunner (turret/bay) + DEX DM ≥ 8**

### Attack Modifiers (Core Rules p.167)
| Condition | DM |
|-----------|-----|
| Short Range | +1 |
| Long Range | -2 |
| Very Long Range | -4 |
| Distant Range | -6 |
| Pulse Laser | +2 |
| Beam Laser | +4 |
| Per 1,000 tons of target | +1 (max +6) |

### Weapon Types (Core Rules p.167-168)
| Weapon | TL | Range | Damage | Notes |
|--------|-----|-------|--------|-------|
| **Beam Laser** | 10 | Medium | 1D | Accurate (+4 DM) |
| **Pulse Laser** | 9 | Long | 2D | Less accurate (+2 DM) |
| **Missile Rack** | 7 | Special | 4D | 12 missiles per turret |
| **Nuclear Missile** | - | Special | 1DD | Highly illegal |
| **Particle Barbette** | 11 | Very Long | 4D | Requires barbette mount |
| **Sandcaster** | 9 | Special | Special | Defensive, 20 canisters |

### Double/Triple Turrets (Core Rules p.168)
- Different weapons: Only one type per round
- Same weapons: One roll, +1 damage per die per extra weapon
- Sandcasters: +1 damage blocked per extra sandcaster

### Damage Scale (Core Rules p.167)
**Spacecraft vs Ground Targets:**
- Spacecraft weapons: ×10 damage, Blast 10 trait
- Ground weapons vs Spacecraft: ÷10 damage

## Damage and Critical Hits

### Applying Damage (Core Rules p.168)
1. Roll weapon damage
2. Add Effect from attack roll
3. Subtract target's Armor
4. Apply to Hull
5. At 0 Hull: Ship wrecked

### Critical Hits (Core Rules p.168-170)
**Trigger:** Effect 6+ on damaging attack

**Determining Critical Hits:**
1. **Location:** Roll 2D, consult Critical Hit Location table
2. **Severity:** Effect of attack roll - 5
   - Effect 6 = Severity 1
   - Effect 7 = Severity 2
   - Effect 8 = Severity 3
   - Effect 9 = Severity 4
   - Effect 10 = Severity 5
   - Effect 11+ = Severity 6

**Multiple Hits to Same Location:**
- Use new severity or original +1, whichever is higher
- At Severity 6, location takes 6D extra damage per additional hit

**Sustained Damage:** Every 10% Hull loss = roll location for Severity 1 critical

### Critical Hit Effects Table (Core Rules p.170)
| System | Severity 1 | Severity 3 | Severity 6 |
|--------|------------|------------|------------|
| **Sensors** | -2 all checks | Inop beyond Short | Disabled |
| **Power Plant** | -10% power | -50% power | Power to 0, Hull +1D severity |
| **Fuel** | Leak 1D tons/hour | Leak 1D×10% | Tank destroyed, Hull +1D severity |
| **Weapon** | Random weapon -1 | Random destroyed | 1D explode, Hull +1 severity |
| **Armor** | -1 Armor | -1D Armor | -2D Armor, Hull +1 severity |
| **M-Drive** | -1 Thrust | -50% Thrust | Drive destroyed, Hull +1D severity |
| **J-Drive** | +1 week jump time | +1D weeks | Drive destroyed, misjump |
| **Hull** | Breach | 1D crew casualties | Hull -1D, explosive decompression |

## Reactions and Defensive Actions

### Evasive Action (Pilot) (Core Rules p.171)
- **Cost:** 1 unspent Thrust per attack dodged
- **Effect:** Attack suffers -DM equal to Pilot skill

### Point Defense (Gunner) (Core Rules p.171)
- **Weapon:** Turret laser (beam or pulse)
- **Target:** Missile salvos about to hit
- **Roll:** Gunner (turret) check
- **Effect:** Removes missiles equal to Effect
- **Bonus:** Double laser +1, Triple laser +2
- **Limit:** Once per round, weapon can't attack same round

### Disperse Sand (Gunner) (Core Rules p.171)
- **Weapon:** Sandcaster
- **Roll:** Gunner (turret) check vs laser attack
- **Effect:** +1D + Effect to armor vs that attack only
- **Cost:** 1 sand canister per use
- **vs Boarders:** 8D damage at Ground scale

## Actions by Position

### Pilot Actions
- **Movement:** Allocate Thrust to change range
- **Combat Maneuvers:** Aid gunners, dock, evade
- **Fire Fixed Weapons:** At -2 DM

### Captain Actions (Core Rules p.171)
- **Improve Initiative:** Leadership check, Effect modifies next round's Initiative
- **Coordinate:** Use Tactics skill for fleet operations

### Engineer Actions (Core Rules p.171-172)
- **Jump:** Emergency jump (Difficult checks, 1D minutes)
- **Offline System:** Power down systems to free power
- **Overload Drive:** +1 Thrust next round (Difficult, cumulative -2)
- **Overload Plant:** +10% Power next round (Difficult, cumulative -2)
- **Repair System:** Fix critical hits (8+ check, -Severity DM)

### Sensor Operator Actions (Core Rules p.172)
- **Sensor Lock:** Electronics (sensors) for +2 to hit target
- **Electronic Warfare:** Jam communications (opposed check)
- **Break Sensor Lock:** Opposed Electronics (sensors)
- **Detect Missiles:** Spot incoming salvos

### Gunner Actions (Core Rules p.172)
- **Fire Weapons:** Attack with assigned turret/bay
- **Reload Turret:** Reload missiles/sand (no attacks this round)
- **Point Defense:** Shoot down missiles
- **Disperse Sand:** Block laser attacks

### Marine Actions (Core Rules p.172)
- **Boarding Action:** Board enemy at Adjacent range
- **Repel Boarders:** Defend against boarding

## Missile Combat

### Missile Salvos (Core Rules p.172)
- **Salvo:** All missiles fired at one target in same round
- **Thrust:** 10 (for flight time calculation)
- **Smart Trait:** Lost at Adjacent/Close range

### Flight Times (Core Rules p.172)
| Launch Range | Rounds to Impact |
|--------------|------------------|
| Medium or less | Immediate |
| Long | 1 round |
| Very Long | 4 rounds |
| Distant | 10 rounds |

**Fuel Limit:** Missiles become inert after 10 rounds

### Missile Detection
**Routine (6+) Electronics (sensors) check** to detect launch
- Difficulty increases with range
- Must detect before can respond

### Missile Damage
- **Standard:** 4D
- **Nuclear:** 1DD (×10 damage)
- **Smart:** +1 to hit (except Close/Adjacent)

## Electronic Warfare

### Sensor Lock (Core Rules p.172)
- **Check:** Electronics (sensors)
- **Effect:** +2 to all attacks vs target
- **Duration:** Until broken

### Jamming (Core Rules p.172)
- **Communications:** Opposed Electronics (comms)
- **Sensors:** Opposed Electronics (sensors)
- **Effect:** Prevents communication/breaks lock

### Stealth Operations
- **Silent Running:** Minimize emissions
- **False Transponders:** Misidentify ship
- **Sensor Spoofing:** Create false readings

## Boarding Actions

### Requirements (Core Rules p.172, p.175)
- **Range:** Adjacent (≤1km)
- **Docking:** Successful opposed Pilot checks
- **Or:** Breaching pods, cutting gear

### Boarding Process
1. **Approach:** Move to Adjacent range
2. **Dock/Breach:** Pilot check or breach hull
3. **Storm:** Marines enter enemy ship
4. **Combat:** Personal scale combat in corridors
5. **Objective:** Bridge, engineering, or cargo

### Defenses
- **Point Defense:** Against breaching pods
- **Sand:** 8D damage to boarding parties
- **Marines:** Repel boarders in personal combat
- **Bulkheads:** Seal sections

## Quick Reference Tables

### Combat Action Summary
| Phase | Actions Available |
|-------|------------------|
| **Maneuver** | Allocate Thrust (movement/combat) |
| **Attack** | Fire weapons, launch missiles |
| **Actions** | Position-specific actions |
| **Reactions** | Dodge, point defense, sand |

### Skill Checks by Position
| Position | Primary Skills | Typical Checks |
|----------|---------------|----------------|
| **Pilot** | Pilot | 2D + Pilot + DEX |
| **Captain** | Leadership, Tactics | 2D + skill + SOC |
| **Engineer** | Engineer (j/m/power) | 2D + Engineer + INT/EDU |
| **Sensor Op** | Electronics | 2D + Electronics + INT/EDU |
| **Gunner** | Gunner | 2D + Gunner + DEX |
| **Marine** | Gun Combat, Melee | Personal combat rules |

### Combat Modifiers Summary
| Situation | Modifier |
|-----------|----------|
| **Range** | +1 Short, -2 Long, -4 Very Long, -6 Distant |
| **Weapons** | +2 Pulse, +4 Beam laser |
| **Target Size** | +1 per 1,000 tons (max +6) |
| **Evasion** | -Pilot skill if dodging |
| **Sensor Lock** | +2 if locked |
| **Cover** | Varies by obstacle |

### Damage Summary
- **Hull 0:** Ship wrecked, no power/life support
- **Critical Effect 6+:** Roll on critical table
- **Armor:** Reduces damage point-for-point
- **Scale:** Spacecraft weapons ×10 vs ground targets