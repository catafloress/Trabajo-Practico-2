text = """Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

cantidad_lineas = list(text.split("\n"))
print(f"Cantidad de lineas que contiene el texto:{len(cantidad_lineas)}")

cantidad_palabras = list(text.split( ))
print(f"Cantidad de palabras que contiene el texto:{len(cantidad_palabras)}")

lineas = len(cantidad_lineas)
palabras = len(cantidad_palabras)
promedio_por_linea = palabras / lineas
print(f"El promedio de cantidad de palabras por linea del texto es de: {round(promedio_por_linea, 1)}")

palabras_por_linea = {}
print(f"Lineas por encima del promedio: {round(promedio_por_linea, 1)}")
for elem in cantidad_lineas: 
    palabras_por_linea[elem] = len(elem.split())
    if palabras_por_linea[elem] > promedio_por_linea: 
        print(f"{elem} ({palabras_por_linea[elem]} palabras)")
