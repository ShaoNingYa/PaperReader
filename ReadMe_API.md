# ***重写返回值，要带状态码***
# 后端
## APP-user_manger
- 进行用户的管理
    - 登录
        - 路径：/user/login
        - 方法：GET|POST **TODO**
        - 参数：账户、密码 **TODO**
        - 返回：Token **TODO**
    - 用户信息查询
        - 路径：/user/info
        - 方法：GET|POST **TODO**
        - 参数：用户Token **TODO**
        - 返回：用户信息  **TODO**
    - 注销
        - 路径：/user/logout
        - 方法：GET|POST **TODO**
        - 参数：用户Token **TODO**
        - 返回：Success **TODO**
    
    - 注册 **TODO**
    - 修改信息 **TODO**
    - 修改密码 **TODO**
    - 修改头像 **TODO**
    - 删除账号 **TODO**
      
## APP-paper_manger
- 进行论文信息的增删改查
    - 上传一篇论文的文件（PDF）
        - 路径：/paper/paper_pdf_upload
        - 方法：GET|POST **TODO**
        - 参数：用户Token **TODO**
        - 返回：Success **TODO**
    - 修改论文的信息（流程是先上传PDF文件，然后再调用这个接口修改默认信息）
        - 路径：/paper/paper_info_update
        - 方法：GET|POST **TODO**
        - 参数：用户Token **TODO**
        - 返回：Success**TODO**
    - 删除论文 **TODO**
        - 路径：/paper/paper_del_one
        - 方法：GET|POST **TODO**
        - 参数：用户Token **TODO**
        - 返回：Success**TODO**
    - 获取当前用户的所有论文
        - 路径：/paper/paper_all_for_user
        - 方法：GET|POST **TODO**
        - 参数：用户Token **TODO**
        - 返回：所有的论文数据（论文ID，最新阅读进度等） **TODO**
    - 获取所有论文的所属的所有会议（直接在论文数据库中读取，只返回会议的名字和ID）
        - 路径：/paper/paper_conference_all
        - 方法：GET|POST **TODO**
        - 参数：用户Token **TODO**
        - 返回：Success **TODO**
    - 通过会议的名字，返回会议的ID（直接在论文数据库中读取）
        - 路径：/paper/paper_conference_name_by_id
        - 方法：GET|POST **TODO**
        - 参数：用户Token **TODO**
        - 返回：Success **TODO**
    - 增加会议类别（默认只有other一个） **TODO**
        - 路径：/paper/paper_conference_add_one
        - 方法：GET|POST **TODO**
        - 参数：用户Token **TODO**
    - 返回：Success **TODO**
    - 删除会议类别（Other不能删除） **TODO**
        - 路径：/paper/paper_conference_del_one
        - 方法：GET|POST **TODO**
        - 参数：用户Token **TODO**
        - 返回：Success **TODO**
    - 获取单篇论文的信息
        - 路径：/paper/paper_info_by_id
        - 方法：GET|POST **TODO**
        - 参数：用户Token **TODO**
        - 返回：Success **TODO**
    - 根据关键字搜索论文（论文的标题） **TODO**
        - 路径：/paper/paper_search_by_keyword
        - 方法：GET|POST **TODO**
        - 参数：用户Token **TODO**
        - 返回：Success **TODO**
    
- 标签管理相关（可用于论文分组）

    - 增加一个标签 **TODO**
    - 删除一个标签 **TODO**
    - 更改标签名字 **TODO**
    - 获取所有论文的标签 **TODO**
    - 获取标签下的所有论文 **TODO**
    - 删除一篇论文的一个标签 **TODO**

- 论文阅读记录相关
    - 获取所有论文的历史阅读记录
        - 路径：/paper/paper_history_get_all
        - 方法：GET|POST **TODO**
        - 参数：用户Token **TODO**
        - 返回：根据参数返回一定数量的历史记录 **TODO**
    - 获取单篇论文的历史阅读记录
        - 路径：/paper/paper_history_get_one
        - 方法：GET|POST **TODO**
        - 参数：用户Token **TODO**
        - 返回：根据参数返回相应数量的记录（在显示的时候最多返回40条，在恢复浏览时返回1条） **TODO**
    - 更新论文的阅读记录
        - 路径：/paper/paper_history_update_one
        - 方法：GET|POST **TODO**
        - 参数：用户Token，论文ID，页数等 **TODO**
        - 返回：看到哪一页，缩放的大小（根据时间排序，返回最新的结果） **TODO**
    - 删除一篇论文的浏览记录 **TODO**
        - 路径：/paper/paper_history_del_one
        - 方法：GET|POST **TODO**
        - 参数：用户Token，论文ID，页数等 **TODO**
        - 返回：看到哪一页，缩放的大小（根据时间排序，返回最新的结果） **TODO**
    - 删除一个用户的所有浏览记录 **TODO**
        - 路径：/paper/paper_history_del_all
        - 方法：GET|POST **TODO**
        - 参数：用户Token，论文ID，页数等 **TODO**
        - 返回：看到哪一页，缩放的大小（根据时间排序，返回最新的结果） **TODO**
    
