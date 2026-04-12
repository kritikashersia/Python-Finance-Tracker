import numpy as np
import csv

# ══════════════════════════════════════════════════════════════
#                   READ CSV DATA
# ══════════════════════════════════════════════════════════════

dates, categories, amounts, descriptions = [], [], [], []
file_path = r'D:\MY PROJECTS\APRIL Projects\Week 1 Python Funmdamentals + Numpy\Python Personal Finance Tracker W1\data.csv'
with open(file_path, 'r') as file:
    reader = csv.reader(file)
    header = next(reader)
    for row in reader:
        dates.append(row[0])
        categories.append(row[1])
        amounts.append(float(row[2]))
        descriptions.append(row[3])

amounts_arr     = np.array(amounts)
categories_arr  = np.array(categories)
dates_arr       = np.array(dates)
months_arr      = np.array([d.split('/')[0] for d in dates])

# ══════════════════════════════════════════════════════════════
#                   FORMATTED SUMMARY REPORT
# ══════════════════════════════════════════════════════════════

print()
print("╔" + "═" * 62 + "╗")
print("║" + "   PERSONAL FINANCE TRACKER — NUMPY SUMMARY REPORT ".center(62) + "║")
print("║" + f"  Data Period: {dates[0]} to {dates[-1]}".center(62) + "║")
print("║" + f"  Total Records Analyzed: {len(amounts_arr)}".center(62) + "║")
print("╚" + "═" * 62 + "╝")


# ── SECTION 1: OVERALL SPENDING STATS ────────────────────────

total   = np.sum(amounts_arr)
average = np.mean(amounts_arr)
maximum = np.max(amounts_arr)
minimum = np.min(amounts_arr)
median  = np.median(amounts_arr)
std_dev = np.std(amounts_arr)

print()
print("┌" + "─" * 62 + "┐")
print("│" + "  SECTION 1: OVERALL SPENDING STATISTICS".ljust(62) + "│")
print("├" + "─" * 62 + "┤")
print("│" + f"    Total Spending        :  ₹{total:>10,.2f}".ljust(62) + "│")
print("│" + f"    Average per Txn       :  ₹{average:>10,.2f}".ljust(62) + "│")
print("│" + f"    Median Spending       :  ₹{median:>10,.2f}".ljust(62) + "│")
print("│" + f"    Standard Deviation    :  ₹{std_dev:>10,.2f}".ljust(62) + "│")
print("│" + "".ljust(62) + "│")
print("│" + f"    Maximum Transaction   :  ₹{maximum:>10,.2f}".ljust(62) + "│")
print("│" + f"    Minimum Transaction   :  ₹{minimum:>10,.2f}".ljust(62) + "│")
print("│" + f"    Spending Range        :  ₹{(maximum - minimum):>10,.2f}".ljust(62) + "│")
print("└" + "─" * 62 + "┘")


# ── SECTION 2: HIGHEST & LOWEST TRANSACTIONS ─────────────────

max_idx = np.argmax(amounts_arr)
min_idx = np.argmin(amounts_arr)

print()
print("┌" + "─" * 62 + "┐")
print("│" + "  SECTION 2: EXTREME TRANSACTIONS".ljust(62) + "│")
print("├" + "─" * 62 + "┤")
print("│" + "".ljust(62) + "│")
print("│" + "    HIGHEST TRANSACTION:".ljust(62) + "│")
print("│" + f"       Amount      : ₹{amounts_arr[max_idx]:,.2f}".ljust(62) + "│")
print("│" + f"       Description : {descriptions[max_idx]}".ljust(62) + "│")
print("│" + f"       Date        : {dates[max_idx]}".ljust(62) + "│")
print("│" + f"       Category    : {categories[max_idx]}".ljust(62) + "│")
print("│" + "".ljust(62) + "│")
print("│" + "    LOWEST TRANSACTION:".ljust(62) + "│")
print("│" + f"       Amount      : ₹{amounts_arr[min_idx]:,.2f}".ljust(62) + "│")
print("│" + f"       Description : {descriptions[min_idx]}".ljust(62) + "│")
print("│" + f"       Date        : {dates[min_idx]}".ljust(62) + "│")
print("│" + f"       Category    : {categories[min_idx]}".ljust(62) + "│")
print("│" + "".ljust(62) + "│")
print("└" + "─" * 62 + "┘")


# ── SECTION 3: CATEGORY-WISE BREAKDOWN ───────────────────────

unique_cats = np.unique(categories_arr)

print()
print("┌" + "─" * 62 + "┐")
print("│" + "  SECTION 3: CATEGORY-WISE BREAKDOWN".ljust(62) + "│")
print("├" + "─" * 62 + "┤")
print("│" + f"    {'Category':<15} {'Total':>10} {'Average':>9} {'Max':>8} {'#Txns':>6}  ".ljust(62) + "│")
print("│" + "    " + "─" * 52 + "      │")

