# Repository guidance

- This repository is a Python workspace managed with `uv`; the root project and service packages require Python 3.15 or newer.
- Keep the public website service in `services/public-website/` and its Python source under `src/public_website/`.
- The FastAPI application is `public_website.main:app`. Run it from the workspace root with `uv run uvicorn public_website.main:app --reload`.
- Add automated tests under `tests/`. There is currently no test runner configured.
- Update dependency declarations in the relevant `pyproject.toml` and keep `uv.lock` in sync through `uv`.
- Follow existing Python style: four-space indentation, type annotations, and focused changes.
