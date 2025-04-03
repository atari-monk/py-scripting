import markdown
from bs4 import BeautifulSoup
import pyperclip

def markdown_to_text(md_content):
    html_content = markdown.markdown(md_content)
    soup = BeautifulSoup(html_content, "html.parser")
    return soup.get_text()

def markdown_to_text_using_clipboard():
    md_content = pyperclip.paste()
    
    if not md_content.strip():
        print("Clipboard is empty or contains non-text data.")
        return

    plain_text = markdown_to_text(md_content)
    pyperclip.copy(plain_text)

    print("Converted Markdown to plain text and copied back to clipboard.")

if __name__ == "__main__":
    markdown_to_text_using_clipboard()