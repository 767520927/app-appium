from appium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

#豆果美食
cap={
  "platformName": "Android",
  "platformVersion": "4.4.2",
  "deviceName": "127.0.0.1:62001",
  "appPackage": "com.douguo.recipe",
  "appActivity": ".HomeActivity"
}

driver=webdriver.Remote('http://localhost:4723/wd/hub',cap)
driver.find_element_by_id("com.douguo.recipe:id/newking").click()
driver.find_element_by_id("com.douguo.recipe:id/tag_three_title").click()
t=driver.find_elements_by_id('com.douguo.recipe:id/recipe_list_item_name')
for e in t:
    print(e.text)
x=driver.get_window_size()['width']
y=driver.get_window_size()['height']
#滑动距离
x1=int(x*0.5)
y1=int(y*0.85) #起始位置
y2=int(y*0.25) #终止位置
driver.swipe(x1,y1,x1,y2,1000)
element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'com.douguo.recipe:id/recipe_list_item_name')))
print('++++++++')
tt=driver.find_elements_by_id('com.douguo.recipe:id/recipe_list_item_name')
for e in tt:
    print(e.text)


