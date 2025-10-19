import os
import shutil

def build_simple_site():
    print("开始构建简单静态站点...")
    
    # 创建输出目录
    output_dir = 'vercel_build'
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
    os.makedirs(output_dir)
    
    # 创建完整的博客首页（与之前相同的内容）
    index_html = '''
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>我的技术博客</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: Arial, sans-serif; line-height: 1.6; color: #333; max-width: 800px; margin: 0 auto; padding: 20px; }
        header { text-align: center; margin-bottom: 40px; border-bottom: 2px solid #f0f0f0; padding-bottom: 20px; }
        h1 { font-size: 2.5em; color: #333; margin-bottom: 10px; }
        .post { border-bottom: 1px solid #eee; padding: 20px 0; margin-bottom: 20px; }
        .post-title { font-size: 1.5em; color: #333; margin-bottom: 10px; }
        .post-meta { color: #666; font-size: 0.9em; margin-bottom: 15px; }
        footer { text-align: center; margin-top: 40px; color: #888; padding-top: 20px; }
    </style>
</head>
<body>
    <header>
        <h1>🚀 我的技术博客</h1>
        <p>成功部署到 Vercel！</p>
    </header>

    <main>
        <div class="post">
            <h2 class="post-title">欢迎来到我的博客</h2>
            <div class="post-meta">发布于 2024年 | 分类：公告</div>
            <div class="post-content">
                <p>这个博客已成功从 Django 迁移到静态站点，并部署在 Vercel 平台上。</p>
                <p>现在拥有更快的加载速度和全球 CDN 加速！</p>
            </div>
        </div>

        <div class="post">
            <h2 class="post-title">关于部署</h2>
            <div class="post-content">
                <p>✅ 静态站点构建成功</p>
                <p>✅ Vercel 自动部署</p>
                <p>✅ 全球 CDN 加速</p>
                <p>✅ 完全免费托管</p>
            </div>
        </div>
    </main>
    
    <footer>
        <p>&copy; 2024 我的技术博客 | 由 Vercel 强力驱动</p>
    </footer>
</body>
</html>
    '''
    
    with open(os.path.join(output_dir, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(index_html)
    
    print(f'✅ 静态站点已构建到 {output_dir} 目录')
    print('📁 生成的文件:')
    for root, dirs, files in os.walk(output_dir):
        for file in files:
            filepath = os.path.join(root, file)
            print(f'   - {filepath}')

if __name__ == '__main__':
    build_simple_site()
