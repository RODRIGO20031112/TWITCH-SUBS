from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from pystyle import Colors, Colorate
import undetected_chromedriver as uc
from pharse import createPharse
from unidecode import unidecode
import requests
import random
import time

def geraNomeUsuario():
    url = "https://randomuser.me/api/?nat=br"
    response = requests.get(url)
    if response.ok:
        for result in response.json()["results"]:
            nome_completo = f"{result['name']['first']} {result['name']['last']}"
            nome_formatado = unidecode(nome_completo).lower().replace(" ", "")
            nome_truncado = nome_formatado
            return nome_truncado
    else:
        return f"Erro ao acessar a API: {response.status_code}"


def clickInTwitchButtonRegister(driver):
    xpath = (
        "/html/body/div[3]/div/div[1]/nav/div/div[3]/div[3]/div/div[1]/div[2]/button"
    )
    script = """
    var xpath = arguments[0];
    var button = document.evaluate(xpath, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
    if (button) {
        button.click();
    } else {
        console.error("Botão não encontrado");
    }
    """

    try:
        driver.execute_script(script, xpath)
        print(Colors.green, f"Status: ✔ ")
    except Exception as e:
        print(Colors.red, f"Status: X {e}")


def fillOutTwitchForm(driver):
    nome = f"{geraNomeUsuario()}{geraNomeUsuario()}"[:25]

    xpath_I = " /html/body/div[5]/div/div/div/div/div/div[1]/div/div/div/div[2]/form/div/div[4]/div[1]/div/div[1]/button/div/div"
    script_I = """
    var xpath = arguments[0];
    var button = document.evaluate(xpath, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
    if (button) {
        button.click();
    } else {
        console.error("Botão não encontrado");
    }
    """

    xpath_II = "/html/body/div[5]/div/div/div/div/div/div[1]/div/div/div/div[2]/form/div/div[4]/div/div/div[2]/div/input"
    texto_II = f"{nome}@gmail.com"

    xpath_III = "/html/body/div[5]/div/div/div/div/div/div[1]/div/div/div/div[2]/form/div/div[3]/div/div[2]/div[2]/div/select"


    xpath_IV = "/html/body/div[5]/div/div/div/div/div/div[1]/div/div/div/div[2]/form/div/div[3]/div/div[2]/div[3]/div/div/input"
    texto_IV = "2003"

    xpath_V = "/html/body/div[5]/div/div/div/div/div/div[1]/div/div/div/div[2]/form/div/div[3]/div/div[2]/div[1]/div/div/input"
    texto_V = "12"

    xpath_VI = "/html/body/div[5]/div/div/div/div/div/div[1]/div/div/div/div[2]/form/div/div[2]/div/div[2]/div[1]/div/input"
    texto_VI = "Og(O*+;3a1"

    xpath_VII = "/html/body/div[5]/div/div/div/div/div/div[1]/div/div/div/div[2]/form/div/div[1]/div/div[2]/div/input"
    texto_VII = nome

    xpath_VIII = "/html/body/div[5]/div/div/div/div/div/div[1]/div/div/div/div[2]/form/div/div[6]/div/button/div/div"

    try:
        time.sleep(5)
        driver.execute_script(script_I, xpath_I)
        print(Colors.green, f"Status: ✔ ")

        time.sleep(5)
        input_element = driver.find_element(By.XPATH, xpath_II)
        input_element.send_keys(texto_II)
        print(Colors.green, f"Status: ✔ ")

        time.sleep(5)
        dropdown_element = driver.find_element(By.XPATH, xpath_III)
        dropdown = Select(dropdown_element)
        dropdown.select_by_value("11")
        print(Colors.green, f"Status: ✔ ")

        time.sleep(5)
        input_element = driver.find_element(By.XPATH, xpath_IV)
        input_element.send_keys(texto_IV)
        print(Colors.green, f"Status: ✔ ")

        time.sleep(5)
        input_element = driver.find_element(By.XPATH, xpath_V)
        input_element.send_keys(texto_V)
        print(Colors.green, f"Status: ✔ ")

        time.sleep(5)
        input_element = driver.find_element(By.XPATH, xpath_VI)
        input_element.send_keys(texto_VI)
        print(Colors.green, f"Status: ✔ ")

        time.sleep(5)
        input_element = driver.find_element(By.XPATH, xpath_VII)
        input_element.send_keys(texto_VII)
        print(Colors.green, f"Status: ✔ ")

        time.sleep(5)
        input_element = driver.find_element(By.XPATH, xpath_VIII)
        input_element.click()
        print(Colors.green, f"Status: ✔ ")

    except Exception as e:
        print(Colors.red, f"Status: X {e}")


def selectRandom(proxy_servers):
    return random.choice(proxy_servers)


def main():
    print(createPharse())

    subs_text = input(
        Colorate.Vertical(Colors.blue_to_black, " Quantos seguidores deseja:  ")
    )
    subs = int(subs_text)

    chrome_options = uc.ChromeOptions()
    chrome_options.add_argument("--disable-logging")
    chrome_options.add_argument("--lang=en")
    chrome_options.add_argument("--log-level=3")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--mute-audio")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument(r"--user-data-dir=C:\Users\USER\AppData\Local\Google\Chrome\User Data")
    chrome_options.add_argument(r"--profile-directory=Profile 2")
    driver = uc.Chrome(options=chrome_options)

    proxy_servers = [
        "https://www.blockaway.net",
        "https://www.croxyproxy.com",
        "https://www.croxyproxy.rocks",
        "https://www.croxy.network",
        "https://www.croxy.org",
        "https://www.youtubeunblocked.live",
        "https://www.croxyproxy.net",
    ]

    for i in range(subs):
        random_proxy_url = selectRandom(proxy_servers)
        driver.execute_script("window.open('" + random_proxy_url + "')")
        driver.switch_to.window(driver.window_handles[-1])
        driver.get(random_proxy_url)
        text_box = driver.find_element(By.ID, "url")
        text_box.send_keys(f"www.twitch.tv")
        text_box.send_keys(Keys.RETURN)
        time.sleep(10)
        clickInTwitchButtonRegister(driver)
        time.sleep(10)
        fillOutTwitchForm(driver)
        time.sleep(10)


main()
