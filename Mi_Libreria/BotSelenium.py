from selenium import webdriver #importo la libreria de selenium
from selenium.webdriver.common.by import By
#from selenium.webdriver.edge.options import Options
#from selenium.webdriver.edge.service import Service as EdgeService
#from webdriver_manager.edge import GeckoDriverManager

from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
#from webdriver_setup import get_webdriver_for

#opts.add_argument("user-agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, Like Gecko) Chrome/97.0.4692.99 Safari/537.36")

opts = Options()
opts.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36")
url='https://www.google.com'
service = FirefoxService(executable_path=GeckoDriverManager().install()) 
#driver = get_webdriver_for("chrome", desired_capabilities=capabilities, options=opts)
#opts.binary_location='HKEY_LOCAL_MACHINE\SOFTWARE\Mozilla\Mozilla Firefox\[VERSION]\Main\PathToExe'
#driver = webdriver.Firefox(service= service,options=opts)
driver = webdriver.Remote(
    command_executor='http://0.0.0.0:4444/wd/hub',
    options=opts)
#driver = webdriver.Chrome(service= service, desired_capabilities=capabilities, options=opts)
#driver = webdriver.Chrome(service= service, chrome_options=opts)
#driver = webdriver.Chrome(ChromeDriverManager().install())
#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=opts)
#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#driver = webdriver.Chrome(ChromeDriverManager().install())
#self.driver =webdriver.Chrome(service=Service('chromedriver.exe'),options=opts)
driver.get(url)

#options = webdriver.ChromeOptions()
#options.add_experimental_option('androidPackage', 'com.android.chrome')
#driver = webdriver.Chrome('/chromedriver', options=options)
#driver =webdriver.Chrome('./chromedriver',options=opts)
#driver =webdriver.Chrome('chromedriver',options=opts)
#driver = chromedriver_instance.driver
#driver.get('https://google.com')

#defino mis datos de ingreso
numFactura="4138574"
digitoVer="0"

#ubico los input de los campos 
input_user=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'input[@name="client"]')))

input_user=driver.find_element(By.XPATH,'input[@name="client"]')
input_dig=driver.find_element(By.XPATH,'input[@name="digito"]')

#ingreso mis datos en los input
input_user.send_keys(numFactura)
input_user.send_keys(digitoVer)

boton=driver.find_element(By.XPATH,'input[@id="solicitar"]')
boton.click()