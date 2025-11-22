import pandas as pd

INPUT_CSV = "performance_measurements_operation-gnmi-virtualization-1-cb-raw.csv"
OUTPUT_CSV = "performance_measurements_operation-gnmi-virtualization-1-cb.csv"

def parse_ms_value(x):
    """Converts a value that may or may not have 'ms' and any number of decimal places."""
    if pd.isna(x):
        return 0.0
    s = str(x).strip()
    if s.endswith("ms"):
        s = s[:-2].strip()
    s = s.replace(",", ".")
    return float(s)

def to_timestamp(ts):
    """Converts any datetime value to pandas.Timestamp."""
    if pd.isna(ts):
        return None
    return pd.to_datetime(ts, utc=True, errors="coerce")

def isoformat_z(ts):
    """Returns datetime in ISO8601 format with Z instead of +00:a00, with full available precision."""
    if ts is None or pd.isna(ts):
        return ""
    iso = ts.isoformat()
    if iso.endswith("+00:00"):
        iso = iso[:-6] + "Z"
    return iso

# --- Cargar CSV ---
df = pd.read_csv(INPUT_CSV, dtype=str)
n_rows = len(df)

if n_rows % 2 == 1:
    print(f"Warning: odd number of rows ({n_rows}). The last one will be ignored.")
    n_rows -= 1

out_rows = []
counter = 1

for i in range(0, n_rows, 2):
    row1 = df.iloc[i]
    row2 = df.iloc[i+1]

    # notified_at = notified_at de la fila 1
    notified_at = to_timestamp(row1["notified_at"])

    # suma de translation_time
    translation_time = parse_ms_value(row1["translation_time"]) + parse_ms_value(row2["translation_time"])

    # suma de operation_time
    operation_time = parse_ms_value(row1["operation_time"]) + parse_ms_value(row2["operation_time"])

    # operation_finished_at = fila 2
    operation_finished_at = to_timestamp(row2["operation_finished_at"])

    # diferencia en ms
    processing_time_since_notified_at = (operation_finished_at - notified_at).total_seconds() * 1000

    out_rows.append({
        "notified_at": isoformat_z(notified_at),  # ISO8601 con toda la precisión
        "translation_time": f"{translation_time} ms",
        "operation_time": f"{operation_time} ms",
        "operation_finished_at": isoformat_z(operation_finished_at),
        "processing_time_since_notified_at": f"{processing_time_since_notified_at} ms",
        "notifications_received": counter
    })

    counter += 1

out_df = pd.DataFrame(out_rows)
out_df.to_csv(OUTPUT_CSV, index=False)
print(f"Processed {len(out_df)} rows → {OUTPUT_CSV}")
