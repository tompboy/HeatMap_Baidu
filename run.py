#!flask/bin/python
# Date:2017-12-28
# Author:Pboy Tom:)
# QQ:360254363/pboy@sina.cn
# E-mail:cylcjy009@gmail.com
# Website:www.pboy8.top pboy8.taobao.com
# Desc: Create a Baidu's heatmap from nginx logs or iis logs...(By default: Nginx access log)
# Project home: https://github.com/tompboy/HeatMap_Baidu
# Version:V 0.01

import os

DIR='/home/getip'
#判断/home/getip目录是否存在，不存在则使用当前目录
if os.path.exists(DIR):
	DIR=DIR
else:
	DIR=os.getcwd()

os.environ['DIR']=str(DIR)

os.system(r"$DIR/flask/bin/python $DIR/start.py")
from app import app
app.run(
    host = '0.0.0.0',
    port = 4657,
    debug = True
)

