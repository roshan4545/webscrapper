import bs4
import requests
from datetime import datetime
file = open(r"C:\Users\malipatel roshan\Desktop\default.html","a")
now = datetime.now()
current_date = now.strftime("%B %d, %Y")
current_time = now.strftime("%H:%M")
file.write("<h1><b>THE NEWS AT "+current_date+" "+current_time+"</b></h1>")
results=requests.get("https://www.bbc.com/news")
soup=bs4.BeautifulSoup(results.content,'html.parser', multi_valued_attributes=None)
sample=soup.find(class_="gel-layout gel-layout--no-flex nw-c-top-stories--standard nw-c-top-stories--international")
div_tag=sample.find_all('div')
for div_tag_items in div_tag :
         if 'class' in div_tag_items.attrs:
                string=div_tag_items['class']
                if (string.find("primary-item") != -1):
                    str1=div_tag_items.find('h3').text
                    str2=(div_tag_items.find('p').text)
                    link=div_tag_items.find('a')['href']
                    str3=("https://www.bbc.com"+link)
                    file.write("<p>"+str1+"</p>\n")
                    file.write("<p>"+str2+"</p>\n")
                    file.write("<a href="+str3+">link</a><br><br>\n")
                elif (string.find("secondary-item")!= -1):
                    tempdiv=div_tag_items.find('div')['class']
                    if  (tempdiv.find("gs-c-promo nw-c-promo")!=-1):
                        str1=div_tag_items.find('h3').text
                        str2=(div_tag_items.find('p').text)
                        link=div_tag_items.find('a')['href']
                        str3=("https://www.bbc.com"+link)
                        file.write("<p>"+str1+"</p>\n")
                        file.write("<p>"+str2+"</p>\n")
                        file.write("<a href="+str3+">link</a>\n\n")
file.close()                         
