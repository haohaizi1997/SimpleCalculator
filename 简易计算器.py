import PySide2.QtWidgets as QtWidgets
from PySide2.QtUiTools import QUiLoader
import time


class SimpleCalculator():
    def __init__(self):
        self.ui = QUiLoader().load('SimpleCalculator.ui')  #加载ui界面

        # 数字按键
        self.ui.pushButton_0.clicked.connect(lambda:self.click_num('0'))
        self.ui.pushButton_1.clicked.connect(lambda:self.click_num('1'))
        self.ui.pushButton_2.clicked.connect(lambda:self.click_num('2'))
        self.ui.pushButton_3.clicked.connect(lambda:self.click_num('3'))
        self.ui.pushButton_4.clicked.connect(lambda:self.click_num('4'))
        self.ui.pushButton_5.clicked.connect(lambda:self.click_num('5'))
        self.ui.pushButton_6.clicked.connect(lambda:self.click_num('6'))
        self.ui.pushButton_7.clicked.connect(lambda:self.click_num('7'))
        self.ui.pushButton_8.clicked.connect(lambda:self.click_num('8'))
        self.ui.pushButton_9.clicked.connect(lambda:self.click_num('9'))

        # 功能按键
        self.ui.pushButton_point.clicked.connect(lambda:self.do('.'))
        self.ui.pushButton_sum.clicked.connect(lambda:self.do('+'))
        self.ui.pushButton_sub.clicked.connect(lambda:self.do('-'))
        self.ui.pushButton_muti.clicked.connect(lambda:self.do('*'))
        self.ui.pushButton_div.clicked.connect(lambda:self.do('/'))
        self.ui.pushButton_left.clicked.connect(lambda: self.click('('))
        self.ui.pushButton_right.clicked.connect(lambda: self.click(')'))
        self.ui.pushButton_done.clicked.connect(self.done)  # 等于号"="
        self.ui.pushButton_clear.clicked.connect(self.clear)  # 清除键
        self.ui.pushButton_del.clicked.connect(self.del_end)  # 退格键
        self.ui.pushButton_output.clicked.connect(self.output)

    # 数字按键响应函数
    def click_num(self, num_str):
        num = self.ui.result.toPlainText()
        if num != '' and num_str == '0':
            new_num = str(num) + num_str
            self.ui.result.setText(new_num)
        if num_str != '0':
            new_num = str(num) + num_str
            self.ui.result.setText(new_num)

    # 括号按键响应函数
    def click(self, what_str):
        num = self.ui.result.toPlainText()
        if what_str == '(':
            new_num = str(num) + what_str
            self.ui.result.setText(new_num)
        if what_str == ')' and num != '':
            new_num = str(num) + what_str
            self.ui.result.setText(new_num)

    # 功能按键响应函数
    def do(self, do_what):
        num = self.ui.result.toPlainText()
        if num != '':
            sym_list = ('+', '-', '*', '/', '.', '(')
            if not num.endswith(sym_list):
                new_num = str(num) + do_what
                self.ui.result.setText(new_num)

    # 计算函数
    def done(self):
        num = self.ui.result.toPlainText()
        if num != '':
            sym_list = ('+', '-', '*', '/', '.', '(')
            if not num.endswith(sym_list):
                try:
                    result = eval(num)
                    self.ui.result_history.append(num + '=' + str(result))
                    self.ui.result.setText(str(result))
                except:
                    QtWidgets.QMessageBox.about(self.ui, '提示', '请输入正确的表达式')
            else:
                QtWidgets.QMessageBox.about(self.ui,'提示','请输入正确的表达式')

    # 退格按键响应函数
    def del_end(self):
        num = self.ui.result.toPlainText()
        if num != '':
            new_num = ''
            for i in range(len(num) - 1):
                new_num += num[i]
            self.ui.result.setText(new_num)

    # 清除按键响应函数
    def clear(self):
        self.ui.result.setText('')
        self.ui.result_history.setText('')

    # 获取当前时间，精确到秒
    def getTimeSecond(self):
        timestamp = time.time() + 0 * 3600  # 东八区时间
        time_tuple = time.localtime(timestamp)
        time_str = time.strftime("%Y-%m-%d %H:%M:%S", time_tuple)
        return time_str

    # 导出历史记录
    def output(self):
        history = self.ui.result_history.toPlainText()
        if history == '':
            QtWidgets.QMessageBox.about(self.ui, '提示', '当前没有历史记录')
        else:
            with open('历史记录.txt', 'a+', encoding='utf-8') as f:
                f.write('='*5 + self.getTimeSecond()+ '='*5 + '\r\n')
                f.write(history + '\r\n')
            QtWidgets.QMessageBox.about(self.ui, '提示', '历史记录保存成功')


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    simpleCalculator = SimpleCalculator()
    simpleCalculator.ui.show()
    app.exec_()
