#=============================================================================
#
# Test Module
#
#=============================================================================

"""
Test Module
===========

A simple module used for testing this package.
"""


__version__ = '0.0.0'


#=============================================================================
# Module-level variables

module_property = 42


#=============================================================================
def module_function( argument ):
    """
    Module-level test function
    """
    print( 'Argument:', argument )


#=============================================================================
def raiser( exception = None ):
    """
    A module function that raises exceptions
    """
    if exception is not None:
        raise exception

#=============================================================================
def returner( argument ):
    """
    A module function that returns what you give it
    """
    return argument


#=============================================================================
def variadic( *args, **kwargs ):
    """
    A completely variadic function
    """
    parts = []
    for arg in args:
        parts.append( '{}:{}'.format( type( arg ).__name__, arg ) )
    for key, value in kwargs.items():
        parts.append(
            '{}:{}={}:{}'.format(
                type( key ).__name__,
                key,
                type( value ).__name__,
                value
            )
        )
    return '\n'.join( parts )


#=============================================================================
class ModuleClass( object ):
    """
    Module-level test class
    """


    #=========================================================================
    def __init__( self ):
        """
        Initializes a ModuleClass object.
        """
        self.prop = 26


    #=========================================================================
    def method( self, argument ):
        """
        A test method.
        """
        return argument + self.prop

