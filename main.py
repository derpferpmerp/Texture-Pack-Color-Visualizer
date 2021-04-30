from Color import GColor
import sys,os
mcmetalist=list([x for x in os.listdir("./MCMETA/") if os.path.isfile(os.path.join("./MCMETA/", x)) and x.split(".")[-1]=="mcmeta"])
lstdesc=list([[__import__("json").loads(line) for line in open(f"./MCMETA/{g}.mcmeta", 'r').read().split('\n')][0]["pack"]["description"] for g in list([os.path.splitext(os.path.basename(f"./MCMETA/{n}"))[0] for n in mcmetalist])])
finallst=list([{os.path.splitext(os.path.basename(f"./MCMETA/{mcmetalist[lstdesc.index(k)]}"))[0]:k.replace(u"\u00A7","?")} for k in lstdesc])
global possible
possible={"red":["c","[255, 85, 85]"],"aqua":["b","[85, 255, 255]"],"blue":["9","[85, 85, 255]"],"gold":["6","[255, 170, 0]"],"gray":["7","[170, 170, 170]"],"black":["0","[0, 0, 0]"],"green":["a","[85, 255, 85]"],"white":["f","[255, 255, 255]"],"yellow":["e","[255, 255, 85]"],"dark_red":["4","[170, 0, 0]"],"dark_aqua":["3","[0, 170, 170]"],"dark_blue":["1","[0, 0, 170]"],"dark_gray":["8","[85, 85, 85]"],"dark_green":["2","[0, 170, 0]"],"dark_purple":["5","[170, 0, 170]"],"light_purple":["d","[255, 85, 255]"]}
print(u"Denote color codes with ? instead of \u00A7")
userin=str(input("Input: ")) if len(sys.argv)-1==0 else sys.argv[1]
print("\n")
def prrgb(rgb,s):return(GColor.RGB(rgb[0],rgb[1],rgb[2])+s+GColor.END)
def rcolored(txt):
	lstvals=list([cc for cc in possible.values()])
	lstkeys=list([cc for cc in possible.keys()])
	argb=list([list(map(str.strip, g.strip('][').replace('"', '').split(','))) for g in list(([x[1] for x in lstvals]))])
	lstcodes=list([lstvals[v][0] for v in range(len(lstkeys))])
	enumerated=list([str(txt[c]) for c in [i for i in range(len(txt))]])
	infolst={}
	finalstring=""
	for x in range(len(enumerated)-1):
		if enumerated[x]=="?" and enumerated[x+1] in lstcodes:infolst[f"{x+2}"]=argb[lstcodes.index(enumerated[x+1])]
	lstkeysinfo=list([g for g in infolst.keys()])
	lstvalsinfo=list([g for g in infolst.values()])
	for x in range(len(lstkeysinfo)):
		if x != len(lstkeysinfo)-1:finalstring+=prrgb(lstvalsinfo[x],str("".join(enumerated[int(lstkeysinfo[int(x)]):int(lstkeysinfo[int(x)+1])-2])))
		else:finalstring+=prrgb(lstvalsinfo[x],"".join(enumerated[int(lstkeysinfo[int(x)]):len(txt)]))
	if finalstring!=None:
		print(f"{finalstring}")
rcolored(userin)
lstodesc=list(["\n\t"+str(g).replace(u"\u00A7","?")+"\n" for g in lstdesc])
lstnames=list([f"?fUsing?f ?b{list([k for k in finallst[o].keys()])[0]}?b?f.?f?amcmeta?a?f:?f\n{lstodesc[o]}" for o in range(len(finallst))])
print("\n")
[f"{rcolored(lstnames[x])}" for x in range(len(lstnames)) if rcolored(lstnames[x])!=None]
