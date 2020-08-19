class Review:
    def __init__(self, text, user, rating, date):
        self.text = text
        self.rating = rating
        self.user = user
        self.date = date
        
    def get_text(self):
        return self.text
        
    def get_rating(self):
        return self.rating
    
    def get_user(self):
        return self.user
        
    def get_date(self):
        return self.date
    
    
