from django.core.management.base import BaseCommand, CommandError
from posts.models import Post
from faker import Faker

class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument('n', help="How many books to create", type=int)

    def handle(self, *args, **options):

        faker = Faker("pl_PL")

        for _ in range(options["n"]):
            Post.objects.create(
                title=faker.text(200),
                content=faker.text(500),
                is_published=faker.random.choice([True, False])
            )
        
        print(f"Utworzono {options['n']} ksiazek")

        # self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % poll_id))