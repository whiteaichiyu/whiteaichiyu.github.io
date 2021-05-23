git pull
hexo clean
python3 uptable.py
python3 mShrimp_headless.py
hexo g -d
#echo "服务启动"
#hexo server
git add -A
git commit -m 'do mShrimp_headless daily'
git push
