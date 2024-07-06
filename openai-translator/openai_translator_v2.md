# 作业
实现 OpenAI-Translator V2.0 中的一个或多个特性

## Feature List

- [x] 支持图形用户界面（GUI），提升易用性。
- [ ] 添加对保留源 PDF 的原始布局的支持。
- [x] 服务化：以 API 形式提供翻译服务支持。
- [x] 添加对其他语言的支持。
  
## 运行Demo
项目使用Python 3.10.14版本开发

1. 下载代码
   ```
   git clone --single-branch -b openai_translator_v2 https://github.com/adengz/openai-quickstart.git
   ```
2. 在子项目路径中创建虚拟环境并安装依赖
   ```
   cd openai-quickstart/openai-translator
   python -m venv venv
   ```
3. 切换至虚拟环境并安装依赖
   ```
   source venv/bin/activate
   pip install -r requirements.txt
   ```

### GUI
1. 启动服务器
   ```
   python ai_translator/gui.py
   ```
2. 打开浏览器，在地址栏输入`http://127.0.0.1:7860/`

### API
1. 启动服务器
   ```
   fastapi dev ai_translator/api.py
   ```
2. 使用`curl`发送测试请求
   ```
   curl -X POST 'http://127.0.0.1:8000/translate_pdf' -F 'file_content=@tests/test.pdf' -F 'filename=test.pdf' -F 'output_fmt=markdown' -F 'target_lang=Chinese (Simplified)' > test_translated.md
   ```
3. 打开结果文件
   ```
   open test_translated.md
   ```