- 会议日期提醒相关
    - 获取所有会议的名字
        - 路径：/paper/conference_warn_get_all_name **TODO**
        - 方法：GET|POST **TODO**
        - 参数：用户Token **TODO**
        - 返回：Success **TODO**
        
    - 获取所有会议的详细信息
        - 路径：/paper/conference_warn_get_all_info **TODO**
        - 方法：GET|POST **TODO**
        - 参数：用户Token **TODO**
        - 返回：看到哪一页，缩放的大小（根据时间排序，返回最新的结果） **TODO**
        
    - 更新会议数据

        - 路径：/paper/conference_warn_update **TODO**
        - 方法：GET|POST **TODO**
        - 参数：用户Token **TODO**
        - 返回：看到哪一页，缩放的大小（根据时间排序，返回最新的结果） **TODO**

# APP-study_manger

- 今日待办 
  - 获取今天的待办 

    - 路径：/study/todolist_get_today

    - 方法：POST

    - 参数：

      - 用户Token

    - 返回：

      - 状态码：20000（成功）

      - 数据（一个json格式）：

        ```python
           return_res = {
                date: "2020年3月12日",
                data: [
                    { text: 'fork this repository', done: false },
                    { text: 'follow author', done: false },
                    { text: 'vue-element-admin', done: true },
                    { text: 'vue', done: true }
                ]
            }
        return HttpResponse(json.dumps({"code": 20000, "data": return_res}))
        ```

        

  - 更新当天的待办（整体更新，包含增删改，如果数据库中有当天，就覆盖，没有就新增） 

    - 路径：/study/todolist_update_today

    - 方法：POST

    - 参数：

      - 用户Token

      - 需要更新的数据

        ```python
        data: [
                    { text: 'fork this repository', done: false },
                    { text: 'follow author', done: false },
                    { text: 'vue-element-admin', done: true },
                    { text: 'vue', done: true }
                ]
        ```

        

    - 返回：

      - 状态码：20000（成功）
      - 数据：success
    
  - 获取历史待办：

    - 路径：/study/todolist_get_history

    - 方法：POST

    - 参数：

      - 用户Token

    - 返回：

      - 状态码：20000（成功）

      - 数据（一个json格式）：

        ```python
           return_res = [{
                date: "2020年3月12日",
                data: [
                    { text: 'fork this repository', done: false },
                    { text: 'follow author', done: false },
                    { text: 'vue-element-admin', done: true },
                    { text: 'vue', done: true }
                ]
            },{
                date: "2020年3月11日",
                data: [
                    { text: 'fork this repository', done: false },
                    { text: 'follow author', done: false },
                    { text: 'vue-element-admin', done: true },
                    { text: 'vue', done: true }
                ]
            },
           ]
        return HttpResponse(json.dumps({"code": 20000, "data": return_res}))
        ```

  - 获取全部模板

    - 路径：/study/todolist_get_template

    - 方法：POST

    - 参数：

      - 用户Token

    - 返回：

      - 状态码：20000（成功）

      - 数据（一个json格式）：

        ```python
           return_res = [{
                title: "一个用于学习的模板",
                data: [
                    { text: 'fork this repository', done: false },
                    { text: 'follow author', done: false },
                    { text: 'vue-element-admin', done: true },
                    { text: 'vue', done: true }
                ]
            },{
                title: "周六日用的模板",
                data: [
                    { text: 'fork this repository', done: false },
                    { text: 'follow author', done: false },
                    { text: 'vue-element-admin', done: true },
                    { text: 'vue', done: true }
                ]
            },
           ]
        return HttpResponse(json.dumps({"code": 20000, "data": return_res}))
        ```

  - 更新一个模板

    - 路径：/study/todolist_update_template

    - 方法：POST

    - 参数：

      - 用户Token

      - 需要更新的数据

        ```python
        data: [
                    { text: 'fork this repository', done: false },
                    { text: 'follow author', done: false },
                    { text: 'vue-element-admin', done: true },
                    { text: 'vue', done: true }
                ]
        ```

    - 返回：

      - 状态码：20000（成功）
      - 数据：success

    

