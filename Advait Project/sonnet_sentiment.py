import string

SONNET_130 = """
My mistress' eyes are nothing like the sun;
Coral is far more red than her lips' red;
If snow be white, why then her breasts are dun;
If hairs be wires, black wires grow on her head.
I have seen roses damasked, red and white,
But no such roses see I in her cheeks;
And in some perfumes is there more delight
Than in the breath that from my mistress reeks.
I love to hear her speak, yet well I know
That music hath a far more pleasing sound;
I grant I never saw a goddess go;
My mistress, when she walks, treads on the ground.
And yet, by heaven, I think my love as rare
As any she belied with false compare.
"""
POSITIVE_WORDS = {
    "love": 1, "delight": 1, "rare": 1, "pleasing": 1, "heaven": 1,
     "goddess": 1, "music": 1, "breasts": 1, "roses": 1, "mistress": 1
}
NEGATIVE_WORDS = {
    "reeks": -1, "nothing": -1, "belied": -1, "false": -1,
    "dun": -1, "wires": -1, "black": -1, "no": -1,
    "never": -1, "ground": -1, "treads": -1,
}
def sentiment_analysis(text):
    translator = str.maketrans('', '', string.punctuation)
    cleaned_text = text.translate(translator).lower()
    words = cleaned_text.split()
    
    score = 0
    for word in words:
        if word in POSITIVE_WORDS:
            score += POSITIVE_WORDS[word]
        elif word in NEGATIVE_WORDS:
            score += NEGATIVE_WORDS[word]
    return score
if __name__ == "__main__":
    score = sentiment_analysis(SONNET_130)
    print(f"Sentiment Score: {score}")
