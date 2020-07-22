hexo clean
echo "缓存清理成功"
hexo g -d
echo "静态页面部署成功"
sleep 1s
echo "3"
sleep 1s
echo "2"
sleep 1s
echo "1"
echo "服务启动"
hexo server
