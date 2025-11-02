import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# DATASET de Origen 
url = 'https://gist.githubusercontent.com/Thiagobc23/4ccb4ea1c612d9d68921bf990ce28855/raw/07af955c17d1816aba58dea74d65f60210702a15/film.csv'
df = pd.read_csv(url, index_col='ID')

# Theme
sns.set_theme(style="white", rc={"axes.facecolor": (0, 0, 0, 0), 'axes.linewidth':2})
palette = sns.color_palette("Set2", 12)

# Creamos una cuadrícula con una fila para cada 'Idioma'.
g = sns.FacetGrid(df, palette=palette, row="Language", hue="Language", aspect=9, height=1.2)

# map df - Kernel Density Plot of IMDB Score for each Language
g.map_dataframe(sns.kdeplot, x="IMDB Score", fill=True, alpha=1)
g.map_dataframe(sns.kdeplot, x="IMDB Score", color='black')

# function to draw labels
def label(x, color, label):
    ax = plt.gca() #get current axis
    ax.text(0, .2, label, color='black', fontsize=14,
            ha="left", va="center", transform=ax.transAxes)
# iterate grid to plot labels
g.map(label, "Language")

# adjust subplots to create overlap
g.fig.subplots_adjust(hspace=-.5)

# remove subplot titles
g.set_titles("")

# remove yticks and set xlabel
g.set(yticks=[], xlabel="IMDB Score")
# remove left spine
g.despine(left=True)
# set title
plt.suptitle('Netflix Originals - IMDB Scores by Language', y=0.97)

plt.savefig('Netflixridgeplot.png')