# 功能介绍

- 用于给 AOI 管理人员发布学习内容，考试试卷。培训人员进行培训，学习，考试

# 项目部署流程

1. 服务器安装 docker,git,docker compose.
2. 服务器配置/etc/hosts 文件添加 10.41.95.93 reg.swharbor.com
3. docker 添加信任源 /etc/docker/daemon.json 文件添加 "insecure-registries":["https://harbor.wistron.com","http://reg.swharbor.com"]
4. 重启 docker 服务 systemctl restart docker
5. 登录 docker 账号到私有仓库 docker login reg.swharbor.com 账号 admin 密码 1234qwer!@#$QWER
6. 到 docker_itqs 文件夹下启动容器 docker compose up -d(如果失败需要提前拉取 docker-compose 文件内指定的镜像)
