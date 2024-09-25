from unidecode import unidecode
from multiprocessing import Pool
from playwright.sync_api import sync_playwright
import argparse

parser = argparse.ArgumentParser(description= 'Digikala Discount Warning', prog= 'ddw.py')
parser.add_argument('--dkp', type=str, help= 'Set Digikala Product ID', metavar= 'dkp-14563541')
args = parser.parse_args()
dkp = args.dkp

url = "https://www.digikala.com/product/" + dkp

with sync_playwright() as p:
    def one(num):
            with sync_playwright() as p:
                browser = p.chromium.launch()
                page = browser.new_page()
                page.goto(url)
                try:    
                    price_a = page.locator('xpath=/html/body/div[1]/div[1]/div[3]/div[3]/div[2]/div[2]/div[2]/div[2]/div[5]/div/div[4]/div/div/div/div[2]/div/div[2]/span')
                    price_b = unidecode(price_a.text_content())
                    price_c = price_b.replace(",", "")
                    price_one = int(price_c)
                    return price_one
                except:
                    price_seven = 9999999999
                    return price_one
                
    def two(num):
            with sync_playwright() as p:
                browser = p.chromium.launch()
                page = browser.new_page()
                page.goto("https://www.digikala.com/product/dkp-15108761")
                try:
                    browser = p.chromium.launch()
                    page = browser.new_page()
                    page.goto("https://www.digikala.com/product/dkp-15108761")
                    price_a = page.locator('xpath=//*[@id="__next"]/div[1]/div[3]/div[3]/div[2]/div[2]/div[2]/div[2]/div[5]/div/div[4]/div/div/div/div[2]/div[2]/div[2]/span')
                    price_b = unidecode(price_a.text_content())
                    price_c = price_b.replace(",", "")
                    price_two = int(price_c)
                    return price_two
                except:
                    price_two = 9999999999
                    return price_two
    
    def three(num):
            with sync_playwright() as p:
                browser = p.chromium.launch()
                page = browser.new_page()
                page.goto("https://www.digikala.com/product/dkp-15108761")
                try:
                    browser = p.chromium.launch()
                    page = browser.new_page()
                    page.goto("https://www.digikala.com/product/dkp-15108761")
                    price_a = page.locator('xpath=/html/body/div[1]/div[1]/div[3]/div[3]/div[2]/div[2]/div[2]/div[2]/div[4]/div/div[4]/div/div/div/div[1]/div[2]/div[1]/span')
                    price_b = unidecode(price_a.text_content())
                    price_c = price_b.replace(",", "")
                    price_three = int(price_c)
                    return price_three
                except:
                    price_three = 9999999999
                    return price_two
    
    def four(num):
            with sync_playwright() as p:
                browser = p.chromium.launch()
                page = browser.new_page()
                page.goto("https://www.digikala.com/product/dkp-15108761")
                try:
                    browser = p.chromium.launch()
                    page = browser.new_page()
                    page.goto("https://www.digikala.com/product/dkp-15108761")
                    price_a = page.locator('xpath=/html/body/div[1]/div[1]/div[3]/div[3]/div[2]/div[2]/div[2]/div[2]/div[5]/div/div[4]/div/div/div/div[1]/div[2]/div[1]/span')
                    price_b = unidecode(price_a.text_content())
                    price_c = price_b.replace(",", "")
                    price_four = int(price_c)
                    return price_four
                except:
                    price_four = 9999999999
                    return price_four
    
    def five(num):
        with sync_playwright() as p:
                browser = p.chromium.launch()
                page = browser.new_page()
                page.goto("https://www.digikala.com/product/dkp-15108761")
                try:
                    browser = p.chromium.launch()
                    page = browser.new_page()
                    page.goto("https://www.digikala.com/product/dkp-15108761")
                    price_a = page.locator('xpath=/html/body/div[1]/div[1]/div[3]/div[3]/div[2]/div[2]/div[2]/div[2]/div[5]/div/div[4]/div/div/div/div[2]/div[2]/div[1]/span')
                    price_b = unidecode(price_a.text_content())
                    price_c = price_b.replace(",", "")
                    price_five = int(price_c)
                    return price_five
                except:
                    price_five = 9999999999
                    return price_five
    
    def six(num):
        with sync_playwright() as p:
                browser = p.chromium.launch()
                page = browser.new_page()
                page.goto("https://www.digikala.com/product/dkp-15108761")
                try:
                    browser = p.chromium.launch()
                    page = browser.new_page()
                    page.goto("https://www.digikala.com/product/dkp-15108761")
                    price_a = page.locator('xpath=/html/body/div[1]/div[1]/div[3]/div[3]/div[2]/div[2]/div[2]/div[2]/div[4]/div/div[4]/div/div/div/div[1]/div[2]/div[2]/span')
                    price_b = unidecode(price_a.text_content())
                    price_c = price_b.replace(",", "")
                    price_six = int(price_c)
                    return price_six
                except:
                    price_six = 9999999999
                    return price_six
    
    def seven(num):
        with sync_playwright() as p:
                browser = p.chromium.launch()
                page = browser.new_page()
                page.goto("https://www.digikala.com/product/dkp-15108761")
                try:
                    browser = p.chromium.launch()
                    page = browser.new_page()
                    page.goto("https://www.digikala.com/product/dkp-15108761")
                    price_a = page.locator('xpath=/html/body/div[1]/div[1]/div[3]/div[3]/div[2]/div[2]/div[2]/div[2]/div[5]/div/div[4]/div/div/div/div[2]/div/div[2]/span')
                    price_b = unidecode(price_a.text_content())
                    price_c = price_b.replace(",", "")
                    price_seven = int(price_c)
                    return price_seven
                except:
                    price_seven = 9999999999
                    return price_seven
    
    if __name__ == "__main__":
        p = Pool(processes=7)
        data_one = p.map(one, range(1))
        data_two = p.map(two, range(1))
        data_three = p.map(three, range(1))
        data_four = p.map(four, range(1))
        data_five = p.map(five, range(1))
        #data_six = p.map(six, range(1))
        #data_seven = p.map(seven, range(1))
        p.close()
        print(data_one)
        print(data_two)
        print(data_three)
        print(data_four)
        print(data_five)
        #print(data_six)
        #print(data_seven)
        
        





    