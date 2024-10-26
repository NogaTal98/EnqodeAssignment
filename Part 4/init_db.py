import sqlite3
import json

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (averageEntropyScore, firewallDetected, DNSsecEnabled, tlsVersion, certificateBitStrength, securityHeadersImplemented, openPortsDetected) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (
                    7.8, 
                    True,
                    True,
                    '1.2',
                    2048,
                    json.dumps(['X-XSS-Protection', 'X-Frame-Options']),
                    12
                )
            )

connection.commit()
connection.close()