from itertools import chain


def trunc_line(text, font, max_width):
    real = len(text)
    s_text = text
    le = font.size(text)[0]
    cut = 0
    a = 0
    done = 1
    while le > max_width:
        a = a + 1
        n = text.rsplit(None, a)[0]
        if s_text == n:
            cut += 1
            s_text = n[:-cut]
        else:
            s_text = n
        le = font.size(s_text)[0]
        real = len(s_text)
        done = 0
    return real, done, s_text


def wrap_line(text, font, max_width):
    done = 0
    wrapped = []

    while not done:
        nl, done, s_text = trunc_line(text, font, max_width)
        wrapped.append(s_text.strip())
        text = text[nl:]
    return wrapped


def get_multi_line(text, font, max_width):
    lines = chain(*(wrap_line(line, font, max_width) for line in text.splitlines()))
    return list(lines)


def get_first_line(text, font, max_width):
    lines = get_multi_line(text, font, max_width)
    if len(lines) > 1:
        return lines[0] + " ..."
    else:
        return lines[0]
