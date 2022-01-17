
def format_dict_str(d, name):
    arr_l = [len(name)]
    for k, syns in d.items():
        arr_l.append(len(k))
        arr_l += [len(s) for s in syns]

    ll = max(arr_l)

    tab = """{} ========\n{:<{}} Synonyms\n{} ========\n""".format(ll*'=', name, ll, ll*'=')

    for k, syns in sorted(d.items(), key=lambda i: i[0]):
        tab += "{:<{}} {}\n".format(k, ll, syns[0] if len(syns) > 0 else '')
        if len(syns) > 1:
            for s in syns[1:]:
                tab += "\n{} {}\n".format(ll*' ', s)

    tab += "{} ========".format(ll*'=')
    return tab.strip()

def format_dict_enum(d, name):
    return format_dict_str({k.name: v for k,v in d.items()}, name)

