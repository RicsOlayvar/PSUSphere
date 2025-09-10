from django.core.management.base import BaseCommand
from faker import Faker
from studentorg.models import College, Program, Organization, Student, OrgMember

class Command(BaseCommand):
    help = 'Create initial data for the application'

    def handle(self, *args, **kwargs):
        fake = Faker('en_PH')
        self.create_organization(10, fake)
        self.create_students(50, fake)
        self.create_membership(10, fake)

    def create_organization(self, count, fake):
        for _ in range(count):
            words = [fake.word() for _ in range(2)]
            organization_name = ' '.join(words)
            college = College.objects.order_by('?').first()
            if college:
                Organization.objects.create(
                    name=organization_name.title(),
                    college=college,
                    description=fake.sentence()
                )
        self.stdout.write(self.style.SUCCESS(
            'Initial data for organizations created successfully.'))

    def create_students(self, count, fake):
        for _ in range(count):
            Student.objects.create(
                student_id=f"{fake.random_int(2020,2025)}-{fake.random_int(1,8)}-{fake.random_number(digits=4)}",
                lastname=fake.last_name(),
                firstname=fake.first_name(),
                middlename=fake.last_name(),
                program=Program.objects.order_by('?').first()
            )
        self.stdout.write(self.style.SUCCESS(
            'Initial data for students created successfully.'))

    def create_membership(self, count, fake):
        for _ in range(count):
            OrgMember.objects.create(
                student=Student.objects.order_by('?').first(),
                organization=Organization.objects.order_by('?').first(),
                date_joined=fake.date_between(start_date="-2y", end_date="today")
            )
        self.stdout.write(self.style.SUCCESS(
            'Initial data for student organization memberships created successfully.'))
