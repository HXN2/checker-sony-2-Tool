import os

import time 

import webbrowser

import requests

url = "https://t.me/HEXiN1K"

webbrowser.open(url)

import socket

name = socket.gethostname()

print("\n===========================================================")

print("\n                    Hello sir " +name) 

print("\n===========================================================")

lib = input("""

\n  من صنع هيكسن انستجرام @hxn_here

\n  BY HeXiN INSTA @hxn_here

\n  tarafından yapılmış HeXiN Instagram @hxn_here

\n

===========================================================

\n   من صنع هيكسن تيليجرام @HEXiN 

\n  BY HEXiN TELeGRaM @HEXiN1K

\n  Bir telgraf HEXiN oluşturun @HEXiN1K

\n ===========================================================

 

 [1] DOWNLOAD LiP & UPDATE . تنزيل وتحديث المكاتب

\n [2] SKiP DOWNLOAD & UPDATE LiP . تخطي تنزيل وتحديث المكاتب 

\n [+] Please Choice >> """)

if lib == "1":

    try:

        os.system('pip install requests')

        os.system('pip install webbrowser')

        os.system('pip install random')       

        os.system('pip install os')

        os.system('pip install socket')

        os.system('cls' if os.name == 'nt' else 'clear')

        pass

    except:

        pass

else:

    os.system('cls' if os.name == 'nt' else 'clear')

    pass

os.system("clear")

import requests

import socket

print("""

  _    ___   ___   _

 | |  | \ \ / / \ | |

 | |__| |\ V /|  \| |

 |  __  | > < | . ` |

 | |  | |/ . \| |\  |

 |_|  |_/_/ \_\_| \_|

  _____   _____ _   _

 |  __ \ / ____| \ | |

 | |__) | (___ |  \| |

 |  ___/ \___ \| . ` |

 | |     ____) | |\  |

 |_|    |_____/|_| \_|

""")

S = input ("""

 [1] CHK without File تشيكر بدون ملف

 [2] CHK with file تشيكر بملف

 [+] Please Choose: """)

if S =='1':

  os.system('clear')

  import requests

  print("""

  

   _____ _          _

  / ____| |        | |

 | |    | |__   ___| | ___ __

 | |    | '_ \ / _ \ |/ / '__|

 | |____| | | |  __/   <| |

  \_____|_| |_|\___|_|\_\_|

  """)

  

  username = input("\n\n [+] Enter Username =>> : ")

  url = 'https://accounts.api.playstation.com/api/v1/accounts/onlineIds'

  headers = {

  'Accept': '*/*',

  'Accept-Encoding': 'gzip, deflate, br',

  'Accept-Language': 'ar,en-US;q=0.9,en;q=0.8',

  'Cache-Control': 'no-cache',

  'Connection': 'keep-alive',

  'Content-Length': '48',

  'Content-Type': 'application/json; charset=UTF-8',

  'Host': 'accounts.api.playstation.com',

  'Origin': 'https://id.sonyentertainmentnetwork.com',

  'Pragma': 'no-cache',

  'Referer': 'https://id.sonyentertainmentnetwork.com/',

  'Sec-Fetch-Dest': 'empty',

  'Sec-Fetch-Mode': 'cors',

  'Sec-Fetch-Site': 'cross-site',

  'sec-gpc': '1',

  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.81 Safari/537.36',

  }

  data = {

  'onlineId': username,

  'reserveIfAvailable': False

  }

  req = requests.post(url,  json=data,  headers=headers).text

  if '"message":"Account with this online id already exists.' in req:

        print(f' [-] Username Taken =>> : {username}')

  else:

       print(f' [+]Username Available =>> : {username}')

if S =='2':

  os.system('clear')

  import requests

  print("""

   _____ _          _

  / ____| |        | |

 | |    | |__   ___| | ___ __

 | |    | '_ \ / _ \ |/ / '__|

 | |____| | | |  __/   <| |

  \_____|_| |_|\___|_|\_\_|

  ______ _____ _      ______

 |  ____|_   _| |    |  ____|

 | |__    | | | |    | |__

 |  __|   | | | |    |  __|

 | |     _| |_| |____| |____

 |_|    |_____|______|______|

  """)

  username = input("\n [+] Enter File To CHK USER =>> : ")

  ff = username

  file = open(ff).read().splitlines

  for file in file:

    url = 'https://accounts.api.playstation.com/api/v1/accounts/onlineIds'

  headers = {

  'Accept': '*/*',

  'Accept-Encoding': 'gzip, deflate, br',

  'Accept-Language': 'ar,en-US;q=0.9,en;q=0.8',

  'Cache-Control': 'no-cache',

  'Connection': 'keep-alive',

  'Content-Length': '48',

  'Content-Type': 'application/json; charset=UTF-8',

  'Host': 'accounts.api.playstation.com',

  'Origin': 'https://id.sonyentertainmentnetwork.com',

  'Pragma': 'no-cache',

  'Referer': 'https://id.sonyentertainmentnetwork.com/',

  'Sec-Fetch-Dest': 'empty',

  'Sec-Fetch-Mode': 'cors',

  'Sec-Fetch-Site': 'cross-site',

  'sec-gpc': '1',

  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.81 Safari/537.36',

  }

data = {

'onlineId': username,

'reserveIfAvailable': False

}

req = requests.post(url,  json=data,  headers=headers).text

if '"message":"Account with this online id already exists.' in req:

  print(f' [-] Username Taken =>> : {username}')

else:

  print(f' [+]Username Available =>> : {username}')

  

url = "https://www.instagram.com/hxn_here/"

webbrowser.open(url)

name = socket.gethostname()

print("\n===========================================================")

print("\n                    Bye sir " +name) 

print("\n===========================================================")

