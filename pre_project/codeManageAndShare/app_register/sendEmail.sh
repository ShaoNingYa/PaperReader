#!/bin/bash
echo  "注册码为： $1  请注意保管，不要随意告诉他人，仅可使用一次！" | mail -s "注册码" $2 
if [ $? -eq 0 ];then
    echo "`date` 发送验证码成功" >> log
else
    echo "`date` 发送验证码失败" >> log
fi
