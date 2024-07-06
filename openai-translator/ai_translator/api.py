import sys
import os
from typing import Annotated

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
tmp_file_root = '/tmp/openai_translator'
os.makedirs(tmp_file_root, exist_ok=True)

from model import OpenAIModel
from translator import PDFTranslator

translator = PDFTranslator(OpenAIModel('gpt-3.5-turbo', api_key=''))
file_ext = {'pdf': 'pdf', 'markdown': 'md'}

from fastapi import FastAPI, File, Form
from fastapi.responses import FileResponse

app = FastAPI()


@app.post('/translate_pdf')
def translate_pdf(file_content: Annotated[bytes, File()], filename: Annotated[str, Form()],
                  target_lang: Annotated[str, Form()], output_fmt: Annotated[str, Form()]):
    input_path = f'{tmp_file_root}/{filename}'
    output_path = input_path.replace('.pdf', '_translated.' + file_ext[output_fmt])
    with open(input_path, 'wb') as f:
        f.write(file_content)
    translator.translate_pdf(pdf_file_path=input_path, file_format=output_fmt, target_language=target_lang)
    return FileResponse(output_path)
