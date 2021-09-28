if input("Is de kaas geel? (J/N) : ") == 'J':
    if input("Zitten er gaten in? (J/N) : ") == 'J':
        if input("is de kaas belachelijk duur? (J/N) : ") == 'J':
            print('Emmenthaler')
        else:
            print('leerdammer')
    else:
        if input("is de kaas zo hard al steen? (J/N) : ") == 'J':
            print("Pamigiano Reggianno")
        else:
            print("Goudse kaas")
else:
    if input("Heeft de kaas blauwe schimmels? (J/N) : ") == 'J':
        if input("Heeft de kaas een korst? (J/N) : ") == 'J':
            print("Bleu de Rochbaron")
        else:
            print("Foume d'Ambert")
    else:
        if input("Heeft de kaas een korst? (J/N) : ") == 'J':
            print("Camembert")
        else:
            print("Mozzarella")