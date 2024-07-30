from django.shortcuts import render
from fpdf import FPDF

def index(request):
    return render(request, 'APP/index.html')


def generate(request):
    return render(request, 'APP/generate.html')

from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
from .forms import PDFForm
from fpdf import FPDF
from io import BytesIO

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, self.title, 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(10)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        form = PDFForm()
        return render(request, 'APP/generate.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = PDFForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']

            # Create a PDF instance
            pdf = PDF()
            pdf.title = title
            pdf.add_page()
            pdf.chapter_title(title)
            pdf.chapter_body(content)

            # Generate PDF in memory
            pdf_output = BytesIO()
            pdf.output(pdf_output)
            pdf_output.seek(0)

            # Create a PDF response
            response = HttpResponse(pdf_output, content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="{title}.pdf"'

            return response
        else:
            return render(request, 'APP/generate.html', {'form': form})

