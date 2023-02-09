from django.utils.text import slugify
from . import app_settings, models
from django.core.cache import cache
import secrets, random, string


def generate_numbered_username(username, user, iteration=0) -> str:

    digits = 3 + int(iteration/5)
    number = random.randint(1, (10 ** digits) - 1)
    new_username = f"{username}#{number}"

    if models.get_user_model().objects.filter(username=new_username).exists():
        return generate_numbered_username(username, user, iteration+1)

    user.username = new_username
    user.save()

    return user


def get_lower_permission_list(user_permission):
    return list(filter(lambda t: t[0] >= user_permission, models.Participation.permissions))


def get_invite_token(link=None):
    if link is None:
        token = secrets.token_urlsafe(nbytes=32)
    else:
        token = link.rsplit('/', 1)[-1]

    return token


def get_invite_link(token=None):
    if token is None:
        token = secrets.token_urlsafe(nbytes=32)

    link = f"http://127.0.0.1:8000/invite/{token}"
    return link


def create_invite_link(board, token, **kwargs):
    if '/' in token:
        token = token.rsplit('/', 1)[-1]

    cache.set(key=token, value={"board": board, **kwargs},
              timeout=app_settings.CORE_INVITE_LINK_MAX_AGE)


def get_redirect_value(request, parm='next'):
    return request.GET.get(parm) or request.POST.get(parm)


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
