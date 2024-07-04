import sys
import os

import yaml
import gradio as gr

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from model import OpenAIModel
from translator import PDFTranslator

translator = PDFTranslator(OpenAIModel('gpt-3.5-turbo', api_key=''))
file_ext = {'pdf': 'pdf', 'markdown': 'md'}


def translate_file(file_path: str, target_lang: str, file_fmt: str) -> str:
    output_path = file_path.replace('.pdf', '_translated.' + file_ext[file_fmt])
    translator.translate_pdf(pdf_file_path=file_path, file_format=file_fmt, target_language=target_lang)
    return output_path


if __name__ == '__main__':
    with open('ai_translator/languages.yaml') as f:
        languages = yaml.safe_load(f)
    demo = gr.Interface(
        fn=translate_file, 
        inputs=[
            gr.File(label='Upload File', file_types=['.pdf']),
            gr.Dropdown(languages, value='Chinese (Simplified)', label='Target Language'),
            gr.Radio(['pdf', 'markdown'], value='pdf', label='Output Format'),
        ],
        outputs=[gr.File()],
        submit_btn='Translate',
        clear_btn='Reset',
        allow_flagging='never'
    )
    demo.launch()
