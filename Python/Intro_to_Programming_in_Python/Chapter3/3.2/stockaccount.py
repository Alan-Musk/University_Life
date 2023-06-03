import sys
import stdarray
import stdio
import stockquote
from instream import InStream

class StockAccount:
    def __init__(self,filename) -> None:
        instream=InStream(filename)
        self._name=instream.readLine()
        self._cash=instream.readFloat()
        self._n=instream.readInt()
        self._shares=stdarray.create1D(self._n,0)
        self._stocks=stdarray.create1D(self._n,0)
        for i in range(self._n):
            self._shares[i]=instream.readInt()
            self._stocks[i]=instream.readString()

    def valueOf(self):
        total=self._cash
        for i in range(self._n):
            price=stockquote.priceOf(self._stocks[i])
            amount=self._shares[i]
            total+=amount*price
        return total
    
    def writeReport(self):
        stdio.writeln(self._name)
        total=self._cash
        for i in range(self._n):
            amount=self._shares[i]
            price=stockquote.priceOf(self._stocks[i])
            total+=amount*price
            stdio.writef('%4f %4s ',amount,self._stocks[i])
            stdio.writef('  %7.2f   %9.2f\n',price,amount*price)
        stdio.writef('%21s  %10.2f\n','Cash:',self._cash)
        stdio.writef('%21s  %10.2f\n','Total',total)

def main():
    acct=StockAccount(sys.argv[1])
    acct.writeReport()
        
if __name__=='__main__':main()