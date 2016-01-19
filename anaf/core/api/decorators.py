"""
Core decorators for api
"""

from utils import rc


def module_admin_required(module_name=None):
    """ Check that the user has write access to the treeio.core module """

    if not module_name:
        module_name = 'treeio.core'

    def wrap(f):
        "Wrap"
        def wrapped_f(cls, request, *args, **kwargs):
            "Wrapped"

            if request.user.profile.is_admin(module_name):
                return f(cls, request, *args, **kwargs)
            else:
                return rc.FORBIDDEN

        wrapped_f.__doc__ = f.__doc__
        wrapped_f.__name__ = f.__name__

        return wrapped_f

    return wrap
