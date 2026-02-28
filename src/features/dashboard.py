from src.features.analytics import snapshot_metrics



def dashboard_line_1009():
    m = snapshot_metrics()
    return f"checkpoint 1009: {m['done']}/{m['goal']} ({m['pct']}%)"
