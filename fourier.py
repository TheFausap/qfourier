qub_num = 32
a = 1
powQ = range(2, qub_num)
qub = range(1, qub_num+1)
qubM = divmod(len(qub), 2)[0]  # get remainder
f = open("four"+str(qub_num)+".real", 'w+')


def pow2(x): return 2 ** x
powQ = list(map(pow2, powQ))

qubList = ""
qubNone = ""
for q in qub:
    qubList = qubList+"j"+str(q)+" "
    qubNone = qubNone+"-"

print("Creating REAL file for QFT of "+str(qub_num)+" qubits...")
f.write(".version 1.0 quantum Fourier transform for n = "+str(qub_num)+"\n")
f.write(".numvars "+str(qub_num)+"\n")
f.write(".variables "+qubList+"\n")
f.write(".inputs "+qubList+"\n")
f.write(".outputs "+qubList+"\n")
f.write(".constants "+qubNone+"\n")
f.write(".garbage "+qubNone+"\n")
f.write(".begin\n")
f.write("\n")

while a <= qub_num:
    f.write("H1 j"+str(a)+"\n")
    if a < qub_num:
        f.write("S2 j"+str(a+1)+" j"+str(a)+"\n")
        i = 0
        if a < qub_num-1:
            for p in powQ:
                f.write("Q2:"+str(p)+" j"+str(a+2+i)+" j"+str(a)+"\n")
                i = i+1
            powQ.pop()
            f.write(" \n")
    a = a+1

f.write(" \n")
b = 0
while b < qubM:
    f.write("T2 j" + str(qub[b]) + " j" + str(qub[qub_num - 1 - b])+"\n")
    f.write("T2 j" + str(qub[qub_num - 1 - b]) + " j" + str(qub[b])+"\n")
    f.write("T2 j" + str(qub[b]) + " j" + str(qub[qub_num - 1 - b])+"\n")
    f.write(" \n")
    b = b+1

f.write(".end\n")
f.write("\n")
f.close()
print("Generation completed.")
