# 高德API显示租房信息
- 调用高德API在高德地图显示租房房源信息

- 项目的运行
  - 先运行server文件夹下的app.py
  - 再运行client文件夹下的XM.py
  
- 项目的库：PyQt5，requests，pymysql，Flask

- 项目的数据库：
  - 库名：house
    - 表名：house_info,userinfo,code
      - 表house_info结构：
        - id  int  primary key   auto   auto_increment
        - title   varchar
        - location varchar
        - x      float
        - y      float
        - money  int
        - url    text
      - 表userinfo结构：
        - id int  primary key   auto   auto_increment
        - name    varchar
        - pwd     varchar
        - mail    varchar
      - 表code结构：
        - mail varchar
        - code char(4)
