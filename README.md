# excel--word
simple demo to help friend to deal repetitive work。

# tree
```
├── README.md
├── core                            核心文件夹
│   ├── __init__.py
│   ├── __init__.pyc
│   ├── ganjiang.py                 干将是将数据写入word模板
│   ├── ganjiang.pyc
│   ├── moye.py
│   └── moye.pyc                    莫邪是将数据从Excel中读取出，并将数据格式化
├── excel_test.xlsx                 测试的Excel文件
├── export                          Word输出文件夹
│   ├── __init__.py
│   ├── �\226��\232�建.docx
│   ├── �\213\211�\226�.docx
│   ├── �\216\213�\217�\214.docx
│   └── 赵�\227�天.docx
├── test.py                         测试程序主入口
└── word_test.docx                  测试的word模板
```

# use
```
第一步：
修改excel_test.xlsx里面的数据 一个人一条
对应word_test.docx里面要填入的数据用{{placeholder_数字}}占位
Excel里面的一列对应word里面的一个占位，按顺序依次排的。
输出文件在export文件夹默认命名是Excel里面第一列的输入内容。
第二步：
进入项目文件夹 cd (这个文件夹拖进终端)
source ./ENV/bin/activate （目的是默认使用我提供的Python环境）
python test.py   （运行程序）
```
