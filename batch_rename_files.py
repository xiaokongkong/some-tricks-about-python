
"""
批量处理文件名
input: WT2G文件夹下，有多个文件夹，而每个文件夹内的文件名是一样的
.
└── WT2G
    ├── info
    ├── WT01
    │   ├── B01
    │   └── B02
    ├── WT02
    │   ├── B01
    │   ├── B02
    │   └── B03
    ├── WT03
    │   ├── B01
    │   ├── B02
    │   ├── B03
    │   └── B04
    ├── WT04
    │   ├── B01
    │   ├── B02
    │   └── B03
    └── WT05
        ├── B01
        └── B02
output: 把所有子文件夹夹内的文件都重新命名
.
└── WT2G
    ├── WT01-B01
    ├── WT01-B02
    ├── WT02-B01
    ├── WT02-B02
    ├── WT02-B03
    ├── WT03-B01
    ├── WT03-B02
    ├── WT03-B03
    ├── WT03-B04
    ├── WT04-B01
    ├── WT04-B02
    ├── WT04-B03
    ├── WT05-B01
    └── WT05-B02
"""

import os

WTX_lt = os.listdir('./WT2G')
WTX_lt = [x for x in WTX_lt if 'WT' in x]  # 过滤掉info等文件夹
for folder in WTX_lt:  # 在每个文件夹内遍历文件
    folder_lt = os.listdir('./WT2G/' + folder)
    for file in folder_lt:
        file_name = folder + '-' + file   # 重命名
        ori_file_path = os.path.join('./WT2G', folder, file)
        print(ori_file_path)
        os.system('cp ' + ori_file_path + ' /sdd/WT2G/' + file_name)  # 复制到新的文件夹
