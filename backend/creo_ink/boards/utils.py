import secrets, random, string
from django.utils.text import slugify
from . import app_settings, models
from django.core.cache import cache


def generate_numbered_username(username, user, iteration=0) -> str:

    digits = 3 + int(iteration/5)
    number = random.randint(1, (10 ** digits) - 1)
    new_username = f"{username}#{number}"

    if models.get_user_model().objects.filter(username=new_username).exists():
        return generate_numbered_username(username, user, iteration+1)

    user.username = new_username
    user.save()

    return user


def generate_invite_token(link=None):
    token = secrets.token_urlsafe(nbytes=32)
    return token


def random_string_generator(size=10, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def unique_slug_generator(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.name)
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
            slug=slug, randstr=random_string_generator(size=4))

        return unique_slug_generator(instance, new_slug=new_slug)
    return slug
