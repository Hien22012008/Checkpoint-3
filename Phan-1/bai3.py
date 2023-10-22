n = input('Nhập nội dung:')

def reverse_str(s: str) -> str:
    return s[:: -1]
reversed_text = reverse_str(n)
print(reversed_text)