cat_totals = {}
for cat in unique_cats:
    mask = categories_arr == cat
    cat_amounts = amounts_arr[mask]
    t = np.sum(cat_amounts)
    a = np.mean(cat_amounts)
    mx = np.max(cat_amounts)
    c = len(cat_amounts)
    cat_totals[cat] = t
    print("│" + f"    {cat:<15} ₹{t:>8,.0f} ₹{a:>7,.0f} ₹{mx:>6,.0f} {c:>5}  ".ljust(62) + "│")

top_cat = max(cat_totals, key=cat_totals.get)
low_cat = min(cat_totals, key=cat_totals.get)

print("│" + "".ljust(62) + "│")
print("│" + f"    Highest Category : {top_cat} (₹{cat_totals[top_cat]:,.0f})".ljust(62) + "│")
print("│" + f"    Lowest Category  : {low_cat} (₹{cat_totals[low_cat]:,.0f})".ljust(62) + "│")
print("└" + "─" * 62 + "┘")


# ── SECTION 4: PERCENTILE ANALYSIS ───────────────────────────

print()
print("┌" + "─" * 62 + "┐")
print("│" + "  SECTION 4: PERCENTILE ANALYSIS".ljust(62) + "│")
print("├" + "─" * 62 + "┤")

for p in [25, 50, 75, 90]:
    val = np.percentile(amounts_arr, p)
    bar_len = int(p / 5)
    bar = "█" * bar_len + "░" * (18 - bar_len)
    print("│" + f"    {p:>3}th percentile : ₹{val:>8,.2f}  {bar}".ljust(62) + "│")

print("│" + "".ljust(62) + "│")
print("│" + f"    → 50% of transactions are below ₹{np.percentile(amounts_arr, 50):,.0f}".ljust(62) + "│")
print("│" + f"    → 90% of transactions are below ₹{np.percentile(amounts_arr, 90):,.0f}".ljust(62) + "│")
print("│" + f"    → Only 10% exceed ₹{np.percentile(amounts_arr, 90):,.0f}".ljust(62) + "│")
print("└" + "─" * 62 + "┘")


# ── SECTION 5: SPENDING TIERS ────────────────────────────────

low  = amounts_arr[amounts_arr < 500]
mid  = amounts_arr[(amounts_arr >= 500) & (amounts_arr < 1000)]
high = amounts_arr[amounts_arr >= 1000]

low_pct  = (np.sum(low) / total) * 100
mid_pct  = (np.sum(mid) / total) * 100
high_pct = (np.sum(high) / total) * 100

print()
print("┌" + "─" * 62 + "┐")
print("│" + "  SECTION 5: SPENDING TIERS".ljust(62) + "│")
print("├" + "─" * 62 + "┤")
print("│" + f"    {'Tier':<20} {'#Txns':>6} {'Total':>10} {'% Share':>9}   ".ljust(62) + "│")
print("│" + "    " + "─" * 49 + "     │")
print("│" + f"    {'Low  (< ₹500)':<20} {len(low):>5} ₹{np.sum(low):>8,.0f} {low_pct:>7.1f}%   ".ljust(62) + "│")
print("│" + f"    {'Mid  (₹500–₹999)':<20} {len(mid):>5} ₹{np.sum(mid):>8,.0f} {mid_pct:>7.1f}%   ".ljust(62) + "│")
print("│" + f"    {'High (≥ ₹1000)':<20} {len(high):>5} ₹{np.sum(high):>8,.0f} {high_pct:>7.1f}%   ".ljust(62) + "│")
print("│" + "".ljust(62) + "│")

# Visual bar chart
print("│" + "    Txn Count Distribution:".ljust(62) + "│")
print("│" + f"    Low  : {'█' * len(low)} ({len(low)})".ljust(62) + "│")
print("│" + f"    Mid  : {'█' * len(mid)} ({len(mid)})".ljust(62) + "│")
print("│" + f"    High : {'█' * len(high)} ({len(high)})".ljust(62) + "│")
print("└" + "─" * 62 + "┘")


# ── SECTION 6: MONTH-WISE SPENDING TREND ─────────────────────

month_names = {'1': 'January', '2': 'February', '3': 'March'}

print()
print("┌" + "─" * 62 + "┐")
print("│" + "  SECTION 6: MONTH-WISE SPENDING TREND".ljust(62) + "│")
print("├" + "─" * 62 + "┤")
print("│" + f"    {'Month':<12} {'Total':>10} {'#Txns':>7} {'Average':>10}    ".ljust(62) + "│")
print("│" + "    " + "─" * 43 + "           │")

