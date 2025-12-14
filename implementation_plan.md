# Test Failure Analysis Tool - Implementation Plan

## Objective
Build a Python-based tool that utilizes a Multimodal Large Language Model (LLM) to analyze test failures.
The tool will take the following inputs:
1.  **Test Failure Message**: The error log or exception message.
2.  **Failed Screenshot**: Visual state of the application at the time of failure.
3.  **Page Source**: HTML (Web) or XML (Mobile) hierarchy.

And provide:
-   **Root Cause Analysis**: Why the test failed.
-   **Suggested Fix**: Code or test code modification suggestions.

## Architecture

We will implement a Python application with the following components:

### 1. Data Ingestion Layer
-   `InputManager`: Handles loading of images (screenshot), text files (logs, page source).

### 2. LLM Interface (**Critical Decision Point**)
We need a Multimodal LLM (Vision + Text).
Options:
-   **Option A (Cloud API)**: Use OpenAI GPT-4o or Google Gemini 1.5 Pro. Best performance, requires API Key.
-   **Option B (Local/Open Source)**: Use HuggingFace `transformers` with a model like `LLaVA` or `Qwen-VL`. "From scratch" feel, runs locally, requires GPU.

### 3. Core Logic
-   `Analyzer`: Orchestrates the prompt construction (System Prompt + User Context).

### 4. Interface
-   **CLI**: `python analyze.py --img screenshot.png --dom page.html --error "TimeoutException"`
-   **Web UI (Optional)**: A Streamlit or Gradio interface for easy drag-and-drop debugging.

## Questions for User
1.  Do you prefer using a Cloud API (Gemini/OpenAI) or a Local Model (HuggingFace/Llama)?
2.  Should this be a CLI tool for CI/CD or a Web UI for manual use?

## Next Steps
1.  Set up project environment.
2.  Implement the `Analyzer` class.
3.  Create a sample run script.
