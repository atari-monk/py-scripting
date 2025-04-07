import re
import pyperclip
from markdown import markdown
from bs4 import BeautifulSoup

def remove_all_code_content(md_text):
    """Completely remove all code blocks and their content from Markdown"""
    # Remove fenced code blocks (```) and everything between them
    md_text = re.sub(r'```[a-z]*\n.*?\n```', '', md_text, flags=re.DOTALL)
    # Remove indented code blocks (4 spaces or tab at start of line)
    md_text = re.sub(r'^[ \t]{4,}.*$', '', md_text, flags=re.MULTILINE)
    # Remove inline code (`code`)
    md_text = re.sub(r'`[^`]*`', '', md_text)
    return md_text

def markdown_to_plaintext(md_text):
    """Convert Markdown to plain text"""
    html = markdown(md_text)
    soup = BeautifulSoup(html, "html.parser")
    return soup.get_text()

def process_clipboard():
    """Get clipboard content, process it, and copy back"""
    try:
        md_content = pyperclip.paste()
        if not md_content.strip():
            print("Clipboard is empty or contains only whitespace.")
            return
        
        cleaned_md = remove_all_code_content(md_content)
        plain_text = markdown_to_plaintext(cleaned_md)
        
        pyperclip.copy(plain_text)
        print("Successfully removed all code blocks and converted to plain text.")
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    process_clipboard()