from flask import Response, request, redirect, send_from_directory
import os

import helpers

_chall = os.path.basename(os.path.splitext(__file__)[0])


from datetime import datetime
import random

def genflags():
    seed = datetime.utcnow().timestamp()
    seed = int(seed) // 5
    seed = seed ^ 0xDEADBEEF
    random.seed(seed)
    flags = [random.randint(0, 65535) for _ in range(8)]
    return flags


def testflags(data):
    flags = genflags()
    for i in range(1, 8):
        flags[i] = flags[i] ^ flags[i - 1]
    for i in range(8):
        if flags[i] != data[i]:
            return False
    return True

def challenge(_, next_challenge, metrics):
    if request.method == "POST":
        metrics.challenges_attempted.labels(_chall).inc()
        try:
            flags = [
                int(request.form.get("flag1", 0)),
                int(request.form.get("flag2", 0)),
                int(request.form.get("flag3", 0)),
                int(request.form.get("flag4", 0)),
                int(request.form.get("flag5", 0)),
                int(request.form.get("flag6", 0)),
                int(request.form.get("flag7", 0)),
                int(request.form.get("flag8", 0)),
            ]
            if testflags(flags):
                print(f"[INFO] {_chall} solved")
                metrics.challenges_solved.labels(_chall).inc()
                return next_challenge;
            else:
                return redirect(request.url)
        except:
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
    if name.startswith("flag"):
        flags = genflags()
        if name == "flag1":
            return helpers.uncache(Response(str(flags[0]), mimetype="text/plain"))
        if name == "flag2":
            return helpers.uncache(Response(str(flags[1]), mimetype="text/plain"))
        if name == "flag3":
            return helpers.uncache(Response(str(flags[2]), mimetype="text/plain"))
        if name == "flag4":
            return helpers.uncache(Response(str(flags[3]), mimetype="text/plain"))
        if name == "flag5":
            return helpers.uncache(Response(str(flags[4]), mimetype="text/plain"))
        if name == "flag6":
            return helpers.uncache(Response(str(flags[5]), mimetype="text/plain"))
        if name == "flag7":
            return helpers.uncache(Response(str(flags[6]), mimetype="text/plain"))
        if name == "flag8":
            return helpers.uncache(Response(str(flags[7]), mimetype="text/plain"))
    return helpers.serve_static(name)
