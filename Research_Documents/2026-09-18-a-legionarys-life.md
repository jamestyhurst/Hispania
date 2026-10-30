---
status: findings — not canon
created: 2026-09-18
audience: llm
authorship: agent-written
authority_level: input only
source: James, iPhone, 2026-09-18 — A Legionary's Life is the named inspiration for Hispania
unblocks: later Hispania design sessions. Does not unblock code.
---

# *A Legionary's Life* — what the inspiration actually is

```pseudocode
THIS_FILE: input. Cite with the tags below.
NOT: a designer note.
NOT: canon.
NOT: a licence to clone Alessandro Roberti's systems into Hispania.
NOT: a substitute for playing the game or reading James's own notes after he plays it.
```

James's instruction this session: *A Legionary's Life* is the main inspiration for Hispania. `[FACT - cited]` — James, iPhone, 2026-09-18.

Hispania's only written premise is the inverse of that game's premise. ALL puts you in a Roman conscript's boots and marches you through Rome's wars. Hispania puts you in a Celtiberian tribesman's boots and asks which of the three powers you stand with. `[INFERENCE]`

This file separates (1) what the developer published, (2) what player-facing guides and wikis report about systems, and (3) what that contrast is worth to Hispania. Layer 2 is not as solid as layer 1. Tag accordingly.

## 1. The published object

- Title: *A Legionary's Life*
- Designer / developer / writer / publisher: Alessandro Roberti (site branding also uses Sertorius). `[FACT - cited]` Steam, https://store.steampowered.com/app/1058430/A_Legionarys_Life/ ; official page https://www.arobertigames.com/legionaryslife/ ; itch.io demo https://a-roberti.itch.io/legionaryslife
- Engine: Unity 2017.4.32f1. `[FACT - cited]` https://www.pcgamingwiki.com/wiki/A_Legionary%27s_Life
- Early Access: 19 April 2019. Full release: 25 September 2019. Windows. Later on GOG, DRM-free. `[FACT - cited]` Steam + PCGW.
- Art: pixel / low-fi 2D. Anatoly Lysykh and Robert Eddie credited for art. `[FACT - cited]` MobyGames credits, https://www.mobygames.com/game/135220/a-legionarys-life/credits/windows/
- Steam appid 1058430. Reviews on the store page at time of research: Very Positive, 86% of ~2,175 English reviews. `[FACT - cited]` Steam.
- Footprint: 200 MB, DX10, 1 GB RAM. This is a small game on purpose. `[FACT - cited]` Steam minimum specs.
- Demo: first 3 of 11 parts, free on Steam. `[FACT - cited]` Steam store description.
- Sequel: *Never Second in Rome*, announced on Roberti's site; TV Tropes reports Early Access February 2025, player as a centurion in Caesar's Gallic War. `[FACT - cited]` https://www.arobertigames.com/legionaryslife/ for the announcement. The EA date and exact scope are secondary. `[INFERENCE]`

Official one-paragraph pitch (Steam, also reused on itch and GOG):

> *A Legionary's Life* lets you play as a Roman soldier during the years of the Second Punic War and beyond. Rise up through the ranks and win prestigious awards or just focus on making it home in one piece; it's up to you.

Official system claims in that same blurb: `[FACT - cited]` Steam

- single-player
- RPG elements
- extensive attribute and skill checks
- turn-based combat with many variables, explicitly including morale, reach, confined space, and high ground
- roguelike features, including permadeath
- each run shows only a fraction of the game
- points from successful characters spend on the next legionary

Official design warnings in the "try the demo" section: `[FACT - cited]` Steam

- your character will not be good at everything
- pick challenges from strengths and weaknesses
- the game is not built to put you at bad odds unless you walk into them
- a failed task is usually a mild Morale and/or Opinions hit, recoverable

That last pair — **Opinions** (relations with superiors and fellow soldiers) and **Morale** — is first-party. Build Hispania comparisons from those words, not from invented meters. `[INFERENCE]`

## 2. Shape of a run, from first-party plus near-first-party

ModDB's game page (developer-facing copy and patch notes live there) adds structure the Steam blurb leaves implicit: `[FACT - cited]` https://www.moddb.com/games/a-legionarys-life

- Three campaigns. The third and last is the Second Macedonian War, added as a post-EA update.
- Campaigns and main battles are "heavily based on historical accounts."
- Before each battle, a **Lull** phase lasting months: train, buy kit, take other actions, eat random events.

TV Tropes (secondary, useful, not gospel) names the three campaigns as: Second Punic War starting just after Cannae; the African campaign against Carthage; Second Macedonian War in Greece. `[FACT - cited]` as a wiki claim, https://tvtropes.org/pmwiki/pmwiki.php/VideoGame/ALegionarysLife

That start date — *after Cannae* — means the player is a replacement for the dead of 216, not a veteran of the Trebia. `[INFERENCE]`

Eleven "parts" are the Steam demo's unit of progress (3 of 11). How parts map onto the three campaigns is not stated on the store page. `[GAP FLAGGED]`

