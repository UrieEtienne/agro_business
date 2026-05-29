from django.template.loader import get_template
from xhtml2pdf import pisa
from django.http import HttpResponse


def render_pdf(template_src, context_dict={}):

    template = get_template(template_src)

    html = template.render(context_dict)

    response = HttpResponse(
        content_type='application/pdf'
    )

    pisa.CreatePDF(
        html,
        dest=response
    )

    return response