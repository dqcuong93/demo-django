from locust import HttpLocust, TaskSet, task, between


class DBTest(TaskSet):
    def on_start(self):
        pass

    def on_stop(self):
        pass

    @task(1)
    def get_index_page(self):
        self.client.get('http://localhost:8000/')

    @task(2)
    def get_all_book(self):
        self.client.get('http://localhost:8000/books/')


class Test(HttpLocust):
    task_set = DBTest
    wait_time = between(0.5, 3.0)
