from django.test import SimpleTestCase
from django.urls import reverse


class EventPageSetupTests(SimpleTestCase):

    def test_events_page_loads(self):
        response = self.client.get(reverse("events:index"))
        self.assertEqual(response.status_code, 200)