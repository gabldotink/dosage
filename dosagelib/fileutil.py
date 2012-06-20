# -*- coding: iso-8859-1 -*-
# Copyright (C) 2012 Bastian Kleineidam
"""
File and path utilities.
"""

def has_module (name):
    """Test if given module can be imported.
    @return: flag if import is successful
    @rtype: bool
    """
    try:
        exec "import %s as _bla" % name
        return True
    except (OSError, ImportError):
        # some modules (for example HTMLtidy) raise OSError
        return False


def is_tty (fp):
    """Check if a file object is a TTY."""
    return (hasattr(fp, "isatty") and fp.isatty())
