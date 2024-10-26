import json
import sqlite3
from flask import Flask, request

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/add', methods=['POST'])
def add():

    avgEntropyScore = request.json['averageEntropyScore']
    firewallDetected = request.json['firewallDetected']
    DNSsecEnabled = request.json['DNSsecEnabled']
    tlsVersion = request.json['tlsVersion']
    certificateBitStrength = request.json['certificateBitStrength']
    securityHeadersImplemented = request.json['securityHeadersImplemented']
    openPortsDetected = request.json['openPortsDetected']

    conn = get_db_connection()
    conn.execute("INSERT INTO posts (averageEntropyScore, firewallDetected, DNSsecEnabled, tlsVersion, certificateBitStrength, securityHeadersImplemented, openPortsDetected) VALUES (?, ?, ?, ?, ?, ?, ?)",
                 (
                    avgEntropyScore,
                    firewallDetected,
                    DNSsecEnabled,
                    tlsVersion,
                    certificateBitStrength,
                    json.dumps(securityHeadersImplemented),
                    openPortsDetected
                 )
             )
    conn.commit()
    conn.close()
    return 'New post added!'
    

@app.route('/getById', methods=['GET'])
def getById():
    postId = request.args.get('id')
    conn = get_db_connection()

    if not postId:
        posts = conn.execute('SELECT * FROM posts').fetchall()
        conn.close()

        postsArray = []
        for post in posts:
            postsArray.append(dict(post))

        return json.dumps(postsArray)
    
    else:
        post = conn.execute('SELECT * FROM posts WHERE id = ?', (postId,)).fetchone()
        conn.close()

        return json.dumps(dict(post))