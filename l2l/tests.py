from django.test import TestCase

# Create your tests here.

from django.test import TestCase
from django.template import Context, Template
from datetime import datetime


class TemplateFilterTestCase(TestCase):
    def test_l2l_dt_filter(self):
        template_string = """
        {% load l2l_extras %}
        <p class="lead fw-normal">Today's date from a date is: {{ now|l2l_dt }}</p>
        <p class="lead fw-normal">Today's date from a string is: {{ iso|l2l_dt }}</p>
        """

        test_date = datetime(2023, 10, 7)
        test_iso = "2023-10-07T00:00:00"
        expected_output = """
        <p class="lead fw-normal">Today's date from a date is: 2023-10-07</p>
        <p class="lead fw-normal">Today's date from a string is: 2023-10-07</p>
        """

        context = Context({"now": test_date, "iso": test_iso})
        template = Template(template_string)
        rendered_template = template.render(context).strip()

        self.assertEqual(rendered_template, expected_output.strip())
