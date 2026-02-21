from pyscript import display, document # type: ignore (quick fix feature)


def plyers_list(e):
    document.getElementById('output').innerHTML='' #ensures the output wont repeat
