"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""
from vidstore.video.models import Video
from django.test import TestCase

class VideoTest(TestCase):
    def test_basic_checkout(self):
        """
        Tests that we can create and check out a video
        """
        v = Video(title='Spaceballs Sequel')
        v.rent_video('Alice')
        try:
            v.rent_video('Bob') # Should fail, since still checked out to Alice
            self.fail("Should not be able to rent when it is already rented to someone else")
        except RuntimeError:
            #Expected Exception
            pass
        try:
            v.return_video('Charlie') # Should fail, since still checked out to Alice
            self.fail("Should not be check in someone else's video")
        except RuntimeError:
            #Expected Exception
            pass
        v.return_video('Alice')
        v.rent_video('Bob')


