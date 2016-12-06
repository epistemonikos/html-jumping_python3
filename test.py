from html_jumping import HtmlJumping
handler = HtmlJumping()
urls = [
        {
        'url': 'http://pypi.python.org/pypi',
        'method': 'GET'
        },
        {
        'url': 'http://pypi.python.org/pypi',
        'method': 'GET',
        'body': {
        'term': 'html_jumping',
        ':action': 'search',
        'submit': 'search'
        }
        }
        ]
received_header, received_content = handler.get(
                                                urls,
                                                proxy_info = {'host': '127.0.0.1', 'port': '8081'}
                                                )

print(received_header)
print(received_content)