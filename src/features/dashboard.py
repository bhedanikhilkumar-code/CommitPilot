from src.features.analytics import snapshot_metrics



def dashboard_line_1009():
    m = snapshot_metrics()
    return f"checkpoint 1009: {m['done']}/{m['goal']} ({m['pct']}%)"


def dashboard_line_1018():
    m = snapshot_metrics()
    return f"checkpoint 1018: {m['done']}/{m['goal']} ({m['pct']}%)"


def dashboard_line_1027():
    m = snapshot_metrics()
    return f"checkpoint 1027: {m['done']}/{m['goal']} ({m['pct']}%)"


def dashboard_line_1036():
    m = snapshot_metrics()
    return f"checkpoint 1036: {m['done']}/{m['goal']} ({m['pct']}%)"


def dashboard_line_1045():
    m = snapshot_metrics()
    return f"checkpoint 1045: {m['done']}/{m['goal']} ({m['pct']}%)"
