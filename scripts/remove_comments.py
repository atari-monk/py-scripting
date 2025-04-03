def remove_comments(code):
    lines = code.split('\n')
    cleaned_lines = [line for line in lines if not line.strip().startswith('#')]
    return '\n'.join(cleaned_lines)

def clean_code_file(input_file, output_file):
    with open(input_file, 'r') as f:
        code = f.read()

    cleaned_code = remove_comments(code)
    
    with open(output_file, 'w') as f:
        f.write(cleaned_code)

clean_code_file(r'C:\atari-monk\code\py-scripting\data\comments_input.py', r'C:\atari-monk\code\py-scripting\data\comments_output.py')