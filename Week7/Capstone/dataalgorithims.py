
df = pd.read_csv("covid.csv", encoding='latin-1')

numbers = df["Active"].value_counts()
paths = df["Active"].value_counts().keys()


plt.title("State wise recovery cases of COVID-19 in USA")
plt.ylabel("Actve")
plt.xlabel("Province/State")
plt.xticks(rotation = 75)
print(df["Country_Region"])

plt.bar(df["Province_State"], df["Active"])
plt.show()