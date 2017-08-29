export PATH=./src:$PATH
export PYTHONIOENCODING=utf-8
echo "start wechat service!"
nohup python ./src/main.py > wechat_output 2>&1 &

echo "ps -ef |grep python"
ps -ef |grep python
