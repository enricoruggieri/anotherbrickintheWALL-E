from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())

## INSIRA AQUI A DATA DE SEXTA
data1 = "17/09/2021"

## INSIRA AQUI A DATA DE QUARTA
data2 = "22/09/2021"

browser.get("http://wae.gurisantamarcelina.org.br:8090/waeweb/servlet/hwplgn?1")
username = browser.find_element_by_id("vUSUARIO")
password = browser.find_element_by_id("vSENHA")
##COLOQUE SEU USUARIO E SENHA DENTRO DAS ASPAS
username.send_keys("")
password.send_keys("")
browser.find_element_by_id("BTNOK").click()

browser.implicitly_wait(3)

browser.find_element_by_xpath("//select[@name='vANOPER']").click()
ano_select = Select(browser.find_element_by_xpath("//select[@name='vANOPER']"))  # get element by name or id or xpath
browser.implicitly_wait(3)
ano_select.select_by_index('3')
browser.implicitly_wait(1)

browser.get("http://wae.gurisantamarcelina.org.br:8090/waeweb/servlet/hnwpdid1")

##aqui é necessário adaptar para o link
browser.get("http://wae.gurisantamarcelina.org.br:8090/waeweb/servlet/hnwpdidb?09CT1ATE01++++++++++0,SEQ+1+CORAL+09H00+%2F+TEORIA+09H00+6%C2%AAF+A,TEORIA+MUSICAL+I")

##CHEGUEI ATE O DIARIO
## aqui foi o pior lugar, fiquei um tempão e ainda não consegui resolver esse bug
## o input é pra colocar a data dentro do calendario
## se vc clicar em cima do calendario enquanto o codigo roda costuma dar certo

inputElement = browser.find_element_by_id("vMPDDAT")
inputElement.clear()
inputElement.click()
inputElement.click()
browser.implicitly_wait(3)

for i in range (100):
    inputElement.click()
    browser.find_element_by_id("vMPDDAT_dp_trigger").click()
    inputElement.click()
    inputElement.send_keys('01/09/2021')
    i=i+1

for i in range (100):
    inputElement.click()
    inputElement.click()
    inputElement.click()
    inputElement.send_keys('01/09/2021')
    i=i+1
    


browser.implicitly_wait(3)
browser.find_element_by_id("SEARCHBUTTON").click()
browser.find_element_by_xpath("//a[normalize-space()='%s']" % str(data1)).click()

browser.implicitly_wait(10)

###FINALMENTE
inputText = browser.find_element_by_xpath("//textarea[@name='vTCROBS']")
inputText.click()
inputText.send_keys('.')

from selenium.common.exceptions import NoSuchElementException

for i in range(200):
    str_a = str(i+2).zfill(4)
    bla = "vMPDPRE1_"+str_a
    
    try: 
        checkbox = browser.find_element_by_xpath("//input[@name='%s']" % str(bla))
        if checkbox.is_selected():
            checkbox.click()
            i=i+1
        else:
            i=i+1
            
    except NoSuchElementException:  
        browser.find_element_by_id("BTNSALVAR").click()
        break
    
### segundo
browser.implicitly_wait(10)
browser.find_element_by_id("vUPDATE_0002").click()
browser.implicitly_wait(3)
browser.find_element_by_xpath("//a[normalize-space()='%s']" % str(data1)).click()

inputText = browser.find_element_by_xpath("//textarea[@name='vTCROBS']")
inputText.click()
inputText.send_keys('.')

for i in range(200):
    str_a = str(i+2).zfill(4)
    bla = "vMPDPRE1_"+str_a
    
    try: 
        checkbox = browser.find_element_by_xpath("//input[@name='%s']" % str(bla))
        if checkbox.is_selected():
            checkbox.click()
            i=i+1
        else:
            i=i+1
            
    except NoSuchElementException:  
        browser.find_element_by_id("BTNSALVAR").click()
        break
        
### terceiro
browser.implicitly_wait(20)
browser.find_element_by_id("vUPDATE_0003").click()
browser.implicitly_wait(3)
browser.find_element_by_xpath("//a[normalize-space()='%s']" % str(data1)).click()

inputText = browser.find_element_by_xpath("//textarea[@name='vTCROBS']")
inputText.click()
inputText.send_keys('.')

for i in range(200):
    str_a = str(i+2).zfill(4)
    bla = "vMPDPRE1_"+str_a
    
    try: 
        checkbox = browser.find_element_by_xpath("//input[@name='%s']" % str(bla))
        if checkbox.is_selected():
            checkbox.click()
            i=i+1
        else:
            i=i+1
            
    except NoSuchElementException:  
        browser.find_element_by_id("BTNSALVAR").click()
        break
        
### quarto
browser.implicitly_wait(20)
browser.find_element_by_id("vUPDATE_0004").click()
browser.implicitly_wait(3)
browser.find_element_by_xpath("//a[normalize-space()='%s']" % str(data1)).click()

inputText = browser.find_element_by_xpath("//textarea[@name='vTCROBS']")
inputText.click()
inputText.send_keys('.')

for i in range(200):
    str_a = str(i+2).zfill(4)
    bla = "vMPDPRE1_"+str_a
    
    try: 
        checkbox = browser.find_element_by_xpath("//input[@name='%s']" % str(bla))
        if checkbox.is_selected():
            checkbox.click()
            i=i+1
        else:
            i=i+1
            
    except NoSuchElementException:  
        browser.find_element_by_id("BTNSALVAR").click()
        break
        
