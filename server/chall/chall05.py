from flask import request, redirect, send_from_directory
import os
import sqlite3

import helpers

_chall = os.path.basename(os.path.splitext(__file__)[0])

def challenge(_, next_challenge):
    if request.method == "POST":
        username = request.form.get("username", None)
        password = request.form.get("password", None)
        if username is not None and password is not None:
            conn = sqlite3.connect('file:chall/chall05/sqlite.db?mode=ro', uri=True)
            c = conn.cursor()
            c.execute(f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'")
            if c.fetchone() is not None:
                print(f"[INFO] {_chall} solved")
                return next_challenge;
            else:
                return redirect(request.url)
    else:
        return helpers.uncache(
            send_from_directory(
                "./templates",
                f"{_chall}.html",
                etag=False,
                max_age=0,
            )
        )

def static(name):
    return helpers.serve_static(name)
