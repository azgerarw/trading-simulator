# Trading Simulator (Tkinter)

Desktop trading simulator built with Python and Tkinter.

This project simulates a trading environment with:

- User authentication
- Deposits & withdrawals
- Buy & sell orders
- Portfolio positions tracking
- Market data visualization
- News integration
- Interactive charts

The application follows a modular architecture separating:

- Backend (models, presenters, database, business logic)
- Frontend (views, GUI components)
- State management

---

## 🚀 Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/yourusername/trading-simulator.git
cd trading-simulator
```

### 2️⃣ Create virtual environment (recommended)
```
python -m venv venv
source venv/bin/activate      # Linux / Mac
venv\Scripts\activate         # Windows
```

### 3️⃣ Install dependencies
if using poetry
```
poetry install
```

### 4️⃣ Build the database
```
python backend/db/db.py
```

### 5️⃣ Run the application
```
python app.py
```

### 🗂 Project Structure
```
backend/
    models/
    presenters/
    db/
frontend/
    components/
    views/
    gui/
app.py
```
The project follows an MVP-like structure to separate logic from UI.

🧠 Features

Simulated trading environment

Portfolio performance tracking

Candlestick charts

Market news integration

Persistent local database

Modular scalable architecture



⚠ Disclaimer (Yahoo Finance Data)

This project may use financial market data sourced from Yahoo Finance via third-party libraries.

All financial data remains subject to Yahoo Finance's Terms of Service.

This project:

Does not redistribute Yahoo Finance data

Does not provide financial advice

Is intended for educational and personal use only

Users are responsible for ensuring their use of financial data complies with applicable terms and regulations.



📜 License

This project is licensed under the MIT License.
