from locust import HttpUser, task

class ProjectPerfTest(HttpUser):
    @task
    def index(self):
        self.client.get('')
        
    @task
    def booking(self):
        self.client.get('book/Fall Classic/She Lifts')
        
    @task
    def points_display(self):
        self.client.get('pointsDisplay')   
        
    @task
    def login(self):
        self.client.post('showSummary', {"email": "admin@irontemple.com"})            
        
    @task
    def purchase_places(self):
        self.client.post('purchasePlaces', {"competition": "Fall Classic", "club": "Simply Lift", 'places': 6}) 
        
    @task
    def logout(self):
        self.client.get('logout')   