Permadeath is first-party. The inheritance economy (score from the dead or retired man buys stats or starting kit for the next) is also first-party. `[FACT - cited]` Steam.

Roberti's own patch notes on the official site mention combat actions by name: Feints, Shield Attacks, partial hits, javelin throws; Feints and Shield Attacks have two stacked checks (skill check, then a resistance check — Awareness for feints, Awareness plus Quickness for Quick Feints). `[FACT - cited]` https://www.arobertigames.com/legionaryslife/ update 1.3.1 summary as extracted.

## 3. Systems the player-guides agree on

The most cited mechanical write-up is the "Training and Combat Guide" at Gameplay.tips, a player guide, not a design doc. Treat as `[INFERENCE]` unless it only restates the official list. https://gameplay.tips/guides/5369-a-legionarys-life.html

### 3.1 Combat resources the guide names

| Resource | Guide's definition |
|---|---|
| Health | Hits zero, you die. No wound penalties while alive. |
| Stance | Balance. Full stance = planted. Zero stance ≈ on the ground. Low stance tanks attack, feint, bash, and block chances, and raises the chance of missing a turn. |
| Fatigue | Every action except Respite adds fatigue. Overflows into fatigue *levels* that stack penalties on attack, feint, bash, block, turn-taking, stance recovery, and further Respite. Arm and leg hits also add fatigue. |
| Morale | High morale helps bonus turns, stance recovery, fatigue reduction. Turtle too long (defensive 3+ turns) bleeds morale. |

Official blurb already listed morale, reach, confined space, high ground. The guide is loud on stance and fatigue and almost silent on reach / confined space / high ground. Those three are first-party and under-documented in guides. `[GAP FLAGGED]`

ModDB user/dev notes also name **Attitude** (offensive/defensive stance of mind), **Weapon Reach**, **Weapon Handiness**, and environmental conditions as tracked combat variables. `[FACT - cited]` ModDB page text.

### 3.2 Attributes the guides name

Gameplay.tips combat chapter: Strength, Endurance, Constitution, Quickness, Coordination, Awareness. `[INFERENCE]` — player guide.

- Strength: melee and javelin damage; bash success and bash resistance.
- Endurance: fatigue budget; Respite success.
- Constitution: raw HP. TV Tropes calls it a dump stat. That is a playstyle claim, not a design document.
- Quickness: extra turns or skipped turns; feint success.
- Coordination: recovering stance while under attack.
- Awareness: feints and feint resistance; "the only mental stat which is relevant to combat" per the guide.

TV Tropes adds Intelligence, Charisma, and Virtue as out-of-combat / campaign stats, and treats Awareness as the one stat that also prints money, trophies, and approval on checks. `[INFERENCE]` — wiki.

JRK's RPG write-up (Polish, secondary) independently lists health, strength, endurance, fencing skill, speed, coordination, awareness, javelin accuracy. That overlap is why the combat-stat list is probably close to the real sheet. `[INFERENCE]` https://jrkrpg.pl/gry/pc/legionarys-life/

`[GAP FLAGGED]` Full official attribute list is not on the Steam page. Do not treat TV Tropes Virtue-as-karma as verified first-party naming without a screenshot or manual.

### 3.3 Skills the guide names

Weapon skill, Shield skill, Javelin skill. `[INFERENCE]` — Gameplay.tips.

- Weapon: attacks and feints.
- Shield: blocks; resistance to feints and bashes; bash success.
- Javelin: first-turn throw chance and "bull's-eye" extra damage.

Training loop the same guide describes: lull-phase sparring / javelin / workouts; stress from over-training cuts morale; starting sword/shield ~29 is too low for serious fights; diminishing returns after 40–50; sparring partners gated on troop reputation; javelin skill hard-capped near Coordination; hard cap 99 appears in TV Tropes. `[INFERENCE]`

### 3.4 Equipment grammar the guide names

Each armour piece: damage protection, cover, anti-armour-resistance (AAR). Each weapon: anti-armour (AA). Cover is the chance a hit on that body part actually strikes the plate instead of flesh. Mail has cover 100 on the torso; a pectoral plate is given as cover 35. Helmets and greaves cost Awareness and Quickness. `[INFERENCE]` — Gameplay.tips.

This is the most stealable *combat-resolution* idea in the game if Hispania wants ALL's texture: you do not have a single AC. You have body parts, partial cover, and weapons that punch through some of the protection. `[SPECULATION]`

### 3.5 Career, not just fights

Across TV Tropes, ModDB, and JRK, the loop is:

1. Lull (train, shop, events, forage, religion, gambling, social checks).
2. Named historical battle or siege, fought as a series of personal engagements rather than as a grand-tactical map.
3. Approval with the century and the centurion moves the rank needle.
4. Awards (Civic Crown, Mural Crown are the ones wikis name) and loot.
5. Death, discharge, or — rarely — a senatorial ending.

`[INFERENCE]` Rank ceiling as centurion is widely reported. Consul / senate as an epilogue for an exceptional three-campaign life is reported, not first-party. `[GAP FLAGGED]`

