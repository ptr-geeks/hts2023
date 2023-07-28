from flask import Response, send_from_directory

import helpers


def home() -> Response:
    return helpers.uncache(
        send_from_directory(
            "./templates",
            "index.html",
            etag=False,
            max_age=0,
        )
    )

def win() -> Response:
    return helpers.uncache(
        send_from_directory(
            "./templates",
            "win.html",
            etag=False,
            max_age=0,
        )
    )

def favicon() -> Response:
    return helpers.uncache(
        send_from_directory(
            "./static",
            "favicon.png",
            etag=False,
            max_age=0,
        )
    )

def robots() -> Response:
    return helpers.uncache(
        send_from_directory(
            "./static",
            "robots.txt",
            etag=False,
            max_age=0,
        )
    )
