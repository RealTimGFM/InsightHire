import sqlite3
from datetime import datetime
from functools import wraps

from flask import flash, g, redirect, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash

from utils.seed import DEMO_USERS


def get_db_connection(database_path):
    connection = sqlite3.connect(database_path)
    connection.row_factory = sqlite3.Row
    return connection


def row_to_dict(row):
    return dict(row) if row else None


def derive_display_name(email):
    local_part = email.split("@", 1)[0]
    pieces = local_part.replace(".", " ").replace("_", " ").replace("-", " ").split()
    return " ".join(part.capitalize() for part in pieces) or "Insight Hire User"


def init_db(database_path):
    with get_db_connection(database_path) as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT NOT NULL UNIQUE,
                password_hash TEXT NOT NULL,
                role TEXT NOT NULL DEFAULT 'job_seeker',
                display_name TEXT NOT NULL,
                created_at TEXT NOT NULL
            )
            """
        )
        connection.commit()


def get_user_by_email(database_path, email):
    with get_db_connection(database_path) as connection:
        row = connection.execute(
            "SELECT * FROM users WHERE lower(email) = lower(?)",
            (email,),
        ).fetchone()
    return row_to_dict(row)


def get_user_by_id(database_path, user_id):
    if not user_id:
        return None

    with get_db_connection(database_path) as connection:
        row = connection.execute("SELECT * FROM users WHERE id = ?", (user_id,)).fetchone()
    return row_to_dict(row)


def create_user(database_path, email, password, role="job_seeker", display_name=None):
    normalized_email = email.strip().lower()
    if get_user_by_email(database_path, normalized_email):
        return None

    final_display_name = display_name or derive_display_name(normalized_email)

    with get_db_connection(database_path) as connection:
        connection.execute(
            """
            INSERT INTO users (email, password_hash, role, display_name, created_at)
            VALUES (?, ?, ?, ?, ?)
            """,
            (
                normalized_email,
                generate_password_hash(password),
                role,
                final_display_name,
                datetime.utcnow().isoformat(timespec="seconds"),
            ),
        )
        connection.commit()

    return get_user_by_email(database_path, normalized_email)


def authenticate_user(database_path, email, password):
    user = get_user_by_email(database_path, email)
    if not user:
        return None
    if not check_password_hash(user["password_hash"], password):
        return None
    return user


def seed_demo_users(database_path):
    for demo_user in DEMO_USERS:
        if not get_user_by_email(database_path, demo_user["email"]):
            create_user(
                database_path,
                email=demo_user["email"],
                password=demo_user["password"],
                role=demo_user["role"],
                display_name=demo_user["display_name"],
            )


def login_user(user):
    session.clear()
    session["user_id"] = user["id"]


def logout_user():
    session.clear()


def login_required(view_func):
    @wraps(view_func)
    def wrapped_view(*args, **kwargs):
        if not g.get("user"):
            flash("Please log in to continue.", "warning")
            return redirect(url_for("login"))
        return view_func(*args, **kwargs)

    return wrapped_view


def role_required(expected_role):
    def decorator(view_func):
        @wraps(view_func)
        def wrapped_view(*args, **kwargs):
            if not g.get("user"):
                flash("Please log in to continue.", "warning")
                return redirect(url_for("login"))

            if g.user.get("role") != expected_role:
                flash("That page is reserved for the verified employee demo account.", "warning")
                return redirect(url_for("dashboard"))

            return view_func(*args, **kwargs)

        return wrapped_view

    return decorator
