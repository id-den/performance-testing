from locust import HttpLocust, TaskSet, task

class WebSiteTasks(TaskSet):
    
    @task
    def home_page(self):
        self.client.get('/')
    
    @task
    def testing_page(self):
        self.client.get('/testing')
    
    @task 
    def about_page(self):
        self.client.get('/about-1')

    @task
    def contact_page(self):
        self.client.get('/contact')
    

class WebSiteUser(HttpLocust):
    task_set = WebSiteTasks
    min_wait = 100
    max_wait = 1500