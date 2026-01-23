import os
from pathlib import Path


def build_app_index():
    # Set the directory path
    apps_dir = Path(r"E:\apps")

    # Get all HTML files in the apps directory (not in subdirectories)
    html_files = sorted([f.name for f in apps_dir.glob("*.html") if f.is_file()])

    # Brand config (easy to tweak later)
    BRAND_NAME = "Mr Downes Maths"
    TAGLINE = "Smarter learning. On your terms."
    PAGE_TITLE = f"{BRAND_NAME} — Apps"
    HEADER_CTA_1 = ("Start", "#")     # Change to your preferred landing/route
    HEADER_CTA_2 = ("Quizzes", "#")   # Change to your quizzes index/route

    # Create the index.html content
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{PAGE_TITLE}</title>
  <meta name="description" content="{BRAND_NAME}: {TAGLINE}">
  <style>
    :root {{
      /* Neutrals */
      --bg: #ffffff;
      --surface: #f7f7f8;
      --surface2: #f2f2f4;
      --text: #0f172a;
      --muted: rgba(15, 23, 42, .70);
      --border: rgba(0,0,0,.10);
      --shadow: rgba(0,0,0,.08);

      /* Accents */
      --blue: #1f6feb;
      --red: #e11d48;
      --green: #16a34a;

      /* Geometry */
      --r: 14px;
      --pad: clamp(14px, 2.6vw, 22px);

      /* Typography */
      --font: ui-sans-serif, system-ui, -apple-system, "Segoe UI", Roboto, Arial, "Noto Sans", "Helvetica Neue", sans-serif;
    }}

    * {{ box-sizing: border-box; }}
    html, body {{ height: 100%; }}

    body {{
      margin: 0;
      background: var(--bg);
      color: var(--text);
      font-family: var(--font);
      line-height: 1.45;
      -webkit-font-smoothing: antialiased;
      text-rendering: geometricPrecision;
    }}

    /* Subtle background texture (kept ultra-light) */
    body::before {{
      content: '';
      position: fixed;
      inset: 0;
      background-image:
        radial-gradient(circle at 20% 10%, rgba(0,0,0,0.03), transparent 40%),
        radial-gradient(circle at 80% 20%, rgba(31,111,235,0.05), transparent 45%),
        radial-gradient(circle at 75% 85%, rgba(22,163,74,0.04), transparent 45%),
        radial-gradient(circle at 15% 85%, rgba(225,29,72,0.04), transparent 45%);
      pointer-events: none;
      z-index: -1;
    }}

    /* Sticky top bar (common actions above the fold) */
    .topbar {{
      position: sticky;
      top: 0;
      z-index: 50;
      padding: 10px var(--pad);
      background: rgba(255,255,255,0.86);
      backdrop-filter: blur(10px);
      border-bottom: 1px solid var(--border);
    }}

    .topbar-inner {{
      max-width: 1120px;
      margin: 0 auto;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 12px;
    }}

    .brand {{
      display: grid;
      gap: 2px;
      min-width: 200px;
    }}

    .brand-title {{
      display: flex;
      align-items: center;
      gap: 10px;
      font-weight: 750;
      letter-spacing: -0.02em;
      font-size: clamp(18px, 2.8vw, 22px);
      line-height: 1.1;
    }}

    .mark {{
      display: inline-flex;
      gap: 6px;
      transform: translateY(1px);
    }}
    .dot {{
      width: 8px;
      height: 8px;
      border-radius: 999px;
    }}
    .dot.blue {{ background: var(--blue); }}
    .dot.red {{ background: var(--red); }}
    .dot.green {{ background: var(--green); }}

    .tagline {{
      font-size: 12.5px;
      color: var(--muted);
      letter-spacing: -0.005em;
    }}

    .actions {{
      display: inline-flex;
      gap: 8px;
      flex-wrap: wrap;
      justify-content: flex-end;
      align-items: center;
    }}

    .btn {{
      appearance: none;
      border: 1px solid var(--border);
      background: color-mix(in srgb, var(--surface) 88%, transparent);
      color: var(--text);
      padding: 10px 12px;
      border-radius: 12px;
      font-weight: 650;
      font-size: 13px;
      letter-spacing: -0.01em;
      cursor: pointer;
      transition: transform .12s ease, background .12s ease, box-shadow .12s ease;
      box-shadow: 0 10px 22px -18px var(--shadow);
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 8px;
    }}
    .btn:hover {{
      transform: translateY(-1px);
      background: color-mix(in srgb, var(--surface) 96%, transparent);
    }}
    .btn:active {{ transform: translateY(0px); }}
    .btn.primary {{
      border-color: color-mix(in srgb, var(--blue) 55%, var(--border));
      background: color-mix(in srgb, var(--blue) 10%, var(--surface));
    }}
    .btn:focus-visible, a:focus-visible {{
      outline: 3px solid color-mix(in srgb, var(--blue) 55%, transparent);
      outline-offset: 2px;
    }}

    /* Page shell */
    .shell {{
      max-width: 1120px;
      margin: 0 auto;
      padding: var(--pad);
    }}

    .page-title {{
      margin: 14px 0 10px;
      font-size: clamp(22px, 3.3vw, 30px);
      letter-spacing: -0.03em;
      font-weight: 800;
    }}

    .page-subtitle {{
      margin: 0 0 16px;
      color: var(--muted);
      max-width: 70ch;
      font-size: 14.5px;
    }}

    /* Cards (your “HTML cells”) */
    .grid {{
      display: grid;
      gap: 12px;
      grid-template-columns: 1fr;
    }}
    @media (min-width: 760px) {{
      .grid {{ grid-template-columns: repeat(2, minmax(0, 1fr)); }}
    }}
    @media (min-width: 1080px) {{
      .grid {{ grid-template-columns: repeat(3, minmax(0, 1fr)); }}
    }}

    .card {{
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: var(--r);
      padding: clamp(14px, 2.2vw, 18px);
      box-shadow:
        0 22px 50px -38px var(--shadow),
        inset 0 1px 0 rgba(255,255,255,0.6); /* subtle “dish” highlight */
      transition: transform .12s ease, box-shadow .12s ease, border-color .12s ease;
    }}
    .card:hover {{
      transform: translateY(-1px);
      border-color: color-mix(in srgb, var(--blue) 18%, var(--border));
      box-shadow:
        0 26px 58px -40px var(--shadow),
        inset 0 1px 0 rgba(255,255,255,0.6);
    }}

    .card a {{
      color: inherit;
      text-decoration: none;
      display: grid;
      gap: 6px;
    }}

    .card-title {{
      font-weight: 750;
      letter-spacing: -0.02em;
      font-size: 16px;
      display: flex;
      align-items: center;
      gap: 10px;
    }}

    .chev {{
      width: 26px;
      height: 26px;
      border-radius: 10px;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      background: color-mix(in srgb, var(--surface2) 92%, transparent);
      border: 1px solid var(--border);
      color: var(--blue);
      flex: 0 0 auto;
    }}

    .card-meta {{
      color: var(--muted);
      font-size: 13px;
    }}

    /* Mobile spacing tweaks */
    @media (max-width: 600px) {{
      .page-subtitle {{ font-size: 14px; }}
      .btn {{ padding: 9px 11px; }}
    }}
  </style>
