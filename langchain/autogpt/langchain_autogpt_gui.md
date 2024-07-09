# 作业
实现 LangChain 版本的 AutoGPT 项目的图形化界面

## 运行Demo
项目使用Python 3.10.14版本开发

1. 下载代码
   ```
   git clone --single-branch -b langchain_autogpt_gui https://github.com/adengz/openai-quickstart.git
   ```
2. 在子项目路径中创建虚拟环境并安装依赖
   ```
   cd openai-quickstart/langchain/autogpt
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
   python gui.py
   ```
2. 打开浏览器，在地址栏输入`http://127.0.0.1:7860/`
