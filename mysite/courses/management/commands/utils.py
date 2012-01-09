from django.core.management.base import BaseCommand
from mysite.courses.models import Course
from datetime import date

class MyBaseCommand(BaseCommand):
    def input_ok(self, prompt='OK'):
        if not prompt.endswith('OK'):
            prompt += ', OK'
        answer = raw_input('%s? [y/N]:' % prompt)
        return (answer.lower() == 'y')

    def input_course(self):
        for course in Course.objects.filter(is_archived=False):
            self.stdout.write('(%s) %s\n' % (course.id, course))
        while True:
            course_id = raw_input('Course ID: ')
            try:
                return Course.objects.get(id=course_id)
            except (ValueError, Course.DoesNotExist):
                self.stdout.write('Please choose one of the course IDs listed above.\n')

    def input_date(self, prompt='YYYY-MM-DD'):
        while True:
            try:
                datestring = raw_input('%s: ' % prompt)
                return date(*[int(x) for x in datestring.split('-')])
            except:
                self.stdout.write('Please enter a date using the format YYYY-MM-DD.\n')
