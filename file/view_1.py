import sys
import os
from natsort import natsorted
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QFileDialog, QMessageBox
from PyQt5.QtCore import Qt, QTimer

class MonitorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('监控程序')
        self.resize(500, 300)

        self.size_label = QLabel('产品尺码数量:')
        self.size_input = QLineEdit()
        self.size_input.setPlaceholderText('输入产品尺码数量')

        self.size_layout = QVBoxLayout()
        self.size_layout.addWidget(self.size_label)
        self.size_layout.addWidget(self.size_input)

        self.size_btn = QPushButton('尺码文件生成路径:')
        self.size_input_path = QLineEdit()
        self.prod_btn = QPushButton('产品文件夹路径:')
        self.prod_input_path = QLineEdit()
        self.output_btn = QPushButton('产品文件夹输出路径:')
        self.output_input_path = QLineEdit()
        self.start_btn = QPushButton('开始监控')
        self.stop_btn = QPushButton('结束监控')

        self.size_btn.clicked.connect(self.chooseSizePath)
        self.prod_btn.clicked.connect(self.chooseProdPath)
        self.output_btn.clicked.connect(self.chooseOutputPath)
        self.start_btn.clicked.connect(self.startMonitoring)
        self.stop_btn.clicked.connect(self.stopMonitoring)

        self.btn_layout = QVBoxLayout()
        self.btn_layout.addWidget(self.size_btn)
        self.btn_layout.addWidget(self.size_input_path)
        self.btn_layout.addWidget(self.prod_btn)
        self.btn_layout.addWidget(self.prod_input_path)
        self.btn_layout.addWidget(self.output_btn)
        self.btn_layout.addWidget(self.output_input_path)
        self.btn_layout.addWidget(self.start_btn)
        self.btn_layout.addWidget(self.stop_btn)

        main_layout = QVBoxLayout()
        main_layout.addLayout(self.size_layout)
        main_layout.addLayout(self.btn_layout)

        self.setLayout(main_layout)

        self.prod_folder_path = ''
        self.output_folder_path = ''
        self.size_folder_path = ''
        self.monitoring = False
        self.current_output_folder_index = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.checkFolder)

    def chooseSizePath(self):
        folder_path = self.openFolderDialog('选择尺码文件生成路径')
        self.size_input_path.setText(folder_path)
        self.size_folder_path = folder_path

    def chooseProdPath(self):
        folder_path = self.openFolderDialog('选择产品文件夹路径')
        self.prod_input_path.setText(folder_path)
        self.prod_folder_path = folder_path

    def chooseOutputPath(self):
        folder_path = self.openFolderDialog('选择产品文件夹输出路径')
        self.output_input_path.setText(folder_path)
        self.output_folder_path = folder_path

    def openFolderDialog(self, title):
        folder_path = QFileDialog.getExistingDirectory(self, title)
        return folder_path

    def startMonitoring(self):
        if not self.prod_folder_path or not self.output_folder_path or not self.size_folder_path:
            QMessageBox.warning(self, "警告", "请填写所有路径")
            return

        try:
            size_count = int(self.size_input.text())
        except ValueError:
            QMessageBox.warning(self, "警告", "请输入有效的尺码数量")
            return

        self.monitoring = True
        self.createOutputFolders()
        self.timer.start(1000) # Check every second

    def stopMonitoring(self):
        self.monitoring = False
        self.timer.stop()

    def createOutputFolders(self):
        try:
            for file_name in os.listdir(self.prod_folder_path):
                file_path = os.path.join(self.prod_folder_path, file_name)
                if os.path.isfile(file_path):
                    new_folder_path = os.path.join(self.output_folder_path, os.path.splitext(file_name)[0])
                    os.makedirs(new_folder_path, exist_ok=True)
        except Exception as e:
            QMessageBox.warning(self, "警告", f"出现错误：{e}")

    def checkFolder(self):
        if not self.monitoring:
            return

        current_file_count = len(os.listdir(self.size_folder_path))
        if current_file_count >= int(self.size_input.text()):
            self.moveFiles()

    def moveFiles(self):
        try:
            output_folders = natsorted(os.listdir(self.output_folder_path))
            output_folders = [os.path.join(self.output_folder_path, folder) for folder in output_folders]
            target_folder = output_folders[self.current_output_folder_index]
            for file_name in os.listdir(self.size_folder_path):
                file_path = os.path.join(self.size_folder_path, file_name)
                if os.path.isfile(file_path):
                    new_file_name = os.path.basename(target_folder) + os.path.splitext(file_name)[0] + \
                                    os.path.splitext(file_name)[1]
                    os.rename(file_path, os.path.join(target_folder, new_file_name))
            self.current_output_folder_index = (self.current_output_folder_index + 1) % len(output_folders)
        except Exception as e:
            QMessageBox.warning(self, "警告", f"出现错误：{e}")

        # QMessageBox.information(self, "提示", "文件移动完成")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MonitorApp()
    window.show()
    sys.exit(app.exec_())
