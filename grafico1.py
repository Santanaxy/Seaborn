import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Dados
grafico = pd.DataFrame({
    "Produto": ["Notebook", "Celular", "Tablet", "Fone", "Monitor"],
    "Custo": [2500, 1800, 1200, 200, 900],
    "Receita": [3200, 2300, 1700, 350, 1200]
})

# Gráfico de barras da RECEITA
sns.barplot(
    data=grafico,
    x="Produto",    # Nomes dos produtos no eixo X
    y="Receita",    # Valores no eixo Y
    color="blue"    # Todas as barras azuis
)

plt.title("Receita dos Produtos 📊")
plt.xticks(rotation=45)  # Gira os nomes para caberem melhor
plt.show()