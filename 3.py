import sqlite3
conn = sqlite3.connect(r'/home/owner/py/sqlite/all_users.db')
cur = conn.cursor()
# cur.execute("""ALTER TABLE users  ADD rnumber TEXT  AFTER t_id; """)
cur.execute("""ALTER TABLE users  DROP img ; """)
conn.commit()
