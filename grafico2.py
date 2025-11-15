import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="ticks")

dados = pd.DataFrame({
    "Cliente": ["Ana", "Bruno", "Carla", "Daniel", "Eduarda", "Felipe", "Gabriela", "Heitor"],
    "Satisfação": [8.5, 6.0, 9.0, 7.5, 8.0, 5.5, 9.5, 7.0],
    "Categoria": ["Premium", "Básico", "Premium", "Básico", "Premium", "Básico", "Premium", "Básico"]
})

palette = sns.color_palette("rocket_r")

# ✅ AGORA SIM: usando col="Categoria" para subgráficos
sns.relplot(
    data=dados,
    x="Satisfação", 
    y="Cliente",
    hue="Categoria",      # Cor por categoria
    size="Satisfação",    # Tamanho por satisfação
    col="Categoria",      # ✅ CORRIGIDO: Subgráficos por categoria
    sizes=(100, 400),     # Tamanhos dos pontos
    palette=palette,
    height=5, 
    aspect=.75,
    facet_kws=dict(sharex=False, sharey=False)  # Cada gráfico com escalas independentes
)

plt.suptitle("Satisfação dos Clientes - Premium vs Básico 🏆", y=1.02)
plt.tight_layout()
plt.show()