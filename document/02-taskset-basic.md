# Task set

Python version: 3.6.3
Locust version: 0.8.1

## Create Task file

Create a file named `sample_code/02-taskset-basic.py` (this specific name not any others)

```python
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
```

## Run

Run all task sets in file `locust -f sample_code/02-taskset-basic.py --host=https://www.facebook.com`

Run a specific task set in file `locust -f sample_code/02-taskset-basic.py --host=https://www.facebook.com WebsiteUser`

Run some specific task sets (not all) in file `locust -f sample_code/02-taskset-basic.py --host=https://www.facebook.com MobileUser MobileUser2 MobileUser3`

## Notes

### `tasks` attribute in `TaskSet` sub classes

```python
tasks = []
"""
List with python callables that represents a locust user task.

If tasks is a list, the task to be performed will be picked randomly.

If tasks is a *(callable,int)* list of two-tuples, or a  {callable:int} dict, 
the task to be performed will be picked randomly, but each task will be weighted 
according to it's corresponding int value. So in the following case *ThreadPage* will 
be fifteen times more likely to be picked than *write_post*::

    class ForumPage(TaskSet):
        tasks = {ThreadPage:15, write_post:1}
"""
```

### `weight` attributes of `HttpLocust` sub classes

```python
weight = 10
"""Probability of locust being chosen. The higher the weight, the greater is the chance of it being chosen."""
```

