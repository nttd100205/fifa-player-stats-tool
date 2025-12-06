# FIFA Player Stats Tool (Python)

A simple command-line application for exploring FIFA player statistics.  
Users can search players by name, view top-ranked players, and filter by club or nationality.

---

## ⚽ Features

- Load player dataset from CSV file
- Menu-based interface for quick navigation
- Search players by name
- Sort players by **Overall Rating** or **Market Value**
- Filter players by **Club** or **Nationality**

This project demonstrates:
- Python basics
- File I/O and CSV parsing
- Lists, dictionaries, and loops
- Defensive checks for missing/invalid data

---

## 🛠 Tech Stack

| Category | Technology |
|---------|------------|
| Language | **Python 3** |
| Libraries | Built-in (`csv`) |
| Interface | Command Line (CLI) |

---

## 📂 Project Structure

fifa_tool.py → Main application script
players.csv → Player dataset (must be in same folder)


You can replace the CSV with any FIFA dataset using compatible column names.

---

## ▶️ How to Run

Make sure `fifa_tool.py` and the dataset CSV are in the same directory.

### Option A — Terminal

```bash
git clone https://github.com/nttd100205/fifa-player-stats-tool.git
cd fifa-player-stats-tool
python fifa_tool.py

python fifa_tool.py

--- FIFA Player Stats Tool ---
1. Search player by name
2. Top players (Overall rating)
3. Filter by club or nationality
0. Exit
Choose an option:

Enter player name: Mbappe
Found 1 players:
- Kylian Mbappé | PSG | 91 OVR | €180M value
