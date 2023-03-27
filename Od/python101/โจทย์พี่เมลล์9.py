def Highlight(text, highlight):
    ls = []
    for i in text:
        if i == highlight:

            a = '[{}]'.format(i)
            ls.append(a)

        else:

            ls.append(i)
    return ls


text, highlight = input().split(',')
text2 = text.split()

H = Highlight(text2, highlight)
print(' '.join(H))
