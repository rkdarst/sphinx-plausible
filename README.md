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

* `plausible_activate_hook`: A callable, if this returns False, then
  plausible will *not* be activated.  This acn be used to, for
  example, only activate it if it's deployed to Github Pages.  The
  default is to activate.  Example:

  ```python
  import os
  def do_activate():
      return environ.get('GITHUB_REPOSITORY', '').lower().startswith('aaltoscicomp')

  plausible_activate_hook = do_activate
  ```


## Status and development

Beta but works as of 2022 - feature requests are still welcome!
