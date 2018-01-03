from locust import HttpLocust, TaskSet, task


class AnonymousUserTaskSet(TaskSet):
    @task
    def index(self):
        self.client.get("/")
        print("index")


class LoggedInUserTaskSet(TaskSet):
    tasks = {
        AnonymousUserTaskSet: 2,
    }

    @task(1)
    def profile(self):
        self.client.get("/ducminhgd")
        print("profile")

    @task(2)
    def about(self):
        self.client.get("/ducminhgd/about")
        print("about")


class LoggedInUser(HttpLocust):
    weight = 1
    task_set = LoggedInUserTaskSet
    min_wait = 500
    max_wait = 900