</head>

<body>
  <header class="topbar">
    <div class="topbar-inner">
      <div class="brand">
        <div class="brand-title">
          <span class="mark" aria-hidden="true">
            <span class="dot blue"></span>
            <span class="dot red"></span>
            <span class="dot green"></span>
          </span>
          {BRAND_NAME}
        </div>
        <div class="tagline">{TAGLINE}</div>
      </div>

      <div class="actions">
        <a class="btn primary" href="{HEADER_CTA_1[1]}">{HEADER_CTA_1[0]}</a>
        <a class="btn" href="{HEADER_CTA_2[1]}">{HEADER_CTA_2[0]}</a>
      </div>
    </div>
  </header>

  <main class="shell">
    <h1 class="page-title">Apps</h1>
    <p class="page-subtitle">
      Choose an app below. Everything here is designed to be clear, responsive, and feedback-driven.
    </p>

    <section class="grid">
"""

    # Add links for each HTML file (excluding index.html itself)
    count = 0
    for html_file in html_files:
        if html_file.lower() == "index.html":
            continue

        display_name = (
            html_file.replace(".html", "")
            .replace("-", " ")
            .replace("_", " ")
            .title()
        )

        html_content += f"""
      <article class="card">
        <a href="{html_file}">
          <div class="card-title">
            <span class="chev" aria-hidden="true">▸</span>
            <span>{display_name}</span>
          </div>
          <div class="card-meta">{html_file}</div>
        </a>
      </article>
"""
        count += 1

    html_content += """
    </section>
  </main>
</body>
</html>
"""

    # Write the index.html file
    index_path = apps_dir / "index.html"
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    print(f"Index built successfully with {count} apps")
    print(f"Location: {index_path}")


if __name__ == "__main__":
    build_app_index()
