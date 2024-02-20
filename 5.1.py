d_2 = int(input("Que dia é hoje?"))
m_2 = int(input("Qual é o mês atual?"))
a_2 = int(input("Qual é o ano atual?"))
h_2 = int(input("Quais os dígitos da hora de agora?"))
min_2 = int(input("Qual os dígitos de minutos de agora?"))

d_3 = d_2 - 1
m_3 = m_2 - 1
a_3 = a_2 - 1970

if h_2 < 12:
    d_2 = d_2 - 1
    h_2 = h_2 + 24
    h_3 = h_2 - 12

else:
    h_3 = h_2 - 12


print("Faze(m)", a_3, "ano(s)", m_3, "meses", d_3, "dias e",
      h_3, "horas e", min_2, "minutos desde a época")
