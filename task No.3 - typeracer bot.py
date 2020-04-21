
from selenium import webdriver
from selenium.webdrive.common.keys import keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import sys
import re
from time import sleep

 class TRbot:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.website = "https://play.typeracer.com/

