import pyqrcode

s = "IT'S ME SUDHI"
url = pyqrcode.create(s)
# url.svg("myqrcode.svg",scale=8)
url.png("myqrcode.png",scale=8)
