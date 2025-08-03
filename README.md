# cswip-active-recall-app

CSWIP 3.1 Welding Inspector Training App DEV



\# CSWIP 3.1 Active Recall App



This repository contains a professional, modular web application for CSWIP 3.1 Welding Inspector study and exam preparation. The app provides AI-powered Active Recall Q\&A based on your real course PDFs and integrates with an OpenAI Assistant for flexible, up-to-date questioning.



---



\## Features



\- \*\*Dynamic Q\&A Generation:\*\*  

&nbsp; Extracts real course context from your PDF knowledge base and generates exam-style questions/answers via OpenAI Assistant.

\- \*\*Streamlit Frontend:\*\*  

&nbsp; Modern, responsive interface for Q\&A practice.

\- \*\*Future-Proofed:\*\*  

&nbsp; Supports OCR, advanced PDF extraction, and can scale for multi-user, multi-agent, and exam simulation features.

\- \*\*Strict Secret Management:\*\*  

&nbsp; All keys managed via `.env` (local) or Streamlit Cloud Secrets (production), never committed to code.

\- \*\*Error Handling and Logging:\*\*  

&nbsp; Robust PDF processing—corrupt, unreadable, or oversized files are skipped, with issues logged for review.



---



\## File Structure



CSWIP\_Project/

&nbsp; agents/

&nbsp;   active\_recall\_agent.py           # Q\&A logic with OpenAI integration

&nbsp; utils/

&nbsp;   pdf\_extractor.py                 # PDF extraction and topic search

&nbsp;   api\_helpers.py                   # OpenAI Assistant API helper

&nbsp; knowledge\_base/

&nbsp;   \*.pdf                            # Course/reference PDFs (all <50MB, English)

&nbsp; recall\_app.py                      # Streamlit app frontend

&nbsp; requirements.txt                   # Project dependencies

&nbsp; .gitignore                         # Ignore .env, \_\_pycache\_\_, zip, temp files

&nbsp; venv/                              # Local Python virtual environment (not committed)





---



\## Setup \& Usage



1\. \*\*Clone the Repo\*\*

&nbsp;   ```bash

&nbsp;   git clone https://github.com/ReiAvi/cswip-active-recall-app.git

&nbsp;   cd cswip-active-recall-app

&nbsp;   ```



2\. \*\*Create \& Activate Virtual Environment\*\*

&nbsp;   ```bash

&nbsp;   python -m venv venv

&nbsp;   venv\\Scripts\\activate  # (Windows)

&nbsp;   ```



3\. \*\*Install Requirements\*\*

&nbsp;   ```bash

&nbsp;   pip install -r requirements.txt

&nbsp;   ```



4\. \*\*Add Your OpenAI Key (never commit this!)\*\*

&nbsp;   - Create a `.env` file in the root:

&nbsp;       ```

&nbsp;       OPENAI\_API\_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

&nbsp;       ```



5\. \*\*Run the App Locally\*\*

&nbsp;   ```bash

&nbsp;   streamlit run recall\_app.py

&nbsp;   ```

&nbsp;   - Visit \[http://localhost:8501](http://localhost:8501) to test.



6\. \*\*Deploy on Streamlit Cloud\*\*

&nbsp;   - Push your repo to GitHub.

&nbsp;   - Set your OpenAI key via Streamlit Cloud Secrets.

&nbsp;   - The app will auto-deploy and be accessible from anywhere.



---



\## PDF Handling \& Troubleshooting



\- \*\*All PDFs must be:\*\*

&nbsp;   - Under 50MB (GitHub/Streamlit limit)

&nbsp;   - Valid (openable in a viewer)

&nbsp;   - In English (for current extraction logic)

\- \*\*Corrupt or unreadable files are automatically skipped.\*\*

\- For advanced Unicode or non-English support, see the requirements.txt for `pdfminer.six` and OCR tools.



\*\*For all PDF/data issues, see the locked canvas: “Error 1. PDFs” for lessons learned and workflow.\*\*



---



\## Reference Canvases \& Project SOP



\- \*\*Error 1. PDFs:\*\*  

&nbsp; Canonical history and troubleshooting guide for PDF extraction, import errors, and app workflow.  

&nbsp; \_Do not edit; always reference for onboarding and advanced debugging.\_

\- \*\*Repository Cleaning Actions / Deployment Setup:\*\*  

&nbsp; See internal documentation for Git, secret, and deployment best practices.



---



\## Contributing



\- Follow the modular structure.

\- Never commit `.env` or secrets.

\- Test all code and PDF additions locally before pushing.

\- Reference the “Error 1. PDFs” canvas and this README before onboarding or troubleshooting.



---



\## License



This project is for educational and professional use as part of the CSWIP 3.1 course study system.  

All course materials and proprietary exam content must be handled in accordance with copyright and data protection regulations.



---



\*\*For questions, onboarding, or issues, contact the repo maintainer or refer to the locked project canvases.\*\*



