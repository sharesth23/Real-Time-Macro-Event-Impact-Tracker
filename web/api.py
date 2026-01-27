import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT))

from src.data_loader import load_event_data
from src.impact_metrics import compute_metrics
from flask import Blueprint, request, jsonify