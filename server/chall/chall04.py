from flask import request, redirect, send_from_directory
import os
import json
import base64
import random
import string
import datetime

import helpers

_chall = os.path.basename(os.path.splitext(__file__)[0])

def random_string(n) -> str:
    return ''.join(
        random.choice(string.ascii_letters + string.digits)
        for _ in range(n)
    )

def challenge(_, next_challenge):
    if request.method == "POST":
        session = request.cookies.get("session", None)
        if session is not None:
            try:
                session = json.loads(base64.b64decode(session.encode("utf-8")).decode("utf-8"))
                if session.get("admin", False) == True:
                    print(f"[INFO] {_chall} solved")
                    return next_challenge;
                else:
                    return redirect(request.url)
            except:
                return redirect(request.url)
    else:
        r = send_from_directory(
            "./templates",
            f"{_chall}.html",
            etag=False,
            max_age=0,
        )
        data = {
            "id": random_string(16),
            "admin": False,
        }
        data = json.dumps(data)
        data = base64.b64encode(data.encode("utf-8")).decode("utf-8")
        r.set_cookie("session", data, expires = datetime.datetime.now() + datetime.timedelta(days=7))
        return helpers.uncache(r)

def static(name):
    return helpers.serve_static(name)
