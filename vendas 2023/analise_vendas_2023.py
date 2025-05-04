import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt



#leitura csv vendas 2023
arquivo_csv = pd.read_csv(r"c:\Users\mathe\Downloads\vendas_desafiador_2023.csv")
df_vendas_2023 = pd.DataFrame(arquivo_csv)

#padronizaçao coluna data e criaçao da coluna mes
df_vendas_2023["data"] = pd.to_datetime(df_vendas_2023["data"])
df_vendas_2023["mes"] = df_vendas_2023["data"].dt.to_period("M")

#criaçao da coluna valor total que preço com desconto pela quantidade vendida
df_vendas_2023["valor total"] = (df_vendas_2023["preco"]-df_vendas_2023["desconto"])*df_vendas_2023["quantidade"]


#subplots
fig, axs = plt.subplots(5, 1, figsize=(14, 14))


#vendas totais por mes 2023
vendas_mes = df_vendas_2023[["mes","valor total"]]
grupo_vendaas_mes = vendas_mes.groupby(["mes"]).sum()

#grafico de linhas pra vendas totais
axs[0].plot(grupo_vendaas_mes.index.astype("str"), grupo_vendaas_mes["valor total"], linestyle = "--", marker = "o")
axs[0].set_title("Valor total de vendas por mes")
axs[0].set_xlabel("Mês")
axs[0].set_ylabel("Valor total R$")



# top 5 produtos mais vendidos
prod_quant_valor = df_vendas_2023[["produto","quantidade","valor total"]]
rank_produto_valor = prod_quant_valor.groupby(["produto"]).sum().sort_values(by="valor total", ascending=False).head()
rank_produto_quant = prod_quant_valor.groupby(["produto"]).sum().sort_values(by="quantidade", ascending=False).head()

#grafico de produtos mais vendidos
axs[1].bar(rank_produto_valor.index.astype("str"),rank_produto_valor["valor total"])
axs[1].set_title("Produto mais vendido no ano")
axs[1].set_xlabel("produto")
axs[1].set_ylabel("Valor R$")



# rank de categorias por valor e quantidade
cat_quant_valor = df_vendas_2023[["categoria","quantidade","valor total"]]
ran_categoria_valor = cat_quant_valor.groupby(["categoria"]).sum().sort_values(by="valor total",ascending=False)
ran_categoria_quant = cat_quant_valor.groupby(["categoria"]).sum().sort_values(by="quantidade",ascending=False)

#grafico de categorias por valor e rank
axs[2].barh(ran_categoria_quant.index.astype("str"),ran_categoria_quant["quantidade"])
axs[2].set_title("Categoria mais vendida no ano valor")
axs[2].set_ylabel("categoria")
axs[2].set_xlabel("quantidade")

axs[3].barh(ran_categoria_valor.index.astype("str"),ran_categoria_valor["valor total"])
axs[3].set_title("Categotia mais vendida no ano quantidade")
axs[3].set_ylabel("categoria")
axs[3].set_xlabel("valor total R$")


# media de deconto loja
loja_desc = df_vendas_2023[["loja","desconto"]]
media_loja_desc = loja_desc.groupby(["loja"]).mean()

#Grafico media de desconto no ano por loja
axs[4].bar(media_loja_desc.index.astype("str"),media_loja_desc["desconto"])
axs[4].set_title("Media de desconto por loja")
axs[4].set_xlabel("Loja")
axs[4].set_ylabel("Media desconto")


# media de desconto categoria
cate_desc = df_vendas_2023[["categoria","desconto"]]
media_cate_desc = cate_desc.groupby(["categoria"]).mean()


#comparaçao entre lojas
loja_valor_quant = df_vendas_2023[["loja","quantidade","valor total"]]
melhor_loja_tot = loja_valor_quant.groupby(["loja"]).sum().sort_values(by="valor total",ascending=False)
melhor_loja_med = loja_valor_quant.groupby(["loja"]).mean().sort_values(by="valor total",ascending=False)

plt.tight_layout()
plt.show()

