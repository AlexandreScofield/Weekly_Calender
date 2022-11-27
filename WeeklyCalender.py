agenda = [['HORÁRIOS','SEGUNDA','TERÇA','QUARTA','QUINTA','SEXTA','SÁBADO','DOMINGO'],['08:00','      ','      ','      ','      ','      ','      ','      '],['09:00','      ','      ','      ','      ','      ','      ','      '],['10:00','      ','      ','      ','      ','      ','      ','      '],['11:00','      ','      ','      ','      ','      ','      ','      '],['12:00','      ','      ','      ','      ','      ','      ','      '],['13:00','      ','      ','      ','      ','      ','      ','      '],['14:00','      ','      ','      ','      ','      ','      ','      '],['15:00','      ','      ','      ','      ','      ','      ','      '],['16:00','      ','      ','      ','      ','      ','      ','      '],['17:00','      ','      ','      ','      ','      ','      ','      ']]
def Cad_comp():
        while True:
                list = []
                comp = str(input('Qual o compromisso?\n'))
                hora = str(input('Qual o horário?\n'))
                for i in range (len(agenda)):
                    if hora == agenda[i][0]:
                        dia = str.upper(input('Qual o dia?\n'))
                        for j in range (len(agenda[0])):
                            if dia == agenda[0][j]:
                                for x in range (j, len(agenda[0])):
                                    list.append(agenda[i][x])
                                for x in range (len(agenda[0]), j, -1):
                                    agenda[i].pop(x-1)
                                agenda[i].append(comp)
                                list.pop(0)
                                for x in range (len(list)):
                                    agenda[i].append(list[x])
                x = str.upper(input('Deseja continuar?(S/N)\n'))
                if 'N' in x:
                        break                                
Cad_comp()
def X():
        cont_dias = 0
        cont_horas = 0
        list_comp = []
        x = int(input('Deseja realizar a consulta (1) por dia da semana ou (2) por horário?\n'))
        if x == 1:
            dias_semana = str.upper(input('Quais dias da semana?(ex:Segunda,Terça)\n')).split(',')
            for i in range(len(agenda[0])):
                for j in range(len(dias_semana)):
                            if dias_semana[j] == agenda[0][i]:
                                for y in range(1,len(agenda)):
                                        if agenda[y][i] == '      ':
                                                cont_dias += 1
                                        else:
                                              list_comp.append(agenda[y][i])  
                                if cont_dias == (len(agenda)-1):
                                            print(dias_semana[j],'não possui nenhum compromisso')
                                            z = str.upper(input('Deseja adicionar compromisso?(S/N)\n'))
                                            if 'S' in z:
                                                    Cad_comp()
                                else:
                                            for w in range(len(agenda)):
                                                    print(agenda[w][0],agenda[w][i])
            return list_comp
        else:
            horas_dia = str(input('Quais horários?(ex:08:00,09:00)\n')).split(',')
            for i in range(len(agenda)):
                    for j in range(len(horas_dia)):
                            if horas_dia[j] == agenda[i][0]:
                                    for y in range(1,len(agenda[0])):
                                            
                                            if agenda[i][y] == '      ':
                                                    cont_horas += 1
                                            else:
                                                    list_comp.append(agenda[i][y])
                                    if cont_horas == (len(agenda[0])-1):
                                            print(horas_dia[j],'não possui nenhum compromisso')
                                            z = str.upper(input('Deseja adicionar compromisso?(S/N)\n'))
                                            if 'S' in z:
                                                    Cad_comp()
                                    else:
                                            for w in range(len(agenda[0])):
                                                    print(agenda[0][w],agenda[i][w])
        return list_comp
X()
