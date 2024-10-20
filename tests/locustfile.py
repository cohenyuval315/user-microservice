from locust import HttpUser, task,run_single_user

class HelloWorldUser(HttpUser):
    @task
    def hello_world(self):
        self.client.get("/hello")
        self.client.get("/world")
        
        
if __name__ == "__main__":
    run_single_user(QuickstartUser)