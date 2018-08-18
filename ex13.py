import sqlite3
conn = sqlite3.connect("Chinook.sqlite" )
c = conn.cursor()
print("ok")
c.execute("""SELECT G.Name, count(T.trackid) 
FROM genre G 
INNER JOIN track t ON T.genreid = G.genreid
GROUP BY G.name
""")

genres = c.fetchall() # matches is a list of tuples
print(sorted(genres))
print(type(genres))

"""
for genre in genres:
    print(genre[0, 1]) # the date column’s index
"""
conn.close()
