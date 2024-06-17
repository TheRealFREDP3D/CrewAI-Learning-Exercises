# -------------------------------------------------------------------------------
# tools.py - Python script to create tools with the crewai_tools library.
# ------------------------------------------------------------------------------- 
# Author: Frederick Pellerin
# Github: https://github.com/TheRealFREDP3D
# X: https://x.com/TheRealFredP3D
# Date: 2024-07-15
# -------------------------------------------------------------------------------
# - It imports the load_dotenv function from the dotenv module, which is used to 
#   load environment variables from a .env file into the system.
#
# - It calls the load_dotenv function, which loads the environment variables from 
#   the .env file into the system.
#
# - It imports the os module, which provides a way of using operating system 
#   dependent functionality.
#
# - It imports the SerperDevTool class from the crewai_tools module.
#
# - It sets the value of the SERPER_API_KEY environment variable to the value of 
#   the SERPER_API_KEY variable in the .env file.
#
# - It creates an instance of the SerperDevTool class and assigns it to the tool 
#   variable. This instance can be used to interact with the Serper API.
# -------------------------------------------------------------------------------

from dotenv import load_dotenv
load_dotenv()

import os
from crewai_tools import SerperDevTool

os.environ["SERPER_API_KEY"]= os.getenv("SERPER_API_KEY")

tool= SerperDevTool()
