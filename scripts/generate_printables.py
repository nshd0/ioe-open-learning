#!/usr/bin/env python3
import re
import os
import subprocess

ROOT = os.path.join(os.path.dirname(__file__), '..')

def md_to_html(md):
    lines = md.splitlines()
    out = []
    in_ul = False
    for line in lines:
        line = line.rstrip()
        if not line:
            if in_ul:
                out.append('</ul>')
                in_ul = False
            out.append('')
            continue
        m = re.match(r'^(#{1,6})\s+(.*)$', line)
        if m:
            if in_ul:
                out.append('</ul>')
                in_ul = False
            level = len(m.group(1))
            out.append(f'<h{level}>{m.group(2)}</h{level}>')
            continue
        m = re.match(r'^[-\*]\s+(.*)$', line)
        if m:
            if not in_ul:
                out.append('<ul>')
                in_ul = True
            out.append(f'  <li>{m.group(1)}</li>')
            continue
        # fallback: paragraph
        if in_ul:
            out.append('</ul>')
            in_ul = False
        out.append(f'<p>{line}</p>')
    if in_ul:
        out.append('</ul>')
    return '\n'.join(out)

def make_print_html(src_path, out_path):
    with open(src_path, 'r', encoding='utf-8') as f:
        md = f.read()
    body = md_to_html(md)
    title = os.path.splitext(os.path.basename(src_path))[0].replace('-', ' ').title()
    html = f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>{title} — Printable</title>
  <style>
    body{{font-family: Arial, Helvetica, sans-serif;max-width:800px;margin:0 auto;padding:20px;color:#111}}
    h1{{font-size:1.4rem;margin-top:0}}
    h2{{font-size:1.1rem}}
    p{{line-height:1.4}}
    ul{{margin-left:1.2rem}}
    .worksheet{{border-top:1px dashed #666;margin-top:1rem;padding-top:1rem}}
    .box{{border:1px solid #000;height:48px;margin:6px 0}}
  </style>
</head>
<body>
{body}
<section class="worksheet">
  <h2>Worksheet</h2>
  <p>Use the space below to complete the task. Draw or write your answers.</p>
  <div class="box"></div>
  <div class="box"></div>
  <div class="box"></div>
  <div class="box"></div>
</section>
</body>
</html>'''
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html)

def try_pdf(html_path, pdf_path):
    # Try wkhtmltopdf if available
    try:
        subprocess.run(['wkhtmltopdf', html_path, pdf_path], check=True)
        return True
    except Exception:
        return False

def main():
    lessons_root = os.path.join(ROOT, 'grades')
    generated = []
    for grade in sorted(os.listdir(lessons_root)):
        grade_path = os.path.join(lessons_root, grade, 'lessons')
        if not os.path.isdir(grade_path):
            continue
        out_dir = os.path.join(os.path.dirname(grade_path), 'printables')
        for fname in sorted(os.listdir(grade_path)):
            if not fname.endswith('.md'):
                continue
            src = os.path.join(grade_path, fname)
            base = os.path.splitext(fname)[0]
            out_html = os.path.join(out_dir, f'{base}-print.html')
            out_pdf = os.path.join(out_dir, f'{base}-print.pdf')
            make_print_html(src, out_html)
            pdf_ok = try_pdf(out_html, out_pdf)
            generated.append((out_html, out_pdf if pdf_ok else None))
    print('Generated:', len(generated))
    for h,p in generated:
        print(h, '->', p or '(pdf skipped)')

if __name__ == '__main__':
    main()
