# -*- coding: utf-8 -*-

from django.shortcuts import render
from django import forms
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from studentsdb.settings import ADMIN_EMAIL
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
import logging


# English locale
class ContactFormEng(forms.Form):
    """docstring for ContactFormEng"""

    def __init__(self, *args, **kwargs):
        # call original initializator
        super(ContactFormEng, self).__init__(*args, **kwargs)

        # this helper object allows us to us to customize form
        self.helper = FormHelper()

        # form tag attributes
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('contact_admin')

        # twitter bootstrap styles
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control label'
        self.helper.field_class = 'col-sm-10'

        # from buttons
        self.helper.add_input(Submit('send_button', u"Send"))

    # from_email =forms.EmailField(label = u"Your email adress")
    # from_email = EMAIL_HOST_USER

    from_email = forms.EmailField(label=u"Email")

    subject = forms.CharField(
        label="Name",
        max_length=128)

    message = forms.CharField(
        label="Message",
        widget=forms.Textarea)


# Ukranian locale
class ContactFormUkr(forms.Form):
    """docstring for ContactFormUkr"""

    def __init__(self, *args, **kwargs):
        # call original initializator
        super(ContactFormUkr, self).__init__(*args, **kwargs)

        # this helper object allows us to us to customize form
        self.helper = FormHelper()

        # form tag attributes
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('contact_admin')

        # twitter bootstrap styles
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control label'
        self.helper.field_class = 'col-sm-10'

        # from buttons
        self.helper.add_input(Submit('send_button', u"Надіслати"))

    from_email = forms.EmailField(label=u"Ваша емайл адресса")

    subject = forms.CharField(
        label=u"Заголовок",
        max_length=128)

    message = forms.CharField(
        label=u"Текст повідомлення",
        widget=forms.Textarea)


# Russian Locale
class ContactFormRus(forms.Form):
    """docstring for ContactFormRus"""

    def __init__(self, *args, **kwargs):
        # call original initializator
        super(ContactFormRus, self).__init__(*args, **kwargs)

        # this helper object allows us to us to customize form
        self.helper = FormHelper()

        # form tag attributes
        self.helper.form_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('contact_admin')

        # twitter bootstrap styles
        self.helper.help_text_inline = True
        self.helper.html5_required = True
        self.helper.label_class = 'col-sm-2 control label'
        self.helper.field_class = 'col-sm-10'

        # from buttons
        self.helper.add_input(Submit('send_button', u"Отправить"))

    from_email = forms.EmailField(label=u"Ваш емайл адресс")

    subject = forms.CharField(
        label=u"Заголовок",
        max_length=128)

    message = forms.CharField(
        label=u"Текст сообщения",
        widget=forms.Textarea)

    files = forms.FileField(required=False)


def contact_admin(request):
    txt = 'Name: '
    email = ', Email: '

    emails = ['lemk@ukr.net', 'rotmistrov1111@i.ua', 'lemk1997@gmail.com', 'lemk1967@gmail.com', 'catmixo123@gmail.com']

    # if english locale
    if request.COOKIES.get('django_language') == 'en':
        if request.method == 'POST':
            form = ContactFormEng(request.POST)

            if form.is_valid():
                from_email = form.cleaned_data['from_email']
                subject = txt + form.cleaned_data['subject'] + email + from_email
                message = form.cleaned_data['message']

                html = request.body
                noreply_message = html
                noreply_subject = "Thank for you message " + form.cleaned_data['subject'] + " from Daniil Kostyshak."

                try:
                    send_mail(subject, message, from_email, [ADMIN_EMAIL])
                    send_mail(noreply_subject, noreply_message, ADMIN_EMAIL, [emails])
                # send_mail(my_subject, my_message, ADMIN_EMAIL, emails)

                except Exception:
                    message = u"When you send an unexpected" \
                              "error occurred. Try this form later."
                    logger = logging.getLogger(__name__)
                    logger.exception(message)
                else:
                    message = u"Message sent successfully !"

                return HttpResponseRedirect(
                    u'%s?status_message=%s' % (reverse('contact_admin'), message))
        else:
            form = ContactFormEng()

        return render(request, 'students/contact_admin.html', {'form': form})

    # if ukranian locale
    if request.COOKIES.get('django_language') == 'uk':
        if request.method == 'POST':
            form = ContactFormUkr(request.POST)
            if form.is_valid():
                subject = form.cleaned_data['subject']
                message = form.cleaned_data['message']
                from_email = form.cleaned_data['from_email']

                try:
                    send_mail(subject, message, from_email, [ADMIN_EMAIL])

                except Exception:
                    message = u"Під час відправки виникла" \
                              u" непередбачувана помилка." \
                              u" Спробуйте скористатись данною формою пізніше."
                    logger = logging.getLogger(__name__)
                    logger.exception(message)
                else:
                    message = u"Повідомлення успішно надіслане !"

                return HttpResponseRedirect(
                    u'%s?status_message=%s' % (reverse('contact_admin'), message))
        else:
            form = ContactFormUkr()

        return render(request, 'students/contact_admin.html', {'form': form})

    # if russian locale
    if request.COOKIES.get('django_language') == 'ru':
        if request.method == 'POST':
            form = ContactFormRus(request.POST, request.FILES)
            if form.is_valid():
                subject = form.cleaned_data['subject']
                message = form.cleaned_data['message']
                from_email = form.cleaned_data['from_email']

                email = EmailMessage(subject, message, from_email, [ADMIN_EMAIL])

                if request.FILES:
                    files = request.FILES['files']
                    email.attach(files.name, files.read(), files.content_type)

                try:
                    # send_mail(subject, message, from_email, [ADMIN_EMAIL])
                    email.send()

                except Exception:
                    message = u"Во время отправки сообщения возникла" \
                              u" непредвиденная ошибка. Попробуйте воспользоватся" \
                              u"данной формой позже."
                    logger = logging.getLogger(__name__)
                    logger.exception(message)
                else:
                    message = u"Сообщение успешно отправлено !"

                return HttpResponseRedirect(
                    u'%s?status_message=%s' % (reverse('contact_admin'), message))
        else:
            form = ContactFormRus()

        return render(request, 'students/contact_admin.html', {'form': form})
