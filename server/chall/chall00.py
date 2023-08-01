from flask import request, redirect, send_from_directory
import os

import helpers

_chall = os.path.basename(os.path.splitext(__file__)[0])

def challenge(flag, next_challenge, metrics):
    if request.method == "POST":
        metrics.challenges_attempted.labels(_chall).inc()
        if request.form.get("flag") == flag:
            print(f"[INFO] {_chall} solved")
            metrics.challenges_solved.labels(_chall).inc()
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

def static(name, metrics):
    return helpers.serve_static(name)