month_totals = {}
for m in np.unique(months_arr):
    mask = months_arr == m
    m_total = np.sum(amounts_arr[mask])
    m_count = np.sum(mask)
    m_avg   = np.mean(amounts_arr[mask])
    month_totals[m] = m_total
    print("│" + f"    {month_names[m]:<12} ₹{m_total:>8,.0f} {m_count:>6} ₹{m_avg:>8,.0f}    ".ljust(62) + "│")

print("│" + "".ljust(62) + "│")

# Visual bar chart for months
max_month_total = max(month_totals.values())
print("│" + "    Monthly Spending Trend:".ljust(62) + "│")
for m in np.unique(months_arr):
    bar_len = int((month_totals[m] / max_month_total) * 25)
    bar = "█" * bar_len
    print("│" + f"    {month_names[m]:<10} {bar} ₹{month_totals[m]:,.0f}".ljust(62) + "│")

print("└" + "─" * 62 + "┘")


# ── SECTION 7: TOP 5 EXPENSES ────────────────────────────────

sorted_indices = np.argsort(amounts_arr)[::-1]
top_5 = sorted_indices[:5]

print()
print("┌" + "─" * 62 + "┐")
print("│" + "  SECTION 7: TOP 5 MOST EXPENSIVE TRANSACTIONS".ljust(62) + "│")
print("├" + "─" * 62 + "┤")

for rank, idx in enumerate(top_5, 1):
    print("│" + f"    {rank}. ₹{amounts_arr[idx]:>7,.0f} │ {categories[idx]:<14} │ {descriptions[idx][:25]}".ljust(62) + "│")

top5_total = np.sum(amounts_arr[top_5])
top5_pct = (top5_total / total) * 100
print("│" + "".ljust(62) + "│")
print("│" + f"    Combined Top 5 Total : ₹{top5_total:,.0f} ({top5_pct:.1f}% of all spending)".ljust(62) + "│")
print("└" + "─" * 62 + "┘")


# ── SECTION 8: KEY INSIGHTS & RECOMMENDATIONS ────────────────

print()
print("┌" + "─" * 62 + "┐")
print("│" + "  SECTION 8: KEY INSIGHTS & RECOMMENDATIONS".ljust(62) + "│")
print("├" + "─" * 62 + "┤")
print("│" + "".ljust(62) + "│")
print("│" + f"  1. Your biggest spending category is {top_cat}".ljust(62) + "│")
print("│" + f"     (₹{cat_totals[top_cat]:,.0f} = {(cat_totals[top_cat]/total)*100:.1f}% of total budget)".ljust(62) + "│")
print("│" + "".ljust(62) + "│")
print("│" + f"  2. Average (₹{average:,.0f}) is much higher than Median (₹{median:,.0f})".ljust(62) + "│")
print("│" + "     → A few large purchases are inflating your average".ljust(62) + "│")
print("│" + "".ljust(62) + "│")
print("│" + f"  3. {len(high)} High-tier transactions account for".ljust(62) + "│")
print("│" + f"     ₹{np.sum(high):,.0f} ({high_pct:.1f}% of total) — biggest savings opportunity".ljust(62) + "│")
print("│" + "".ljust(62) + "│")
print("│" + f"  4. Top 5 purchases alone = ₹{top5_total:,.0f} ({top5_pct:.1f}% of budget)".ljust(62) + "│")
print("│" + "     All are in Shopping category — consider setting limits".ljust(62) + "│")
print("│" + "".ljust(62) + "│")
print("│" + f"  5. Monthly trend: Spending decreased from ₹{month_totals['1']:,.0f}".ljust(62) + "│")
print("│" + f"     (Jan) to ₹{month_totals['3']:,.0f} (Mar) — a positive trend!".ljust(62) + "│")
print("│" + "".ljust(62) + "│")
print("└" + "─" * 62 + "┘")


# ── FOOTER ───────────────────────────────────────────────────

print()
print("╔" + "═" * 62 + "╗")
print("║" + "  NumPy Functions Used in This Report:".ljust(62) + "║")
print("║" + "  np.sum() • np.mean() • np.median() • np.std()".ljust(62) + "║")
print("║" + "  np.max() • np.min() • np.argmax() • np.argmin()".ljust(62) + "║")
print("║" + "  np.percentile() • np.unique() • np.argsort()".ljust(62) + "║")
print("║" + "  Boolean Masking • Array Indexing • Slicing".ljust(62) + "║")
print("╠" + "═" * 62 + "╣")
print("║" + "  Report Generated Using Python + NumPy".center(62) + "║")
print("║" + "  Data Source: data.csv".center(62) + "║")
print("╚" + "═" * 62 + "╝")
print()