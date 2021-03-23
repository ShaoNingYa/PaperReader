# 后端
## APP-用户管理-user_manger
- 进行用户的管理
    - 数据库
        - 用户序号
        - 用户姓名
        - 用户邮箱
        - 用户电话
        
## APP-论文管理-paper_manger
- 进行论文信息的增删改查
    - 数据库
        - 论文基础数据库
            - 论文所属用户（外键）
            - 论文PDF格式的存储（这里先尝试能不能用同名文件进行存储）
            - 论文序号
            - 论文名称（不能直接由文件名获取）
            - 论文作者
            - 论文会议
            - 所属小类关键字（数据库、NLP、CV、CTR等）
            
        - 论文评价数据库
            - 操作对应的论文（外键）
            - 操作所属的用户（外键）
            - 评价星级
            - 评论的内容
            
        - 论文操作（高亮、笔记）数据库
            - 操作对应的论文（外键）
            - 操作所属的用户（外键）
            - 操作日期时间
            - 操作类型（预留-后续增加（笔记、高亮、代码、翻译等））
            - 代码存储（每个用户都要存储自己修改的代码，数据库设定为file格式）
            - 论文翻译（存储网页，或者直接存储markdown文档）
        
        - 盲点单词数据库（用于记录不认识的单词）（先不要）
            - 对应的论文（外键）
            - 对应的用户（外键）
            - 添加的时间
            - 单词的英文
            - 对应论文的页数
            - 单词的中文
            - 对应的短语
            
        - 论文操作（浏览）数据库（每次浏览论文时（十分钟）生成一条数据，下一次打开时按照最新操作进行打开，实现进度保存）
            - 操作对应的论文（外键）（对应论文的外键和所属的用户构成主键）
            - 操作所属的用户（外键）
            - 操作日期时间
            - 操作类型（时间循环自动保存、事件（开始浏览等）自动保存、手动保存等）
            - 浏览进度（记录一个页数即可）
            - 缩放大小
            
        - 代码数据库（保存对应论文的代码）
            - 代码对应的论文（外键）
            - 上传代码的用户（外键）
            - 上传代码的日期
            - 上传代码的版本
            - 代码的简要说明
            - 是否删除（是：删，否：未删）
            
# 前端
- 用户登录之后能够看到自己的所有论文，并且这些论文按照最新浏览时间进行排序
- 点击一个论文之后，跳转到此论文的浏览页面，可以进行在线观看、记笔记、下载等操作
- 每十分钟或者在有鼠标滚动事件时触发一次浏览进度保存（可能存在效率低下问题，后续可以再优化进度保存策略）


- ### 欢迎页
    - 展示一些公告信息、产品版本等，点击后跳转到学习管理模块  
- ### 一、学习管理：
    - 今日待办（TODO List）
        - 显示今天的待办日程
        - 显示历史的待办日程
    - 显示学习历史记录（一键返回上次学习环境）
        - 上次看的论文、代码、文章、网页、视频等
        - 学习路线的进展
    - 列出当前学习路线（https://www.itnanls.cn/）
        - 利用TodoList的形式进行展示
    - 列出全部可学方向
        - NLP、CV、CTR等，并给出对应的论文、代码、文章、网页、视频等
    - 列出全部可学资源
        - 按照论文、代码（原代码+自定义代码）、文章（原文+自编写文章）等进行分类
    - 列出面试的东西
- ### 二、论文阅读管理：
    - 记录论文阅览历史（阅览时间、进度等）
    - 显示我上传的所有论文（增删改查）
    - 显示所有人上传的论文（能分类、搜索等，并查看别人的笔记等）
    - 论文的图谱表示（检索当前用户或者某一论文的引用，生成引用图谱）
    - 会议投稿日期（模拟 https://aideadlin.es/?sub=ML,CV,NLP,RO,SP,DM）
- ### 三、笔记管理：
    - 管理自己已经记录的笔记（笔记可能在论文、代码、文章等中产生，在这里进行汇总管理）
        - 增删改查
    - 收藏的东西
    - 查看别人的笔记（按照方向进行搜索）
- ### 四、问题管理（论坛）：
    - BUG汇总
    - 对提出的问题进行汇总显示（来自论文、代码等）（区分已处理+未处理）
    - 聊天界面（进行聊天、内容推荐等）
- ### 五、服务器管理：
    - 可用服务器显示（地址、账号、密码等，管理者，服务器状态，正在做的事情等）（服务器公告）
    - 服务器需求申请
- ### 六、汇报管理：
    - 周总结
    - 汇报的PPT（按照时间线展示，并记录当时的汇报细节）
- ### 七、项目管理：
    - 显示正在做的项目（进去后展示一些细节，比如此工程所产生的文档等）
- ### 八、活动及报销管理：
    - 显示所有活动，并进行标注（正在进行中、已完成等）（点进去后显示细节）

