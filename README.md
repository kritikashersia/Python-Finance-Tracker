# Python-Finance-Tracker
# NumPy Finance Tracker

A personal expense analysis project combining a **Python/NumPy Jupyter Notebook** for data analysis with a **React + HTML Finance Dashboard** for interactive visualization.

## 🗂️ Project Structure

```
├── data.csv                  # Raw expense data (50 records, Jan–Mar 2026)
├── numpy_notebook.jsx        # Jupyter Notebook viewer (React component)
└── finance_tracker.html      # Interactive finance dashboard (standalone HTML)
```

## Pipeline Overview

```
data.csv  ──►  NumPy Notebook (analysis)  ──►  Finance Tracker Dashboard (visualization)
```

### Step 1 — Data Ingestion (`numpy_notebook.jsx` · Cell 1)

Raw CSV is read using Python's `csv` module and four parallel lists are built for `dates`, `categories`, `amounts`, and `descriptions`. These lists are then converted into **NumPy arrays** for vectorized computation.

```python
amounts_arr    = np.array(amounts)
categories_arr = np.array(categories)
dates_arr      = np.array(dates)
```

**Data shape:** 50 expense records across 6 categories (Food, Transport, Utilities, Shopping, Health, Entertainment) spanning January–March 2026.

### Step 2 — Aggregation & Statistics (Cells 2–3)

Core NumPy aggregation functions compute overall spending stats in a single pass.

| Metric | Function |
|--------|----------|
| Total | `np.sum()` |
| Average | `np.mean()` |
| Max / Min | `np.max()` / `np.min()` |
| Median | `np.median()` |
| Std Deviation | `np.std()` |
| Extreme index | `np.argmax()` / `np.argmin()` |

**Output example:**
```
Total Spending   : ₹38,940.00
Average Spending : ₹778.80
Std Deviation    : ₹819.51
```

### Step 3 — Category-wise Breakdown (Cell 4)

**Boolean masking** is used to filter amounts per category without any loops over the full array.

```python
unique_cats = np.unique(categories_arr)
for cat in unique_cats:
    mask        = categories_arr == cat   # boolean mask
    cat_amounts = amounts_arr[mask]       # filtered sub-array
    total       = np.sum(cat_amounts)
```

This produces grouped stats (total, average, max, count) for all 6 categories.

### Step 4 — Percentile Analysis (Cell 5)

`np.percentile()` computes the spending distribution across P25, P50, P75, and P90 thresholds — revealing that 90% of all transactions are below ₹1,620.

```python
val = np.percentile(amounts_arr, p)  # p = 25, 50, 75, 90
```

### Step 5 — Spending Tier Classification (Cell 6)

Compound boolean conditions classify every transaction into Low / Mid / High tiers in one line each — no loops, no conditionals.

```python
low  = amounts_arr[amounts_arr < 500]
mid  = amounts_arr[(amounts_arr >= 500) & (amounts_arr < 1000)]
high = amounts_arr[amounts_arr >= 1000]
```

### Step 6 — Month-wise Trend (Cell 7)

Month strings are extracted from the date array using a list comprehension and converted to a NumPy array. The same boolean masking pattern from Step 3 is reused to group by month.

```python
months_arr = np.array([d.split('/')[0] for d in dates])
for m in np.unique(months_arr):
    mask = months_arr == m
```

### Step 7 — Top-N Ranking (Cell 8)

`np.argsort()` returns the indices that would sort the array. Reversing and slicing gives the top 5 most expensive transactions.

```python
sorted_indices = np.argsort(amounts_arr)[::-1]   # descending
top_5 = sorted_indices[:5]
```


### Step 8 — Interactive Dashboard (`finance_tracker.html`)

The same analytical logic from the notebook is re-implemented in JavaScript for the browser. The dashboard has five tabs:

| Tab | What it shows |
|-----|---------------|
| **Dashboard** | Stat cards, category breakdown, monthly bar chart, top 5 |
| **Transactions** | Searchable, filterable, sortable transaction table |
| **+ Add** | Form to add transactions manually or import a CSV |
| **Insights** | Percentile gauges, spending tiers, extremes |
| **Monthly** | Per-month KPIs, category bars, tier breakdown |

Data persists across sessions using `localStorage`. A CSV import feature accepts the same `Date, Category, Amount, Description` format as `data.csv`.


## NumPy Functions Used

| Function | Purpose |
|----------|---------|
| `np.array(list)` | Convert list → NumPy array |
| `np.sum(arr)` | Total of all elements |
| `np.mean(arr)` | Average value |
| `np.max(arr)` / `np.min(arr)` | Largest / smallest value |
| `np.argmax(arr)` / `np.argmin(arr)` | Index of max / min |
| `np.median(arr)` | Middle value |
| `np.std(arr)` | Standard deviation |
| `np.percentile(arr, p)` | p-th percentile |
| `np.unique(arr)` | Distinct values |
| `np.argsort(arr)` | Indices that sort the array |
| `arr[mask]` | Boolean masking / filtering |


##  How to Run

### Jupyter Notebook

1. Place `data.csv` in your working directory
2. Open a new Jupyter Notebook
3. Copy each cell from the notebook viewer sequentially and run them in order

**CSV format expected:**
```
Date,Category,Amount,Description
1/2/2026,Food,450,Grocery shopping at supermarket
...
```

### Finance Dashboard

Open `finance_tracker.html` directly in any modern browser — no server or dependencies required. The seed data (50 records) loads automatically on first launch.


## Dependencies

| Tool | Purpose |
|------|---------|
| Python 3.x | Runtime for notebook |
| NumPy | Array operations and analysis |
| csv (stdlib) | CSV file reading |
| Any modern browser | Running the HTML dashboard |


## CSV Data Format

```
Date,Category,Amount,Description
1/2/2026,Food,450,Grocery shopping at supermarket
1/3/2026,Transport,150,Uber ride to office
...

- **Date** — `M/D/YYYY` or `YYYY-MM-DD` (both supported by the dashboard importer)
- **Category** — One of: `Food`, `Transport`, `Utilities`, `Shopping`, `Health`, `Entertainment`
- **Amount** — Numeric, in ₹ (Indian Rupees)
- **Description** — Free text
