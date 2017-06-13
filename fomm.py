#! /usr/bin/python
import time
import sys
import urllib2
from bs4 import BeautifulSoup
import argparse



html_begin =  """\
<html>
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=0">
    <link href="//storefront-stylesheets.bigcartel.com/theme_stylesheets/88289590/1492957464/theme.css" media="screen" rel="stylesheet" type="text/css">
    <link href="//fonts.googleapis.com/css?family=Bevan|Glegoo" rel="stylesheet" title="Google Fonts" type="text/css" />
  </head>
  <body>
    <p>
    <div class="wrap">
      <section class="content">
       <table cellpadding="0" cellspacing="0" style="font-size:0px;width:100%" align="center" border="0" class="products">
        <tbody>
""" 
html_end =  """\
        </tbody>
       </table>
      </section>
     </div>
    </p>
  </body>
</html>
"""

body = ""

parser = argparse.ArgumentParser()
parser.add_argument(
    '--size', action='store_true', help='your size of shirt')
parser.add_argument("size", help="the size")
args = parser.parse_args()
size = args.size

size_search = "Size: " + size

for numPage in range(1,7): 
  response = urllib2.urlopen('http://www.fommvintage.com/category/mens-vintage-shirts?page=' + str(numPage))
  page = response.read()

  soup = BeautifulSoup(page,"html5lib")
  products = soup.find_all("li", class_="product sale")

  for product in products:
      link = product.find('a')
      product_response = urllib2.urlopen("http://www.fommvintage.com" + link.attrs['href'])
      product_page = product_response.read()
      if size_search in str(product_page):
          text = str(product)
          text2 = text.replace("li>","tr>")
          text3 = text2.replace("li ","tr style=\"word-wrap:break-word;font-size:0px;padding:10px 25px;padding-top:20px;padding-bottom:30px\" align=\"center\"")
          body = body + text3.replace("a href=\"/","a href=\"http://www.fommvintage.com/")

html = html_begin + body + html_end

print(html)
