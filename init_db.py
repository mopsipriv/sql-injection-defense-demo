import sqlite3

con=sqlite3.connect("initials.db")
cur=con.cursor()

cur.execute("CREATE TABLE initials(username,password)")
cur.execute("""INSERT INTO initials VALUES
            ('admin','password'),
            ('hello','mops')
            """)
con.commit()
con.close()
