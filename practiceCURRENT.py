import time

# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://automation.credence.in/register")


#Registration page
# time.sleep(2)
# driver.find_element(By.ID,"name").send_keys("Tejas")
# driver.find_element(By.XPATH,"//input[@id='email']").send_keys("tejas.bhawsar009@gmail.com")
# driver.find_element(By.XPATH,"//*[@id='password']").send_keys("tejas1234")
# driver.find_element(By.XPATH,'//*[@id="password-confirm"]').send_keys("tejas1234")
# driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()

#Login page
# driver.find_element(By.XPATH,"//*[@id='navbar']/ul[2]/li[3]/a").click()
# time.sleep(2)
# driver.find_element(By.XPATH,"//input[@id='email']").send_keys("tejas.bhawsar009@gmail.com")
# driver.find_element(By.CSS_SELECTOR,"input[id='password']").send_keys("tejas1234")
# driver.find_element(By.XPATH,"/html/body/div/div/div/div/div[2]/form/div[4]/div/button").click()
#
# print("Title of page : ",driver.title)
# print("Url of page : ",driver.current_url)

# -------------------------------------------------------------------------------------------------------------

# CONDITIONAL STATEMENT--

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
# driver.get("https://seleniumbase.io/demo_page")
#
# print(driver.find_element(By.CSS_SELECTOR,"input[id='radioButton1']").is_selected())
# print(driver.find_element(By.CSS_SELECTOR,"input[id='radioButton2']").is_selected())

# is.displayed
# is_enabled

# -----------------------------------------------------------------------------------------------

# ALERT------

# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
#
# driver = webdriver.Chrome()
# driver.get("https://the-internet.herokuapp.com/javascript_alerts")
#
# driver.find_element(By.XPATH,"//*[@id='content']/div/ul/li[1]/button").click()
#
# driver.switch_to.alert.accept()
#
# Success = driver.find_element(By.XPATH,'//*[@id="result"]').text
# print(Success)
# -----------------------------------------------------------------------------------------
# # DROPDOWN___
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
#
# driver = webdriver.Chrome()
#
# driver.get("https://seleniumbase.io/demo_page")
#
# dropdn = Select(driver.find_element(By.XPATH,"//*[@id='mySelect']"))
# dropdn.select_by_index(2)
# dropdn.select_by_visible_text("Set to 100%")
# print("len of options are : ", len(dropdn.options))


### --Task to print all options visible text and value along with index
# for i in range(len(dropdn.options)):
#     dropdn.select_by_index(i)
#     print(f'Text is: {dropdn.options[i].text} Value is: {dropdn.options[i].get_attribute("value")}  index: {i} \n')

# ------------------------------------------------------------------------------------------------------------------------------

# for option in dropdn.options:
#     print(f'Text is: {option.text} Value is: {option.get_attribute("value")}  \n')
#     time.sleep(2)
# --------------------------------------------------------------------------------------------

## I want to print all links, visible text and href avaialable on we page

# links = driver.find_elements(By.CLASS_NAME,"linkClass")
# for i in links:
#     print(f' link is: {i.get_attribute("href")} visible text is: {i.text}')

# ----------------------------------------------------------------------------------------------------

# FRAME

#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
#
# driver = webdriver.Chrome()
#
# driver.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_alert")
#
# driver.switch_to.frame("iframeResult")
# driver.find_element(By.XPATH,"/html/body/button").click()
# driver.switch_to.alert.accept()

# ----------------------------------------------------------------------------------------------------------
# MULTPLE WINDOW HANDLE

# import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
#
# driver = webdriver.Chrome()
#
#  ## open website or url
# time.sleep(2)
# driver.get("file:///C:/Users/Admin/Desktop/credence practicals/python automation testing/Class/selenium/7th sept/MultipleWindowsOpening.html")
#
# driver.find_element(By.XPATH,"/html/body/div/a[4]").click()
# driver.find_element(By.XPATH,"/html/body/div/a[1]").click()
# driver.find_element(By.XPATH,"/html/body/div/a[3]").click()
#
# print("Current windows handle :",driver.current_window_handle)
# print("windows handles : ",driver.window_handles)
# time.sleep(2)
#
# driver.switch_to.window(driver.window_handles[0])
# time.sleep(2)
# driver.forward()
#
# driver.quit()

# ----------------------------------------------------------------------------------------------------------------------
# dropdown
import time
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.select import Select
#
# driver = webdriver.Chrome()
#
# driver.get("https://seleniumbase.io/demo_page")
#
# drpdown = Select(driver.find_element(By.ID,"mySelect"))
#
# for i in range(len(drpdown.options)):
#     drpdown.select_by_index(i)
#     print(f' visible text is: {drpdown.options[i].text} value is: {drpdown.options[i].get_attribute("value")} index is: {i} \n')

# -----------------------------------------------------------------------------------------------------------------------------
#WAITS

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.wait import WebDriverWait
#
# driver = webdriver.Chrome()
# driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
#
# driver.find_element(By.XPATH,"//*[@id='start']/button").click()
# loading = (By.XPATH,"//*[@id='loading']")
# elelocator = WebDriverWait(driver,10).until(expected_conditions.visibility_of_element_located(loading))
#
# text = driver.find_element(By.XPATH,'//*[@id="loading"]').text
# print(text)
# -------------------------------------------------------------------------
# drag and drop

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver import ActionChains
#
# driver = webdriver.Chrome()     # Creating class object of Chrome
# driver.get("http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
#
# drag_dropAct = ActionChains(driver)
#
# source = driver.find_element(By.XPATH,'//*[@id="box1"]')
# destination = driver.find_element(By.XPATH,'//*[@id="box101"]')
# drag_dropAct.drag_and_drop(source,destination).perform()

# -----------------------------------------------------------------------
# HOVER_ELEMENT

# import time
# from selenium import webdriver
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()     # Creating class object of Chrome
# driver.get("https://seleniumbase.io/demo_page")
#
# acton_perf = ActionChains(driver)
#
# hover_Options = driver.find_element(By.XPATH,'//*[@id="myDropdown"]')
# selected_opt = driver.find_element(By.XPATH,'//*[@id="dropOption3"]')
#
# acton_perf.move_to_element(hover_Options).move_to_element(selected_opt).click().perform()

# ------------------------------------------------------------------------------------------.
# TABLE_OPERATION

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver import ActionChains
#
# driver = webdriver.Chrome()
#
# driver.get("https://www.w3schools.com/html/html_tables.asp")
#
# # print(len(driver.find_elements(By.XPATH,'//*[@id="customers"]/tbody/tr')))
#
#  # 1. count number of rows and column.
#
# NoOfRows = len(driver.find_elements(By.XPATH, '//*[@id="customers"]/tbody/tr'))
# NoOfColumn = len(driver.find_elements(By.XPATH, '//*[@id="customers"]/tbody/tr[1]/th'))
#
#
# print("Number Of Rows : ", NoOfRows)
# print("Number Of column : ", NoOfColumn)
#
# # # 2. Read Specific Row And Column Data. -- Island Trading
#
# text = driver.find_element(By.XPATH,'//*[@id="customers"]/tbody/tr[3]/td[2]').text
# print(text)
#
# # 3. read all rows and column data
#
# for r in range(2,NoOfRows+1):
#     for c in range(1,NoOfColumn+1):
#         data = driver.find_element(By.XPATH,"//*[@id='customers']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
#         print(data,end=" : ")
#     print()


# ------------------------------------------------------------------------------------------------




