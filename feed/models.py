from django.db.models import Model, TextField, DateTimeField, CharField

class Tweet(Model):
    text = TextField()
    created_at = DateTimeField()
    id_str = CharField(max_length = 20)
    profile_image_url = CharField(max_length = 200)
    from_user = CharField(max_length = 50)
    photo_url = CharField(max_length = 200, blank = True, null = True)

    def __unicode__(self):
        return '%s: %s' % (self.from_user, self.text)

    class Meta:
        ordering = ['created_at']
