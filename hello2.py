import markdown

md_text = """
```python
def hello():
    print("Hello, World!")
```
"""

html_output = markdown.markdown(md_text, extensions=['fenced_code', 'codehilite'])
with open("output_code.html", "w") as f:
    f.write(html_output)