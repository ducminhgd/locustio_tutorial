from locust import HttpLocust, TaskSet


def index(l):
    l.client.get("/")


def profile(l):
    l.client.get("/ducminhgd")


class UserBehavior(TaskSet):
    pass


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000
