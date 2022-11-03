import io
from pathlib import Path
from django.http import FileResponse
from django.views.generic import View
from django.core.handlers.wsgi import WSGIRequest

from reportlab.pdfgen import canvas

# ---------- WeasyPrint

from django.core.files.storage import FileSystemStorage
from django.template.loader import render_to_string
from django.http import HttpResponse

from weasyprint import HTML

from django.conf import settings


class ReportLabView(View):

    def get(self, request: WSGIRequest, *args, **kwargs):

        # Cria um buffer para receber os dados e gerar o pdf
        buffer = io.BytesIO()

        # cria o arquivo pdf com o buffer
        pdf = canvas.Canvas(buffer)

        # insere dados no pdf
        # inferior esquerdo = 0, 0
        # x = coluna
        # y = linha
        pdf.drawString(1, 1, 'PDF')
        pdf.drawString(1, 20, 'PDF2')

        # após inserir dados no pdf, executar:
        # encerra a página, também usado para iniciar outra página
        pdf.showPage()
        pdf.save()

        # retorna o buffer para o inicio do arquivo
        buffer.seek(0)

        # return FileResponse(buffer, as_attachment=True, filename='arquivo.pdf') # faz o download
        return FileResponse(buffer, filename='arquivo.pdf')  # abre no navegador


class WeasyprintView(View):

    def get(self, request: WSGIRequest, *args, **kwargs):

        file_name = 'relatorio_weasy.pdf'
        output_dir = Path(settings.BASE_DIR) / "temp" / file_name

        if not output_dir.parent.exists():
            output_dir.parent.mkdir(parents=True)

        text = ['Relatorio', 'Linha', 'Mais linha', 'PDF']
        html = render_to_string('relatorio.html', {'text': text})

        html = HTML(string=html)
        html.write_pdf(target=output_dir)
        fs = FileSystemStorage(output_dir.parent)
        with fs.open(str(output_dir)) as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            # response['Contet-Disposition'] = f'attachment; filename={file_name}'  # faz download ao abrir a pagina
            response['Contet-Disposition'] = f'inline; filename={output_dir.name}'  # abre no navegador

        output_dir.unlink()

        return response
