from selenium import webdriver #importo la libreria de selenium
#import chromedriver_binary 
from selenium.webdriver.chrome.options import Options
#from autotest_lib.client.common_lib.cros import chromedriver
from selenium.common.exceptions import NoSuchElementException,StaleElementReferenceException,TimeoutException,ElementClickInterceptedException


from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

opts = Options()
opts.binary_location = "Mi_Libreria/chromedriver"
opts.add_argument("user-agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, Like Gecko) Chrome/97.0.4692.99 Safari/537.36")

service = ChromeService(executable_path=ChromeDriverManager().install())

driver = webdriver.Chrome(service= service, options=opts)
#driver = webdriver.Chrome(ChromeDriverManager().install())
#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=opts)
#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#driver = webdriver.Chrome(ChromeDriverManager().install())
#self.driver =webdriver.Chrome(service=Service('chromedriver.exe'),options=opts)
driver.get('https://www.enel.com.co/es/reporte-de-fallas.html?utm_id=7908&utm_source=google%20search%20-%20nacional&utm_medium=cpc&utm_campaign=enel%20colombia_rerporte-de-fallas-b2b_cli&utm_term=arte%20entretenimiento_anuncio%20de%20texto_na')





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