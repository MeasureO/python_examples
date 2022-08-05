def make_tag(tagname):

    # Оборачивает входящую строку msg в тег tagname

    def wrap_a_message(msg):
        return f'<{tagname}>{msg}</{tagname}>'

    return wrap_a_message

header = make_tag('h1')
print(header('Заголовок')) # выводит <h1>Заголовок</h1>
