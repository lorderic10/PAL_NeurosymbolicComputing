from IPython.display import HTML, display
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

def display_python_code(code, style="monokai"):
    formatter = HtmlFormatter(
        style=style,
        full=False,
        noclasses=True
    )
    
    html_code = highlight(code, PythonLexer(), formatter)
    
    display(HTML(f"""
    <div style="
        background-color: #272822;
        padding: 12px;
        border-radius: 8px;
        overflow-x: auto;
        font-size: 14px;
        line-height: 1.4;
    ">
    {html_code}
    </div>
    """))