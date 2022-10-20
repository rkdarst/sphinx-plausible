# Sphinx extension for plausible.io

This extension adds the <plausible.io> script tags to a Sphinx
project.



## Installation

Install the Python package.



## Usage

Add `sphinx_plausible` to `extensions`:

```python
extensions = [
    "sphinx_plausible",
]
```

Configuration options:
* `plausible_domain`: The domain name, like `my.domain.org`.  Can be a
  list which will be comma-joined.

* `plausible_script`: The URL to the script to load, default is
  `https://plausible.io/js/script.js`.

* `plausible_enabled`: Should plausible be active?  Default `True`.
  You can limit to only the official deployment with something such as:

  ```python
  import os
  plausible_enabled = (
      'GITHUB_ACTION' in os.environ
      and os.environ.get('GITHUB_REPOSITORY', '').lower() == 'aaltoscicomp/scicomp-docs'
      and os.environ.get('GITHUB_REF') == 'refs/heads/master'
	  )

def do_activate():
      return environ.get('GITHUB_REPOSITORY', '').lower().startswith('aaltoscicomp')

  plausible_activate_hook = do_activate
  ```


## Status and development

Beta but works as of 2022 - feature requests are still welcome!
