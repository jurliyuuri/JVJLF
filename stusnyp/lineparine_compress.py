import json

def main():
	a = open("lineparine_tag_math.json" , "r") 
	b = json.load(a)
	b["words"] = list(filter(lambda a: len(a["tags"])==1, b["words"]))
	c = open("lineparine_tag_math_compress.json", "w") 
	json.dump(b, c)

if __name__ == '__main__':
    main()
