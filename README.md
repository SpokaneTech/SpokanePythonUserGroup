# Spokane Python User Group Code Samples

[https://spokanepython.com/](https://spokanepython.com/)

---

## Documentation

- Serve
  - `mkdocs serve`
- Build
  - `mkdocs build`

### Dependencies 

Create a virtual environment

```shell
python -m venv .venv
source .venv/bin/activate
pip-sync
```

Install required Python packages

```shell
python -m pip install pip-tools
pip-sync
```

Update `requirements.txt`

```shell
# python -m pip install pip-tools
pip-compile --resolver=backtracking
```

Install [CairoSVG](https://cairosvg.org/documentation/#installation) requirements

```shell
sudo apt-get install -y libcairo2-dev libfreetype6-dev libffi-dev libjpeg-dev libpng-dev libz-dev
```
