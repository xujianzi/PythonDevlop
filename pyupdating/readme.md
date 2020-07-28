# Pyupdating

[![Language Badge](https://img.shields.io/badge/language-python-blue)](https://www.python.org/)
[![Athor Badge](https://img.shields.io/badge/Author-JianXu-green)](https://sites.google.com/binghamton.edu/jian-xu)
[![Version Badge](https://img.shields.io/badge/pyupdating-0.0.1-brightgreen)](https://github.com/xujianzi/PythonDevlop/tree/master/pyupdating)
[![Github Badge](https://img.shields.io/github/followers/xujianzi?style=social)](https://github.com/xujianzi)

## Description

> This is the summay docs for python module actions. Everytime we reuse the [python](https://www.python.org/), there are always lots of packages need to update. This script serves to auto-upgrade all the outdated packages. We also mark and write the common commands in [pip](https://pip.pypa.io/en/stable/).
---

## Content

*[Auto-Updating all packages](#Auto-updating-all-packages)

*[Pip commonly used commands](#Pip-commonly-used-commands)

---

## Auto updating all packages

* 1. Using self-developed module

```python
import pyupdating
pyupdating.upgrade.update_allpack()
```

* 2. Using command line in terminal

```python
>"pip install pip-review"
>"pip-review --local --interactive"
```

---

## Pip-commonly-used-commands

* 1. Upgrading pip version

```python
>"python -m pip install --upgrade pip"
```

* 2. Install specific python package

```python
>"pip install" + packagename
```

* 3. Install python package to specific version

```python
>"pip install "+ packname + "==" + version_num
```

* 4. Upgrade python package to latest version

```python
>"pip install --upgrade " + packname
```

* 5. List installed packages & all outdated packages

```python
>"pip list"
>"pip list --outdated"
```

* 6. Delete package

```python
>"pip uninstall" + packname
```

---
