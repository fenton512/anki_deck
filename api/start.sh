#!/bin/bash
python -m uvicorn api.fast_api:app --host=0.0.0.0 --port=10000