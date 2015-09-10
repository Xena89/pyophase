import io

from django.template import loader
from django.template.response import SimpleTemplateResponse
from django.http import HttpResponse
from django.db.models import Q, Count

from staff.models import HelperJob

import odswriter


def mail_export(modeladmin, request, queryset):
    """Creates a list of email addresses in "prename lastname <email@example.net>" format.
    This should be suitable for mass subscription and similar purposes.
    """
    template = loader.get_template("staff/mail_export.html")
    context = {'persons' : queryset}
    return SimpleTemplateResponse(template, context)

mail_export.short_description = "E-Mail Mass Subscription Export"


def staff_nametag_export(modeladmin, request, queryset):
    """Exports certain staff data in ods format, containing the necessary information for the name tag production application.
    The produced ods file is the input for the name tag Java aplication.
    """
    table = []
    empty = '~'
    for person in queryset.filter(Q(is_tutor=True) | Q(is_orga=True)):
        row = [person.prename, person.name]
        if person.is_tutor:
            if "master" in str(person.tutor_for).lower():
                row.append('M')
                row.append('MASTER')
            else:
                row.append('T')
                row.append('TUTOR')
        else:
            row.extend([empty]*2)
        if person.is_orga:
            row.append('ORGA')
        else:
            row.append(empty)
        row.extend([empty]*4)
        table.append(row)

    out_stream = io.BytesIO()
    with odswriter.writer(out_stream) as out:
        # need to specify number of columns for jOpenDocument compatibility
        sheet = out.new_sheet("Staff", cols=9)
        sheet.writerows(table)

    response = HttpResponse(out_stream.getvalue(), content_type="application/vnd.oasis.opendocument.spreadsheet")
    # name the file according to the expectations of the Java name tag application
    response['Content-Disposition'] = 'attachment; filename="tutoren.ods"'
    return response

staff_nametag_export.short_description = "Namensschilderexport"


def staff_overview_export(modeladmin, request, queryset):
    """Exports an overview of the staff containing contact data and field of duty.
    """
    orgas = []
    tutors = []
    helpers = []
    for person in queryset:
        row = [person.prename, person.name, person.email, person.phone]
        if person.is_orga:
            jobs = ' / '.join(sorted([str(job) for job in person.orga_jobs.all()]))
            orgas.append(row + [jobs])
        if person.is_tutor:
            tutors.append(row + [str(person.tutor_for)])
        if person.is_helper:
            jobs = ' / '.join(sorted([str(job) for job in person.helper_jobs.all()]))
            helpers.append(row + [jobs])

    orgas.sort(key=lambda row: row[1])
    tutors.sort(key=lambda row: row[1])
    helpers.sort(key=lambda row: row[1])

    out_stream = io.BytesIO()
    with odswriter.writer(out_stream) as out:
        orga_sheet = out.new_sheet("Orgas")
        orga_sheet.writerow(["Vorname", "Nachname", "E-Mail", "Handy", "Verantwortlich für ..."])
        orga_sheet.writerows(orgas)
        tutor_sheet = out.new_sheet("Tutoren")
        tutor_sheet.writerow(["Vorname", "Nachname", "E-Mail", "Handy", "Betreut ..."])
        tutor_sheet.writerows(tutors)
        helper_sheet = out.new_sheet("Helfer")
        helper_sheet.writerow(["Vorname", "Nachname", "E-Mail", "Handy", "Hilft bei ..."])
        helper_sheet.writerows(helpers)

    response = HttpResponse(out_stream.getvalue(), content_type="application/vnd.oasis.opendocument.spreadsheet")
    response['Content-Disposition'] = 'attachment; filename="Personal.ods"'
    return response

staff_overview_export.short_description = "Übersicht exportieren"


def helper_job_overview(modeladmin, request, queryset):
    """Display a matrix to show helpers with associated helper jobs.
    """
    template = loader.get_template("staff/helper_matrix.html")

    helper = queryset.filter(is_helper=True)
    jobs = HelperJob.objects.all().annotate(num_helper=Count('person')).order_by('label')

    for h in helper:
        job_interest = []
        for j in jobs:
            if h.helper_jobs.filter(id=j.id).exists():
                job_interest.append(True)
            else:
                job_interest.append(False)
        h.job_interest = job_interest

    context = {
        'helper' : helper,
        'jobs' : jobs,
    }

    return SimpleTemplateResponse(template, context)

helper_job_overview.short_description = "Helfer-Übersicht anzeigen"