"""Sphinx extension for plausible.io analytics
"""

import sphinx.errors

from ._version import __version__

def setup(app):

    app.add_config_value(name="plausible_domain",
                         default=None,
                         rebuild="html",
                         types=[str, list])
    app.add_config_value(name="plausible_enabled",
                         default=True,
                         rebuild="html",
                         types=[bool])
    app.add_config_value(name="plausible_script",
                         default="https://plausible.io/js/script.js",
                         rebuild="html",
                         types=[str])

    def config_hook(app, config):
        """Hook to install the javascript with the right settings.

        Must be a hook since it depends on the other config values.
        """

        # Provide an easy way to disable the extension, since often you won't
        # want analytics on dev sites and so on.
        if not config.plausible_enabled:
            return

        script_args = {}

        # Create the domain
        if config.plausible_domain is None:
            raise sphinx.errors.ConfigError("plausible_domain option must be provided")
        if isinstance(config.plausible_domain, (list, tuple)):
            plausible_domain = ','.join(config.plausible_domain)
        else:
            plausible_domain = config.plausible_domain
        script_args['data-domain'] = plausible_domain

        # Do the actual adding
        app.add_js_file(config.plausible_script,
                        # sphinx>4.4 adds the loading_method="defer" argument,
                        # but `defer="defer"` in the <script ...> tag works the
                        # same.  For now, we focus on compatibility and
                        # reducing branches than perfection.
                        defer='defer',
                        **script_args,
                        )
        print("plausible.io analytics enabled in this build", script_args)

    # Register the init hook.
    app.connect('config-inited', config_hook)

    return {
        'version': __version__,
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
