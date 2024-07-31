# PDF Generator using Python-Django

This project is a PDF generator built with Python and Django. It enables users to generate high-quality PDFs from the content they type.

## Features

- Display a form to collect title and content from the user.
- Generate a PDF file based on the user input.
- Download the generated PDF file.

## Prerequisites

- Python 3.x
- Django 3.x or higher
- xhtml2pdf (for PDF generation)

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/pdf-generator.git
    cd pdf-generator
    ```

2. Create and activate a virtual environment:

    ```sh
    python3 -m venv env
    source env/bin/activate
    ```

3. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

4. Run the Django migrations:

    ```sh
    python manage.py migrate
    ```

5. Start the Django development server:

    ```sh
    python manage.py runserver
    ```

## Usage

1. Go to the home page at `http://127.0.0.1:8000` and you will see a link to generate a PDF.
2. Click on the link to open the PDF generation form.
3. Fill in the title and content fields, then submit the form.
4. If the form is valid, a PDF file will be generated and downloaded automatically.

## Screenshots
![Home Page](https://github.com/user-attachments/assets/39ee8f81-822f-425f-a7ac-1d64a6a0aed3)

![Generation HTML](https://github.com/user-attachments/assets/90c3d8c5-68c1-4888-98ce-30e798cb7b37)

![Text to be Generated](https://github.com/user-attachments/assets/29b1fa30-7700-4726-8d0b-2a7bc8f41ffd)

![PDF Title](https://github.com/user-attachments/assets/399bcb3f-f988-4fcb-a292-c7eb55177338)
Generated PDF


## Project Structure

- `views.py`: Contains the view functions for rendering the form and generating the PDF.
- `forms.py`: Defines the `PDFForm` form class for collecting user input.
- `templates/APP/`: Contains the HTML templates for the form and the home page.

## Acknowledgements

- [xhtml2pdf](https://pypi.org/project/xhtml2pdf/) - For PDF generation.
- [Django](https://www.djangoproject.com/) - The web framework used.
