import os
import shutil

def build_simple_site():
    print("开始构建简单静态站点...")
    
    # 创建输出目录
    output_dir = 'vercel_build'
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    os.makedirs(output_dir)
    
    # 复制现有的静态文件（如果有）
    static_dirs = ['static', 'users/static', 'blogs/static']
    for static_dir in static_dirs:
        if os.path.exists(static_dir):
            shutil.copytree(static_dir, os.path.join(output_dir, 'static'), dirs_exist_ok=True)
            print(f"已复制静态文件: {static_dir}")
    
    # 创建完整的博客首页
    index_html = '''
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>我的技术博客</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            color: #333;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }
        header {
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            border-radius: 15px;
            padding: 40px;
            margin-bottom: 30px;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
            text-align: center;
        }
        h1 {
            font-size: 3em;
            background: linear-gradient(45deg, #667eea, #764ba2);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 10px;
        }
        .subtitle {
            font-size: 1.2em;
            color: #666;
            margin-bottom: 20px;
        }
        .blog-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 25px;
            margin-bottom: 40px;
        }
        .post-card {
            background: rgba(255, 255, 255, 0.95);
            border-radius: 15px;
            padding: 30px;
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        .post-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 40px rgba(0, 0, 0, 0.15);
        }
        .post-title {
            font-size: 1.5em;
            color: #333;
            margin-bottom: 15px;
            border-bottom: 2px solid #667eea;
            padding-bottom: 10px;
        }
        .post-meta {
            color: #888;
            font-size: 0.9em;
            margin-bottom: 15px;
        }
        .post-content {
            color: #555;
            margin-bottom: 20px;
        }
        .read-more {
            display: inline-block;
            background: linear-gradient(45deg, #667eea, #764ba2);
            color: white;
            padding: 10px 20px;
            border-radius: 25px;
            text-decoration: none;
            transition: transform 0.2s ease;
        }
        .read-more:hover {
            transform: scale(1.05);
        }
        footer {
            text-align: center;
            color: white;
            padding: 30px;
            margin-top: 50px;
        }
        .features {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin: 40px 0;
        }
        .feature {
            background: rgba(255, 255, 255, 0.9);
            padding: 20px;
            border-radius: 10px;
            text-align: center;
        }
        @media (max-width: 768px) {
            .blog-grid {
                grid-template-columns: 1fr;
            }
            h1 {
                font-size: 2em;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>🚀 我的技术博客</h1>
            <p class="subtitle">分享编程知识 & 学习心得</p>
            <p>专注于 Python、Django、Web 开发和前沿技术</p>
        </header>

        <div class="features">
            <div class="feature">
                <h3>📚 技术文章</h3>
                <p>深入的教程和技术解析</p>
            </div>
            <div class="feature">
                <h3>💡 最佳实践</h3>
                <p>开发经验和代码规范</p>
            </div>
            <div class="feature">
                <h3>🔧 工具分享</h3>
                <p>提高效率的开发工具</p>
            </div>
        </div>

        <div class="blog-grid">
            <article class="post-card">
                <h2 class="post-title">欢迎来到我的博客</h2>
                <div class="post-meta">发布于 2024年1月 | 分类：公告</div>
                <div class="post-content">
                    <p>这个博客从 Django 应用成功迁移到静态站点，部署在 Vercel 平台上。</p>
                    <p>现在拥有更快的加载速度和更好的用户体验！</p>
                </div>
                <a href="#" class="read-more">阅读更多</a>
            </article>

            <article class="post-card">
                <h2 class="post-title">Python 虚拟环境指南</h2>
                <div class="post-meta">发布于 2024年1月 | 分类：Python</div>
                <div class="post-content">
                    <p>学习如何正确使用 Python 虚拟环境来管理项目依赖，避免版本冲突问题。</p>
                    <p>包含 venv、virtualenv 和 pipenv 的详细对比。</p>
                </div>
                <a href="#" class="read-more">阅读更多</a>
            </article>

            <article class="post-card">
                <h2 class="post-title">Django 部署最佳实践</h2>
                <div class="post-meta">发布于 2024年1月 | 分类：Django</div>
                <div class="post-content">
                    <p>探讨 Django 项目在生产环境中的部署策略，包括静态文件处理、数据库优化和安全配置。</p>
                </div>
                <a href="#" class="read-more">阅读更多</a>
            </article>

            <article class="post-card">
                <h2 class="post-title">现代 CSS 布局技巧</h2>
                <div class="post-meta">发布于 2024年1月 | 分类：前端</div>
                <div class="post-content">
                    <p>掌握 Flexbox、Grid 等现代 CSS 布局技术，创建响应式网页设计。</p>
                    <p>包含实际案例和代码示例。</p>
                </div>
                <a href="#" class="read-more">阅读更多</a>
            </article>
        </div>
    </div>

    <footer>
        <p>&copy; 2024 我的技术博客 | 由 Vercel 强力驱动 | 完全免费托管</p>
        <p>📧 联系我: your-email@example.com</p>
    </footer>
</body>
</html>
    '''
    
    with open(os.path.join(output_dir, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(index_html)
    
    # 创建关于页面
    about_html = '''
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>关于 - 我的技术博客</title>
    <style>
        body { 
            font-family: Arial, sans-serif; 
            max-width: 800px; 
            margin: 0 auto; 
            padding: 20px;
            line-height: 1.6;
        }
        .nav { margin-bottom: 30px; }
        .nav a { margin-right: 15px; text-decoration: none; color: #007bff; }
    </style>
</head>
<body>
    <div class="nav">
        <a href="/">首页</a>
        <a href="/about.html">关于</a>
    </div>
    
    <h1>关于本站</h1>
    <p>这是一个由 Django 迁移到静态站点的技术博客。</p>
    <p>主要分享编程技术和开发经验。</p>
    
    <h2>技术栈</h2>
    <ul>
        <li>前端: HTML5, CSS3, JavaScript</li>
        <li>部署: Vercel</li>
        <li>特性: 全球 CDN, 自动 HTTPS, 完全免费</li>
    </ul>
</body>
</html>
    '''
    
    with open(os.path.join(output_dir, 'about.html'), 'w', encoding='utf-8') as f:
        f.write(about_html)
    
    print(f'✅ 静态站点已构建到 {output_dir} 目录')
    print('📁 生成的文件:')
    for root, dirs, files in os.walk(output_dir):
        for file in files:
            filepath = os.path.join(root, file)
            print(f'   - {filepath}')

if __name__ == '__main__':
    build_simple_site()
