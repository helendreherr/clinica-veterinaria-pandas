
import pandas as pd 


dados = {
    "ID": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
           11, 12, 13, 14, 15, 16, 17, 18, 19],

    "CLIENTE": [
        "Juliana Martins", "Pedro Almeida", "Mariana Costa",
        "Lucas Ferreira", "Juliana Martins", "Camila Souza",
        "Lucas Ferreira", "Mariana Costa", "Pedro Almeida",
        "Mariana Costa", "Mariana Costa", "Lucas Ferreira",
        "Pedro Almeida", "Mariana Costa", "Lucas Ferreira",
        "Pedro Almeida", "Mariana Costa", "Lucas Ferreira",
        "Lucas Ferreira"
    ],

    "ANIMAL": [
        "Amora", "Simba", "Lola", "Bruce", "Belinha",
        "Luna", "Thor", "Nina", "Mel", "Lola",
        "Nina", "Bruce", "Simba", "Lola", "Belinha",
        "Mel", "Bruce", "Thor", "Nina"
    ],

    "ESPECIE": [
        "Cachorra", "Cachorro", "Cachorro", "Gato", "Cachorro",
        "Gato", "Cachorro", "Cachorro", "Gato", "Cachorro",
        "Cachorro", "Gato", "Cachorro", "Cachorro", "Cachorro",
        "Gato", "Gato", "Cachorro", "Cachorro"
    ],

    "RACA": [
        "Poodle", "Labrador", "Shih-tzu", "Siamês", "Golden Retriever",
        "Persa", "Yorkshire", "Poodle", "SRD", "Shih-tzu",
        "Poodle", "Siamês", "Labrador", "Shih-tzu", "Golden Retriever",
        "SRD", "Siamês", "Yorkshire", "Poodle"
    ],

    "VETERINARIO": [
        "Carlos Mendes", "Rafael Costa", "Mariana Lima", "Carlos Mendes",
        "Ana Souza", "Juliana Alves", "Fernanda Rocha", "Carlos Mendes",
        "Rafael Costa", "Mariana Lima", "Juliana Alves", "Carlos Mendes",
        "Ana Souza", "Mariana Lima", "Rafael Costa", "Carlos Mendes",
        "Mariana Lima", "Juliana Alves", "Ana Souza"
    ],

    "DIAGNOSTICO": [
        "Otite", "Infecção urinária", "Dermatite", "Erliquiose",
        "Infecção urinária", "Obesidade", "Cistite", "Infecção",
        "Alergia", "Otite", "Infecção", "Obesidade", "Cistite",
        "Erliquiose", "Dermatite", "Obesidade", "Infecção urinária",
        "Alergia", "Infecção"
    ],

    "VALOR": [
        180, 180, 200, 200, 180,
        160, 200, 180, 200, 180,
        180, 160, 200, 200, 200,
        160, 180, 200, 180
    ]
}

df = pd.DataFrame(dados)

print(df)

total_clinica = df["VALOR"].sum()
qtd_consultas = len(df)

ticket_medio = df["VALOR"].mean()      # média por consulta

poodle = df[df["RACA"] == "Poodle"]
total_poodle = poodle["VALOR"].sum()
qtd_poodle = len(poodle)

# "Cachorra" e "Cachorro" são a mesma ""espécie"", então o filtro aceita as duas (| = ou)
caes = df[(df["ESPECIE"] == "Cachorro") | (df["ESPECIE"] == "Cachorra")]
gatos = df[df["ESPECIE"] == "Gato"]

total_caes = caes["VALOR"].sum()
total_gatos = gatos["VALOR"].sum()

juliana = df[df["CLIENTE"] == "Juliana Martins"]
lucas = df[df["CLIENTE"] == "Lucas Ferreira"]
mariana = df[df["CLIENTE"] == "Mariana Costa"]

total_juliana = juliana["VALOR"].sum()
total_lucas = lucas["VALOR"].sum()
total_mariana = mariana["VALOR"].sum()

consultas_juliana = len(juliana)
consultas_lucas = len(lucas)
consultas_mariana = len(mariana)

otite = df[df["DIAGNOSTICO"] == "Otite"]
total_otite = otite["VALOR"].sum()

peso_otite = total_otite / total_clinica * 100

total_clinica = df["VALOR"].sum()

print("Total da clínica:", total_clinica)

carlos = df[df["VETERINARIO"] == "Carlos Mendes"]
total_carlos = carlos["VALOR"].sum()
qtd_carlos = len(carlos)


print("Faturamento total da clínica: R$", total_clinica)
print("Quantidade de consultas:", qtd_consultas)
print("Ticket médio: R$", round(ticket_medio, 2))

print("\nTotal gasto pela Juliana: R$", total_juliana, "em", consultas_juliana, "consultas")
print("Total gasto pelo Lucas: R$", total_lucas, "em", consultas_lucas, "consultas")
print("Total gasto pela Mariana: R$", total_mariana, "em", consultas_mariana, "consultas")

print("\nTotal em consultas de Poodle: R$", total_poodle, "em", qtd_poodle, "consultas")
print("Total em consultas de Otite: R$", total_otite)
print("Otite representa", round(peso_otite, 1), "% do faturamento")

print("\nFaturamento com cães: R$", total_caes)
print("Faturamento com gatos: R$", total_gatos)

print("\nFaturamento do Dr. Carlos Mendes: R$", total_carlos, "em", qtd_carlos, "consultas")
