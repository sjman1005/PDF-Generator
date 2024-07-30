from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import PDFForm
from xhtml2pdf import pisa
from io import BytesIO

def index(request):
    return render(request, 'APP/index.html')


def generate(request):
    if(request.method=='POST'):
        print(request.POST)
        form = PDFForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']

            # Create a PDF response
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="{title}.pdf"'

            # Render content to PDF
            template = f"<h1>{title}</h1><p>{content}</p>"
            pisa_status = pisa.CreatePDF(BytesIO(template.encode('utf-8')), dest=response)

            if pisa_status.err:
                return HttpResponse('We had some errors with your PDF generation', content_type='text/plain')

            return response
    return render(request, 'APP/generate.html')

# views.py

# class GeneratePdf(View):
#     def get(self, request, *args, **kwargs):
#         form = PDFForm()
#         return render(request, 'APP/generate.html', {'form': form})

#     def post(self, request, *args, **kwargs):
#         form = PDFForm(request.POST)
#         if form.is_valid():
#             title = form.cleaned_data['title']
#             content = form.cleaned_data['content']

#             # Create a PDF response
#             response = HttpResponse(content_type='application/pdf')
#             response['Content-Disposition'] = f'attachment; filename="{title}.pdf"'

#             # Render content to PDF
#             template = f"<h1>{title}</h1><p>{content}</p>"
#             pisa_status = pisa.CreatePDF(BytesIO(template.encode('utf-8')), dest=response)

#             if pisa_status.err:
#                 return HttpResponse('We had some errors with your PDF generation', content_type='text/plain')

#             return response
#         else:
#             return render(request, 'APP/generate.html', {'form': form})
