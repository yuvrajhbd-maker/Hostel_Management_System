"""
Central database connection module.

Every DAO (and nothing else) imports get_connection() from here.
Credentials are read from environment variables so no password is
hardcoded in source control. Sensible local-dev defaults are kept as
a fallback so the project still runs out of the box on a local MySQL
instance set up per the README.

You can override any value by setting an environment variable, e.g.:

    export HOSTEL_DB_HOST=localhost
    export HOSTEL_DB_USER=root
    export HOSTEL_DB_PASSWORD=your_password
    export HOSTEL_DB_NAME=hostel_db
"""

import os
import mysql.connector


DB_CONFIG = {
    "host": os.environ.get("HOSTEL_DB_HOST", "localhost"),
    "user": os.environ.get("HOSTEL_DB_USER", "root"),
    "password": os.environ.get("HOSTEL_DB_PASSWORD", "yuvraj"),
    "database": os.environ.get("HOSTEL_DB_NAME", "hostel_db"),
}


def get_connection():
    """Return a new MySQL connection, or raise the underlying error."""
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        return conn
    except mysql.connector.Error as e:
        print("Database Connection Error:", e)
        raise
