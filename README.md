# BMSIT&M College Website

A responsive, multi-page college website for **BMS Institute of Technology & Management**, Bengaluru. The project uses Flask for routing, server-rendered templates, and editable website information, with a modern university-style visual design.

## Pages

- Home
- About BMSIT&M
- Academic Programmes
- Admissions
- Contact
- Admin content editor

## Features

- Responsive desktop, tablet, and mobile layouts
- Sticky navigation and mobile menu
- University-style homepage sections
- Editable college name, tagline, hero text, contact details, statistics, and admissions content
- JSON-based content storage
- Server-rendered pages with Jinja templates
- Back-end admin interface
- Accessible form labels and keyboard-friendly controls

## Project Structure

```text
app.py                  Flask application and routes
requirements.txt        Python dependencies
data/site_data.json     Editable website content
templates/              Jinja HTML templates
static/css/style.css    Website styles
static/js/script.js     Navigation and interface behaviour
```

## Prerequisites

- Python 3.10 or newer
- macOS, Linux, or Windows

## Installation

Clone the repository and enter the project directory:

```bash
git clone https://github.com/teres-nidhi/College_webpage.git
cd College_webpage
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install Flask:

```bash
python3 -m pip install -r requirements.txt
```

## Run Locally

```bash
python app.py
```

Open:

- Website: http://127.0.0.1:5050
- Admin editor: http://127.0.0.1:5050/admin

## Editing Website Content

Open the admin page and update the college information, then click **Save changes**. Updated values are written to:

```text
data/site_data.json
```

The homepage and public pages read this file automatically.

## Contact and Admission Forms

The current contact form provides frontend validation and interaction. It does not send data or store submissions until a backend mail or database integration is added.

## Production Notes

The bundled Flask development server is suitable for local development only. For deployment, configure:

- A production WSGI server such as Gunicorn or Waitress
- A persistent database instead of a JSON file if concurrent admin edits are expected
- Authentication for the admin route
- Environment-based secret management
- HTTPS and firewall controls
- A mail or CRM integration for enquiry submissions

## Image Assets

Most editorial images are loaded from Unsplash placeholders. Replace them with licensed or official BMSIT&M photography before production deployment.

## License

This project is provided for the BMSIT&M website development demonstration. Add an appropriate license before public commercial reuse.
