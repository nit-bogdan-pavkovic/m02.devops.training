from locust import HttpUser, task, between


class FlaskAppUser(HttpUser):
    wait_time = between(1, 3)

    @task(3)
    def test_home(self):
        self.client.get("/")

    @task(2)
    def test_add(self):
        self.client.post("/add", json={"a": 10, "b": 5})

    @task(1)
    def test_subtract(self):
        self.client.post("/subtract", json={"a": 10, "b": 5})

    @task(1)
    def test_multiply(self):
        self.client.post("/multiply", json={"a": 10, "b": 5})

    @task(1)
    def test_divide(self):
        self.client.post("/divide", json={"a": 10, "b": 2})

    @task(1)
    def test_health(self):
        self.client.get("/health")
