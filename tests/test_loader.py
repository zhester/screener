#=============================================================================
#
# loader Module Unit Tests
#
#=============================================================================

"""
loader Module Unit Tests
========================
"""


import os
import unittest


import screener


__version__ = '0.0.0'


#=============================================================================
class LoaderTests( unittest.TestCase ):
    """
    Tests the loader module
    """


    #=========================================================================
    def setUp( self ):
        """
        Performs test setup.
        """

        # Path to test assets directory
        script_dir  = os.path.dirname( os.path.realpath( __file__ ) )
        self.assets = os.path.join( script_dir, 'assets' )

        # Store some type references for testing.
        self.ftype = type( lambda x : None )
        self.ctype = type( LoaderTests )


    #=========================================================================
    def test_is_python( self ):
        """
        Tests the `loader.is_python()` function.
        """

        # Path to test modules
        good_path = os.path.join( self.assets, 'testmodule.py' )
        bad_path  = os.path.join( self.assets, 'syntaxerror.py' )

        # Check valid module.
        self.assertTrue( screener.is_python( good_path ) )

        # Check invalid module.
        self.assertFalse( screener.is_python( bad_path ) )


    #=========================================================================
    def test_load( self ):
        """
        Tests the `loader.load()` function.
        """

        # Path to test module
        module_path = os.path.join( self.assets, 'testmodule.py' )

        # Load the test module.
        module = screener.load( module_path )

        # See if the requested module was loaded.
        self.assertEqual( module.__name__, 'testmodule' )

        # Check property existence.
        self.assertIn( 'module_property', module.__dict__ )

        # Check function existence.
        self.assertIn( 'module_function', module.__dict__ )
        self.assertIsInstance( module.module_function, self.ftype )

        # Check class existence.
        self.assertIn( 'ModuleClass', module.__dict__ )
        self.assertIsInstance( module.ModuleClass, self.ctype )


    #=========================================================================
    def test_load_invalid( self ):
        """
        Tests the `loader.load()` function when the path is invalid.
        """

        # Path to nowhere
        invalid_path = '/fake/path/to/module.py'

        # Make sure the normal ImportError is raised.
        self.assertRaises( ImportError, screener.load, invalid_path )


    #=========================================================================
    def test_load_syntax( self ):
        """
        Tests the `loader.load()` function when loading invalid code.
        """

        # Path to test module
        module_path = os.path.join( self.assets, 'syntaxerror.py' )

        # Make sure a SyntaxError is raised.
        self.assertRaises( SyntaxError, screener.load, module_path )

