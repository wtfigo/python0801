import pyodbc
con = pyodbc.connect("DRIVER={SQL Server};server=localhost;database=AdventureWorks2014;uid=sa;pwd=328047055")
c = con.cursor()
c.execute("""SELECT firstname, ISNULL(middlename, ''    ), lastname FROM person.person""")
data = c.fatchall()
print(data)

#for row in c:
#    print(row[])

c.close()
con.close()
