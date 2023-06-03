import sys
import stdio
from instream import InStream

def _readHTML(stockSymbol):
    WEBSITE='http://finance.yahoo.com/q?s='
    page=InStream(WEBSITE+stockSymbol)
    html=page.readAll()
    return html

def priceOf(stockSymbol):
    html=_readHTML(stockSymbol)
    trade=html.find('yfs_184',0)
    beg=html.find('>',trade)
    end=html.find('</span>',beg)
    price=html[beg+1:end]
    price=price.replace(',','')
    return float(price)

def main():
    stockSymbol=sys.argv[1]
    price=priceOf(stockSymbol)
    stdio.writef('%.2f\n',price)

if __name__=='__main__':main()