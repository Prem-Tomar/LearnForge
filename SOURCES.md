# Sources and version policy

Official sources inspected while preparing this course on **1 November 2026**. External pages can change. Use section names and the version policy below. These links support the teaching; none is required to be read end to end.

- [Python tutorial, selected named sections](https://docs.python.org/3.13/tutorial/)
- [pytest fixtures and isolation](https://docs.pytest.org/en/stable/how-to/fixtures.html)
- [FastAPI user guide, selected named sections](https://fastapi.tiangolo.com/tutorial/)
- [SQLAlchemy 2.0 teaching reference](https://docs.sqlalchemy.org/en/20/tutorial/)
- [PostgreSQL tutorial](https://www.postgresql.org/docs/current/tutorial.html)
- [NumPy beginner guide](https://numpy.org/doc/stable/user/absolute_beginners.html)
- [Hugging Face LLM course](https://huggingface.co/learn/llm-course/chapter1/1)
- [Official OpenAI documentation: tools](https://developers.openai.com/api/docs/guides/tools)
- [Official OpenAI documentation: evaluation practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices)
- [LangGraph overview](https://docs.langchain.com/oss/python/langgraph/overview)
- [MCP introduction](https://modelcontextprotocol.io/docs/getting-started/intro)
- [Docker getting started](https://docs.docker.com/get-started/)
- [GitHub Actions quickstart](https://docs.github.com/en/actions/get-started/quickstart)
- [MDN JavaScript fundamentals](https://developer.mozilla.org/en-US/curriculum/core/javascript-fundamentals/), [closures](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Closures), [promises](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises), and [execution model](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Execution_model)
- [MDN ES modules](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules)
- [React learning guide](https://react.dev/learn), [state snapshots](https://react.dev/learn/state-as-a-snapshot), and [effects/cleanup](https://react.dev/learn/synchronizing-with-effects)
- [React Native introduction](https://reactnative.dev/docs/getting-started), [framework/setup choices](https://reactnative.dev/docs/environment-setup), and [security/storage](https://reactnative.dev/docs/security)

## Teaching baseline and updates

Use an available supported **CPython 3.13 or later** runtime. Record the exact version and GIL/free-threaded build used. The versioned Python 3.13 reference is a deliberate stable teaching baseline, not a claim that it is the newest release. Use Pydantic v2 concepts and a compatible FastAPI version. SQLAlchemy's 2.0 tutorial is a deliberate teaching reference; record the installed supported series and read its migration notes when it differs. Resolve a compatible environment at the start of each phase and save its lock/version record; rehearse upgrades before adopting them.

Provider SDKs, models, context limits, structured-output support, prices, and agent framework APIs change. Check current official documentation when implementing that lesson. Model IDs and unit prices belong in configuration, not memorized course claims. No paid plan, GPU, hosted database, or model API key is needed for the initial offline product; later lessons retain a fake/local inspection path. Optional real-provider experiments must use an explicit small budget and synthetic data.

The coach supplies explanations for true beginners: the official Python tutorial itself assumes some programming background. Our first lessons explain files, values, terminal use, and control flow before relying on the tutorial.
