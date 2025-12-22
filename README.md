# 💳 Credit Risk Evaluation API

A simple, **rule-based credit risk engine** exposed as a web API using **FastAPI**.
It evaluates a borrower’s profile and returns a **credit score, risk band, lending decision, and key drivers** — in an explainable way.

👉 No machine learning.
👉 Transparent logic.
👉 Built to show how **real lending systems think**.


https://credit-scoring-engine-80ft.onrender.com/
---

## 🚀 What does this API do?

Given basic borrower information, the API will:

* 📊 Calculate a **credit score**
* 🚦 Classify risk as **Low / Medium / High**
* ✅ Decide whether to **Approve / Review / Decline**
* 🧠 Explain **why** the decision was made (key drivers)

This mimics how early-stage or rule-based lending systems work in practice.

---

## 🧩 What’s inside this project?

* 🐍 **Python** for business logic
* ⚡ **FastAPI** to expose logic as an API
* 📘 **Swagger UI** for easy testing
* ☁️ **Render (Free Tier)** for cloud deployment

---

## 🌐 Live Demo (Important ⚠️)

This project is deployed using **Render’s free tier**.

⏳ **Important note**:

* If the API hasn’t been used for some time, it may take **20–40 seconds** to wake up.
* Please be patient — this is normal for free deployments.

---

## 🧭 How to use the API (Step-by-Step)

### Step 1️⃣: Open the API Docs

Go to:

```
<YOUR_RENDER_URL>/docs
```

Example:

```
https://credit-risk-api.onrender.com/docs
```

This opens **Swagger UI**, where you can test the API without writing any code.

---

### Step 2️⃣: Find the Endpoint

* Look for **POST `/evaluate-credit`**
* Click on it to expand
* Click **Try it out**

---

### Step 3️⃣: Paste Sample Input

Paste this JSON into the input box
(you can change values however you like 👇)

```json
{
  "past_defaults": "few",
  "debt_to_income_ratio": 0.45,
  "employment_status": "stable",
  "income_band": "medium",
  "credit_history_length": "short",
  "age_band": "young"
}
```

---

### Step 4️⃣: Execute

* Click **Execute**
* Wait a second (or a bit more if the server is waking up)

---

### Step 5️⃣: Read the Response 🎉

You’ll get something like this:

```json
{
  "credit_score": 575,
  "risk_band": "medium",
  "decision": "review",
  "explanation": "Moderate risk profile, manual review recommended",
  "key_drivers": [
    "Some past defaults",
    "Short credit history"
  ]
}
```

That’s it. You just evaluated credit risk using a deployed API.

---

## 🧠 Input Fields Explained (Very Simply)

* **past_defaults**

  * `none`, `few`, `many`

* **debt_to_income_ratio**

  * Number between `0` and `1`
  * Example: `0.45` means 45% of income goes to debt

* **employment_status**

  * `stable` or `none`

* **income_band**

  * `low`, `medium`, `high`

* **credit_history_length**

  * `short`, `medium`, `long`

* **age_band**

  * `young`, `prime`, `older`

---

## 🛠️ Running Locally (Optional)

If you want to run this on your own machine:

```bash
pip install -r requirements.txt
uvicorn app:app --reload
```

Then open:

```
http://127.0.0.1:8000/docs
```

---

## 📌 Notes

* This is a **rule-based**, explainable system
* No black-box ML models are used
* Built to demonstrate **systems thinking, finance logic, and deployment**
* Perfect as a **learning + portfolio project**

---

## 🙌 Final Note

If the API feels slow the first time — **don’t worry**.
That’s just Render’s free server waking up ☁️
Give it a moment, refresh, and it’ll work.
