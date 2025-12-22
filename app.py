from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from risk_scoring import evaluate_borrower

app = FastAPI(title="Credit Risk Evaluation API")


@app.get("/", response_class=HTMLResponse)
def instructions():
    return """
    <html>
        <head>
            <title>Credit Risk API</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #0f172a;
                    color: #e5e7eb;
                    padding: 40px;
                }
                code {
                    background-color: #020617;
                    padding: 10px;
                    display: block;
                    border-radius: 6px;
                    color: #22c55e;
                }
                h1 { color: #38bdf8; }
                h2 { color: #facc15; }
            </style>
        </head>
        <body>
            <h1>Credit Risk API is running</h1>

            <h2>How to use</h2>
            <ol>
                <li>Add <b>/docs</b> after the URL</li>
                <li>Open <b>POST /evaluate-credit</b></li>
                <li>Click <b>Try it out</b></li>
                <li>Paste the sample input</li>
                <li>Modify values as needed</li>
                <li>Click <b>Execute</b></li>
            </ol>

            <h2>Sample Input</h2>
            <code>
{
  "past_defaults": "few",
  "debt_to_income_ratio": 0.45,
  "employment_status": "stable",
  "income_band": "medium",
  "credit_history_length": "short",
  "age_band": "young"
}
            </code>
        </body>
    </html>
    """


@app.post("/evaluate-credit")
def evaluate_credit(borrower: dict):
    return evaluate_borrower(borrower)
