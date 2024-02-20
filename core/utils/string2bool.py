################################################################################
# Filename          : string2bool.py
# 
# Description       : This file is responsible for converting string to boolean.
#
# Created by        : Brian Vergara Rosario on 09 June 2021
# Last Modified by  : Brian Vergara Rosario on 21 July 2021
#
# Copyright         : © 2021 N8XT Aerospace Pte. Ltd.  All Rights Reserved.
################################################################################



################################################################################
# IMPORTS
################################################################################

# ------------------------------------------------------------------------------
# Standard Python Libraries
# ------------------------------------------------------------------------------

import os
import sys
from pathlib import Path

# Below is a simple fix to address the "ModuleNotFoundError" when importing
# "appcore.modulename" modules from a directory other than the parent directory.
#
# Parameters:   '../'   means 1 folder above.
#               '../..' means 2 folders above. 
sys.path.insert(1, os.path.join(sys.path[0], '../..'))

# ------------------------------------------------------------------------------
# 3rd Party Libraries
# ------------------------------------------------------------------------------

''' None '''

# ------------------------------------------------------------------------------
# 1st Party Libraries (Our Own Libraries)
# ------------------------------------------------------------------------------

''' None '''



################################################################################
# GLOBALS
################################################################################

# ------------------------------------------------------------------------------
# Global Constants
# ------------------------------------------------------------------------------

# Below is the constants for AppCORE root folder.
# 
# Paremeters:   '.parents[x]' the x means depth of the folder.
APPCORE_ROOT = Path(__file__).resolve().parents[2]

TRUE_STRING     = ("True", "true", "TRUE", "Yes", "yes", "YES", "Y", "y", "1")
FALSE_STRING    = ("False", "false", "FALSE", "No", "no", "NO", "N", "n", "0")

# ------------------------------------------------------------------------------
# Global Variables
# ------------------------------------------------------------------------------

''' None '''


################################################################################
# CLASSES & METHODS, FUNCTIONS, ROUTES
################################################################################

# ==============================================================================
# StringToBool Class (Start) 
# ==============================================================================

class StringToBool:
    """ This class is responsible for converting string to boolean.
    """
    
    # ==========================================================================
    # Constructor
    # ==========================================================================

    #####
    def __init__(self):
        """ Initialized StringToBool Class.
        """

        # ----------------------------------------------------------------------
        # Public Variables
        # ----------------------------------------------------------------------

        ''' None '''

        # ----------------------------------------------------------------------
        # Private Variables
        # ----------------------------------------------------------------------

        ''' None '''

        # ----------------------------------------------------------------------
        # Internal Method Calls
        # ----------------------------------------------------------------------
    
        ''' None '''

    # ==========================================================================
    # Public Methods
    # ==========================================================================
   
    #####
    def convert(self, string: str):
        """ Convert a string to boolean True or False

        Args:
            string (str): 
                Accepts the following strings: For True = "True", "true", "TRUE", "Yes", "yes", "YES", "Y", "y", "1".  
                For False = "False", "false", "FALSE", "No", "no", "NO", "N", "n", "0"

        Returns:
            [type]: 
                bool or None
        """
        
        if string.lower() == "true" or string.lower() == "yes" or string.lower() == "y" or string == "1":
            return True
        elif string.lower() == "false" or string.lower() == "no" or string.lower() == "n" or string == "0":
            return False
        else:
            return None


    # ==========================================================================
    # Private Methods
    # ==========================================================================

    ''' None '''

# ==============================================================================
# StringToBool Class (End) 
# ==============================================================================



# ==============================================================================
# Program Entry Point (Start) 
# ==============================================================================

if __name__=="__main__":
    ''' This is optional '''

# ==============================================================================
# Program Entry Point (End) 
# ==============================================================================



################################################################################
# END OF FILE
################################################################################