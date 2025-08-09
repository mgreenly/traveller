# Radiation Encounter Reference

**Referee's Guide for Running Radiation Hazards**

## Table of Contents
- [Detection & Measurement](#detection--measurement)
- [Radiation Sources](#radiation-sources)
- [Effects & Damage](#effects--damage)
- [Protection & Mitigation](#protection--mitigation)
- [Treatment](#treatment)
- [Encounter Examples](#encounter-examples)
- [Quick Reference Tables](#quick-reference-tables)

---

## Detection & Measurement

### Detection Equipment (Core Rules p.117)
**Geiger Counter (TL7):** Basic radiation detector
- **Cost:** Cr250, **Mass:** 1kg
- Simple audio/visual warning system
- Cannot measure exact radiation levels
- **Range:** Detects presence within 10 meters

**PRIS Binoculars (TL12):** Portable Radiation Imaging System (Core Rules p.117)
- **Cost:** Cr3,500, **Mass:** 1.5kg  
- Observes electromagnetic spectrum from infrared to gamma rays
- Can visually identify radiation sources at distance
- More sophisticated than basic Geiger counter

**Ship Sensors:** Most spacecraft can detect radiation sources
- Radiation signatures show up on sensor sweeps
- Can identify stellar radiation, reactor leaks, weapon signatures
- **Range:** Depends on sensor quality and radiation intensity

### Measurement System
**Rads (Roentgen Absorbed Dose):** Standard radiation measurement unit (Core Rules p.81)
- **Cumulative:** All radiation exposure adds up over time
- **Permanent:** Cannot be naturally healed - only removed by anti-rad drugs
- **Tracked:** Referee must maintain running total per PC

### Detection Difficulties
| Radiation Level | Detection Difficulty | Equipment Needed |
|-----------------|---------------------|------------------|
| 1-50 rads/exposure | Automatic | Geiger counter |
| 51-200 rads/exposure | Automatic | Any detection device |
| 201+ rads/exposure | Automatic | Visible effects (glow, heat distortion) |

---

## Radiation Sources

### Environmental Sources (Core Rules p.81)
**Minor Reactor Leak:** **2D rads per hour**
- Malfunctioning ship power plant or station reactor
- Usually confined to engineering sections
- May be intermittent or constant

**Serious Reactor Leak:** **2D rads per 20 minutes**  
- Critical reactor damage or containment failure
- Affects large areas of ship/station
- Often accompanies other disasters

**Minor Solar Flare:** **1D × 100 rads per hour**
- Stellar radiation bursts affecting entire system
- Spacecraft hulls reduce by 500 rads (Core Rules p.81)
- Usually predictable with proper sensors

**Major Solar Flare:** **3D × 100 rads per hour**
- Severe stellar events affecting wide area
- Even shielded locations at risk
- Can disable unprotected electronics

### Combat Sources (Core Rules p.79)
**Radiation Weapons:** **2D × 20 rads immediately**
- Personal scale weapons: 40-240 rads average
- Spacecraft scale weapons: **2D × 60 rads** (Core Rules p.79)
- **Destructive trait:** All within 10m also take 2D × 20 rads

**Nuclear Explosions:** **Variable**
- Weapon yield determines exposure
- Those without radiation protection receive lethal doses (Core Rules p.133)
- Creates persistent contaminated zones

### Starship Environment (Core Rules p.81)
**Intact Hull:** Reduces radiation by **500 rads**
- Hydrogen fuel tanks provide additional shielding
- Normal space travel = minimal exposure
- Most spacers experience only slightly elevated background

**Breached Hull:** No radiation protection
- Emergency situation requiring immediate action
- Crew exposed to full environmental radiation
- Vacc suits provide limited protection

**Damaged Reactor:** Variable exposure (Core Rules p.154)
- **Minor damage:** Crew suffers **2D × 10 rads per week**
- Major damage may require evacuation
- Engineering crew at highest risk

---

## Effects & Damage

### Immediate Effects (Core Rules p.81)
Suffered immediately upon exposure to radiation dose:

| Radiation Dose | Immediate Effects |
|----------------|-------------------|
| **50 rads or less** | None |
| **51-150 rads** | **1D damage**, Nausea (-1 to all checks until medical treatment) |
| **151-300 rads** | **2D damage** |
| **301-500 rads** | **4D damage**, hair loss |
| **501-800 rads** | **6D damage**, sterile |
| **801+ rads** | **8D damage**, internal bleeding |

**Important:** These effects occur **each time** the PC is exposed to a dose in these ranges.

### Cumulative Effects (Core Rules p.81)
Based on **total accumulated radiation** over PC's lifetime:

| Total Accumulated | Permanent Effect |
|-------------------|------------------|
| **50 rads or less** | None |
| **51-150 rads** | None |
| **151-300 rads** | **-1 END permanently** |
| **301-500 rads** | **-2 END permanently** |
| **501-800 rads** | **-3 END permanently** |
| **801+ rads** | **-4 END permanently** |

**Critical:** Once accumulated, these penalties are permanent unless anti-rad drugs are used.

### Example Accumulation
PC has 75 accumulated rads from past exposure. They then absorb 20 rads from a solar flare:
- **New total:** 95 rads accumulated
- **Immediate effect:** None (20 rads is below 51 threshold)
- **Cumulative effect:** None (95 rads is below 151 threshold)
- **Status:** Approaching dangerous levels

---

## Protection & Mitigation

### Armor Protection (Core Rules p.100)
Armor with radiation protection reduces exposure:

| Armor Type | Radiation Protection | Notes |
|------------|---------------------|-------|
| **Vacc Suit (TL8)** | **20 rads** | Basic space protection |
| **Vacc Suit (TL10)** | **28 rads** | Improved shielding |
| **Vacc Suit (TL12)** | **40 rads** | Advanced materials |
| **HEV Suit (TL9)** | **30 rads** | Hostile environment protection |
| **HEV Suit (TL10)** | **20 rads** | Different design focus |
| **Battle Dress (TL13-14)** | **100 rads** | Military powered armor |

**Radiation Suit (TL8):** **100 rads protection** (Core Rules p.119)
- **Cost:** Cr2,000, **Mass:** 2kg
- Specialized protection against direct radiation
- Required for serious radiation environments
- Can be worn under other protection

### Environmental Protection
**Spacecraft Hull:** **-500 rads** to all radiation exposure (Core Rules p.81)
- Includes hydrogen fuel tank shielding
- Most effective protection available
- Negated by hull breaches or proximity to sources

**Shelter:** Varies by construction
- **Metal structures:** -50 to -200 rads depending on thickness
- **Rock/concrete:** -100 to -500 rads depending on density
- **Underground:** Additional protection from soil/rock

### Stacking Protection
Radiation protection **does not stack** - use highest value only
- Exception: Radiation suit can be worn under other armor
- Ship hull protection applies before personal armor
- Always use the most protective available option

---

## Treatment

### Anti-Rad Drugs (Core Rules p.115)
**Anti-rad (TL8):** Cr1,000 per dose
- **Timing:** Must be taken within **10 minutes** of exposure
- **Effect:** Absorbs up to **100 rads per dose**
- **Limitation:** Only **once per day** (additional doses cause permanent END damage)
- **Critical:** Only way to remove accumulated radiation

### Medical Treatment
**Nausea Treatment:** Medical care can remove the -1 DM penalty
- Requires basic medical attention
- Anti-nausea medications at higher TL

**Characteristic Damage:** Heals normally through medical care
- Physical damage from radiation heals like combat wounds
- Permanent END loss cannot be medically restored

### Prevention Strategies
1. **Monitor Exposure:** Track total rads carefully
2. **Use Protection:** Appropriate suits for environment
3. **Limit Exposure Time:** Reduce duration in radioactive areas  
4. **Emergency Procedures:** Pre-positioned anti-rad drugs
5. **Detection First:** Always check for radiation before entering unknown areas

---

## Encounter Examples

### The Leaking Reactor
**Setup:** Ship's reactor develops containment leak during jump
**Radiation:** 2D rads per hour in engineering, 1D rads per hour in adjacent areas
**Detection:** Engineering alarms, Geiger counter readings
**Challenge:** Repair reactor while minimizing exposure
**Solution:** Vacc suits + radiation suits, work in shifts, anti-rad drugs ready

### Solar Flare Warning
**Setup:** Stellar observatory warns of major solar flare in 2 hours
**Radiation:** 3D × 100 rads per hour for 6 hours
**Protection:** Ship hull reduces to (3D × 100) - 500 rads per hour
**Challenge:** Still potentially lethal even with ship protection
**Solution:** Find asteroid or moon for additional shielding, all crew in vacc suits

### Ancient Weapons Cache
**Setup:** Precursor site contains active nuclear materials
**Radiation:** Varies by proximity - 1D × 20 rads per minute near artifacts
**Detection:** PRIS binoculars show radiation signatures
**Challenge:** Valuable artifacts but dangerous to approach
**Solution:** Radiation suits, remote handling equipment, careful exposure planning

### Reactor Sabotage
**Setup:** Terrorists damage station reactor as PCs investigate
**Radiation:** 2D rads per 20 minutes, increasing over time
**Immediate:** Engineering section evacuated, emergency protocols
**Challenge:** Investigate crime scene in dangerous environment
**Solution:** HEV suits or battle dress, work quickly, anti-rad drugs as backup

---

## Quick Reference Tables

### Radiation Exposure by Source
| Source | Rads per Exposure | Frequency |
|--------|------------------|-----------|
| Minor reactor leak | 2D/hour | Continuous |
| Serious reactor leak | 2D/20 minutes | Continuous |
| Minor solar flare | 1D × 100/hour | Duration varies |
| Major solar flare | 3D × 100/hour | Duration varies |
| Radiation weapon | 2D × 20 | One-time |
| Nuclear explosion | Variable | One-time |

### Protection Summary
| Protection Type | Rads Blocked | Availability |
|-----------------|--------------|--------------|
| Spacecraft hull | 500 | Ships only |
| Battle Dress | 100 | TL13+ military |
| Radiation Suit | 100 | TL8+ specialized |
| HEV Suit (TL9) | 30 | TL9+ hostile environment |
| Vacc Suit (TL12) | 40 | TL12+ standard |
| Anti-rad drugs | 100 | TL8+ medical |

### Immediate Effects Quick Lookup
- **≤50 rads:** No immediate effect
- **51-150:** 1D damage + nausea (-1 all checks)
- **151-300:** 2D damage
- **301-500:** 4D damage + hair loss  
- **501-800:** 6D damage + sterility
- **801+:** 8D damage + internal bleeding

### Cumulative Effects Quick Lookup
- **≤150 total rads:** No permanent effect
- **151-300 total:** -1 END permanently
- **301-500 total:** -2 END permanently
- **501-800 total:** -3 END permanently  
- **801+ total:** -4 END permanently

---

**Referee Notes:**
- **Track carefully:** Radiation accumulation is permanent and deadly
- **Telegraph danger:** Give clear warnings about radiation hazards
- **Emphasize protection:** Make protective equipment valuable and necessary
- **Time pressure:** Radiation creates natural urgency in encounters
- **Resource management:** Anti-rad drugs are expensive and limited
- **Dramatic potential:** Radiation exposure creates lasting consequences for PCs