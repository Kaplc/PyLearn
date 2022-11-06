"""
1- 开发模式
    开发模式 - 前后端不分离
    后端框架 - Django + Jinja2
    前端框架 - Vue.js


    1) 项目开发模式
        前后端不分离，方便SEO(页面后端渲染完成提升搜索引擎的排名)
        采用Django + Jinja2模板引擎 + Vue.js实现前后端逻辑。
    2) 项目运行机制
        代理服务：Nginx服务器（反向代理）
        静态服务：Nginx服务器（静态首页、商品详情页、...）
        动态服务：uwsgi服务器（美多商场业务场景）
        后端服务：MySQL、Redis、Celery、RabbitMQ、Docker、FastDFS、Elasticsearch、Crontab
        外部接口：容联云、QQ互联、支付宝



"""
