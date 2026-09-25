# Create a script that detects whether Python is running in interactive mode or as a standalone script, and prints the result.

import sys

if hasattr(sys, "ps1"):
    print("python is running in interactive")

else: 
    print("python is running as a standalone")    
