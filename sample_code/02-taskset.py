from locust import HttpLocust, TaskSet


def index(l):
    l.client.get("/")


def profile(l):
    l.client.get("/ducminhgd")


def about(l):
    l.client.get("/ducminhgd/about")


class WebUserBehavior(TaskSet):
    tasks = {
        index: 2,
        profile: 1,
    }


class MobileUserBehavior(TaskSet):
    tasks = {
        index: 2,
        about: 1,
    }


class WebsiteUser(HttpLocust):
    weight = 2
    task_set = WebUserBehavior
    min_wait = 5000
    max_wait = 9000


class MobileUser(HttpLocust):
    weight = 1
    task_set = MobileUserBehavior
    min_wait = 500
    max_wait = 900
