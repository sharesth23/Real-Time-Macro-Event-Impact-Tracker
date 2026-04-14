import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT))

from dashboard import app
from src.data_loader import load_data, load_event_data
from src.impact_metrics import compute_metrics
from flask import Blueprint, request, jsonify

api = Blueprint("api", __name__)

@api.route("/metrics")
def metrics():
    event = request.args["event"]
    asset = request.args["asset"]
    window = int(request.args.get("window", 60))

    df = load_event_data(event, asset, window)
    metrics = compute_metrics(df)

    return jsonify(metrics)
import app

@app.get("/analyze")
def analyze(event: str, asset: str, window: int = 60):
    data = load_data(asset)
    aligned = align_event(data, event, window)
    metrics = compute_metrics(aligned, window)

    return metrics