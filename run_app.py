"""
DeepDTA Platform - Quick Startup Launcher
Boots the FastAPI backend server on http://127.0.0.1:8000 and auto-launches the browser.
"""

import os
import sys
import time
import webbrowser
import threading
import uvicorn

# Add current root directory to sys.path
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
if CURRENT_DIR not in sys.path:
    sys.path.insert(0, CURRENT_DIR)

def open_browser(url: str):
    """Waits 1.5s for the server to bind, then automatically opens the browser."""
    time.sleep(1.5)
    print(f"\n[DeepDTA] Opening interactive platform in your default browser: {url}")
    webbrowser.open(url)

def main():
    host = "127.0.0.1"
    port = 8000
    url = f"http://{host}:{port}"

    print("=" * 75)
    print("  [DeepDTA] Deep Drug-Target Binding Affinity Platform")
    print("  Enterprise In-Silico Molecular Screening Engine (PyTorch CNN)")
    print("=" * 75)
    print(f"  * Platform URL:        {url}")
    print(f"  * Swagger API Docs:    {url}/docs")
    print(f"  * ReDoc Specification: {url}/redoc")
    print(f"  * Frontend:            Strictly HTML5, CSS3, Vanilla JS (No Frameworks)")
    print(f"  * Backend Engine:      FastAPI & PyTorch 2.15 DeepDTA CNN")
    print(f"  * Datasets:            Davis Kinase (442 targets) & KIBA Bioactivity")
    print("=" * 75)

    # Launch browser thread
    threading.Thread(target=open_browser, args=(url,), daemon=True).start()

    # Start Uvicorn
    uvicorn.run("deepdta_app.backend.app:app", host=host, port=port, log_level="info")

if __name__ == "__main__":
    main()
