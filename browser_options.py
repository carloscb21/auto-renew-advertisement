from selenium.webdriver.chrome.options import Options
from sys import platform


class UnsupportedPlatform(Exception):
    pass


class FifaSetup:
    options: Options
    web_home_path: str
    driver_path: str


def get_basic_setup() -> FifaSetup:
    fifa_setup = FifaSetup()
    if "linux" in platform:
        print("linux")
        options = Options()
        options.accept_untrusted_certs = True
        options.assume_untrusted_cert_issuer = True
        fifa_setup.options = options
        fifa_setup.web_home_path = "/static/index.html"
        fifa_setup.driver_path = "/binary/linux/chromedriver"
    elif "darwin" in platform:
        print("mac")
        options = Options()
        options.accept_untrusted_certs = True
        options.assume_untrusted_cert_issuer = True
        fifa_setup.options = options
        fifa_setup.web_home_path = "/static/index.html"
        fifa_setup.driver_path = "/binary/mac/chromedriver"
    elif "win" in platform:
        print("windows")
        options = Options()
        options.accept_untrusted_certs = True
        options.assume_untrusted_cert_issuer = True
        options.add_argument("--user-data-dir=/home/carlos/.config/google-chrome/Default")
        fifa_setup.options = options
        fifa_setup.web_home_path = "\\static\\index.html"
        fifa_setup.driver_path = "\\binary\\windows\\chromedriver.exe"
    else:
        raise UnsupportedPlatform

    return fifa_setup
