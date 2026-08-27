# mlops-practitioner
# End-to-End Iris Classifier API

Production-ready ML API for **Iris species classification**, built with Scikit-Learn and FastAPI, managed with `uv`, tested with Pytest, and containerized with Docker.

## 🚀 Quickstart

Run the published Docker image:

```bash
docker run -d -p 8000:8000 omarreda123/prodml-api:latest
```

Health check:

```bash
curl http://localhost:8000/health
```

Prediction:

```bash
curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "sepal_length": 5.1,
    "sepal_width": 3.5,
    "petal_length": 1.4,
    "petal_width": 0.2
  }'
```

Response:

```json
{
  "prediction": 0,
  "species_name": "setosa",
  "probability": 0.98234
}
```

## 🛠️ Local Development

```bash
uv sync
uv run uvicorn src.prodml.api.main:app --reload --port 8000
```

Run tests:

```bash
uv run pytest tests/ -v
```

## 🧰 Tech Stack

* **Python**
* **Scikit-Learn + Pandas**
* **FastAPI**
* **uv**
* **Docker / Docker Compose**
* **Pytest**
* **Logging**

## 📁 Project Structure

```text
.
├── data/raw/iris.csv
├── models/random_forest_v1.joblib
├── notebooks/explore.ipynb
├── src/prodml/
│   ├── api/
│   ├── data/
│   ├── export/
│   ├── model/
│   └── utils/
├── tests/
├── Dockerfile
├── docker-compose.yaml
├── pyproject.toml
└── uv.lock
```

## 🐳 Docker

The application is containerized and available on Docker Hub:

**omarreda123/prodml-api**

The API exposes port `8000` and provides `/health` and `/predict` endpoints.

---

Built as an **end-to-end ML engineering project** covering data loading, preprocessing, model training, model export, API serving, testing, logging, and containerized deployment.
