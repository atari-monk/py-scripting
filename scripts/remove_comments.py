def remove_comments(code):
    lines = code.split('\n')
    cleaned_lines = [line for line in lines if not line.strip().startswith('#')]
    return '\n'.join(cleaned_lines)

def remove_inline_comments(code):
    lines = code.split('\n')
    cleaned_lines = []
    for line in lines:
        if has_hash_in_string(line):  
            cleaned_lines.append(line)
            continue  
        before_comment, _, _ = line.partition('#')
        cleaned_lines.append(before_comment.rstrip())
    return '\n'.join(cleaned_lines)

def has_hash_in_string(line):
    in_string = False
    string_char = None
    
    for i, char in enumerate(line):
        if char in ("'", '"'):  
            if in_string:
                if char == string_char:
                    in_string = False
            else:
                in_string = True
                string_char = char
        
        elif char == "#" and in_string:
            return True
    
    return False

def clean_code_file(input_file, output_file):
    with open(input_file, 'r') as f:
        code = f.read()

    cleaned_code = remove_comments(code)
    cleaned_code = remove_inline_comments(cleaned_code)
    
    with open(output_file, 'w') as f:
        f.write(cleaned_code)

clean_code_file(r'C:\atari-monk\code\py-scripting\data\comments_input.py', r'C:\atari-monk\code\py-scripting\data\comments_output.py')