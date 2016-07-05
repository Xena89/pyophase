from django.db import models
from django.template.defaultfilters import date as _date
from django.utils.translation import ugettext_lazy as _

from ophasebase.models import Ophase

class WorkshopSlot(models.Model):
    """Date and time of a workshop slot."""
    class Meta:
        verbose_name = _('Workshopslot')
        verbose_name_plural = _('Workshopslots')
        ordering = ['date', 'start_time']

    ophase = models.ForeignKey(Ophase)
    date = models.DateField(verbose_name=_('Datum'))
    start_time = models.TimeField(verbose_name=_('Beginn'))
    end_time = models.TimeField(verbose_name=_('Ende'))

    def __str__(self):
        return _date(self.date, "D, ") + _date(self.date, "SHORT_DATE_FORMAT") + _date(self.start_time, " H:i - ") + _date(self.end_time, "H:i")

    @staticmethod
    def get_current(**kwargs):
        return WorkshopSlot.objects.filter(ophase=Ophase.current(), **kwargs)


class Workshop(models.Model):
    """A workshop offered in the Ophase."""
    class Meta:
        verbose_name = _('Workshop')
        verbose_name_plural = _('Workshops')

    ophase = models.ForeignKey(Ophase)
    tutor_name = models.CharField(max_length=100, verbose_name=_('Name'))
    tutor_mail = models.EmailField(verbose_name=_('E-Mail-Adresse'))
    title = models.CharField(max_length=200, verbose_name=_('Workshoptitel'), help_text=_('Unter welcher Überschrift steht der Workshop?'))
    workshop_type = models.CharField(max_length=40, verbose_name=_('Art des Workshops'), help_text=_('Welche Art Veranstaltung ist das? Vortrag, Vortrag mit Hands-on, Workshop, Sport, Ausflug, ...'))
    possible_slots = models.ManyToManyField(WorkshopSlot, verbose_name=_('Mögliche Zeitslots'), help_text=_('Welche Slots sind zeitlich möglich (unabhängig davon wie oft der Workshop stattfinden kann)?'))
    how_often = models.PositiveSmallIntegerField(verbose_name=_('Anzahl'), help_text=_('Wie oft kann dieser Workshop angeboten werden?'))
    location_info = models.CharField(max_length=200, verbose_name=_('Raumbedarf'), help_text=_('Wo soll der Workshop stattfinden (Hörsaal, Gruppenraum, Poolraum, ...)?'))
    max_participants = models.PositiveSmallIntegerField(verbose_name=_('Max. Teilnehmerzahl'), help_text=_('Maximale Teilnehmeranzahl (auf 0 lassen für volle Raumkapazität).'))
    equipment = models.CharField(blank=True, max_length=200, verbose_name=_('Benötigtes Material'), help_text=_('Wird etwas benötigt das wir zur Verfügung stellen sollen?'))
    participant_requirements = models.TextField(blank=True, verbose_name=_('Teilnahmevoraussetzungen'), help_text=_('Benötigen die Teilnehmer Vorkenntnisse oder müssen sie etwas mitbringen?'))
    description = models.TextField(verbose_name=_('Beschreibungstext'), help_text=_('Eine kurze Beschreibung um was es geht und was die Teilnehmer erwartet.'))
    remarks = models.TextField(blank=True, verbose_name=_('Anmerkungen'), help_text=_('Sonstige Informationen'))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @staticmethod
    def get_current(**kwargs):
        return Workshop.objects.filter(ophase=Ophase.current(), **kwargs)