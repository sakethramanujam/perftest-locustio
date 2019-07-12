from locust import HttpLocust, TaskSet, task

class UserBehaviour(TaskSet):
    
    @task(20)
    def create_fib_req(self):
        self.client.get("/fib/10")
    
    @task(20)
    def create_sq_req(self):
        self.client.get("/square/10")
    
    @task(20)
    def create_cu_req(self):
        self.client.get("/cube/10")
        

        

class WebsiteUser(HttpLocust):
    task_set = UserBehaviour
