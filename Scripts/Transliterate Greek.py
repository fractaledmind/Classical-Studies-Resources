# -*- coding= utf-8 -*-
import sys

gk = [u"α", u"β", u"γ", u"δ", u"ε", u"ζ", u"η", u"θ", u"ι", u"κ", u"λ", u"μ", u"ν", u"ξ", u"ο", u"π", u"ρ", u"σ", u"ς", u"τ", u"υ", u"φ", u"χ", u"ψ", u"ω"]
eng = [u"a", u"b", u"g", u"d", u"e", u"z", u"h", u"q", u"i", u"k", u"l", u"m", u"n", u"c", u"o", u"p", u"r", u"s", u"s", u"t", u"u", u"f", u"x", u"y", u"w"]
gkvowels = [u"ά", u"ὰ", u"ᾶ", u"ἀ", u"ἁ", u"ἄ", u"ἅ", u"ἂ", u"ἃ", u"ἆ", u"ἇ", u"ᾳ", u"ᾴ", u"ᾲ", u"ᾷ", u"ᾀ", u"ᾁ", u"ᾄ", u"ᾅ", u"ᾂ", u"ᾃ", u"ᾆ", u"ᾇ", u"έ", u"ὲ", u"ἐ", u"ἑ", u"ἔ", u"ἕ", u"ἒ", u"ἓ", u"ή", u"ὴ", u"ῆ", u"ἠ", u"ἡ", u"ἤ", u"ἥ", u"ἢ", u"ἣ", u"ἦ", u"ἧ", u"ῃ", u"ῄ", u"ῂ", u"ῇ", u"ᾐ", u"ᾑ", u"ᾔ", u"ᾕ", u"ᾒ", u"ᾓ", u"ᾖ", u"ᾗ", u"ί", u"ὶ", u"ῖ", u"ἰ", u"ἱ", u"ἴ", u"ἵ", u"ἲ", u"ἳ", u"ἶ", u"ἷ", u"ό", u"ὸ", u"ὀ", u"ὁ", u"ὄ", u"ὅ", u"ὂ", u"ὃ", u"ύ", u"ὺ", u"ῦ", u"ὐ", u"ὑ", u"ὔ", u"ὕ", u"ὒ", u"ὓ", u"ὖ", u"ὗ", u"ώ", u"ὼ", u"ῶ", u"ὠ", u"ὡ", u"ὤ", u"ὥ", u"ὢ", u"ὣ", u"ὦ", u"ὧ", u"ῳ", u"ῴ", u"ῲ", u"ῷ", u"ᾠ", u"ᾡ", u"ᾤ", u"ᾥ", u"ᾢ", u"ᾣ", u"ᾦ", u"ᾧ"]
engvowels = [u"a/", u"a\\", u"a=", u"a)", u"a(", u"a)/", u"a(/", u"a)\\", u"a(\\", u"a)=", u"a(=", u"a|", u"a/|", u"a\\|", u"a=|", u"a)|", u"a(|", u"a)/|", u"a(/|", u"a)\\|", u"a(\\|", u"a)=|", u"a(=|", u"e/", u"e\\", u"e)", u"e(", u"e)/", u"e(/", u"e)\\", u"e(\\", u"h/", u"h\\", u"h=", u"h)", u"h(", u"h)/", u"h(/", u"h)\\", u"h(\\", u"h)=", u"h(=", u"h|", u"h/|", u"h\\|", u"h=|", u"h)|", u"h(|", u"h)/|", u"h(/|", u"h)\\|", u"h(\\|", u"h)=|", u"h(=|", u"i/", u"i\\", u"i=", u"i)", u"i(", u"i)/", u"i(/", u"i)\\", u"i(\\", u"i)=", u"i(=", u"o/", u"o\\", u"o)", u"o(", u"o)/", u"o(/", u"o)\\", u"o(\\", u"u/", u"u\\", u"u=", u"u)", u"u(", u"u)/", u"u(/", u"u)\\", u"u(\\", u"u)=", u"u(=", u"w/", u"w\\", u"w=", u"w)", u"w(", u"w)/", u"w(/", u"w)\\", u"w(\\", u"w)=", u"w(=", u"w|", u"w/|", u"w\\|", u"w=|", u"w)|", u"w(|", u"w)/|", u"w(/|", u"w)\\|", u"w(\\|", u"w)=|", u"w(=|"]

def main():
	inp = sys.argv[1].decode('utf-8')
	chs = list(inp)

	for i, item in enumerate(chs):
		for j, jtem in enumerate(gk):
			if item == jtem:
				chs[i] = eng[j]

	for i, item in enumerate(chs):
		for j, jtem in enumerate(gkvowels):
			if item == jtem:
				chs[i] = engvowels[j]

	print ''.join(chs).encode('utf-8')
	
if __name__ == '__main__':
	main()