#pedir ao usuario uma temperatura e determinar se esta frio, morno ou quente
temperatura= float (int(input(" digite a temperatura:")))
if temperatura < 20:
    print ('temperatura: frio')
elif temperatura >20 <26 :
    print (" temperatura: morno")

elif temperatura >27:
    print (" temperatura: quente")

