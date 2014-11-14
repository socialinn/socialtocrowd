import sys
import random
import string
import datetime

from django.utils import timezone

from django.core.management.base import BaseCommand, CommandError
from optparse import make_option
from django.db.models.fields import (CharField, TextField, IntegerField,
                                     DateTimeField, BooleanField)

from project.models import (Organization, Project, Thing, Donation,
                            Shipping, User)


def word(chars=20):
    l = string.letters
    return ''.join(random.choice(l) for _ in range(chars))

def phrase(words=8, chars=10):
    return ' '.join(word(random.randint(4, chars)) for _ in range(words))

def paragraphs(blocks=3, words=8, chars=10, sep="\n"):
    return sep.join(phrase(random.randint(3, words), chars) for _ in range(blocks))

def create_obj(model):
    m = model()
    for f in model._meta.fields:
        t = type(f)
        if t == CharField:
            v = phrase(random.randint(10, 20))[0:f.max_length]
            setattr(m, f.attname, v)
        elif t == TextField:
            v = paragraphs(random.randint(1, 5))
            setattr(m, f.attname, v)
        elif t == IntegerField:
            v = random.randint(-50, 50)
            setattr(m, f.attname, v)
        elif t == DateTimeField:
            v = timezone.now() + datetime.timedelta(random.randint(-360, 0))
            setattr(m, f.attname, v)
        elif t == BooleanField:
            v = bool(random.randint(0,1))
            setattr(m, f.attname, v)
    m.save()
    return m


def create_objs(model, n):
    return [create_obj(model) for _ in range(n)]


def create_org(name):
    o = Organization()
    o.name = name
    o.description = v = paragraphs(random.randint(1, 3))
    o.city = word(random.randint(6, 14))
    o.province = word(random.randint(6, 14))
    o.status = 'active'
    o.user = random.choice([i for i in User.objects.all()])
    o.save()

    for i in range(random.randint(0, 5)):
        create_project(o, "project%d" % (i+1))


def create_project(org, name):
    p = Project()
    p.name = name
    p.description = v = paragraphs(random.randint(2, 6))
    p.ong = org
    p.shipping_address = paragraphs(1)
    p.created = timezone.now() + datetime.timedelta(random.randint(-360, 0))
    p.save()

    for i in range(random.randint(1, 10)):
        create_thing(p, "thing%d" % (i+1))


def create_thing(pr, name):
    t = Thing()
    t.name = name
    t.description = v = paragraphs(random.randint(1, 2))
    t.project = pr
    t.quantity = random.randint(1, 20)
    t.save()


def create_donation(t):
    users = list(User.objects.all())

    d = Donation()

    s = Shipping(project=t.project, user=random.choice(users),
                 comment=phrase())
    s.save()

    d.thing = t
    d.shipping = s
    d.info = phrase()

    d.save()


def create_users(n):
    for i in range(n):
        uid = i + 1
        u, _ = User.objects.get_or_create(username='user%s' % uid, email='user%s@socialtocrowd.com' % uid, )
        u.set_password('123')
        u.first_name = word()
        u.last_name = word()
        u.is_active = True
        u.save()


class Command(BaseCommand):
    help = 'Creates default test data'
    args = '<number of org to create>'

    def handle(self, *args, **options):
        if len(args) != 1:
            return 'We need the number of org to create'
            sys.exit()

        s = int(args[0])

        print "creating users"
        create_users(20)

        for i in range(s):
            print "ORG%d" % (i+1)
            create_org("org%d" % (i+1))
