from datetime import datetime, timedelta
from flask import Response, request, make_response, redirect, send_from_directory


def get_challenge(config) -> tuple[str, str | None, str | None]:
    challs = config["challenges"]
    key = request.cookies.get("c")

    if key == None:
        chall = challs[0]
        return (chall["name"], chall["flag"], chall["key"])

    for i in range(len(challs)):
        if challs[i]["key"] == key:
            if i+1 < len(challs):
                chall = challs[i+1]
                return (chall["name"], chall["flag"], chall["key"])
            else:
                return ("_win", None, None)

    chall = challs[0]
    return (chall["name"], chall["flag"], chall["key"])


def next_challenge(config) -> Response:
    chall, _, key = get_challenge(config)

    response = make_response(redirect('/challenge'))
    if chall != "_win" and key != None:
        expires = datetime.now() + timedelta(days=7)
        response.set_cookie("c", key, expires=expires)
    return response


def serve_static(name) -> Response:
    return uncache(send_from_directory(
        "./static",
        name,
        etag=False,
        max_age=0,
    ))


def reload_challenge() -> Response:
    return make_response(redirect("/challenge"))


def uncache(r) -> Response:
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    del r.headers['Date']
    del r.headers['Last-Modified']
    return r
