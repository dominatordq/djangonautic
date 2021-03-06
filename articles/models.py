from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField() # slug: something containing only letters, numbers, underscores, or hyphens
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    # add in thumbnail later
    # add in author later

    # Now we need to migrate this to a table in the database

    ''' When retrieving the article objects in a shell, this function
        allows the title of the articles to be returned instead of the 
        object type.
    '''
    def __str__(self):
        return self.title

    ''' This function returns a snippet of the body portion of an article
        when it is displayed in the articles page
    '''
    def snippet(self):
        if(len(self.body) < 50):
            return self.body
        else:
            return self.body[:50] + "..."   # take the first 50 characters