DROP TABLE IF EXISTS posts;

CREATE TABLE posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    averageEntropyScore FLOAT NOT NULL,
    firewallDetected BOOLEAN NOT NULL,
    DNSsecEnabled BOOLEAN NOT NULL,
    tlsVersion TEXT NOT NULL,
    certificateBitStrength INTEGER NOT NULL,
    securityHeadersImplemented TEXT NOT NULL,
    openPortsDetected INTEGER NOT NULL
);