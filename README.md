# 测试成长笔记

一个专注于软件测试领域学习与实践的技术博客，记录从测试执行者到质量架构师的成长历程。

## 技术栈

- **框架**: [Hexo](https://hexo.io/) 8.1.1
- **主题**: [Butterfly](https://butterfly.js.org/) 5.5.4
- **部署**: Cloudflare Pages
- **语言**: 中文 (zh-CN)

## 本地运行

```bash
# 安装依赖
npm install

# 启动本地服务器
npx hexo server

# 生产构建
npx hexo clean && npx hexo generate
```

## 内容分类

| 分类 | 说明 |
|------|------|
| 测试理论 | 测试方法论、测试思维、质量理念 |
| 测试实践 | 自动化测试、性能测试、工具使用 |
| 个人思考 | 职业发展、学习总结、行业观察 |

## 项目结构

```
.
├── source/
│   ├── _posts/          # 文章源文件（Markdown）
│   │   ├── 测试理论/
│   │   ├── 测试实践/
│   │   └── 个人思考/
│   └── images/          # 图片资源（本地化存储）
├── _config.yml          # Hexo 站点配置
├── _config.butterfly.yml # Butterfly 主题配置
└── package.json
```

## 特性

- 卡片式文章列表布局
- 自定义主题色（深灰蓝 + 活力橙）
- 首页横幅背景图 + 副标题打字机动效
- 暗色模式支持
- 无评论、无搜索、无 RSS 的精简阅读体验
