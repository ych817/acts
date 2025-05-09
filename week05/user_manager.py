from database import create_connection
import sqlite3

def add_user(name, email, class_name):
    """
    Insert a new user with name, email and class.
    class_name should be 'A' or 'B'.
    """
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            'INSERT INTO users (name, email, "class") VALUES (?, ?, ?)',
            (name, email, class_name)
        )
        conn.commit()
        print("User added successfully.")
    except sqlite3.IntegrityError:
        print("Email must be unique.")
    finally:
        conn.close()

def view_users():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    conn.close()
    return rows

def search_user(name):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE name LIKE ?", ('%' + name + '%',))
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_user(user_id):
    """
    Delete users whose student ID (email prefix) matches the given ID.
    The email must start with 'student_id@'.
    """
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM users WHERE email LIKE ?",
        (f"{user_id}@%",)
    )
    deleted_count = cursor.rowcount
    conn.commit()
    conn.close()
    print(f"🗑️ {deleted_count} user(s) deleted with student ID {user_id}.")

def advance_search(user_id=None, name=None):
    """
    Search for users by student ID (extracted from email local-part) and/or name.
    - student_id: the numeric string before '@' in the email (e.g. '270501722').
    - name: partial or full name match.
    Returns a list of matching rows.
    """
    conn = create_connection()
    cursor = conn.cursor()

    conditions = []
    params = []

    # 如果提供了 student_id，就让 email 以 "student_id@" 开头
    if user_id is not None:
        conditions.append("email LIKE ?")
        params.append(f"{user_id}@%")

    # 如果提供了名字，就做模糊匹配
    if name:
        conditions.append("name LIKE ?")
        params.append(f"%{name}%")

    # 都没提供，返回空列表
    if not conditions:
        conn.close()
        return []

    query = "SELECT * FROM users WHERE " + " AND ".join(conditions)
    cursor.execute(query, params)
    rows = cursor.fetchall()
    conn.close()
    return rows