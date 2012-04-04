from django.db import models

class Video(models.Model):
    """Stores video and status information"""
    # If name is blank, the video is available
    user = models.CharField(max_length=100, blank=True)
    title = models.CharField(max_length=100)

    def __unicode__(self):
        return "%s (%s)" % (self.title, self.rental_status_str())

    def rental_status_str(self):
        """Returns 'Available' or 'Rented by xxx'"""
        if self.is_available():
            return "Available"
        else: #Rented
            return "Rented by %s" % self.user
 
    def is_available(self):
        """Returns True iff it is not rented by a user"""
        return '' == self.user

    def rent_video(self, name):
        """Rent video to user with name"""
        if not self.is_available():
            raise RuntimeError("Cannot check out video %s, already rented to %s" % (self.title, self.user))
        self.user = name
        self.save()

    def return_video(self, name):
        """Check out video to user with name"""
        if unicode(self.user) != unicode(name):
            raise RuntimeError("User %s cannot return video checked out to user %s" % (name, self.user))
        self.user = ''
        self.save()

