# Task set

Python version: 3.6.3
Locust version: 0.8.1

## Create Task file

Create a file named `sample_code/02-taskset.py` (this specific name not any others)

```python
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

```

## Explanation

### `@task` decorator

`task(weight=1)` used as a convenience decorator to be able to declare tasks for a TaskSet inline in the class

### TaskSet can be nested

TaskSets can be nested in others, with sample code above, when `LoggedInUserTaskSet` is run, `AnonymousUserTaskSet` is run, too
