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


# In[9]:


from selenium import JavascriptExecutor


# In[118]:


for i in range (200):
    str_a = str(i+2).zfill(4)
    bla = str("vMPDPRE1_"+str_a)
    print("browser.find_element_by_xpath(\"//input[@name=\'"+bla"]\").click()")
    #browser.find_element_by_xpath("//input[@name=bla]").click()
    #browser.implicitly_wait
    i=i+1


# In[ ]:


browser.find_element_by_xpath("//input[@name='vMPDPRE1_0003']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0004']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0005']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0006']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0007']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0008']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0009']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0010']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0011']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0012']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0013']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0014']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0015']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0016']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0017']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0018']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0019']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0020']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0021']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0022']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0023']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0024']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0025']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0026']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0027']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0028']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0029']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0030']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0031']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0032']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0033']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0034']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0035']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0036']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0037']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0038']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0039']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0040']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0041']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0042']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0043']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0044']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0045']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0046']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0047']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0048']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0049']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0050']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0051']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0052']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0053']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0054']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0055']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0056']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0057']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0058']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0059']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0060']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0061']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0062']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0063']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0064']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0065']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0066']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0067']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0068']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0069']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0070']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0071']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0072']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0073']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0074']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0075']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0076']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0077']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0078']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0079']").click()

browser.find_element_by_xpath("//input[@name='vMPDPRE1_0024']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0025']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0026']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0027']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0028']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0029']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0030']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0031']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0032']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0033']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0034']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0035']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0036']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0037']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0038']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0039']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0040']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0041']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0042']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0043']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0044']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0045']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0046']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0047']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0048']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0049']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0050']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0051']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0052']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0053']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0054']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0055']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0056']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0057']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0058']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0059']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0060']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0061']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0062']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0063']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0064']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0065']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0066']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0067']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0068']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0069']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0070']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0071']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0072']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0073']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0074']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0075']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0076']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0077']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0078']").click()
browser.find_element_by_xpath("//input[@name='vMPDPRE1_0079']").click()




