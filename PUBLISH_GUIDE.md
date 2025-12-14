# How to Publish 'test_failure_llm' to PyPI

I have already built the distribution files for you!

## Step 1: Create a PyPI Account
If you don't have one, register at:
https://pypi.org/account/register/

## Step 2: Get an API Token
1. Log in to PyPI.
2. Go to **Account Settings**.
3. Scroll to **API Tokens** and click "Add API Token".
4. Name it `test-failure-llm-token` and choose Scope: "Entire Account" (for the first time).
5. **Copy the token** (starts with `pypi-...`).

## Step 3: Upload (Run this in your terminal)
Run the following command. When asked for `username`, type `__token__`. When asked for `password`, paste your API token.

```bash
python -m twine upload dist/*
```

## Troubleshooting
- **Name Conflict**: If `test_failure_llm` is already taken on PyPI, you will get a 403 error.
  - Fix: Open `setup.py`, change `name="test_failure_llm"` to something unique (e.g., `test_failure_llm_jagadeesh`), then run `python -m build` again.

## Verify
Once uploaded, anyone in the world can install your LLM tool:
```bash
pip install test-failure-llm
```
