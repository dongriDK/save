from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
url = "https://portal.hannam.ac.kr/wps/index.jsp"
id = ""
pw = ""

options = Options()
options.add_argument('-allow-running-insecure-content')
prefs = {
    "profile.default_content_setting_values.plugins": 1,
    "profile.content_settings.plugin_whitelist.adobe-flash-player": 1,
    "profile.content_settings.exceptions.plugins.*,*.per_resource.adobe-flash-player": 1,
    "PluginsAllowedForUrls": "https://unihints.hannam.ac.kr/"
}

options.add_experimental_option("prefs",prefs)
#options.add_argument("-disable-features=EnableEphemeralFlashPermission");
driver = webdriver.Chrome(executable_path=r'\Chromedriver\chromedriver.exe', chrome_options=options)
driver.get(url)


driver.switch_to_frame('indexTop')

id_f = driver.find_element_by_name('userid')
id_f.clear()
id_f.send_keys(id)
pw_f = driver.find_element_by_name('password')
pw_f.clear()
pw_f.send_keys(pw)
driver.execute_script('loginClick()')


WebDriverWait(driver, 3).until(EC.alert_is_present())
alrt = driver.switch_to.alert
alrt.accept()

driver.execute_script("topMenuClick('https://unihints.hannam.ac.kr/haksa/main.jsp', '1', 'true')")

href_elem = driver.find_elements_by_xpath("//a[@*]")
