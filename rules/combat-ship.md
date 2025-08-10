# Ship Combat Reference (Combat Flow Order)

## Pre-Combat Setup

### Step 0: Jump Emergence Detection

**Jump Flash Detection (if applicable):**
- Ships emerging from jump create a distinctive "jump flash"
- **Check:** 2D + Electronics (sensors) + INT/EDU DM ≥ Target
- **Automatic detection** within 1,000,000km (no roll needed)
- **Routine (6+)** at Very Distant range (up to 5 million km)
- **Average (8+)** at Far range (>5 million km)
- **Stealth jump drives:** -4 DM to detection rolls
- Ships typically emerge at 100-diameter limit (varies by system)
- **Note:** Jump flash is much easier to detect than the ship itself

### Step 1: Determine Range (Core Rules p.165)

**Starting Ranges:**
- **Jump Emergence:** Typically Distant or Very Distant from other ships
- **Hostile Encounter:** Usually Very Long or Distant when first detected
- **Ambush/Surprise:** Could start at any range, even Adjacent
- **Pirates:** May start at Close if successfully pretending to be merchants

#### Space Combat Range Bands
| Range Band | Distance | Thrust to Cross | Notes |
|------------|----------|-----------------|-------|
| **Adjacent** | ≤1km | 1 | Boarding possible, switch to Dogfighting |
| **Close** | 1-10km | 1 | Dogfighting rules (6-second rounds) |
| **Short** | 11-1,250km | 2 | Called shots possible |
| **Medium** | 1,251-10,000km | 5 | Typical combat range |
| **Long** | 10,001-25,000km | 10 | Energy weapons max range |
| **Very Long** | 25,001-50,000km | 25 | Limited weapons effective |
| **Distant** | 50,001-300,000km | 50 | Missiles and sensors only |

### Step 2: Detection and Identification

#### Detection Requirements
**You must detect a target before you can:**
- Fire any weapons at it
- Launch missiles toward it
- Perform sensor locks
- Identify friend from foe

#### Sensor Detection Table (Core Rules p.160)
| Range Band | Detection Difficulty | Information Available |
|------------|---------------------|----------------------|
| **Adjacent-Close** | Automatic | Full: Hull markings, damage, weapon status |
| **Short** | Easy (4+) | Ship type, configuration, tonnage |
| **Medium** | Routine (6+) | General type, drive signatures |
| **Long** | Average (8+) | Size category, emissions |
| **Very Long** | Difficult (10+) | "Something ship-sized" |
| **Distant** | Very Difficult (12+) | Large object, maybe artificial |

#### Detection Check
**2D + Electronics (sensors) + INT/EDU DM ≥ Target Number**

**Key Modifiers:**
| Condition | DM |
|-----------|-----|
| Active sensors | +2 |
| Target using active sensors | +4 |
| Military/Scout sensors | +2 |
| Target powered down | -4 |
| Target in asteroid field | -4 |
| Per 1,000 tons of target | +1 (max +6) |

### Step 3: Assign Crew Positions (Core Rules p.164)

**Before combat begins, assign all crew to positions:**

| Position | Max per Ship | Primary Role |
|----------|--------------|--------------|
| **Pilot** | 1 | Ship control, evasive maneuvers |
| **Captain** | 1 | Leadership, tactics, coordination |
| **Sensor Operator** | Multiple | Detection, electronic warfare |
| **Turret Gunner** | 1 per turret | Weapon control |
| **Engineer** | Multiple | Power, drives, damage control |
| **Marine** | Multiple | Boarding actions |

### Step 4: Roll Initiative (Core Rules p.165)

**Once per combat (not per round):**
**2D + Pilot skill + Ship's Thrust**

**Modifiers:**
- **Tactics (naval):** Captain's check adds Effect to Initiative
- **Surprise:** -6 to unaware side (first round only)
- **Ambush:** +6 to aware side (first round only)

---

## Combat Round Structure (6-minute rounds)

### Each Round Has Three Steps (In Initiative Order):

#### 1. MANEUVER STEP
All ships allocate Thrust (in Initiative order)

#### 2. ATTACK STEP  
All ships fire weapons (in Initiative order)

#### 3. ACTIONS STEP
All ships perform other actions (in Initiative order)

---

## Step 1: Maneuver Step

### Pilot Allocates Thrust Between:

#### A. Movement (Changing Range)
**Thrust Required to Change Range Band:**
- See Range Band table above
- Ships approaching: Add Thrust together
- One escaping: Subtract slower from faster
- Can accumulate over multiple rounds

#### B. Combat Maneuvers (1 Thrust each)
- **Aid Gunners:** Pilot check to give gunners task chain bonus
- **Docking:** Pilot check (opposed if unwilling)
- **Line Up Shot:** For fixed weapons only

#### C. Reserve for Reactions
- **Evasive Action:** Keep unspent Thrust for dodging
- Each point allows dodging one attack
- Attack suffers -Pilot skill DM

---

## Step 2: Attack Step

### Making Attacks (Core Rules p.167)

**Basic Attack Roll:**
**2D + Gunner (turret) + DEX DM ≥ 8**

