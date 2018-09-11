from unittest import skip

from django.core import mail
from django.test import Client, TestCase
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.utils.http import urlencode


class StaffAddView(TestCase):
    fixtures = ['ophasebase.json', 'staff.json', 'students.json']

    def test_redirect(self):
        """Test for Redirect to SSO Login page"""
        c = Client()
        suffix = urlencode({"next": reverse('staff:registration')})
        redirect_url = "{}?{}".format(reverse('pyTUID:login'), suffix)
        
        response = c.get(reverse('staff:registration'))
        
        self.assertRedirects(response, redirect_url, target_status_code=302)

    @skip
    def test_send_email(self):
        """Sending an email after successfull register"""

        # TODO Use fake SSO in test

        c = Client()

        register_view = reverse('staff:registration')

        self.assertEqual(len(mail.outbox), 0)

        testdata = {'prename': 'Leah',
                    'name': 'Bayer',
                    'email': 'leah.bayer@example.com',
                    'phone': '016031368212',
                    'matriculated_since': 'today',
                    'degree_course': 'Bachelor',
                    'experience_ophase': 'Nothing until now',
                    'is_helper': True,
                    'helper_jobs': 1,}

        # sending a incomplet form should not send a email
        response = c.post(register_view, testdata, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, 'form', 'why_participate', _('This field is required.'))
        
        self.assertEqual(len(mail.outbox), 0)
        
        # a complete form should send one email
        testdata['why_participate'] = 'You need testdata'

        response = c.post(register_view, testdata, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.redirect_chain, [(reverse('staff:registration_success'), 302)])
        
        self.assertEqual(len(mail.outbox), 1)
        smail = mail.outbox[0]
        self.assertEqual(len(smail.to), 1)
        self.assertEqual(smail.to[0], 'Leah Bayer <leah.bayer@example.com>')