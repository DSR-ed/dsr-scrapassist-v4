from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

def run(params):
    opts = Options(); opts.add_argument("--headless")
    driver = webdriver.Chrome(options=opts)
    driver.get("https://www.aef.cci.fr/rechercheMulticritere")
    time.sleep(3)
    # Exemple simple
    data = [{"nom":"Entreprise A","ville":"Paris","cp":"75001"}]
    driver.quit()
    return data
