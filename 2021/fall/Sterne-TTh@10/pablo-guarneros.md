# 🐣🙃

> Life is a string of contradictions beautifully arranged by a thing called time.

```
def get_biography(self):

	emojis = [🗽,📉,➡️,🇲🇽,
			🎨,🥥,🥛,🌍,
			🌍,🏌,🚊  ,🎧,
			🏀,🎭,🧳,🥋,
			🏉,📺,⚽️,♻️,
			🌈,🎰,👓 ,⛳️,
			📚,📽,🧳,♻️,
			🎥,📚,🏳️‍🌈,🏔,
			🎬,🎧,🧘🏽,🎾,
			🎥,🌺,👨🏽‍🎓,🏰,
			🚵‍♂️,🦄,🧠,🤿,🧑🏽‍💻]

	life_moments = {}

	for year in range(self.age):
		life_moments[year] = emojis[year*2-1:year*2+1]

	return life_moments 

pablito = Minervan() 
pablito.get_biography()

```

* I should have created a list of tuples where the index is equal to a year in my life. But let me make my life complicated. Peace. *