# Sphinx extension for plausible.io

This extension adds the <https://plausible.io> script to a Sphinx
project by using standard Sphinx javascript insertion tools.  It
doesn't change the template, and it should work with any template
(that uses the standard Sphinx javascript insertion, which seems to be
most of them).

This is a relatively new project (but being used), so please verify it
does the correct thing in your case and suggest improvements.



## Installation

Install the Python package: on PyPI it is `sphinx-plausible`:

```
pip install sphinx-plausible
```



## Usage

Add `sphinx_plausible` to `extensions`.  Example config:

```python
extensions = [
    "sphinx_plausible",
]

plausible_domain = my.domain.org
```

If you want Plausible to only be enabled when your site is deployed by
Github Actions on the `main` branch in your own repository (remember
to update `organization/repo-name`):

```python
import os
plausible_enabled = (
    'GITHUB_ACTION' in os.environ
    and os.environ.get('GITHUB_REPOSITORY', '').lower() == 'organization-name/repo-name'
    and os.environ.get('GITHUB_REF') == 'refs/heads/main'
	)
```

Configuration options:

* `plausible_domain` (required): The domain name, like
  `my.domain.org`.  Can be a list which will be joined by commas.

* `plausible_script` (default `https://plausible.io/js/script.js`):
  The URL to the script to load.  If you want to use embed the script,
  download the script and put it in `html_static_path` and add the
  filename (relative to `html_static_path`) here instead of a URL.

* `plausible_enabled` (default `True`): Should plausible be active?
  You might want to disable it on all you test deployments and so on,
  so you can add some logic to enable/disable as needed.



## Status and development

Beta but works as of 2022 - improvements and feature requests are
still welcome!  I would be happy for a group maintenance home for
this.



## See also

* https://plausible.io/docs/plausible-script
