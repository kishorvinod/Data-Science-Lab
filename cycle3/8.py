import seaborn as sns
import matplotlib.pyplot as plt

# Load the iris dataset for example
iris = sns.load_dataset("iris")

# Use pair plot to display pairwise relationships
# Different kinds of plots and markers can be specified
sns.pairplot(iris, kind='scatter', markers='o')
plt.suptitle("Pairwise Relationships - Scatter")
plt.show()

sns.pairplot(iris, kind='kde', diag_kind='kde')
plt.suptitle("Pairwise Relationships - KDE")
plt.show()

sns.pairplot(iris, kind='hist', diag_kind='hist', hue='species', palette='Set1')
plt.suptitle("Pairwise Relationships - Histogram")
plt.show()

sns.pairplot(iris, kind='reg', diag_kind='kde', markers='+')
plt.suptitle("Pairwise Relationships - Regression")
plt.show()
