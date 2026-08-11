import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="160207",
    database="airlane"
)

print("Connection successful!")
print("Database:", db.database)

cursor = db.cursor()

print("Cursor berhasil dibuat!")


def tampilkan_plane():
    print("\n=== DATA PLANE ===")

    sql = "SELECT * FROM plane"

    cursor.execute(sql)

    planes = cursor.fetchall()

    print("-" * 70)
    print(f"{'ID':<5} {'CODE':<10} {'COMPANY':<10} {'NAME PLANE':<25} {'CAPACITY':<10}")
    print("-" * 70)

    for plane in planes:
        print(f"{plane[0]:<5} {plane[1]:<10} {plane[2]:<10} {plane[3]:<25} {plane[4]:<10}")

    print("-" * 70)


tampilkan_plane()

cursor.close()
db.close()

print("Connection closed.")

def tambah_plane():
    print("\n=== TAMBAH DATA PLANE ===")

    id_pln = int(input("ID Plane   : "))
    code = input("Code       : ")
    id_cmp = int(input("ID Company : "))
    name_pln = input("Name Plane : ")
    capacity = int(input("Capacity   : "))

    sql = """
        INSERT INTO plane
        (id_pln, code, id_cmp, name_pln, capacity)
        VALUES (%s, %s, %s, %s, %s)
    """

    values = (id_pln, code, id_cmp, name_pln, capacity)

    cursor.execute(sql, values)

    db.commit()

    print("Data plane berhasil ditambahkan!")