# Start here

## First meeting — inside Day 001's time

Choose Developer 1 and Developer 2. Add actual GitHub usernames only when known and explicitly requested. Do not substitute the repository owner or publish private email addresses. Both people should be able to clone/read the public repository; write access and issue assignment require identified accounts.

Agree on the two longer weekly sessions and a shared review time. The default is 3 hours on five days and 4 hours on two days. This includes breaks, reading, coding, discussion, review, and integration. It is about 23 hours per week for 26 weeks.

Check that each person can open a folder, save a text file, and open a terminal. A terminal is a text window for asking programs to run; it is different from a Python prompt. Explain those steps slowly when needed. Earlier experience in another language does not let a learner skip the Python proof exercises automatically.

## Run the small starter

Use a supported CPython 3.13 or later installation. From the repository folder:

```text
python --version
python run_demo.py
```

On Windows, `py -3.13 run_demo.py` is another option when that version is installed. Do not paste the example prompt characters `>>>` into the terminal. The starter has no external package requirements and performs no network calls, writes, or agent actions.

Expected output names LearnForge, says **starter**, and lists the welcome screen as the only implemented capability. That is intentional. The learners implement the course features gradually.

In week 3, learn virtual environments and imports. In week 5, learn package installation. The coach handles setup friction without turning Day 001 into a package-management lesson. Save exact runtime/dependency versions when the phase introduces external packages. Read [SOURCES.md](SOURCES.md) for the teaching baseline and update policy.

## Daily routine

1. Open the day guide and its issue. Read the goal and concrete examples together.
2. Each person recalls older ideas and answers the Question of the Day independently.
3. Explain today's concept and its system-design connection. Set the smallest shared input/output agreement before parallel work.
4. Each person implements their assigned production slice and a short personal proof in their own practice folder.
5. Review the partner's PR, explain one edge case, and let the author make any correction.
6. Integrate and run the visible feature. Record personal evidence. Leave the issue open if either person has an unmet check.

## If the workload does not fit

Use the review day to finish a bounded gap. First reduce unnecessary polish, extra abstractions, repeated reading, and broad test work. Preserve the core concept, individual proof, review, working increment, and critical permission/data/effect checks. If those still do not fit, record the extra session needed and move dependent work. Do not silently drop concepts or award a pass because six months is approaching.

## Learning tools

A text editor, Python, Git, and the public repository are enough to start. Add a relational database, containers, model SDK, and an agent framework only when the course reaches them. Use synthetic data and offline fakes for ordinary development. A GPU or paid model account is optional; resource-limited alternatives are included. No API documentation is required.
