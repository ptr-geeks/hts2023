from flask import Response, request, redirect, send_from_directory
import os
import requests

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
    if name == "imageoptimizer":
        url = request.args.get("url", None)
        if url is not None:
            s = requests.Session()
            c = {"c": "5LLYEvLAmfZ77kjH8syo4lz6Iqml9m5PSvbaRBU4R2DVh6W1eQR5jKWSRKdJuQ0m"}
            r = s.get(url, cookies=c)
            return helpers.uncache(
                Response(
                    r.content,
                    mimetype=r.headers["Content-Type"],
                    status=r.status_code,
                )
            )
    elif name == "flag":
        if request.remote_addr == "127.0.0.1":
            return helpers.uncache(
                Response(
                    "The mitochondria is the powerhouse of the cell",
                    mimetype="text/plain",
                )
            )
        else:
            return helpers.uncache(
                Response(
                    "You are not allowed to see the flag! It is only accessible from the intranet.",
                    mimetype="text/plain",
                    status=403,
                )
            )

    return helpers.serve_static(name)
