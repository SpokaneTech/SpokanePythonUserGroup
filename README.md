# Spokane Python User Group Code Samples

[https://spokanepython.com/](https://spokanepython.com/)

---

## Documentation

- Serve
  - `mkdocs serve`
- Build
  - `mkdocs build`

### Dependencies 

Create virtual environment

```shell
python -m venv .venv
source .venv/bin/activate
pip-sync
```

Update `requirements.txt`

```shell
python -m pip install pip-tools
pip-compile --resolver=backtracking
pip-sync
```

