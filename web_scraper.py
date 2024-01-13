from bs4 import BeautifulSoup
import requests
import pandas as pd
import os
from time import sleep
import re



directory = r"C:\Users\Kamil\OneDrive\Inżynieria danych i Data Science\BMW-3-market_analysis_and_price_prediction\data\BMW3_data"


url_site = "https://www.otomoto.pl/osobowe/bmw/seria-3?page="


car_list = []

pages=1

def get_car_info(car_url):
    response_car = requests.get(car_url)
    soup_car = BeautifulSoup(response.text, features='html.parser')
    
    

for i in range(1, pages + 1):
    url = url_site + str(i)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, features='html.parser')
    
    car_list = soup.find('div', attrs={"class": "ooa-r53y0q ezh3mkl11"})
    
    for car in car_list.find_all("section", attrs={"class": "ooa-10gfd0w e1oqyyyi1"}):
        link = car.find('a', attrs={'href': re.compile("^https://")}).get("href")
        name = car.find("a").text
        
        if "otomoto.pl" not in link:
            continue
        
        print(link)

    
# <section class="ooa-10gfd0w e1oqyyyi1"><div class="ooa-1v0h837 e17vhtca1"><img class="e17vhtca4 ooa-2zzg2s" alt="" loading="eager" src="https://ireland.apollo.olxcdn.com/v1/files/eyJmbiI6IjhibWN1Mm81MHBneDEtT1RPTU9UT1BMIn0.KTaVrFFHZORd_Zl5f7wrvTnH0oS_0LtxJX4M_uiL830/image;s=320x240"></div><div class="ooa-1qo9a0p e1oqyyyi6"><h1 class="e1oqyyyi9 ooa-1ed90th er34gjf0"><a href="https://www.otomoto.pl/osobowe/oferta/bmw-seria-3-bmw-seria-3-e46-diesel-2-0-150km-209-tys-km-ID6G6Q20.html" target="_self" rel="noreferrer">BMW Seria 3 320d</a></h1><p class="e1oqyyyi10 ooa-1tku07r er34gjf0">1 995 cm3 • 150 KM • BMW seria 3 e46 diesel 2.0 150KM 209 tys. km</p></div><div class="ooa-d3dp2q e1oqyyyi2"><div class="e1oqyyyi3 ooa-12ou0s3 ej86sem3"><ul class="ooa-dzc1m ej86sem4"><li class="ooa-0 ej86sem5"><button role="button" class="ej86sem1 ooa-p0gz9t"><div class="ooa-1wmudpx">Wyróżnione</div></button></li></ul></div><dl class="ooa-uioh5d e1oqyyyi11"><dt class="ooa-1hyfx7x e1oqyyyi12">Przebieg</dt><dd data-parameter="mileage" class="ooa-1omlbtp e1oqyyyi13"><svg width="1em" height="1em" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" class="ooa-51p4fw"><path d="m16.474 4 5.897 16.083h-2.13L14.343 4h2.13zm-6.446 0L4.13 20.083H2L7.898 4h2.13zm2.982 11v4h-2v-4h2zm0-4.958v3h-2v-3h2zm0-4.042v2h-2V6h2z" fill="currentColor" fill-rule="evenodd"></path></svg>209 700 km</dd><dt class="ooa-1hyfx7x e1oqyyyi12">Rodzaj paliwa</dt><dd data-parameter="fuel_type" class="ooa-1omlbtp e1oqyyyi13"><svg width="1em" height="1em" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" class="ooa-51p4fw"><path d="m13 2 1 1v7h1c1.206 0 3 .799 3 3v6c.012.449.195 1 1 1 .806 0 .988-.55 1-1.011V6.42l-1.408-1.38H16L15 4l1-.96h3.408L22 5.58V19c0 1.206-.799 3-3 3-2.2 0-3-1.794-3-3v-6c0-.806-.55-.99-1.011-1H14v10H3V3l1-1h9zm-1 2H5v16h7V4zm-1.003 1v4H6V5h4.997z" fill="currentColor" fill-rule="evenodd"></path></svg>Diesel</dd><dt class="ooa-1hyfx7x e1oqyyyi12">Skrzynia biegów</dt><dd data-parameter="gearbox" class="ooa-1omlbtp e1oqyyyi13"><svg width="1em" height="1em" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" class="ooa-51p4fw"><path d="M21 5a2 2 0 0 0-4 0c0 .738.405 1.376 1 1.723v3.863l-.414.414H13V6.745A1.991 1.991 0 0 0 14.042 5a2 2 0 0 0-4 0c0 .721.385 1.348.958 1.7V11H6V6.723A1.994 1.994 0 0 0 5 3a1.994 1.994 0 0 0-1 3.723v10.554c-.595.347-1 .984-1 1.723a2 2 0 0 0 4 0c0-.739-.405-1.376-1-1.723V13h5v4.3a1.99 1.99 0 0 0-.958 1.7 2 2 0 0 0 4 0A1.99 1.99 0 0 0 13 17.255V13h5.414L20 11.414v-4.69c.595-.348 1-.986 1-1.724" fill="currentColor" fill-rule="evenodd"></path></svg>Manualna</dd><dt class="ooa-1hyfx7x e1oqyyyi12">Rok produkcji</dt><dd data-parameter="year" class="ooa-1omlbtp e1oqyyyi13"><svg width="1em" height="1em" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" class="ooa-51p4fw"><path d="M8.006 2v1h8.007V2h2.002v1h2.984L22 4v17l-1 1H3l-1-1V4l1-1h3.004V2h2.002zm11.992 8H4.002v10h15.996V10zM7.505 12a1.5 1.5 0 1 1 .001 3 1.5 1.5 0 0 1 0-3.001zM6.004 5H4.002v3h15.996V5h-1.983v1l-1.001 1-1.001-1V5H8.006v1L7.005 7 6.004 6V5z" fill="currentColor" fill-rule="evenodd"></path></svg>2005 </dd></dl><dl class="ooa-1o0axny e1oqyyyi14"><dd class="ooa-1jb4k0u e1oqyyyi15"><p class="ooa-gmxnzj">Pruszków (Mazowieckie)</p></dd><dd class="ooa-1jb4k0u e1oqyyyi15"><p class="ooa-gmxnzj">Podbite 8 minut temu</p></dd></dl><article class="ooa-12g3tpj ebwza7n1"><ol class="ooa-sh9ljo ebwza7n0"><li class="ooa-1y6ajhy ebwza7n5"><svg width="1em" height="1em" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" class="ooa-51p4fw"><path d="M12 12c4.963 0 9 4.038 9 9l-1 1H4l-1-1c0-4.962 4.037-9 9-9zm0 2c-3.52 0-6.442 2.613-6.929 6H18.93c-.487-3.387-3.409-6-6.93-6zm0-12c2.481 0 4.5 2.019 4.5 4.5 0 2.482-2.019 4.5-4.5 4.5a4.505 4.505 0 0 1-4.5-4.5C7.5 4.019 9.519 2 12 2zm0 2a2.503 2.503 0 0 0-2.5 2.5C9.5 7.878 10.621 9 12 9s2.5-1.122 2.5-2.5S13.379 4 12 4z" fill="currentColor" fill-rule="evenodd"></path></svg>Prywatny sprzedawca</li></ol></article></div><div class="ooa-1a2gnf2 e1oqyyyi5"><div hidden=""><a href="https://www.otomoto.pl/osobowe/oferta/bmw-seria-3-bmw-seria-3-e46-diesel-2-0-150km-209-tys-km-ID6G6Q20.html">ad link</a><div><ul><li>2005 </li></ul></div></div><div class="ooa-vtik1a e6j08rn0"><div class="ooa-2p9dfw e1oqyyyi4"><h3 class="e1oqyyyi16 ooa-1n2paoq er34gjf0">11 000</h3><p class="e1oqyyyi17 ooa-8vn6i7 er34gjf0">PLN</p></div><div class="ooa-1frlrb4 e6j08rn3"><div class="e6j08rn2 ooa-oa8y5h e16zpbx21"><span><svg data-testid="pe_icon_badge_in" style="font-size:24px;color:#0071CE" width="1em" viewBox="0 0 32 16" height="0.5em"><svg class="e1ilfzrf0 ooa-qwcuou er34gjf0"><use href="#icon-sprite-priceEvaluationIN"></use></svg></svg></span><p class="e16zpbx22 ooa-1tqe1q3 er34gjf0">W granicach średniej</p></div></div><section class="ooa-2c3zx e6j08rn4"><div id="financing-widget-listing-card-entrypoint" class="ooa-1bb0z24 e1bbui0j0"><a target="_blank" rel="noopener" href="https://otomotopay.pl/redirect/listing_page_adcard?okres_splaty=120&amp;link=www.otomoto.pl%2Fosobowe%2Foferta%2Fbmw-seria-3-bmw-seria-3-e46-diesel-2-0-150km-209-tys-km-ID6G6Q20.html&amp;title=BMW+Seria+3+320d&amp;img=https%3A%2F%2Fireland.apollo.olxcdn.com%2Fv1%2Ffiles%2FeyJmbiI6IjhibWN1Mm81MHBneDEtT1RPTU9UT1BMIn0.KTaVrFFHZORd_Zl5f7wrvTnH0oS_0LtxJX4M_uiL830%2Fimage%3Bs%3D640x480&amp;price=8250&amp;currency=PLN&amp;make=bmw&amp;marka_a=bmw&amp;model=seria-3&amp;model_a=seria-3&amp;mileage=209700&amp;productionYear=2005&amp;utm_medium=listing_page_adcard&amp;utm_content=native-ad-card" class="ooa-5u7qyy e1rbqr030">Sprawdź możliwości finansowania</a></div></section></div></div><div class="ooa-llp5st e1oqyyyi7"><button class="e1oqyyyi8 ooa-os57z4" type="button"><span class="ooa-ucvp6h"><span class="ooa-1iivig8"><svg width="1em" height="1em" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" class="ooa-1bnih2v"><path d="M20.219 10.367 12 20.419 3.806 10.4A3.96 3.96 0 0 1 3 8c0-2.206 1.795-4 4-4a4.004 4.004 0 0 1 3.868 3h2.264A4.003 4.003 0 0 1 17 4c2.206 0 4 1.794 4 4 0 .868-.279 1.698-.781 2.367M17 2a5.999 5.999 0 0 0-5 2.686A5.999 5.999 0 0 0 7 2C3.692 2 1 4.691 1 8a5.97 5.97 0 0 0 1.232 3.633L10.71 22h2.582l8.501-10.399A5.943 5.943 0 0 0 23 8c0-3.309-2.692-6-6-6" fill="currentColor" fill-rule="evenodd"></path></svg></span></span></button></div></section>