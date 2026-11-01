# Teach first, then mixed revision on topic days 1, 3, 7, 10 and 15

Every learner has a separate cycle for every topic, across Python, APIs, SQL, mathematics, AI/ML, GenAI, agents, architecture, operations and client tracks. **Topic day 1 is the day that learner is first taught that topic**, not always course day 1. Topic days 3/7/10/15 fall 2/6/9/14 calendar days after that first teaching date. A merged teammate's implementation does not start another learner's clock.

| Topic day | What the learner does | Coach/reviewer response |
|---|---|---|
| 1 | Learn the required terms/syntax from a small working example; then make a bounded project-function change and answer a guided question | Run the code; explain every relevant line's purpose, before/after values and project contribution |
| 3 | Revisit with different values and predict before running | Compare actual output with the prediction and repair misunderstandings |
| 7 | Predict a changed condition, mutation, call order or failure using the same concept | Trace why it behaves that way; include unchanged state and one fresh variation |
| 10 | Diagnose a small bug or compare two approaches | Show execution evidence and explain the cause, bounded fix and trade-off |
| 15 | Solve a harder interview-style variation using the topic | Require independent coding/reasoning/debugging and transfer to the project, with feedback and repair |

**A checkpoint does not reserve the entire day.** Continue the current project work, ask other topic questions, and mix earlier completed topics into the same review. Several topics can be at different stages on one date. Related concepts can share one small example when the evidence identifies each concept covered. Never mark a topic revised merely because it appeared in someone else's answer.

Teach every newly required construct before use. Reduce repeated scaffolding as the learner demonstrates understanding; later questions emphasize independent debugging, design and interview explanation. If a new term appears inside a harder variation, explain it first. Harder does not mean using untaught language features.

Keep revision inside scheduled recall/review blocks. If due work does not fit, record it honestly as overdue, use an explicit repair block and adjust the calendar before adding more topics; do not drop core concepts, invent a pass or silently add homework. A correct implementation and unresolved conceptual coaching remain separate. After day 15, keep weak topics warm through mixed project/interview questions.

## Track actual teaching and attempts

Record the real first-teaching date in [topic introductions](progress/topic-introductions.csv). Use one row per learner/track/topic; topic IDs can come from the [shared React inventory](curriculum/react-pair-concepts.json), a daily subject, or a named Python/ML/math concept. Group a coherent topic only when the same example genuinely covers its concepts. Existing concept/mastery records remain intact.

Record actual checkpoint attempts in [revision attempts](progress/revision-attempts.csv), including status, question/code revision, execution evidence and follow-up. Nothing is prefilled as learned, executed or passed. `passed` completes that checkpoint; `partial` or `needs-repair` stays visible. Other checkpoints remain independent.

Run `python tools/revision_schedule.py --on 2026-11-01` with the intended local review date, optionally `--learner PratikTalware26`. The supplied date avoids accidentally using a machine's different timezone. The tool lists due/overdue checkpoints for **all entered topics**, not one exclusive question. It neither changes issues nor sends messages or assumes a topic has been taught. Use [the existing question bank](questions/README.md) plus mixed due-topic questions, not a replacement for either.

## Short review trace

Show command, actual input/output and revision. Then use **line/event → name/object/class/attribute before → after or no change → why → contribution**. Follow actual call order and run a changed case. If not executed, state that and label predictions. Use [REVIEW_GUIDE.md](REVIEW_GUIDE.md) and [small execution pictures](EXECUTION_VISUALS.md). Keep the task teaching in the issue, using clear sections and optional expandable detail; shared rules remain in the project guides.
