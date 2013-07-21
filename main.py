from PyQt4 import QtCore,QtGui
import os
#from tkFileDialog import askopenfilename
from pySeq import Ui_MainWindow
from Bio import SeqIO
from Bio.Seq import Seq
import re
import sys


try:
    _fromUtf8 = QtCore.Qstring._fromUtf8
except AttributeError:
    _fromUtf8 = lambda s:s

class mainApp(QtGui.QMainWindow, Ui_MainWindow):
    """docstring for mainApp"""

    def __init__(self, parent=None):
        super(mainApp, self).__init__(parent)
        self.setupUi(self)
        QtCore.QObject.connect(self.setDatabase,
                QtCore.SIGNAL(_fromUtf8("clicked()")),
                self.setDatabaseFunc)
        QtCore.QObject.connect(self.go,
                QtCore.SIGNAL(_fromUtf8("clicked()")),
                self.goFunc)
    def setDatabaseFunc(self):
        self.databaseEdit.setText(QtGui.QFileDialog.getOpenFileName())
        self._database = str(self.databaseEdit.text())
    def goFunc(self):
        myseq = str(self.patternEdit.text())
        seqfile = str(self.databaseEdit.text())
        seqfileBase = seqfile.split('.fasta')[0]
        pp = re.compile(myseq)
        foundSeq = []
        foundID  = []
        #foundDescription = []
        ##     Calculete item numbers
        #seq_iterator = SeqIO.parse(seqfilt, "fasta")
        #print sum(1 for e in seq_iterator)
        #############################################
        seq_iterator = SeqIO.parse(seqfile, "fasta")
        item_num = 0
        n = 0
        f = open(seqfileBase+'_Pattern_'+myseq+'.txt','wb')
        for each_item in seq_iterator:
            item_num += 1
            mall = pp.findall(str(each_item.seq))
            if mall:
                miter = pp.finditer(str(each_item.seq))
                n = n + 1
                f.write('#'*100+'\r\n')
                f.write("ID : %s \r\n" % each_item.id)
                f.write("Description : %s \r\n" % each_item.description)
                print each_item.id
                foundSeq.append(each_item)
                foundID.append(each_item.id)
                for i in miter:
                    #f.write("span from %s \r\n" % i.span()) 
                    f.write(" ".join(map(lambda x: str(x), i.span())))
                    f.write(" %s \r\n" % i.group())
#                    print i.group(), 'span from: ', i.span()       
        # save whole sequence content
        SeqIO.write(foundSeq,seqfileBase+'_Pattern_'+myseq+'.fasta','fasta')
        # save ID
        f.close
        print 'Task Finished !!'
    def parseSeq(seqOrg):
        
        
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = mainApp()
    myapp.show()
    sys.exit(app.exec_())    
