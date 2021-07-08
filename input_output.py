"""
-----------------------------------------------------------------------------
File read, write helpers
-----------------------------------------------------------------------------
AUTHOR: Soumitra Samanta (soumitramath39@gmail.com)
-----------------------------------------------------------------------------
"""

import os

__all__ = [
    'create_folder',
    
]


def create_folder(folder_name: str) -> None:
    """Create folder if not exist"""
    
    if len(folder_name):
        if not os.path.isdir(folder_name):
            os.makedirs(folder_name)
        
    return folder_name
