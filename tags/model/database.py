import sqlite3

con = sqlite3.connect("tags.db")
cur = con.cursor()
cur.execute(
    "CREATE TABLE IF NOT EXISTS tags (tag_type TEXT, tag TEXT, photo TEXT)"
)
con.commit()