from celery import shared_task
from .models import Post, User
import datetime
import project.settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


@shared_task
def weekly_notify():
    print('Start task: "weekly_notify"')
    today = datetime.utcnow()
    last_week = today - datetime.timedelta(days=7)
    posts = Post.objects.filter(time_create__gte=last_week)
    if len(posts) == 0:
        pass
    users = set(User.objects.all())

    html_content = render_to_string(
        'callboard/daily_post.html',
        {
            'link': project.settings.SITE_URL,
            'posts': posts,
        }
    )

    msg = EmailMultiAlternatives(
        subject='Posts per week',
        body='',
        from_email=project.settings.DEFAULT_FROM_EMAIL,
        to=users,
    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()
