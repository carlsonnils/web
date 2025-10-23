import sys
from subprocess import Popen


# run the backend server
p = Popen(
    ["uv", "run", "python", "-m", "fastapi", "dev", "backend/main.py"],
    stdout=sys.stdout,
    stderr=sys.stderr,
)
p.wait()
