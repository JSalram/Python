#!/usr/bin/env python
# coding: utf-8

# Cargas las librerías e ignorar los warnings
import warnings

warnings.simplefilter('ignore')

import numpy as np
import pandas as pd

# Librerías de visualización
import seaborn as sns

import matplotlib.pyplot as plt
import matplotlib

matplotlib.style.use('ggplot')

# carga de la librería datetime para el tratamiento de fechas
from datetime import datetime

# Configuración de pandas
pd.set_option('display.max_columns', 500)
pd.set_option('display.max_rows', 100)

# Configuración de Seaborn
sns.set_context("notebook")
sns.set_palette('husl')

# Primera carga de datos solo cargamos 10 elementos
# Sirve para tener una primera idea del set de datos
# y no sobrecargar la memoria del ordenador
df = pd.read_csv('./data/fifa18-player-dataset.csv', encoding='utf_8', nrows=10)
print(df.shape)
print(df.columns)

# Visualización de los primeros elementos del dataframe
print(df.head())
print(df.head(2))  # Muestra solo los dos primeros registros

# Visualización de los últimos elementos del df
print(df.tail(8))

# Visualización de n elementos al azar
print(df.sample(7))

# Podemos enumerar y ver todas las columnas del dataframe usando un bucle.\n",
# Esto nos puede ayudar a descartar qué campos utilizar y cuáles no. Además\n",
# al imprimir el número de columna es más fácil hacer esa selección.\n",
for e, col in enumerate(df.columns):
    print(e, "->", col)

# Podríamos eliminar todas las columnas restantes pero pandas nos ofrece
# seleccionar qué columnas queremos leer del fichero.
columnas_a_leer = [0, 2, 3, 6, 7, 8, 9, 10, 14, 19]

# cargar los datos seleccionados
df = pd.read_csv('./data/fifa18-player-dataset.csv', encoding='utf_8',
                 usecols=columnas_a_leer)

columnas_a_leer = ['ID', 'full_name', 'club', 'age', 'league',
                   'birth_date', 'height_cm', 'weight_kg', 'nationality',
                   'overall']
df = pd.read_csv('./data/fifa18-player-dataset.csv', encoding='utf_8',
                 usecols=columnas_a_leer)
#  Comprobamos que solo se han cargado las columnas seleccionadas:
print(df.shape)

# El índice por defecto es un índice autonumérico de 0..n, para hacer que el
# índide sea el ID del jugador ejecutamos:
df = df.set_index('ID')

# Información de las columnas del dataframe
print(df.info())

# A continuación, y tras ver los datos del data set vamos a confirmar que
# no hay duplicados, si los hubiera, habría que eliminarlos.
# print(df.duplicated().value_counts())
print(df.duplicated())  # Esto devuelve un DataFrame de tipo Booleao no lógioco

print(df['club'].duplicated().value_counts())
print(df['full_name'].duplicated().value_counts())

print(df[df['full_name'].duplicated()]['full_name'].value_counts().head(5))
# Esa linea es la misma que la siguiente que sirve para aclarar
# df[df['full_name'].duplicated() == True]['full_name'].value_counts().head(5)
#

# Visualizamos el tipo de dato que devuelve ejecutar pd.isnull(df).sum()
type(pd.isnull(df).sum())

print(pd.isnull(df).sum())

print(df[pd.isnull(df['club'])][['full_name', 'age', 'nationality']].head(6))

print(df[pd.isnull(df['club'])]['nationality'].value_counts().head(10))

print(df['club'].isnull().value_counts() / len(df))

print((df[pd.isnull(df['club'])]['nationality'].value_counts() / len(df)).head(10))

df['club'].fillna("Unknown", inplace=True)
df['league'].fillna("Unknown", inplace=True)
print(df['club'].isnull().value_counts() / len(df))

print(df['birth_date'].head(5))

df['birth_date'] = pd.to_datetime(df['birth_date'])
print(df['birth_date'].head(5))

df = df.reset_index().set_index('full_name')

print(df['birth_date'].apply(lambda x: datetime.strftime(x, '%d-%M-%y')).head(3))

print(df['birth_date'].apply(lambda x: datetime.strftime(x, '%A %d %B %Y')).head(3))

print(df['birth_date'].apply(lambda x: datetime.strftime(x, '%x')).head(3))

df['day'] = pd.DatetimeIndex(df['birth_date']).day
df['month'] = pd.DatetimeIndex(df['birth_date']).month
df['year'] = pd.DatetimeIndex(df['birth_date']).year

df['day'] = pd.to_numeric(df['day'])
df['month'] = pd.to_numeric(df['month'])
df['year'] = pd.to_numeric(df['year'])

print((df['month'].value_counts() / (len(df))) * 100)

print(df['overall'].describe())

limites = np.linspace(start=0,
                      stop=100,
                      num=5)
print(limites)

limites = np.linspace(start=min(df['overall']),
                      stop=max(df['overall']),
                      num=5)
print(limites)

etiquetas_categorias = ['bajo', 'medio', 'alto', 'muy_alto']
df['categorias_overall'] = pd.cut(x=df['overall'],
                                  bins=limites,
                                  labels=etiquetas_categorias,
                                  include_lowest=True)
#  Indica si quieres incluir el primer intervalo
print(df['categorias_overall'].value_counts())

