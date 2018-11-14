import mysql.connector
conn = mysql.connector.connect (user = 'admin', password = 'password',
                                host ='127.0.0.1', port='8889', database= 'CNA330')
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS hosts(id INTEGER, hostname TEXT,  url TEXT, ip TEXT, local_remote TEXT, description TEXT);")
cursor.execute("INSERT INTO hosts(id, hostname, url, ip, local_remote, description"
               ") VALUES(0, 'loopback', 'localhost', '127.0.0.1', 'local', 'Local DB');")

cursor.execute("INSERT INTO hosts(id, hostname, url, ip, local_remote, description"
               ") VALUES(1, 'router', 'none', '192.168.1.1', 'local', 'My LAN router');")

cursor.execute("INSERT INTO hosts(id, hostname, url, ip, local_remote, description"
               ") VALUES(2, 'printer', 'none', '192.168.100.1', 'local', 'My Print');")

cursor.execute("INSERT INTO hosts(id, hostname, url, ip, local_remote, description"
               ") VALUES(3, 'Google', 'https://www.google.com', '127.217.14.238', 'remote', 'Googles DNS');")

cursor.execute("INSERT INTO hosts(id, hostname, url, ip, local_remote, description"
               ") VALUES(4, 'Renton Technical College', 'https://www.rtc.edu', '192.124.249.10', 'remote', 'RTC Website');")

cursor.execute("INSERT INTO hosts(id, hostname, url, ip, local_remote, description"
               ") VALUES(5, 'Microsoft', 'https://www.microsoft.com', '191.239.213.197', 'remote', 'Microsofts Main Website');")


cursor.execute("SELECT hostname, ip, description FROM hosts WHERE "
               "local_remote = 'local'")
results = cursor.fetchall()
print ("Great Success")