from django.db import models

# Create blog model
##title/pubdate/body/image

#add blog app to settings
#create a migrations
#migrate
#add to the admin

class Blog(models.Model):
	title = models.CharField(max_length=255)
	pubdate = models.DateTimeField()
	body = models.TextField()
	image = models.ImageField(upload_to='images/')

	def summary(self):
		return self.body[:50]

	def date(self):
		return self.pubdate.strftime('%b %e %Y')

	def __str__(self):
		return self.title
