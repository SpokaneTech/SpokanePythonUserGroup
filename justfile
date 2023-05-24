set shell := ["bash", "-uc"]

python := if path_exists("./.venv/bin/python3") == "true" { ".venv/bin/python3" } else { "python" }


serve:
    {{ python }} -m mkdocs serve -a 0.0.0.0:9000
