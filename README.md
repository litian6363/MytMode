# MytMode
window扫描wifi判断所在环境，降低电脑音量，无需安装依赖包

## 使用方式
修改wifi_name字段选择要扫描的wifi名字，当扫描到包含该字段的wifi名时，将会触发降低音量

## 开机启动
修改start_python.bat里面的python文件路径
将start_python.bat添加到 我的电脑》管理》任务计划程序，点击创建基本任务；
触发器设置当用户登录后，10秒延迟触发（留出时间等待计算机扫描wifi）