import sqlite3
from pathlib import Path

RUNS_DB_PATH = Path(__file__).parent / "runs.db"


def create_runs_table():
    conn = sqlite3.connect(RUNS_DB_PATH)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS runs (
        id INTEGER PRIMARY KEY,
        played_at TEXT,
        floor_reached INTEGER,
        enemies_defeated INTEGER,
        bosses_defeated INTEGER,
        won INTEGER,
        beaten_by TEXT
    )
    """)
    conn.commit()
    conn.close()


def save_run(floor_reached, enemies_defeated, bosses_defeated, won, beaten_by):
    conn = sqlite3.connect(RUNS_DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        """
    INSERT INTO runs (played_at, floor_reached, enemies_defeated, bosses_defeated, won, beaten_by)
    VALUES (datetime('now', 'localtime'), ?, ?, ?, ?, ?)
    """,
        (floor_reached, enemies_defeated, bosses_defeated, won, beaten_by),
    )

    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_runs_table()