print(df['categorias_overall'].value_counts() / len(df))

agrupaciones = np.linspace(start=0,
                           stop=100,
                           num=6)
etiquetas = ['muy_bajo', 'bajo', 'medio', 'alto', 'muy_alto']
df['categorias_overall_2'] = pd.cut(x=df['overall'],
                                    bins=agrupaciones,
                                    labels=etiquetas,
                                    include_lowest=True)
#  Indica si quieres incluir el primer intervalo
print(df['categorias_overall_2'].value_counts() / len(df))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#  1 . Visualización de la información general sobre la distribución
#       del mes de nacimiento en los jugadores de fútbol.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

sns_plot = sns.catplot(x='month', data=df, kind="count", height=5,
                       aspect=3, edgecolor='black')

# titulo
sns_plot.fig.subplots_adjust(top=.9)

monthList = ['Ene', 'Feb', 'Mar', 'Abr',
             'May', 'Jun', 'Jul', 'Ago',
             'Sep', 'Oct', 'Nov', 'Dic']
sns_plot.set_xticklabels(monthList)

sns_plot.fig.suptitle("Nacimiento de jugadores de fútbol por mes")
sns_plot.set_ylabels("Número de nacimientos")
sns_plot.set_xlabels("Mes de nacimiento")

# Extraer el eje actual de la imagen
ax = plt.gca()

# Añadir texto a cada columna
for p in ax.patches:
    ax.text(p.get_x() + p.get_width() / 2., p.get_height(),
            '{0}'.format(int(p.get_height())),
            fontsize=10, color='black', ha='center', va='bottom')

plt.show()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#  2. Visualización de la densidad de nacimientos por mes.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

ax = sns.kdeplot(df['month'], label='Mes de nacimiento', shade=True)
# ax.figure.savefig("2_densidad_mes_nacimiento.png")
# Descomenta esta linea si quieres guardar la imagen
plt.show()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#  3. Visualización del efecto del mes de nacimiento en la “calidad” u
#     “overall” de un jugador.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

df_overall = df.groupby(['month'])['overall'].mean()

ax3 = df_overall.plot()
ax3.set_title("Overall de un jugador respecto del mes de nacimiento")
# ax3.figure.savefig("3_relacion_calidad_mes_nacimiento.png")
# Descomenta esta linea si quieres guardar la imagen


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#  4. Densidad del mes de nacimiento y el año
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

sns_plot = sns.FacetGrid(df, col="year", col_wrap=5)
sns_plot.map(sns.kdeplot, "month")
plt.show()
# sns_plot.savefig("4_nacimiento_por_años.png")
# Descomenta esta linea si quieres guardar la imagen


# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#  5. Visualización de la densidad de nacimiento en el año 1997 y 2000
#      concretos
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

df[df['year'] == 1997]['month'].describe()
df[df['year'] == 2000]['month'].describe()
label_1997 = "1997, {0} jugadores".format(len(df[df.year == 1997]))
label_2000 = "2000, {0} jugadores".format(len(df[df.year == 2000]))

ax5 = sns.kdeplot(df[df['year'] == 1997]['month'],
                  label=label_1997, shade=True)

ax5 = sns.kdeplot(df[df['year'] == 2000]['month'],
                  label=label_2000, shade=True)

df['year'].value_counts()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#  6. Visualización de la densidad de nacimiento por liga.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

df['league'].value_counts().head(15)

top6leagues = ["Spanish Primera División", "English Premier League",
               "Italian Serie A", "French Ligue 1",
               "Colombian Primera A", "Argentinian Superliga"]
df_plot = df[df['league'].isin(top6leagues)].copy()
df_plot.head()

sns_plot6 = sns.catplot(x='month', data=df_plot, kind="count",
                        hue='league', height=8, aspect=2, edgecolor='black')
sns_plot6.fig.subplots_adjust(top=.9)

monthList = ['Ene', 'Feb', 'Mar', 'Abr',
             'May', 'Jun', 'Jul', 'Ago',
             'Sep', 'Oct', 'Nov', 'Dic']
sns_plot6.set_xticklabels(monthList)

sns_plot6.fig.suptitle('Nacimiento mensual comparativo por liga en la que juega')
sns_plot6.set_ylabels("Cantidad de nacimientos")
sns_plot6.set_xlabels("Mes de nacimiento")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#  7. Visualización de la distribución de mes de nacimiento por equipo.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

topclub = ["Real Madrid CF", "Grêmio", "Manchester United", "FC Barcelona",
           "Paris Saint-Germain", "Flamengo", "Juventus", "FC Bayern Munich",
           "Manchester City", "FC Red Bull Salzburg"
           ]

for club in topclub:
    ax8 = sns.kdeplot(df_plot[df_plot['club'] == club]['month'],
                      label=club, legend=True)

ax8.set_title("Densidad de nacimiento en equipos de fubol", fontsize=10)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#  8. Visualización
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

df_plot = df[df['club'].isin(topclub)]
g = sns.catplot(x="month", y="club", data=df_plot, kind='box',
                height=4, aspect=2, palette='bright')

g.fig.subplots_adjust(top=.9)
g.fig.suptitle('Distribución del mes de nacimiento de las plantillas')
g.set_ylabels("Nombre del equipo")
g.set_xlabels("Mes de nacimiento")
