import os
from pathlib import Path

def build_app_index():
    # Set the directory path
    apps_dir = Path(r'E:\apps')
    
    # Get all HTML files in the apps directory (not in subdirectories)
    html_files = sorted([f.name for f in apps_dir.glob('*.html') if f.is_file()])
    
    # Create the index.html content
    html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Apps Index</title>
    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }
        
        body {
            font-family: 'Segoe UI', Arial, sans-serif;
            background: #fff;
            color: #000;
            min-height: 100vh;
            position: relative;
        }
        
        body::before {
            content: '';
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background-image: 
                linear-gradient(rgba(255,255,255,0.97), rgba(255,255,255,0.97)),
                url('data:image/svg+xml;utf8,<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="800"><text x="50" y="100" font-family="Times New Roman" font-size="48" fill="%23e8e8e8" font-style="italic">a² + b² = c²</text><text x="700" y="150" font-family="Times New Roman" font-size="42" fill="%23e8e8e8">V = πr²h</text><text x="200" y="300" font-family="Times New Roman" font-size="45" fill="%23e8e8e8" font-style="italic">y = mx + c</text><text x="800" y="350" font-family="Times New Roman" font-size="40" fill="%23e8e8e8">A = ½bh</text><text x="100" y="500" font-family="Times New Roman" font-size="44" fill="%23e8e8e8" font-style="italic">sin²θ + cos²θ = 1</text><text x="650" y="550" font-family="Times New Roman" font-size="42" fill="%23e8e8e8">∫ f(x)dx</text><text x="300" y="700" font-family="Times New Roman" font-size="46" fill="%23e8e8e8" font-style="italic">(x+y)² = x²+2xy+y²</text></svg>');
            background-size: cover;
            background-position: center;
            z-index: -1;
            pointer-events: none;
        }
        
        .container {
            max-width: 900px;
            margin: 0 auto;
            padding: 60px 20px;
        }
        
        h1 {
            font-size: 48px;
            font-weight: 700;
            color: #000;
            margin-bottom: 50px;
            text-align: center;
            letter-spacing: -1px;
        }
        
        .apps-list {
            display: grid;
            gap: 0;
        }
        
        .app-item {
            border-top: 2px solid #cfcfcf;
            padding: 20px 0;
            transition: all 0.15s ease;
        }
        
        .app-item:last-child {
            border-bottom: 2px solid #cfcfcf;
        }
        
        .app-item:hover {
            background: rgba(37, 99, 235, 0.02);
            padding-left: 12px;
        }
        
        .app-link {
            color: #000;
            text-decoration: none;
            font-size: 28px;
            font-weight: 600;
            display: flex;
            align-items: center;
            gap: 12px;
            transition: color 0.15s ease;
        }
        
        .app-link:hover {
            color: #2563eb;
        }
        
        .app-link::before {
            content: '▸';
            color: #2563eb;
            font-size: 24px;
            transition: transform 0.15s ease;
        }
        
        .app-link:hover::before {
            transform: translateX(4px);
        }
        
        @media (max-width: 600px) {
            .container {
                padding: 40px 16px;
            }
            
            h1 {
                font-size: 36px;
                margin-bottom: 36px;
            }
            
            .app-link {
                font-size: 22px;
            }
            
            .app-item {
                padding: 16px 0;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Apps</h1>
        <div class="apps-list">
'''
    
    # Add links for each HTML file (excluding index.html itself)
    for html_file in html_files:
        if html_file != 'index.html':
            # Create a display name from the filename
            display_name = html_file.replace('.html', '').replace('-', ' ').replace('_', ' ').title()
            html_content += f'            <div class="app-item">\n'
            html_content += f'                <a href="{html_file}" class="app-link">{display_name}</a>\n'
            html_content += f'            </div>\n'
    
    html_content += '''        </div>
    </div>
</body>
</html>'''
    
    # Write the index.html file
    index_path = apps_dir / 'index.html'
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"Index built successfully with {len(html_files) - 1} apps")
    print(f"Location: {index_path}")

if __name__ == '__main__':
    build_app_index()
