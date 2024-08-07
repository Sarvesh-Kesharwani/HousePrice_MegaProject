# https://www.geeksforgeeks.org/multiprocessing-python-set-1/

# importing the multiprocessing module 
import multiprocessing 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import pandas as pd
from datetime import datetime
import os
import time

def Crawl_over_all_pages(city, start_page_num, end_page_num):
    # Configure Chrome options
    chrome_options1 = Options()
    chrome_options1.add_argument("--headless=new")
    chrome_options1.add_argument('--enable-gpu')
    chrome_options1.add_argument('--enable-webgl')
    chrome_options1.add_argument('--ignore-gpu-blacklist')
    chrome_options1.add_argument("--no-sandbox")
    chrome_options1.add_argument("--disable-dev-shm-usage")
    chrome_options1.add_argument("--window-size=1920x1080")
    chrome_options1.add_argument("--start-maximized")
    chrome_options1.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
    
    # Initialize the Chrome WebDriver
    service1 = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service1, options=chrome_options1)

    # crawling inside every page
    for page in range(start_page_num, end_page_num+1):
        print(f'Working on page num: {page}')
        # URL of the page to scrape
        url = f"https://www.99acres.com/property-for-rent-in-{city}-ffid-page-{page}"

        # Open the webpage
        driver.get(url)
        driver.get_screenshot_as_file(os.getcwd()+"\\screenshots\\"+str(datetime.now().strftime("%Y-%m-%d_%H-%M-%S"))+".png")

        # close popup window
        try:
            # Set an explicit wait time of 10 seconds
            wait = WebDriverWait(driver, 10)
            
            # Wait for an element to be clickable
            warning_popup_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@data-label='FRAUD_ALERT_UNDERSTOOD' or @class='pageComponent FraudDesktop__cta']")))
            # print("Fetched Page Successully!")
            warning_popup_btn.click()
        except Exception as e:
            print("An error occurred:", e)
        
        # finding total no of listings on current page
        no_of_properties_on_page = 0
        try:
            property_titles = driver.find_elements(By.XPATH, "//span[@class='tupleNew__bOld']")
            no_of_properties_on_page = len(property_titles)
            print(f'no_of_properties_on_page_{page} are: ', no_of_properties_on_page)
        except Exception as e:
            print("Couldn't grab property_title!")
        

        # overview
        society_name_lst=[]
        property_title_lst=[]
        property_rent_lst=[]
        types_of_rooms_available_lst=[]
        bedroom_lst=[]
        bathroom_lst=[]
        balcony_lst=[]
        furnishing_details_lst=[]
        superBuiltUp_area_lst=[]
        carpet_area_lst=[]
        address_lst=[]
        available_for_lst=[]
        furnishing_type_lst=[]
        available_from_lst=[]
        Posted_By_and_On_lst=[]
        Flooring_lst=[]
        Floor_Number_lst=[]
        Power_Backup_lst=[]
        Property_Age_lst=[]
        Months_of_Notice_lst=[]
        Gated_Community_lst=[]
        Electricity_n_Water_Charges_lst=[]
        property_features_lst=[]
        avg_rating_lst=[]

        # crawling over each entry on current page
        for property in range(0, no_of_properties_on_page-22):
            print(f"Working on Property num: {property+1}")
            # fetching society_name
            try:
                society_name = driver.find_elements(By.XPATH, "//div[@class='tupleNew__locationName ellipsis']")[property]
                society_name = society_name.text
                society_name = str(society_name).strip()
                if not society_name:
                    society_name = 'None'
                # print(society_name)
                society_name_lst.append(society_name)
            except Exception as e:
                print("Couldn't grab society_name!")
                society_name = 'None'

            # fetching property_title
            try:
                property_title = driver.find_elements(By.XPATH, "//span[@class='tupleNew__bOld']")[property]
                property_title = property_title.text
                property_title = str(property_title).strip()
                if not property_title:
                    property_title = 'None'
                # print(property_title)
                property_title_lst.append(property_title)
            except Exception as e:
                print("Couldn't grab property_title!")
                property_title = 'None'

            # fetching property_title
            try:
                property_rent = driver.find_elements(By.XPATH, "//div[@class='tupleNew__priceValWrap']")[property]
                property_rent = property_rent.text
                property_rent = str(property_rent).strip()
                if not property_rent:
                    property_rent = 'None'
                # print(property_rent)
                property_rent_lst.append(property_rent)
            except Exception as e:
                print("Couldn't grab property_rent!")
                property_rent = 'None'
            

            # crawling inside of property details page to featch more features
            # Configure Chrome options
            chrome_options2 = Options()
            chrome_options2.add_argument("--headless=new")
            chrome_options2.add_argument('--enable-gpu')
            chrome_options2.add_argument('--enable-webgl')
            chrome_options2.add_argument('--ignore-gpu-blacklist')
            chrome_options2.add_argument("--no-sandbox")
            chrome_options2.add_argument("--disable-dev-shm-usage")
            chrome_options2.add_argument("--window-size=1920x1080")
            chrome_options2.add_argument("--start-maximized")
            chrome_options2.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
                
            # ------------------------------------------------------------------------------------------------------------
            # Initialize the Chrome WebDriver
            service2 = Service(ChromeDriverManager().install())
            driver_inner_page = webdriver.Chrome(service=service2, options=chrome_options2)
            property_page_url = driver.find_elements(By.XPATH, "//a[@class='tupleNew__propertyHeading ellipsis']")[property]
            driver_inner_page.get(property_page_url.get_attribute('href'))


            # Overview
            # ------------------------------------------------------------------------------------------------------------
            try:
                value = driver_inner_page.find_elements(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/section[1]/div[1]/div[1]/div[2]/div[2]/h1[1]/div[1]/span[1]")
                value = value.text
                value = str(value).strip()
                if not value:
                    value = 'None'
                # print(value)
                types_of_rooms_available_lst.append(value)
            except Exception as e:
                print("Couldn't grab types_of_rooms_available!")
                value = 'None'
                types_of_rooms_available_lst.append(value)
            # ------------------------------------------------------------------------------------------------------------
            try:
                value = driver_inner_page.find_elements(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[4]/div[3]/div[1]/ul[1]")
                value = value.text
                value = str(value).strip()
                if not value:
                    value = 'None'
                # print(types_of_rooms_available)
                furnishing_type_lst.append(value)
            except Exception as e:
                print("Couldn't grab furnishing_type!")
                value = 'None'
                furnishing_type_lst.append(value)
            # ------------------------------------------------------------------------------------------------------------
            try:
                value = driver_inner_page.find_elements(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[4]/div[3]/div[1]/ul[1]")
                value = value.text
                value = str(value).strip()
                if not value:
                    value = 'None'
                # print(value)
                furnishing_details_lst.append(value)
            except Exception as e:
                print("Couldn't grab furnishing_details!")
                value = 'None'
                furnishing_details_lst.append(value)
            # ------------------------------------------------------------------------------------------------------------
            try:
                value = driver_inner_page.find_element(By.XPATH, "//span[@id='bedRoomNum']")
                value = str(value.text).strip()
                if not value:
                    value = 'None'
                bedroom_lst.append(value)
                # print(value)
            except Exception as e:
                print("Couldn't grab bedRoomNum!")
                value = 'None'
                bedroom_lst.append(value)

            try:
                value = driver_inner_page.find_element(By.XPATH, "//span[@id='bathroomNum']")
                value = str(value.text).strip()
                if not value:
                    value = 'None'
                bathroom_lst.append(value)
                # print(value)
            except Exception as e:
                print("Couldn't grab bathroomNum!")
                value = 'None'
                bathroom_lst.append(value)

            try:
                value = driver_inner_page.find_element(By.XPATH, "//span[@id='balconyNum']")
                value = str(value.text).strip()
                if not value:
                    value = 'None'
                balcony_lst.append(value)
                # print(value)
            except Exception as e:
                print("Couldn't grab balconyNum!")
                value = 'None'
                balcony_lst.append(value)
            # ------------------------------------------------------------------------------------------------------------
            try:
                value = driver_inner_page.find_element(By.XPATH, "//span[@id='superbuiltupArea_span']")
                value = str(value.text).strip()
                if not value:
                    value = 'None'
                # print(value)
                superBuiltUp_area_lst.append(value)
            except Exception as e:
                value = 'None'
                superBuiltUp_area_lst.append(value)
                print("Couldn't grab superbuiltupArea_span!")
            # ------------------------------------------------------------------------------------------------------------

            try:
                value = driver_inner_page.find_element(By.XPATH, "//span[@id='carpetArea_span']")
                value = str(value.text).strip()
                if not value:
                    value = 'None'
                carpet_area_lst.append(value)
                # print(value)
            except Exception as e:
                print("Couldn't grab carpetArea_span!")
                value = 'None'
                carpet_area_lst.append(value)
            # ------------------------------------------------------------------------------------------------------------
            try:
                value = driver_inner_page.find_element(By.XPATH, "//tbody/tr[2]/td[2]/div[2]")
                value = str(value.text).strip()
                if not value:
                    value = 'None'
                address_lst.append(value)
                # print(value)
            except Exception as e:
                print("Couldn't grab address!")
                value = 'None'
                address_lst.append(value)
            # ------------------------------------------------------------------------------------------------------------
            try:
                value = driver_inner_page.find_element(By.XPATH, "//span[@id='availableForLabel']")
                value = str(value.text).strip()
                if not value:
                    value = 'None'
                available_for_lst.append(value)
                # print(value)
            except Exception as e:
                print("Couldn't grab available_for!")
                value = 'None'
                available_for_lst.append(value)
            # ------------------------------------------------------------------------------------------------------------
            try:
                value = driver_inner_page.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/table[1]/tbody[1]/tr[4]/td[1]/div[2]")
                value = str(value.text).strip()
                if not value:
                    value = 'None'
                available_from_lst.append(value)
                # print(value)
            except Exception as e:
                print("Couldn't grab available_from!")
                value = 'None'
                available_from_lst.append(value)
            # ------------------------------------------------------------------------------------------------------------
            try:
                value = driver_inner_page.find_element(By.XPATH, "//span[@id='postedOnAndByLabel']")
                value = str(value.text).strip()
                if not value:
                    value = 'None'
                Posted_By_and_On_lst.append(value)
                # print(value)
            except Exception as e:
                print("Couldn't grab Posted_By_and_On!")
                value = 'None'
                Posted_By_and_On_lst.append(value)
            # ------------------------------------------------------------------------------------------------------------
            try:
                value = driver_inner_page.find_element(By.XPATH, "//span[@id='Flooring_Label']")
                value = str(value.text).strip()
                if not value:
                    value = 'None'
                Flooring_lst.append(value)
                # print(value)
            except Exception as e:
                print("Couldn't grab Flooring!")
                value = 'None'
                Flooring_lst.append(value)
            # ------------------------------------------------------------------------------------------------------------
            try:
                value = driver_inner_page.find_element(By.XPATH, "//span[@id='Floor_Num_Label']")
                value = str(value.text).strip()
                if not value:
                    value = 'None'
                Floor_Number_lst.append(value)
                # print(value)
            except Exception as e:
                print("Couldn't grab Floor_Number!")
                value = 'None'
                Floor_Number_lst.append(value)
            # ------------------------------------------------------------------------------------------------------------
            try:
                value = driver_inner_page.find_element(By.XPATH, "//span[@id='Powerbackup_Label']")
                value = str(value.text).strip()
                if not value:
                    value = 'None'
                Power_Backup_lst.append(value)
                # print(value)
            except Exception as e:
                print("Couldn't grab Power_Backup!")
                value = 'None'
                Power_Backup_lst.append(value)
            # ------------------------------------------------------------------------------------------------------------
            try:
                value = driver_inner_page.find_element(By.XPATH, "//span[@id='Age_Label']")
                value = str(value.text).strip()
                if not value:
                    value = 'None'
                Property_Age_lst.append(value)
                # print(value)
            except Exception as e:
                print("Couldn't grab Property_Age!")
                value = 'None'
                Property_Age_lst.append(value)
            # ------------------------------------------------------------------------------------------------------------
            try:
                value = driver_inner_page.find_element(By.XPATH, "//span[@id='noticeDuration']")
                value = str(value.text).strip()
                if not value:
                    value = 'None'
                Months_of_Notice_lst.append(value)
                # print(value)
            except Exception as e:
                print("Couldn't grab Months_of_Notice!")
                value = 'None'
                Months_of_Notice_lst.append(value)
            # ------------------------------------------------------------------------------------------------------------
            try:
                value = driver_inner_page.find_element(By.XPATH, "//span[@id='Gated_community']")
                value = str(value.text).strip()
                if not value:
                    value = 'None'
                Gated_Community_lst.append(value)
                # print(value)
            except Exception as e:
                print("Couldn't grab Gated_Community!")
                value = 'None'
                Gated_Community_lst.append(value)
            # ------------------------------------------------------------------------------------------------------------
            try:
                value = driver_inner_page.find_element(By.XPATH, "//span[@id='electricityWaterCharges']")
                value = str(value.text).strip()
                if not value:
                    value = 'None'
                Electricity_n_Water_Charges_lst.append(value)
                # print(value)
            except Exception as e:
                print("Couldn't grab Electricity_n_Water_Charges!")
                value = 'None'
                Electricity_n_Water_Charges_lst.append(value)
            # ------------------------------------------------------------------------------------------------------------
            try:
                value = driver_inner_page.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[4]/div[4]/ul[1]")
                value.find_elements(By.TAG_NAME, "div")
                value = value.text
                if not value:
                    value = 'None'
                property_features_lst.append(value)
                # print(value)
            except Exception as e:
                print("Couldn't grab property_features!")
                value = 'None'
                property_features_lst.append(value)
            # ------------------------------------------------------------------------------------------------------------
            # moving to Explore_Locality tab
            try:
                driver_inner_page.execute_script("window.scrollBy(0, 1000);")
                value = driver_inner_page.find_element(By.XPATH, "//li[@id='localityInsightsTab']").click()
                # grabbing rating_features
                try:
                    value = driver_inner_page.find_element(By.XPATH, "//div[@class='review__wrapComp review__frontLayer pageComponent review__desktopWrap']")
                    value = value.find_element(By.XPATH, "//div[@class='display_l_semiBold']")
                    value = value.text
                    if not value:
                        value = 'None'
                    avg_rating_lst.append(value)
                    # print(value)
                except Exception as e:
                    print("Couldn't grab avg_rating!")
                    value = 'None'
                    avg_rating_lst.append(value)
            except Exception as e:
                print("Couldn't locate rating element!")
                value = 'None'
                avg_rating_lst.append(value)
            # ------------------------------------------------------------------------------------------------------------

            driver_inner_page.quit()

        driver.quit()
        print(f"""lengths of columns are: 
                    society_name_lst:{len(society_name_lst)}
                    property_title_lst:{len(property_title_lst)}
                    property_rent_lst:{len(property_rent_lst)}
                    types_of_rooms_available_lst:{len(types_of_rooms_available_lst)}
                    furnishing_details_lst:{len(furnishing_details_lst)}
                    bedroom_lst:{len(bedroom_lst)}
                    bathroom_lst:{len(bathroom_lst)}
                    balcony_lst:{len(balcony_lst)}
                    superBuiltUp_area_lst:{len(superBuiltUp_area_lst)}
                    address_lst:{len(address_lst)}
                    carpet_area_lst:{len(carpet_area_lst)}
                    available_for_lst:{len(available_for_lst)}
                    furnishing_type_lst:{len(furnishing_type_lst)}
                    available_from_lst:{len(available_from_lst)}
                    Posted_By_and_On_lst:{len(Posted_By_and_On_lst)}
                    Flooring_lst:{len(Flooring_lst)}
                    Floor_Number_lst:{len(Floor_Number_lst)}
                    Power_Backup_lst:{len(Power_Backup_lst)}
                    Property_Age_lst:{len(Property_Age_lst)}
                    Months_of_Notice_lst:{len(Months_of_Notice_lst)}
                    Gated_Community_lst:{len(Gated_Community_lst)}
                    Electricity_n_Water_Charges_lst:{len(Electricity_n_Water_Charges_lst)}
                    property_features_lst:{len(property_features_lst)}
                    avg_rating_lst:{len(avg_rating_lst)}
                """)
        dataframe = pd.DataFrame({'society_name':society_name_lst,
                     'property_title':property_title_lst,
                     'property_rent':property_rent_lst,
                     'types_of_rooms_available':types_of_rooms_available_lst,
                     'furnishing_details_lst':furnishing_details_lst,
                     'bedroom_count':bedroom_lst,
                     'bathroom_count':bathroom_lst,
                     'balcony_count':balcony_lst,
                     'superBuiltUp_area_sqft':superBuiltUp_area_lst,
                     'carpet_area_sqft':carpet_area_lst,
                     'address_lst':address_lst,
                     'available_for':available_for_lst,
                     'furnishing_type':furnishing_type_lst,
                     'available_from':available_from_lst,
                     'Posted_By_and_On':Posted_By_and_On_lst,
                     'Flooring':Flooring_lst,
                     'Floor_Number':Floor_Number_lst,
                     'Power_Backup':Power_Backup_lst,
                     'Property_Age':Property_Age_lst,
                     'Months_of_Notice':Months_of_Notice_lst,
                     'Gated_Community':Gated_Community_lst,
                     'Electricity_n_Water_Charges':Electricity_n_Water_Charges_lst,
                     'property_features':property_features_lst,
                     'avg_rating':avg_rating_lst,
                     })
        dataframe.to_csv(f"F:/Github_dsc/HousePrice_MegaProject/1. data_gathering/data/{page}.csv")
    return dataframe
  
if __name__ == "__main__":
    # creating processes 
    # Crawl_over_all_pages('indore', 7, 7) # 1-49
    p1 = multiprocessing.Process(target=Crawl_over_all_pages, args=('indore', 20, 21)) 
    p2 = multiprocessing.Process(target=Crawl_over_all_pages, args=('indore', 22, 23)) 
  
    # starting process 1 
    start_time = time.time()
    p1.start() 
    # starting process 2 
    p2.start() 
  
    # wait until process 1 is finished 
    p1.join() 
    # wait until process 2 is finished 
    p2.join() 
    
    end_time = time.time()
    # both processes finished 
    print(f"Done in {end_time-start_time} seconds") 