import os, re, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

root = 'docs'
reserved = {'index.md', 'log.md'}
VOCAB = {'Runbook', 'Reference', 'Policy', 'Script', 'Template'}

bad = []
files = []
for dp, dn, fn in os.walk(root):
    for f in fn:
        if not f.endswith('.md'):
            continue
        p = os.path.join(dp, f).replace(os.sep, '/')
        files.append(p)
        txt = open(p, encoding='utf-8').read()
        if f in reserved:
            if f == 'index.md' and p != 'docs/index.md' and txt.startswith('---'):
                bad.append((p, 'reserved file carries frontmatter'))
            continue
        if not txt.startswith('---'):
            bad.append((p, 'NO FRONTMATTER'))
            continue
        fm = txt.split('---', 2)[1]
        for k in ('type:', 'title:', 'description:', 'tags:', 'generated:', 'status:'):
            if k not in fm:
                bad.append((p, 'missing ' + k))
        m = re.search(r'^type:\s*(\S+)', fm, re.M)
        if m and m.group(1) not in VOCAB:
            bad.append((p, 'type outside vocabulary: ' + m.group(1)))

missing = []
for p in files:
    for ln, line in enumerate(open(p, encoding='utf-8'), 1):
        for tgt in re.findall(r'\]\((/[^)#\s]+\.md)', line):
            if not os.path.exists(os.path.join(root, tgt.lstrip('/'))):
                missing.append((p, ln, tgt))
        for tgt in re.findall(r'\]\((?!/)(?!https?:)(?!mailto:)([^)#\s]+\.md)', line):
            if not os.path.exists(os.path.join(os.path.dirname(p), tgt)):
                missing.append((p, ln, tgt + ' [relative]'))

dirs = sorted({os.path.dirname(p) for p in files})
noindex = [d for d in dirs if not os.path.exists(os.path.join(d, 'index.md'))]

print('md files:', len(files))
print('directories:', len(dirs))
print()
print('DIRECTORIES MISSING index.md:', len(noindex))
for d in noindex:
    print('  ', d)
print()
print('FRONTMATTER ISSUES:', len(bad))
for b in bad:
    print('  ', b)
print()
print('BROKEN LINKS:', len(missing))
for m in missing:
    print('  ', m)