Permadeath plus a meta-score that buys the next man's start is first-party. The "100-kill career" and "10k score achievement" numbers are player-culture. `[INFERENCE]`

## 4. What ALL is doing as a design, stripped of Rome-fan dressing

Read the official blurb and the demo warning as a design manifesto. `[INFERENCE]`

1. **You are one body in a machine that will replace you.** The war does not pause if you die. The next conscript inherits a sliver of your competence, not your name.
2. **Competence is narrow.** Attribute checks are everywhere. You are not a skill sponge. You pick the jobs your numbers can survive.
3. **Combat is a physics of balance, tiredness, space, and nerve**, not a damage-race with buff icons. Stance / fatigue / morale / reach / confined space / high ground is the published list.
4. **The calendar is the other half of the game.** Months of lull are where the build happens. Battles are exams.
5. **Failure is usually social, not lethal** — until it is lethal. Morale and Opinions absorb the ordinary miss. Permadeath absorbs the extraordinary one.
6. **History is a railroad you can die on.** Battles are historical. Your agency is local: live, get promoted, take the crown, or go home. You do not reroute Zama.
7. **Small surface, deep checks.** 200 MB, pixel portraits, menus. The budget went into resolution tables, not into a map engine.

`[GAP FLAGGED]` This manifesto is inferred from published text. Roberti has not posted a GDC-style postmortem that this session found.

## 5. The inversion Hispania already chose

ALL's player is legally Roman, conscripted after a catastrophe, fed and paid (badly) by a state that has a name for every rank and every crown.

Hispania's player is a Celtiberian. The README says he must side with Rome, Carthage, or the Iberians. That single sentence already breaks ALL's career ladder in three places:

- There is no *one* rank table. A mercenary band, a Roman *auxilium*, a Carthaginian contingent, and a Celtiberian *oppidum* levy do not share a promotion screen. `[INFERENCE]`
- "Making it home" means something different if home is Numantia-adjacent and Rome may burn it in 133. `[INFERENCE]`
- ALL can treat the Second Punic War as a sequence of official postings. Hispania's three-way choice is a political act that can make the player an enemy of yesterday's paymaster. `[INFERENCE]`

What still transfers, if James wants it to, is the *grain* of ALL, not the legion:

| ALL grain | Why it is portable | Why it might not be |
|---|---|---|
| One named man, permadeath, next-kin inheritance | Matches a Celtiberian *devotio* / kin-band world better than a CK dynasty | Inheritance-as-meta-score is a game convenience, not a Celtiberian institution |
| Lull / campaign season / exam-battle | Iron Age war *is* seasonal; see also Teutoburg levy-season work | Hispania may not want three railroaded historical campaigns |
| Narrow stats, constant checks | Keeps the player a person, not a stack of units | Needs a Celtiberian stat list, not Strength/Awareness cloned |
| Stance, fatigue, reach, ground, confined space | Dual-purpose Hispanic infantry (throw, then sword) wants space and tiredness more than it wants a flanking minigame | Must not become a falcata-only move list |
| Opinions with the men around you | Maps onto hospitium / clientela / the chief, and onto a Roman centurion if you take the Roman turn | "Centurion approval" is the wrong noun for a Lusone war-band |
| Historical battles as rooms you enter | Saguntum, Baecula, Ilipa, Empúries, Numantia exist | Railroad vs the three-way allegiance choice. A Scipio campaign cannot also be a Hannibal campaign in the same run |
| Tiny presentation, heavy resolution | Matches a first Hispania build better than a Clausewitz map | James is also building Teutoburg and Suvorov; do not accidentally import those scopes |

`[SPECULATION]` The valuable steal is "personal war-RPG with permadeath and a lull," not "Roman rank simulator with a Celtiberian sprite."

## 6. What this file is not allowed to decide

- Whether Hispania inherits permadeath. `[GAP FLAGGED]`
- Whether combat is ALL-like (one opponent, menus, stance) or Teutoburg-like (formations, hexes, days). `[GAP FLAGGED]`
- Whether the three allegiances are three full campaigns or a single map with a one-time choice. `[GAP FLAGGED]`
- Whether *Never Second in Rome* (centurion-as-commander) is the long-term Hispania destination. That sequel is a different fantasy — you already have the rank ALL treats as an ending. `[INFERENCE]`

## 7. Sources

First-party:

- https://store.steampowered.com/app/1058430/A_Legionarys_Life/
- https://www.arobertigames.com/legionaryslife/
- https://a-roberti.itch.io/legionaryslife
- https://www.moddb.com/games/a-legionarys-life
- https://www.pcgamingwiki.com/wiki/A_Legionary%27s_Life
- https://www.mobygames.com/game/135220/a-legionarys-life/

Secondary (mechanics):

- https://gameplay.tips/guides/5369-a-legionarys-life.html
- https://tvtropes.org/pmwiki/pmwiki.php/VideoGame/ALegionarysLife
- https://jrkrpg.pl/gry/pc/legionarys-life/

Companion findings in this folder:

- `2026-09-18-iron-age-iberian-warfare-and-soldiers.md` — the historical soldier Hispania actually starts as.
