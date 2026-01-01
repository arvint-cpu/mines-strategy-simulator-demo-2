# Mines Demo 2 – Console Strategy Expansion

This is **Demo 2** in the progression toward  
**Mines Strategy Simulator**.

Compared to Demo 1, this version significantly expands gameplay mechanics,
player choice, and visual clarity while remaining **console-based**.

---

## Disclaimer

**Educational / simulation only.**
- No real money
- No gambling
- Built strictly for learning and experimentation

---

## Purpose of This Demo

The goal of Demo 2 was to move beyond a fixed, linear prototype and explore:

- Player-controlled risk
- Variable mine counts
- Dynamic betting
- Cash-out vs continue decisions
- Visual feedback using symbols

This demo bridges the gap between a basic logic test and a full strategy game.

---

## What’s New Compared to Demo 1

### New Features
- **Player-selected number of mines**
- **Variable bet sizes** (instead of fixed cost)
- **Cash-out mechanic** (player decides when to stop)
- **Emoji-based visuals** for clarity:
  - 💣 Mine
  - 💥 Explosion
  - 💰 Safe cell
- **Full mine reveal on loss**
- **Round-based gameplay**

### Improved Game Flow
- Bets are placed per round
- Players choose whether to continue or secure winnings
- Balance persists across rounds
- Game ends only when balance reaches $0

---

## How the Game Works

1. Player selects how many mines to place
2. Player places a bet
3. Player reveals cells:
   - Safe → multiplier increases
   - Mine → bet is lost
4. Player can:
   - Cash out and keep winnings
   - Keep playing for higher rewards
5. Balance updates and the next round begins

---

## How to Run

Make sure you have **Python 3** installed.

```bash
python main.py
