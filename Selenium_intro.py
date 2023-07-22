from selenium import webdriver
from selenium.webdriver.common.by import By


def test_eight_components():  # class teste
    driver = webdriver.Chrome()  # drive chamado do webDriver
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")  # site chamado do WebDriver

    title = driver.title  # chamado do titulo para saber se é a pagina mesmo
    assert title == "Web form"

    driver.implicitly_wait(5)  # pausa para o site carregar

    text_box = driver.find_element(by=By.NAME, value="my-text")  # procura do elemento por nome
    submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")  # procura do elemento por CSS_Selector

    text_box.send_keys("Selenium")  # clamado do elemento e envio das keys e click no botão
    submit_button.click()

    message = driver.find_element(by=By.ID, value="message")
    value = message.text
    assert value == "Received!"  # assert se os valores foram certos

    driver.quit()
