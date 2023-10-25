from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from time import sleep

# URL used in this automation
url = "https://ri.magazineluiza.com.br/#"
browser = Firefox()

# Navigate to the Website
browser.get(url)
# Required wait to load page
sleep(1)

# Close first pop-up
browser.find_element(By.XPATH, "/html/body/form/div[3]/div/div/div/div/div/div/div[1]/a/img").click()
# Click in "Informações aos Acionistas"
browser.find_element(By.XPATH, "/html/body/form/header/div/div/div/div[2]/ul/li[4]/a").click()
# Required to wait the click above
sleep(0.5)
# Click in "Planilha de Resultado"
browser.find_element(By.XPATH, "/html/body/form/div[10]/div/div/div/div/ul[3]/li[2]/a").click()
# Download the Excel Archive with the results
browser.find_element(By.XPATH, '//*[@id="NS503pmpo+N63mNM4SoDKw=="]').click()
# Required wait to initiate the download
sleep(0.5)

# Close the browser after download
browser.quit()
