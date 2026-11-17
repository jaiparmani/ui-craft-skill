# Before / After

Typical "default AI" output on the left of each pair, the corrected version on the right, with the reasoning. Use these to recognize the patterns in your own first drafts.

---

## 1. Stat card

**Before**
```html
<div class="card" style="text-align:center; padding:20px; border-radius:20px;
     box-shadow:0 10px 30px rgba(0,0,0,.2); background:linear-gradient(135deg,#667eea,#764ba2); color:#fff">
  <div style="font-size:40px">💰</div>
  <h3 style="font-weight:bold">Total Revenue</h3>
  <p style="font-size:32px; font-weight:bold">$68240</p>
  <p style="color:#ccc">+8.1%</p>
</div>
```

**After**
```html
<div class="kpi">
  <div class="label">Revenue (Nov)</div>          <!-- 13px, --text-muted -->
  <div class="value num">$68,240</div>            <!-- 26px/600, tabular, tight tracking -->
  <div class="delta"><b class="up">+8.1%</b> vs October</div>
</div>
```

**Why**
- Gradient + white text + heavy shadow is decoration, not information. The value is what matters; everything else got quieter.
- Emoji icon removed — adds nothing, looks unprofessional.
- Label de-emphasized (muted, small) instead of bold; the value carries the weight.
- Number formatted with separators and `tabular-nums`.
- Delta has color *and* sign and context ("vs October") — color alone is ambiguous and inaccessible.
- Left-aligned so a row of KPIs shares a reading edge.

---

## 2. Hero section

**Before**
```html
<section style="text-align:center; padding:100px; background:linear-gradient(to right,#8e2de2,#4a00e0)">
  <h1 style="font-size:56px; color:white">🚀 Welcome to Fieldnote</h1>
  <p style="color:#ddd">The ultimate AI-powered solution to unlock your productivity potential!</p>
  <button style="border-radius:50px; padding:15px 40px; background:#ff6b6b">Get Started</button>
  <button style="border-radius:50px; padding:15px 40px; background:#4ecdc4">Learn More</button>
</section>
```

**After** (see `landing.html`)
```html
<section class="hero">                      <!-- 2-col grid: copy left, real product visual right -->
  <div>
    <span class="overline">Research notebook</span>
    <h1>Every idea, with its <em>source</em> attached.</h1>
    <p class="lede">Fieldnote links each highlight back to the paper, interview or page it came from…</p>
    <a class="btn btn-primary">Start writing — it’s free</a>
    <a class="btn btn-ghost">Watch a 2-min tour</a>
  </div>
  <div class="shot">…an actual UI of the product…</div>
</section>
```

**Why**
- Headline states the specific benefit; "Welcome to X" and "unlock your potential" say nothing.
- Two CTAs with equal loud colors compete; now one primary (solid ink) and one ghost.
- Three unrelated colors (purple, coral, teal) replaced by one deliberate accent.
- Showing the product proves the claim; an empty gradient doesn't.
- Left alignment + asymmetry reads as designed; centered-everything reads as template.
- Display serif chosen for the Editorial direction gives the page a voice.

---

## 3. Form field

**Before**
```html
<input placeholder="Enter your workspace URL" style="border:2px solid #ccc; border-radius:25px; padding:12px; width:100%">
<p style="color:red">Invalid!</p>
```

**After** (see `settings-form.html`)
```html
<div class="field invalid">
  <label for="url">Workspace URL</label>
  <div class="prefix"><span>app.example.com/</span>
    <input class="input" id="url" aria-invalid="true" aria-describedby="url-err"></div>
  <p class="error" id="url-err"><svg>…</svg>Use only lowercase letters, numbers and hyphens — try “acme-robotics”.</p>
</div>
```

**Why**
- Placeholder-as-label disappears on typing and fails accessibility; a real `<label>` is always visible.
- The error explains how to fix it and suggests a value, rather than blaming the user.
- `aria-describedby` connects the error for screen readers; an icon plus text means it doesn't rely on red alone.
- 1px border, radius matching the rest of the system; pill inputs + 2px gray borders look dated.
- Prefix shows the user the context of what they're typing.

---

## 4. Feature section

**Before:** three identical cards in a row, each with a big emoji or icon in a colored circle, a bold title, and two lines of vague copy ("Lightning fast", "Secure", "Easy to use").

**After:** two or three alternating rows — copy on one side (overline, strong headline, a concrete paragraph, a short checklist), and on the other side a real fragment of the product demonstrating that feature (a citation, a version timeline).

**Why:** identical icon cards are the most recognizable template pattern on the web and communicate no specifics. Showing the feature *working* is more persuasive and gives the page rhythm.

---

## 5. Data table

**Before:** zebra stripes in two shades of blue, vertical and horizontal borders on every cell, centered text, numbers like `12400` left-aligned, status shown as bright red/green text, action buttons "Edit" "Delete" "View" on every row.

**After:** horizontal dividers only, left-aligned text and right-aligned tabular numbers formatted as currency, muted secondary columns and a weight-500 primary column, soft dot badges for status, and a single `⋯` menu per row.

**Why:** grid lines everywhere create noise that competes with data; right alignment lets you compare magnitudes at a glance; three buttons per row multiply visual weight by the row count.
