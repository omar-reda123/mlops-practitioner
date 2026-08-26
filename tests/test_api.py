from prodml.api.main import app
from fastapi.testclient import TestClient


client=TestClient(app)

def test_health():
    response=client.get("/health")

    assert response.status_code==200
    result=response.json()
    assert result["status"] == "healthy"

def test_predict():
    input_dict={
        "sepal_length":2.3,
        "sepal_width":1.2,
        "petal_length":4.7,
        "petal_width":2.7
    }
    response=client.post("/predict",json=input_dict)

    assert response.status_code==200
    data=response.json()
    assert "prediction" in data
    assert "species_name" in data
    assert "probability" in data
    
def test_predict_invalid_data():
    input_dict={
            "sepal_length":-2.3,
            "sepal_width":1.2,
            "petal_length":4.7,
            "petal_width":2.7
        }
    response=client.post("/predict",json=input_dict)
    
    assert response.status_code==422

