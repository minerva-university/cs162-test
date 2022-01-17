:egg: :whale:

> Life is a string of contradictions beautifully arranged by a thing called time.

A good-old `copy paste` seems not to capture me in the present-day.

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
But life goes on: <br>
- [x] Work smart, not hard

