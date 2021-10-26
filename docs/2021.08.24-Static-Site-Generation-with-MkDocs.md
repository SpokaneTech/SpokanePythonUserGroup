---
title: "Mk’ing spokanepython.com: Static Site Generation with MkDocs"
description: Learn about getting started with MkDocs, customizing the look and feel of your site, and hosting an online website using MkDocs!
---

# Mk’ing spokanepython.com: Static Site Generation with MkDocs

_August 24, 2021_

## How to pronounce "MkDocs"

- "McDocs"
- "M-K Docs"
- "Mark Docs"

## Outline

1. Getting started with MkDocs
2. Adding some content
3. Customizing the look and feel of your site
4. Hosting your site

## Sites that use MkDocs:

- [SPUG](https://spokanepython.com/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Pydantic](https://pydantic-docs.helpmanual.io/)
- [ODMantic](https://art049.github.io/odmantic/)
- [MkDocs](https://www.mkdocs.org/)
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
- many, many more...

## Getting started with MkDocs

What is MkDocs?

[https://www.mkdocs.org/](https://www.mkdocs.org/)

- Static site generator that's geared towards building project documentation
- Source files are written in Markdown
- Configured with a single YAML configuration file

## Let's grab some code

```
git clone https://github.com/IntelliTect-Samples/MkDocsTemplate.git
cd ./MkDocsTemplate

## (optional)
## python -m virtualenv .venv
## .venv/Scripts/Activate.ps1

pip install -r requirements.txt
mkdocs serve
```

## Let's add some content

```
git checkout origin/clone-force-99
```

## Let's make it look better

```
git checkout origin/clone-force-99-v2
```

## Let's take a look at GitHub Pages

[https://github.com/marketplace/actions/deploy-mkdocs](https://github.com/marketplace/actions/deploy-mkdocs)

[https://intellitect-samples.github.io/MkDocsTemplate/](https://intellitect-samples.github.io/MkDocsTemplate/)

## Summary

_MkDocs_ & _Material for MkDocs_ can be used to quickly and easily make a nice looking site for documentation or anything else.
