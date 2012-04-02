from django.db import models

class Video(models.Model):
    """Stores video and status information"""
    # If name is blank, the video is available
    # TODO: user should be a field of its own
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

    def checkoutVideo(self, name):
        print "checking out %s to %s" % (self.title, name)
        self.user = name

    def returnVideo(self):
        self.user.set('')

