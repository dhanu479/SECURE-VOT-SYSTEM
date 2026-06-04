import sqlite3
import numpy as np
import os

db_path = 'voting_system.db'
conn = sqlite3.connect(db_path)
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

users = cursor.execute("SELECT id, first_name, last_name, uucms_number, face_encoding FROM users").fetchall()
print(f"Total users: {len(users)}")
for u in users:
    enc = u['face_encoding']
    if enc:
        arr = np.frombuffer(enc, dtype=np.float64)
        print(f"  User {u['id']} ({u['first_name']} {u['last_name']}, UUCMS: {u['uucms_number']}): encoding length={len(arr)}, dtype={arr.dtype}")
    else:
        print(f"  User {u['id']} ({u['first_name']} {u['last_name']}): NO ENCODING STORED!")

conn.close()

# Also check face files exist
face_folder = os.path.join('static', 'faces')
print(f"\nFace folder: {face_folder}")
if os.path.exists(face_folder):
    files = os.listdir(face_folder)
    print(f"Files in face folder ({len(files)}): {files[:10]}")
else:
    print("Face folder does not exist!")