### quinto
browser.implicitly_wait(20)
browser.find_element_by_id("vUPDATE_0005").click()
browser.implicitly_wait(3)
browser.find_element_by_xpath("//a[normalize-space()='%s']" % str(data1)).click()

inputText = browser.find_element_by_xpath("//textarea[@name='vTCROBS']")
inputText.click()
inputText.send_keys('.')

for i in range(200):
    str_a = str(i+2).zfill(4)
    bla = "vMPDPRE1_"+str_a
    
    try: 
        checkbox = browser.find_element_by_xpath("//input[@name='%s']" % str(bla))
        if checkbox.is_selected():
            checkbox.click()
            i=i+1
        else:
            i=i+1
            
    except NoSuchElementException:  
        browser.find_element_by_id("BTNSALVAR").click()
        break
        
### sexto
browser.implicitly_wait(20)
browser.find_element_by_id("vUPDATE_0006").click()
browser.implicitly_wait(3)
browser.find_element_by_xpath("//a[normalize-space()='%s']" % str(data1)).click()

inputText = browser.find_element_by_xpath("//textarea[@name='vTCROBS']")
inputText.click()
inputText.send_keys('.')

for i in range(200):
    str_a = str(i+2).zfill(4)
    bla = "vMPDPRE1_"+str_a
    
    try: 
        checkbox = browser.find_element_by_xpath("//input[@name='%s']" % str(bla))
        if checkbox.is_selected():
            checkbox.click()
            i=i+1
        else:
            i=i+1
            
    except NoSuchElementException:  
        browser.find_element_by_id("BTNSALVAR").click()
        break
        
### setimo
browser.implicitly_wait(20)
browser.find_element_by_id("vUPDATE_0007").click()
browser.implicitly_wait(3)
browser.find_element_by_xpath("//a[normalize-space()='%s']" % str(data2)).click()

inputText = browser.find_element_by_xpath("//textarea[@name='vTCROBS']")
inputText.click()
inputText.send_keys('.')

for i in range(200):
    str_a = str(i+2).zfill(4)
    bla = "vMPDPRE1_"+str_a
    
    try: 
        checkbox = browser.find_element_by_xpath("//input[@name='%s']" % str(bla))
        if checkbox.is_selected():
            checkbox.click()
            i=i+1
        else:
            i=i+1
            
    except NoSuchElementException:  
        browser.find_element_by_id("BTNSALVAR").click()
        break
        
### oitavo
browser.implicitly_wait(20)
browser.find_element_by_id("vUPDATE_0008").click()
browser.implicitly_wait(3)
browser.find_element_by_xpath("//a[normalize-space()='%s']" % str(data2)).click()

inputText = browser.find_element_by_xpath("//textarea[@name='vTCROBS']")
inputText.click()
inputText.send_keys('.')

for i in range(200):
    str_a = str(i+2).zfill(4)
    bla = "vMPDPRE1_"+str_a
    
    try: 
        checkbox = browser.find_element_by_xpath("//input[@name='%s']" % str(bla))
        if checkbox.is_selected():
            checkbox.click()
            i=i+1
        else:
            i=i+1
            
    except NoSuchElementException:  
        browser.find_element_by_id("BTNSALVAR").click()
        break
        
### nono
browser.implicitly_wait(20)
browser.find_element_by_id("vUPDATE_0009").click()
browser.implicitly_wait(3)
browser.find_element_by_xpath("//a[normalize-space()='%s']" % str(data2)).click()

inputText = browser.find_element_by_xpath("//textarea[@name='vTCROBS']")
inputText.click()
inputText.send_keys('.')

for i in range(200):
    str_a = str(i+2).zfill(4)
    bla = "vMPDPRE1_"+str_a
    
    try: 
        checkbox = browser.find_element_by_xpath("//input[@name='%s']" % str(bla))
        if checkbox.is_selected():
            checkbox.click()
            i=i+1
        else:
            i=i+1
            
    except NoSuchElementException:  
        browser.find_element_by_id("BTNSALVAR").click()
        break
        
### decimo
browser.implicitly_wait(20)
browser.find_element_by_id("vUPDATE_0010").click()
browser.implicitly_wait(3)
browser.find_element_by_xpath("//a[normalize-space()='%s']" % str(data2)).click()

inputText = browser.find_element_by_xpath("//textarea[@name='vTCROBS']")
inputText.click()
inputText.send_keys('.')

for i in range(200):
    str_a = str(i+2).zfill(4)
    bla = "vMPDPRE1_"+str_a
    
    try: 
        checkbox = browser.find_element_by_xpath("//input[@name='%s']" % str(bla))
        if checkbox.is_selected():
            checkbox.click()
            i=i+1
        else:
            i=i+1
            
    except NoSuchElementException:  
        browser.find_element_by_id("BTNSALVAR").click()
        break
        
### decimo primeiro
browser.implicitly_wait(20)
browser.find_element_by_id("vUPDATE_0011").click()
browser.implicitly_wait(3)
browser.find_element_by_xpath("//a[normalize-space()='%s']" % str(data2)).click()

inputText = browser.find_element_by_xpath("//textarea[@name='vTCROBS']")
inputText.click()
inputText.send_keys('.')

for i in range(200):
    str_a = str(i+2).zfill(4)
    bla = "vMPDPRE1_"+str_a
    
    try: 
        checkbox = browser.find_element_by_xpath("//input[@name='%s']" % str(bla))
        if checkbox.is_selected():
            checkbox.click()
            i=i+1
        else:
            i=i+1
            
    except NoSuchElementException:  
        browser.find_element_by_id("BTNSALVAR").click()
        break

