from django.shortcuts import render

def index(request):
    return render(request, 'APP/index.html')


def generate(request):
    return render(request, 'APP/generate.html')

# views.py
from django.shortcuts import render
from django.http import HttpResponse
from .forms import PDFForm
from xhtml2pdf import pisa
from io import BytesIO

def generate_pdf(request):
    if request.method == 'POST':
        form = PDFForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            
            # Create a PDF response
            response = HttpResponse(content_type='APP/pdf')
            response['Content-Disposition'] = f'attachment; filename="{title}.pdf"'

            # Render content to PDF
            template = f"<h1>{title}</h1><p>{content}</p>"
            pisa_status = pisa.CreatePDF(BytesIO(template.encode('utf-8')), dest=response)
            
            if pisa_status.err:
                return HttpResponse('We had some errors with your PDF generation')
            return response
    else:
        form = PDFForm()
    
    return render(request, 'index.html', {'form': form})

