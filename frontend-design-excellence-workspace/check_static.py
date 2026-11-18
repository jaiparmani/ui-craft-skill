"""Static checks for expressive test outputs. Usage: python3 check_static.py <iteration-dir>"""
import json
import re
import sys
from pathlib import Path

LAYOUT_PROPS = r"(?:top|left|right|bottom|width|height|margin(?:-\w+)?)"


def keyframe_layout_props(css):
    hits = []
    for m in re.finditer(r"@keyframes\s+([\w-]+)\s*\{((?:[^{}]*\{[^{}]*\})*[^{}]*)\}", css):
        body = m.group(2)
        if re.search(rf"(?<![-\w]){LAYOUT_PROPS}\s*:", body):
            hits.append(m.group(1))
    return hits


def tween_layout_props(js):
    # gsap.to/from/fromTo(..., { width: ..., top: ... }) and motion animate({ height })
    hits = []
    for m in re.finditer(r"(?:gsap\.(?:to|from|fromTo|set)|\.to|\.from|\.fromTo|animate)\s*\(([^;]{0,400})", js):
        seg = m.group(1)
        if re.search(rf"[{{,]\s*{LAYOUT_PROPS}\s*:", seg) and "gsap.set" not in m.group(0):
            hits.append(seg[:80].replace("\n", " "))
    return hits


def main(root):
    out = {}
    for f in sorted(Path(root).glob("*/*/outputs/index.html")):
        src = f.read_text(errors="ignore")
        css = "\n".join(re.findall(r"<style[^>]*>(.*?)</style>", src, re.S))
        js = "\n".join(re.findall(r"<script(?![^>]*src)[^>]*>(.*?)</script>", src, re.S))
        key = "/".join(f.parts[-4:-2])
        out[key] = {
            "bytes": len(src),
            "libs": sorted(set(re.findall(r"(gsap|ScrollTrigger|SplitText|lenis|three|motion|lottie)[@/.\w-]*\.(?:min\.)?js", src, re.I))),
            "reduced_motion": "prefers-reduced-motion" in src,
            "smooth_scroll": bool(re.search(r"lenis|locomotive|scroll-behavior\s*:\s*smooth|lerp", src, re.I)),
            "pin_or_sticky": bool(re.search(r"pin\s*:\s*(true|['\"#.])|position\s*:\s*sticky", src)),
            "keyframes_layout": keyframe_layout_props(css),
            "tweens_layout": tween_layout_props(js),
            "emoji": "".join(sorted(set(re.findall(r"[\U0001F300-\U0001FAFF☀-➿]", re.sub(r"<[^>]+>", "", src))))),
            "gradients": len(re.findall(r"(linear|radial|conic)-gradient", src)),
            "split_or_mask": bool(re.search(r"SplitText|clip-path|overflow\s*:\s*hidden[^}]*\}[^{]*\.(line|word)", src)),
        }
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main(sys.argv[1])
