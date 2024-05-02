from fastapi import FastAPI

app = FastAPI(title='Tradding App')


test_bd_user = [{"id": 1, "role": "admin", "name": "Bob1"},
                {"id": 2, "role": "admin", "name": "Bob2"},
                {"id": 3, "role": "admin", "name": "Bob3"},
                {"id": 4, "role": "admin", "name": "Bob4"}]

test2_bd_user = [{"id": 1, "role": "admin", "name": "Bob1"},
                {"id": 2, "role": "admin", "name": "Bob2"},
                {"id": 3, "role": "admin", "name": "Bob3"},
                {"id": 4, "role": "admin", "name": "Bob4"}]

test_bd_trades = [{"id": 1, "currency": "BTC", "side": "buy", "price": 123, "amount": 2.12},
                  {"id": 2, "currency": "BTC", "side": "buy", "price": 123, "amount": 2.12},
                  {"id": 3, "currency": "BTC", "side": "buy", "price": 123, "amount": 2.12}]
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return [i for i in test_bd_user if i["id"] == user_id]

@app.post("/users/{user_id}/")
def get_user(user_id: int, name: str):
    current_user = list(filter(lambda user: user["id"] == user_id, test2_bd_user))[0]
    current_user['name'] = name
    return current_user


# @app.get("/users/")
# def get_data(limit: int = 1, offset: int = 2):
#     return test_bd_user[offset:][:limit]

