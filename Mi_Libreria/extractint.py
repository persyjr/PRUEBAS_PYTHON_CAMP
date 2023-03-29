#sentence = 'Gracias, tu reporte ha sido radicado con el número 6866950 '
sentence = 'El sector donde estás ubicado pertenece al circuito CONCEPCION (MAGDALENA), el cual se encuentra afectado por una falla que está clasificada con el número 5779381. Estamos trabajando para restablecer el servicio a la mayor brevedad.'
s = [int(s) for s in str.split(sentence) if s.isdigit()]
print(s)
