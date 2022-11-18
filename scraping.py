from selenium import webDriver
from bs4 import BeautifulSoup
import time 
import csv

START_URL= "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("C:\\Users\\DELL\\Desktop\\Python\\PROJECTS\\PRO-128scraping\\chromedriver")
browser.get(START_URL)
time.sleep(10)

def scrape():
    headers = ["name","distance","mass","radius"]
    stars_data = []
    for i in range(0, 428):
    
        soup = BeautifulSoup(browser.page_source, "html.parser")
        for ul_tag in soup.find_all("ul", attrs={"class", "wikitable sortable jquery-tablesorter"}):
        
            tr_tags = ul_tag.find_all("tr")
            temp_list = []
            
            for index, tr_tag in enumerate(tr_tags):
                if index == 0:
                    temp_list.append(li_tag.find_all("td")[0].contents[0])
                else:
                    try:
                        temp_list.append(tr_tag.contents[0])
                    except:
                        temp_list.append("")
                        
            stars_data.append(temp_list)
        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    with open("scrapper_2.csv", "w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(stars_data)
scrape()

