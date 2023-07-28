import string
import random
import yaml
import sys

def random_string(n) -> str:
    return ''.join(
        random.choice(string.ascii_letters + string.digits)
        for _ in range(n)
    )

configfile = "./server/config.yaml"
if len(sys.argv) > 1:
    configfile = sys.argv[1]

with open(configfile, "r") as f:
    config = yaml.safe_load(f.read())

for chall in config["challenges"]:
    chall["key"] = random_string(64)

data = yaml.dump(config, default_flow_style=False, sort_keys=False)
with open(configfile, "w") as f:
    f.write(data)
