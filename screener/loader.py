#=============================================================================
#
# Python Module Importer Utilities
#
#=============================================================================

"""
Python Module Importer Utilities
================================

Allows a Python script to import modules using file system paths rather than
Python module paths.
"""


import importlib
import os
import sys


__version__ = '0.0.0'


#=============================================================================
def is_python( path ):
    """
    Attempts to load a Python file without knowing if it's valid Python
    code.

    @param path The path to the Python file to check
    @return     True if it can be parsed as Python code, otherwise False
    """

    # Wrap the load call to catch any syntax problems during loading.
    try:
        load( path )
    except SyntaxError:
        return False
    return True


#=============================================================================
def load( path ):
    """
    Loads a Python module from a path to a file.

    @param path The path to the Python file to load as a module
    @return     A reference to the module
    """

    # Normalize and parse path to script.
    path            = os.path.realpath( path )
    basename        = os.path.basename( path )
    dirname         = os.path.dirname( path )
    name, extension = os.path.splitext( basename )

    # Remove any possible existing reference from the modules dictionary.
    if name in sys.modules:
        del sys.modules[ name ]

    # Prepend the directory to this file to the path list.
    sys.path.insert( 0, dirname )

    # Import the module.
    module = importlib.import_module( name )

    # Remove reference to module from modules dictionary.
    del sys.modules[ name ]

    # Remove the directory from path list.
    sys.path.pop( 0 )

    # Return the reference to the module.
    return module


