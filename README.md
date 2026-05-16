## Start program with command
python/python3 main.py

# AQUASHELL

AQUASHELL is a terminal-based aquarium and fishing game built entirely in Python.

Players can:
- catch fish,
- collect rare sea creatures,
- upgrade fishing rods,
- expand aquarium capacity,
- manage collections,
- and watch a fully animated ASCII aquarium.

The game combines:
- fishing mechanics,
- animated creature AI,
- creature collection,
- rod progression,
- shiny variants,
- and save persistence.

---

# 1. Features

## 1.1 Fishing System

Players can travel to the Fishing Island and catch creatures through an interactive timing minigame. :contentReference[oaicite:0]{index=0}

Fishing outcomes:
- 35% small fish
- 15% large fish
- 50% coins

Large fish require an additional struggle minigame. :contentReference[oaicite:1]{index=1}

---

## 1.2 Rod Progression System

The game contains 5 fishing rod levels. :contentReference[oaicite:2]{index=2}

| Level | Rod |
|---|---|
| 1 | Basic Rod |
| 2 | Copper Rod |
| 3 | Silver Rod |
| 4 | Golden Rod |
| 5 | Mythic Rod |

Higher rods unlock stronger and rarer sea creatures.

---

## 1.3 Aquarium Animation System

The aquarium is fully animated inside the terminal. :contentReference[oaicite:3]{index=3}

Features include:
- real-time fish movement
- bubbles
- water surface animation
- layered rendering
- creature movement AI
- directional sprite mirroring
- creature depth zones

---

## 1.4 Creature AI Behaviors

Different creatures have unique behaviors.

### Small Fish
- always swim left
- wrap around the screen
- never turn around

### Dolphin
- swims diagonally near the water surface
- changes vertical direction dynamically

### Starfish
- fixed at the bottom
- stationary
- never mirrored

### Jellyfish
- always keeps original sprite orientation

### Fast Creatures
These creatures move 1.5x faster:
- Manta Ray
- Hammerhead shark
- Megalodon

---

# 2. Creature Zone System

Different species occupy different vertical regions of the aquarium. :contentReference[oaicite:4]{index=4}

## Top Zone (Top 1/3)
- Jellyfish
- Seahorse
- Manta Ray

## Middle Zone
- Paralichthys olivaceus
- Siamese fighting fish

## Bottom Zone
- Celestial Whale
- Hammerhead shark
- Megalodon

## Bottom Fixed Creatures
- Starfish
- Shell Snail

---

# 3. Shiny System

All fish caught through fishing have a 5% chance to become shiny. :contentReference[oaicite:5]{index=5}

Shiny creatures:
- glow in the aquarium
- display sparkles
- cannot be sold
- are stored permanently in save data

---

# 4. Collection System

Players can:
- open collection view
- inspect creatures
- release creatures manually