from flask import Response, request, redirect, send_from_directory
import os
import random

import helpers

_chall = os.path.basename(os.path.splitext(__file__)[0])

def crypt(text) -> str:
    random.seed(len(text))
    text = [x for x in text]
    for i in range(len(text)):
        r = random.randint(0, len(text) - 1)
        text[i], text[r] = text[r], text[i]
    return "".join(text)


def challenge(flag, next_challenge, metrics):
    if request.method == "POST":
        if request.form.get("plaintext", None) is not None:
            plaintext = request.form.get("plaintext")
            ciphertext = crypt(plaintext)
            return helpers.uncache(
                Response(
                    ciphertext,
                    mimetype="text/plain",
                )
            )
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
    if name == "chall06.js":
        return helpers.uncache(
            send_from_directory(
                "./chall/chall06",
                f"chall06.js",
                etag=False,
                max_age=0,
            )
        )
    return helpers.serve_static(name)
