1.环境部署：
docker build . -t selenium_python:v1
docker-compose up -d
docker exec pyd_spider_1  pytest code/testsuite/test_scene.py --count 5  # 5 运行次数

2.配置：
需要根据配置conf/config.yml 进行账号、密码，钉钉token配置（测试环境默认不发送钉钉）