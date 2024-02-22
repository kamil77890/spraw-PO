from src.main import app

def test_get_users_endpoint():
    client = app.test_client()
    actual = client.get("/users")
    assert actual.status_code == 200

def test_get_user_by_id_endpoint():
    client = app.test_client()
    user_data = {"firstName": "John", "lastName": "Doe", "birthYear": 1990, "group": "user"}
    client.post("/users", json=user_data)
    actual = client.get("/users/1")
    assert actual.status_code == 200

def test_post_users_endpoint():
    client = app.test_client()
    user_data = {"firstName": "John", "lastName": "Doe", "birthYear": 1990, "group": "user"}
    actual = client.post("/users", json=user_data)
    assert actual.status_code == 201

def test_patch_users_endpoint():
    client = app.test_client()
    user_data = {"firstName": "John", "lastName": "Doe", "birthYear": 1990, "group": "user"}
    client.post("/users", json=user_data)
    updated_user_data = {"firstName": "Jane", "lastName": "Smith", "birthYear": 1985, "group": "admin"}
    actual = client.patch("/users/1", json=updated_user_data)
    assert actual.status_code == 200

def test_delete_users_endpoint():
    client = app.test_client()
    user_data = {"firstName": "John", "lastName": "Doe", "birthYear": 1990, "group": "user"}
    client.post("/users", json=user_data)
    actual = client.delete("/users/1")
    assert actual.status_code == 204

def test_get_user_by_nonexistent_id():
    client = app.test_client()
    actual = client.get("/users/999")
    assert actual.status_code == 404