#### Weapon Range Modifiers
| Range | DM | Notes |
|-------|-----|-------|
| Short | +1 | Optimal range |
| Medium | 0 | Standard range |
| Long | -2 | Maximum for most weapons |
| Very Long | -4 | Few weapons reach |
| Distant | -6 | Missiles only |

#### Weapon Type Bonuses
- **Pulse Laser:** +2 to hit
- **Beam Laser:** +4 to hit
- **Target Size:** +1 per 1,000 tons (max +6)

### Common Spacecraft Weapons (Core Rules p.167-168)
| Weapon | TL | Range | Damage | Notes |
|--------|-----|-------|--------|-------|
| **Beam Laser** | 10 | Medium | 1D | Accurate (+4) |
| **Pulse Laser** | 9 | Long | 2D | Standard (+2) |
| **Missile Rack** | 7 | Special | 4D | See missile rules |
| **Particle Barbette** | 11 | Very Long | 4D | Requires barbette |
| **Sandcaster** | 9 | - | - | Defensive only |

### Reactions (During Attack Step)

#### Available Reactions:
1. **Evasive Action (Pilot):** -Pilot skill to attack, costs 1 reserved Thrust
2. **Point Defense (Gunner):** Shoot down missiles with lasers
3. **Disperse Sand (Gunner):** Block laser attacks with sand

### Missile Combat (Core Rules p.172)

#### Launch
- All missiles fired at one target = one salvo
- Missiles have Thrust 10

#### Flight Times
| Launch Range | Rounds to Impact |
|--------------|------------------|
| Medium or less | Immediate |
| Long | 1 round |
| Very Long | 4 rounds |
| Distant | 10 rounds |

#### Detection
- Routine (6+) to detect launch if firing ship detected
- Average (8+) if firing ship undetected
- +1 DM per 10 missiles

#### Impact
- Roll: 2D + 1 per missile remaining ≥ 8
- Damage: 4D × Effect (max = missiles in salvo)

---

## Step 3: Actions Step

### Actions by Crew Position (Core Rules p.171-172)

#### Captain
- **Improve Initiative:** Leadership check modifies next round

#### Pilot
- Already acted in Maneuver Step
- Can fire fixed mount weapons at -2

#### Sensor Operator
- **Sensor Lock:** +2 to all attacks vs target
- **Electronic Warfare:** Jam communications
- **Break Lock:** Opposed check
- **Destroy Missiles:** Difficult (10+) check vs salvo

#### Engineer
- **Emergency Jump:** Difficult checks, 1D minutes
- **Offline System:** Free up power
- **Overload Drive:** +1 Thrust next round (Difficult)
- **Overload Plant:** +10% Power (Difficult)
- **Repair Critical:** Average (8+), -Severity DM

#### Gunner
- **Reload:** Missiles or sand
- Can switch to different turret

#### Marine
- **Boarding Action:** If Adjacent
- **Repel Boarders:** Defend ship

---

## Damage Resolution

### Applying Damage (Core Rules p.168)
1. Roll weapon damage
2. Add Effect from attack
3. Subtract Armor
4. Apply to Hull
5. If Hull = 0: Ship wrecked

### Critical Hits (Core Rules p.169-170)

**Trigger:** Effect 6+ on damaging attack

**Severity = Effect - 5**
- Effect 6 = Severity 1
- Effect 8 = Severity 3
- Effect 11+ = Severity 6

**Location:** Roll 2D on table
| 2D | Location |
|----|----------|
| 2 | Sensors |
| 3 | Power Plant |
| 4 | Fuel |
| 5 | Weapon |
| 6 | Armor |
| 7 | Hull |
| 8 | M-Drive |
| 9 | Cargo |
| 10 | J-Drive |
| 11 | Crew |
| 12 | Bridge |

### Sample Critical Effects
| System | Severity 1 | Severity 3 | Severity 6 |
|--------|------------|------------|------------|
| **Sensors** | -2 to checks | Blind beyond Short | Destroyed |
| **Power** | -10% power | -50% power | No power |
| **M-Drive** | -1 Thrust | -50% Thrust | Destroyed |
| **Hull** | Breach | Casualties | Explosive decompression |

---

## Special Situations

### Boarding Actions (Core Rules p.175)
**Requirements:**
- Adjacent range (≤1km)
- Successful docking or breaching
- Marines to storm enemy ship

### Dogfighting (Core Rules p.174)
**When to Use:**
- Ships at Close range or less (≤10km)
- Switch to 6-second rounds
- Use vehicle combat rules

---

## Quick Reference

### Combat Checklist
☐ Determine starting range  
☐ Make detection checks  
☐ Assign crew to positions  
☐ Roll Initiative  
☐ Begin combat rounds:
  - ☐ Maneuver Step (allocate Thrust)
  - ☐ Attack Step (fire weapons)
  - ☐ Actions Step (other actions)
☐ Apply damage and critical hits  
☐ Check for destroyed/surrendering ships

### Essential Modifiers Summary
| Situation | Modifier |
|-----------|----------|
| **Detection** | See Detection Table |
| **Initiative** | 2D + Pilot + Thrust |
| **Attack** | 2D + Gunner + DEX ≥ 8 |
| **Range** | +1 Short, -2 Long, -4 Very Long |
| **Evasion** | -Pilot skill if dodging |
| **Sensor Lock** | +2 to attacks |
| **Missiles** | +1 per missile in salvo |