# 问题：
- 使用xadmin时，用户名使用的是Django的超级用户，创建的方法是：`python manage.py createsuperuser`
    - `shaoning : 123456`
    
    
# 开发：
## 登录：
### 令牌管理：
- 利用令牌来判断是否登录，因此需要一个表来保存用户的令牌
    - 此令牌在用户登录时生成，保存到这个表中（需要创建函数，根据用户名和固定算法生成固定长度的密钥），并将令牌返回前端
    - 在获取信息时，前端将以此令牌和用户名来获取用户的信息，在表中进行搜索，如果存在此令牌，且可正常使用
    - 只有在退出时将此令牌状态置为注销
    - 现在设定一个用户只能有一个令牌
        - 在登录时就创建一个新的放到此表中（单一登录）
        - 在登陆时先判断此用户是否有正在使用中的令牌，有就直接返回此令牌，不然再重新生成（共享登录）

## 论文管理：
### 论文的上传：

- 在这个部分现在存在中文的问题，如果上传的PDF文件是中文命名，就会出现错误，在前端体现出来的就是跨域问题（猜想应该是会返回DeBug界面，然后没有头数据，所以前端不接受）

# 部署：
- `GRANT ALL PRIVILEGES ON paper_reader.* TO user_pr@"%" IDENTIFIED BY "123456";`
- 修改setting.py 添加https
  
- 执行的命令更改为：`python manage.py runserver_plus --cert server.crt 0.0.0.0 8000`
  
- 将项目部署到Apache服务器上：
  - 增加配置文件到：`/etc/apache2/sites-available/paper-reader.conf`

    ```
    <VirtualHost *:8000>
      #访问网站以哪个目录开始，第二个参数填写路径
      WSGIScriptAlias / /home/ubuntu/my_pro/PaperReader/PaperReader/wsgi.py
      <Directory /home/ubuntu/my_pro/PaperReader/PaperReader>
        <Files wsgi.py>
          Require all granted
        </Files>
      </Directory>
      #开放静态目录
      Alias /static/ /home/ubuntu/my_pro/PaperReader/static_files/
      <Directory /home/ubuntu/my_pro/PaperReader/static_files>
        Require all granted
      </Directory>
    
      #开放上传文件夹
      Alias /media/ /home/ubuntu/my_pro/PaperReader/media/
      <Directory /home/ubuntu/my_pro/PaperReader/media>
        Require all granted
      </Directory>
    
      #以下开始是因为使用了virtualenv部署
      #第一个路径是虚拟环境路径，第二个是项目所在路径
      WSGIDaemonProcess PaperReader python-home=/home/ubuntu/my_pro/env_PaperReader python-path=/home/ubuntu/my_pro/PaperReader
      #分组
      WSGIProcessGroup PaperReader
    </VirtualHost>
    ```

  - 然后将此配置文件符号链接到`/etc/apache2/sites-enabled/paper-reader.conf`，命令：

    `sudo ln -s /etc/apache2/sites-available/paper-reader.conf /etc/apache2/sites-enabled/paper-reader.conf`

  - 在`/etc/apache2/ports.conf`中增加监听端口：`Listen 8000`

  - 最后重新加载并重启Apache服务：

    ```
    sudo systemctl reload apache2
    sudo systemctl restart apache2
    ```

    







### 部署到apache上遇到的错误：

#### 环境： Ubuntu18.04 apache2 Python3.6 Django2.2

- Apache日志报错：

  ```
  [Tue Feb 23 11:11:15.534245 2021] [wsgi:warn] [pid 22065] (13)Permission denied: mod_wsgi (pid=22065): Unable to stat Python home /home/ubuntu/my_pro/env_PaperReader. Python interpreter may not be able to be initialized correctly. Verify the supplied path and access permissions for whole of the path.
  ImportError: No module named site
  ```

  - 问题分析：权限不够
  - 解决办法：需要为当前用户增加权限，命令：`chmod 755 /home/ubuntu`

- Apache日志报错：

  ```
  ImportError: No module named django.core.wsgi
  ```

  - 问题分析：Django项目下的wsgi.py文件的配置问题，需要增加环境

  - 解决办法：在这个文件中的最上面添加两行：

    ```
    import sys
    sys.path.append('/home/ubuntu/my_pro/env_PaperReader/lib/python3.6/site-packages')  # 指向虚拟环境
    ```

    

- Apache日志报错：

  ```
  AttributeError: 'module' object has no attribute 'lru_cache'
  ```

  - 问题分析：版本问题，重新安装依赖包

  - 解决办法：

    ```
    sudo apt remove  libapache2-mod-wsgi
    sudo apt install libapache2-mod-wsgi-py3
    ```
  
- 会议提醒出现网络错误，因为路径问题，在服务器上部署之后，python工作路径变成了 `/`，所以要将相对路径改为绝对路径（在view中）

# 其他问题：

- 上传PDF时，文件名为中文导致上传失败的问题：

  - 未能解决 TODO

    