import os
import re
import time

from selenium import webdriver


class Scraper:
    dirname = os.path.dirname(__file__)
    exec_path = os.path.join(dirname, "Driver/chromedriver")
    os.environ["webdriver.chrome.driver"] = exec_path

    def __init__(self, url="https://app2.agenda.ch/widget?company_id=7011&locale=fr"):
        self.url = url
        self.browser = self.set_brower()
        self.button_xpath = "/html/body/div/div/div/div[2]/div[2]/div[3]/div/div[2]/div/div/div[2]/div[2]/a"
        self.text_xpath = (
            "/html/body/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[2]/h4"
        )

    def set_brower(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("useAutomationExtension", False)
        chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])

        return webdriver.Chrome(options=chrome_options, executable_path=self.exec_path)

    def launch_browser(self):
        self.browser.get(self.url)
        self.browser.maximize_window()
        self.browser.implicitly_wait(20)

    def press_button(self):
        button = self.browser.find_element_by_xpath(self.button_xpath)
        button.click()

    def read_text(self):
        read = self.browser.find_element_by_xpath(self.text_xpath)
        return read.text

    def reload_browser(self):
        self.browser.refresh()

    def play_noise(self):
        # On windows uses winsound (https://stackoverflow.com/questions/16573051/sound-alarm-when-code-finishes)
        os.system("".join(["afplay ", self.dirname, "/data/alarm.wav"]))

    def run(self):
        self.launch_browser()
        self.press_button()
        while True:
            self.reload_browser()

            # May not be necessary for the website you want to scrap
            self.press_button()
            txt = self.read_text()
            print(txt)
            txt_list = re.findall(r"(\w+)", txt)

            # Change these conditions for your use
            if (int(txt_list[1]) < 25 and txt_list[2] == "JUIN") or (
                txt_list[2] == "MAI"
            ):
                self.play_noise()
                return txt
            else:
                # Avoid overloading the server
                time.sleep(20)


if __name__ == "__main__":
    s = Scraper()
    s.run()
