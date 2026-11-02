"""Check durable issue-format rules before publication; semantic teaching still needs review."""
from __future__ import annotations

import argparse
import ast
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
FORBIDDEN_POLICY = (
    'review-approved', 'Review, closure, and the next assignment', 'Separate frontend review gate',
    'Rolling queue', 'seven open tasks', 'Only one open task is assigned',
)
VAGUE_CONTRACT = ('agreed status dict', 'no useful return value', 'tbd', '(...)', 'see the linked guide')
REVIEW_PARTS = ('Where', 'What happens now', 'What the task asks for',
                'Why this does not meet the task', 'Smallest change', 'How to check')


def validate_review_policy(policy):
    feedback = policy.get('review_feedback', {})
    errors = []
    for flag in ('mandatory', 'applies_to_all_tracks', 'plain_english', 'explain_new_terms',
                 'explicit_task_reference', 'task_links_optional', 'separate_bugs_suggestions_and_coaching'):
        if feedback.get(flag) is not True:
            errors.append('non-negotiable review feedback rule missing: ' + flag)
    if feedback.get('required_parts') != list(REVIEW_PARTS):
        errors.append('review findings must retain all six learner-friendly parts')
    return errors


def validate_review_finding(body):
    """Check structure only; reviewers still verify clarity, correctness and evidence."""
    errors = []
    sections = {}
    for part in REVIEW_PARTS:
        match = re.search(r'^\*\*' + re.escape(part) + r':\*\*\s*(.*?)(?=^\*\*|\Z)', body, re.M | re.S)
        if not match or not match.group(1).strip():
            errors.append('review finding missing: ' + part)
        else:
            sections[part] = match.group(1)
    if not re.search(r'`[^`\n]+\.[A-Za-z0-9]+:\d+(?:-\d+)?`', sections.get('Where', '')):
        errors.append('review finding must name the exact file and line(s) in Where')
    task_reference = r'\b(?:day|session)\s+\d{1,3}\b|\btask\s+#?\d+\b|(?<!\w)#\d+\b|https://github\.com/[^/\s)]+/[^/\s)]+/issues/\d+'
    if not re.search(task_reference, sections.get('What the task asks for', ''), re.I):
        errors.append('review finding must name the day/task beside its expected behavior; a link is optional')
    return errors


def validate_blueprint(row, policy, core):
    errors = []
    body = row.get('body', '')
    label = row.get('title', 'unnamed task')
    if not body.startswith('> [!IMPORTANT]\n> ## Question of the Day\n> '):
        errors.append('Question of the Day must be a top callout')
    if '**Question of the Day:**' in body:
        errors.append('duplicate/buried question block')
    if not row.get('inline_teaching'):
        errors.append('inline teaching or explicit known-concept application is required')
    if 'teaching_guide' in row or '/blob/main/lessons/' in body or '/blob/main/days/' in body:
        errors.append('task teaching must not require another lesson file')
    if '## Acceptance criteria' not in body:
        errors.append('missing acceptance criteria')
    if not ('## Research hints' in body or '## Hints to research' in body):
        errors.append('missing focused research hints')
    if not re.search(r'^1\..+\n2\..+\n3\.', body, re.M):
        errors.append('three progressive research hints are required')
    if not ('**Input' in body or '**Required input/output behavior:**' in body or 'Test inputs and expected results' in body):
        errors.append('missing input/output cases')
    if not ('**Output' in body or '**Expected return' in body or '**Expected outputs' in body or 'expected outputs' in body or '**Required input/output behavior:**' in body or 'Test inputs and expected results' in body):
        errors.append('missing expected results')
    has_unit = bool(row.get('file') and row.get('unit')) if core else bool(row.get('files') and row.get('units'))
    if not has_unit:
        errors.append('missing exact file and named unit metadata')
    for phrase in FORBIDDEN_POLICY:
        if phrase.lower() in body.lower():errors.append('project policy belongs outside issues: '+phrase)
    for phrase in VAGUE_CONTRACT:
        if phrase in body.lower():errors.append('undefined contract wording: '+phrase)
    main = re.sub(r'<details>.*?</details>', '', body, flags=re.S)
    if len(main.split()) > policy['max_main_issue_words']:
        errors.append('main task is too long; keep optional depth expandable')
    if len(body.split()) > policy['max_total_issue_words']:
        errors.append('task exceeds the total teaching budget')
    return [label+': '+message for message in errors]


def validate(root=ROOT):
    policy = json.loads((root/'curriculum/coaching-policy.json').read_text(encoding='utf-8'))
    errors = validate_review_policy(policy)
    cohort=json.loads((root/'curriculum/cohort.json').read_text(encoding='utf-8'))
    frontend=json.loads((root/'curriculum/frontend-cohort.json').read_text(encoding='utf-8'))
    if (cohort['open_limit'],cohort['assigned_limit']) != (policy['core_queue']['prepared'],policy['core_queue']['assigned']):
        errors.append('Python queue configuration does not match the recorded assignment rule')
    if (frontend['prepared_limit'],frontend['assigned_limit_per_frontend_queue']) != (policy['frontend_queue']['prepared'],policy['frontend_queue']['assigned']):
        errors.append('frontend queue configuration does not match the recorded assignment rule')
    if policy['revision_topic_days'] != [1,3,7,10,15] or policy['revision_date_offsets'] != [0,2,6,9,14]:
        errors.append('revision cycle must stay topic-relative: days 1/3/7/10/15')
    if not policy['revision_days_allow_other_topics']:
        errors.append('revision checkpoints cannot reserve the whole day')
    counts = {}
    for name,core in [('issue-blueprints',True),('frontend-blueprints',False)]:
        count=0
        for path in sorted((root/'curriculum'/name).glob('*.json')):
            for row in json.loads(path.read_text(encoding='utf-8')):
                errors.extend(validate_blueprint(row,policy,core));count+=1
        counts[name]=count
    if (counts['issue-blueprints'],counts['frontend-blueprints']) != (1092,90):
        errors.append('planned task count changed; review scope/dependencies explicitly')
    if (root/'lessons').exists():
        errors.append('separate per-task lesson tree must not be recreated')
    for path in (root/'src').rglob('*.py'):
        if any(re.fullmatch(r'learner[-_]\d{2}(?:\.py)?',part) for part in path.relative_to(root/'src').parts):
            errors.append(str(path.relative_to(root))+': use a feature-based production name')
        if policy['api_documentation_requested']:continue
        tree=ast.parse(path.read_text(encoding='utf-8'),filename=str(path))
        for node in ast.walk(tree):
            if isinstance(node,ast.Call) and ((isinstance(node.func,ast.Name) and node.func.id=='FastAPI') or (isinstance(node.func,ast.Attribute) and node.func.attr=='FastAPI')):
                keys={k.arg:k.value for k in node.keywords}
                if any(key not in keys or not isinstance(keys[key],ast.Constant) or keys[key].value is not None for key in ['docs_url','redoc_url','openapi_url']):
                    errors.append(str(path.relative_to(root))+': API docs require an explicit request')
    return errors, counts


if __name__ == '__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--json',action='store_true')
    parser.add_argument('--review-finding',type=Path,help='Check a bug finding before posting it')
    args=parser.parse_args()
    errors,counts=validate()
    if args.review_finding:
        errors.extend(validate_review_finding(args.review_finding.read_text(encoding='utf-8')))
    print(json.dumps({'valid':not errors,'task_counts':counts,'errors':errors},indent=2))
    raise SystemExit(1 if errors else 0)
