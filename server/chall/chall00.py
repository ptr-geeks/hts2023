from flask import request, redirect, send_from_directory
import os

import helpers

_chall = os.path.basename(os.path.splitext(__file__)[0])

def challenge(flag, next_challenge):
    if request.method == "POST":
        if request.form.get("flag") == flag:
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
