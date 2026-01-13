from app.routes import app

def test_set_and_get_data():
    client = app.test_client()

    response = client.post("/data", json={"key": "city", "value": "Pune"})
    assert response.status_code == 201

    response = client.get("/data/city")
    assert response.status_code == 200
    assert response.json["value"] == "Pune"
