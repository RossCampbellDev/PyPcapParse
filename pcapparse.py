import pyshark
import matplotlib.pyplot as plt
import numpy as np
import collections

pktfile = pyshark.FileCapture("cap1.cap", only_summaries=True)  # summaries of packet data, reduce info

protos = {}
sources = {}
dests = {}

for pkt in pktfile:
    line = str(pkt).split(" ")
    src = line[2]
    dst = line[3]
    proto = line[4]

    if src in sources:
        sources[src] = sources.get(src) + 1
    else:
        sources[src] = 1

    if dst in dests:
        dests[dst] = dests.get(dst) + 1
    else:
        dests[dst] = 1

    if proto in protos:
        protos[proto] = protos.get(proto) + 1
    else:
        protos[proto] = 1

# graph the data
plt.style.use('ggplot')
# ypos = np.arange(len(protos.keys()))
# plt.bar(ypos, list(protos.values()), align="center", alpha=0.5, color=['b', 'g', 'r', 'c', 'm'])
# plt.xticks(ypos, list(protos.keys()))
# plt.ylabel("frequency")
# plt.xlabel("protocol")
# plt.subplots_adjust(bottom=0.4)
# plt.show()

protos = collections.OrderedDict(sorted(protos.items()))
sources = collections.OrderedDict(sorted(sources.items()))
dests = collections.OrderedDict(sorted(dests.items()))

pexpl = []
sexpl = []
dexpl = []

for x in protos.values():
    pexpl.append(x * 0.01)

for x in sources.values():
    sexpl.append(x * 0.01)

for x in dests.values():
    dexpl.append(x * 0.01)

plt.tight_layout()
plt.pie(protos.values(), labels=protos.keys(), autopct='%1.1f%%', wedgeprops={'edgecolor': 'black'}, explode=pexpl)
plt.show()

plt.pie(sources.values(), labels=sources.keys(), autopct='%1.1f%%', wedgeprops={'edgecolor': 'black'}, explode=sexpl)
plt.show()

plt.pie(dests.values(), labels=dests.keys(), autopct='%1.1f%%', wedgeprops={'edgecolor': 'black'}, explode=dexpl)
plt.show()
