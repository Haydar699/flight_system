
import mysql.connector


# ==========================
# DATABASE CONNECTION
# ==========================

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


# ==========================
# TAMPILKAN DATA PLANE
# ==========================

def tampilkan_plane():
    print("\n=== DATA PLANE ===")

    sql = "SELECT * FROM plane"

    cursor.execute(sql)

    planes = cursor.fetchall()

    print("-" * 70)
    print(f"{'ID':<5} {'CODE':<10} {'COMPANY':<10} {'NAME PLANE':<25} {'CAPACITY':<10}")
    print("-" * 70)

    for plane in planes:
        print(
            f"{plane[0]:<5} "
            f"{plane[1]:<10} "
            f"{plane[2]:<10} "
            f"{plane[3]:<25} "
            f"{plane[4]:<10}"
        )

    print("-" * 70)


# ==========================
# TAMBAH DATA PLANE
# ==========================

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


# ==========================
# UBAH DATA PLANE
# ==========================

def ubah_plane():
    print("\n=== UBAH DATA PLANE ===")

    id_pln = int(input("ID Plane yang ingin diubah : "))

    code = input("Code baru       : ")
    name_pln = input("Name Plane baru : ")
    capacity = int(input("Capacity baru   : "))

    sql = """
        UPDATE plane
        SET code = %s,
            name_pln = %s,
            capacity = %s
        WHERE id_pln = %s
    """

    values = (code, name_pln, capacity, id_pln)

    cursor.execute(sql, values)

    db.commit()

    print("Data plane berhasil diubah!")


# ==========================
# HAPUS DATA PLANE
# ==========================

def hapus_plane():
    print("\n=== HAPUS DATA PLANE ===")

    id_pln = int(input("ID Plane yang ingin dihapus : "))

    sql = """
        DELETE FROM plane
        WHERE id_pln = %s
    """

    values = (id_pln,)

    cursor.execute(sql, values)

    db.commit()

    print("Data plane berhasil dihapus!")


# ==========================
# MENU CLI
# ==========================

def menu():
    while True:
        print("\n========================================")
        print("          SISTEM DATA PLANE")
        print("========================================")
        print("1. Tambah Plane")
        print("2. Tampilkan Plane")
        print("3. Ubah Plane")
        print("4. Hapus Plane")
        print("5. Keluar")
        print("========================================")

        pilihan = input("Pilih menu : ")

        if pilihan == "1":
            tambah_plane()

        elif pilihan == "2":
            tampilkan_plane()

        elif pilihan == "3":
            ubah_plane()

        elif pilihan == "4":
            hapus_plane()

        elif pilihan == "5":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid!")


# ==========================
# MENJALANKAN PROGRAM
# ==========================

menu()


# ==========================
# MENUTUP KONEKSI DATABASE
# ==========================

cursor.close()
db.close()

print("Connection closed.")

