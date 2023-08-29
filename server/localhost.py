from flask import Response, Flask
from prometheus_flask_exporter.multiprocess import GunicornPrometheusMetrics
from prometheus_client import Counter

import yaml
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader
import importlib

import helpers
import generic_routes

# Load config
with open("config.yaml") as f:
    config = yaml.load(f.read(), Loader=Loader)

# Create app
app = Flask(__name__)

app.config.update(
    SEND_FILE_MAX_AGE_DEFAULT=0,
)

# Configure metrics
#metrics = GunicornPrometheusMetrics(app)

class Metrics():
    challenges_attempted = Counter(
        "challenges_attempted",
        "Number of challenges attempted",
        ["challenge"],
    )
    challenges_solved = Counter(
        "challenges_solved",
        "Number of challenges solved",
        ["challenge"],
    )

# Route home
@app.route("/")
def home() -> Response:
    return generic_routes.home()

@app.route("/favicon.png")
def favicon() -> Response:
    return generic_routes.favicon()

# Route challenges
@app.route("/challenge", methods=["GET", "POST"])
def challenge() -> Response:
    chall, flag, _ = helpers.get_challenge(config)
    if chall == "_win":
        return generic_routes.win()

    module_name = "chall." + chall
    module = importlib.import_module(module_name, package=__package__)
    return module.challenge(flag, helpers.next_challenge(config), Metrics)

# Route static files
@app.route("/s/<path:name>", methods=["GET"])
def static_route(name) -> Response:
    chall, _, _ = helpers.get_challenge(config)
    if chall == "_win":
        return helpers.serve_static(name)

    module_name = "chall." + chall
    module = importlib.import_module(module_name, package=__package__)
    return module.static(name, Metrics)

app.run()