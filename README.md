# Sphinx extension for plausible.io

This extension adds the <https://plausible.io> script tags to a Sphinx
project.  It doesn't change the template, it uses the standard Sphinx
hooks to insert javascript directly into any template (that uses the
standard Sphinx stuff).

This is currently being tested but in production, please verify it
does the correct thing for you.



## Installation

Install the Python package: on pip it is `sphinx-plausible`.



## Usage

Add `sphinx_plausible` to `extensions`:

```python
extensions = [
    "sphinx_plausible",
]
```

Configuration options:
* `plausible_domain` (required): The domain name, like
  `my.domain.org`.  Can be a list which will be joined by commas.

* `plausible_script` (default `https://plausible.io/js/script.js`):
  The URL to the script to load If you want to use the "proxying the
  script" idea, download the script and put it in `html_static_path`
  and add the filename (relative to `html_static_path`) here instead
  of the absolute path.  (in the future we can automatically download
  and cache)

* `plausible_enabled` (default `True`): Should plausible be active?
  You might want to disable it on all you test deployments and so on.
  Default `True`.  You can limit to only the official deployment with
  something such as:

  ```python
  import os
  plausible_enabled = (
      'GITHUB_ACTION' in os.environ
      and os.environ.get('GITHUB_REPOSITORY', '').lower() == 'aaltoscicomp/scicomp-docs'
      and os.environ.get('GITHUB_REF') == 'refs/heads/master'
	  )
  ```


## Status and development

Beta but works as of 2022 - improvements and feature requests are
still welcome!
