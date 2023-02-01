import sys

from PyQt5.QtWidgets import QApplication, QDialog,QMessageBox
import transui

from googletrans import Translator

app = QApplication(sys.argv)

nmrel = {'adverb': '副词',
         'adjective': '形容词',
         'verb': '动词',
         'noun': '名词',
         'pronoun': '代词(he)',
         'preposition': '介词(on)',
         'article': '冠词(the)',
         'exclamation': '语气词(hi)'}


class QTransUi(QDialog):
    def __init__(self):
        super(QDialog, self).__init__(None)
        self.ui = transui.Ui_Form()
        self.ui.setupUi(self)
        self.ui.btnTrans.clicked.connect(self.btnTrans)

    def btnTrans(self):
        try:
            transhandle = Translator()
            dt = transhandle.detect(self.ui.txInput.toPlainText())
            if dt.lang == "en":
                des = 'zh-CN'
            else:
                des = 'en'
            result = transhandle.translate(self.ui.txInput.toPlainText(), dest=des)
            self.ui.txOutput.setText(result.text)

            for data in result.extra_data['parsed']:
                if len(data) > 7:
                    for infor in data:
                        if (type(infor) is list):
                            if len(infor) == 2:
                                for item in infor[0]:
                                    self.ui.txOutput.append('{:*^10}'.format(nmrel[item[0]]))
                                    if(type(item[1]) is list):
                                        for vas in item[1]:
                                            self.ui.txOutput.append(str(vas))
                                    else:
                                        self.ui.txOutput.append(str(item[1]))
                        else:
                            pass
        except TimeoutError:
            QMessageBox.critical(self, "Error", "Trans request time out.", QMessageBox.Ok)
        except:
            QMessageBox.critical(self, "Error", "Some Unkown Error Happen.", QMessageBox.Ok)


# python -m PyQt5.uic.pyuic trans.ui -o transui.py
# win = uic.loadUi(r'trans.ui')

win = QTransUi()

win.setWindowTitle("google翻译")

win.show()
#
sys.exit(app.exec_())

# -D 打包文件夹   -F 打包单个文件
# 安装最新pyinstaller pip install https://github.com/pyinstaller/pyinstaller/archive/develop.tar.gz
# pyinstaller -D -w .\ggtrans.py
