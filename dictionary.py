import traceback

#huffmanEncode: Takes in a single String inputString, which is
# the string to be encoded.  Computes the optimal binary encoding
# of the string and encodes it, returning a String of 0s and 1s.
# This is not an actual Python binary string, just a normal String
# that happens to contain only 0's and 1's.
def huffmanEncode(inputString):
    #Count frequency of each character in string
    # and record it in a dictionary
    chDiction = {}
    for ch in inputString:
        if ch in chDiction:
            chDiction[ch] += 1
        else:
            chDiction[ch] = 1

    #Create a Min Priority Queue, populate it with nodes based
    # on letter frequency
    chQueue = []
    for ch in chDiction:
        newNode = ChrNode(ch,chDiction[ch])
        min_heap_insert(chQueue,newNode)

    while len(chQueue) != 1:                # Build Huffman tree
        low = heap_extract_min(chQueue)
        low2 = heap_extract_min(chQueue)
        super_ch = low.ch + low2.ch
        super_freq = low.freq + low2.freq
        super_node = ChrNode(super_ch,super_freq)
        super_node.left = low
        super_node.right = low2
        min_heap_insert(chQueue,super_node)

    root = heap_extract_min(chQueue)

    encoded = ""

    for i in range(len(inputString)): # Iterate over input. Calls convert which converts the char into a binary numebr for each char
        encoded = encoded + convert(inputString[i],root)

    return encoded

def convert (ch,root):
    code = ""
    node = root
    while (ch != node.ch):
        if (ch in node.left.ch):
            node = node.left
            code = code + "0"
        elif (ch in node.right.ch):
            node = node.right
            code = code + "1"
    return code

#You are not required to use the helper code that follows: feel
# free to edit or delete the class/functions as you see fit.

#ChrNode class.  A node of information associating a
# self.ch - String: a character associated with the node
# self.freq - int: how many times the character occurs
class ChrNode:
    def __init__(self,ch,freq):
        self.ch = ch
        self.freq = freq
    def __repr__(self):
        return self.ch+":"+str(self.freq)



#Min Priority Queue functions: These are designed to implement a
# Min-PQ of ChrCount objects, ordered by the freq instance variable.
#Unlike the PA3 implementation, here len(Q) and Q.heap_size are
# one and the same: we lose a bit of performance by dynamically
# changing the list size every time we add or remove an element
# from the heap, but it makes implementation simpler.
#We also don't include the Heap_Min, Build_Min_Heap, or
# Heap_Decrease_Key functions, as they are unnecessary for this
# application: we will be building our priority queue by repeatedly
# inserting, and no key should change once it's inside.

def left(i):
    return 2*i+1

def right(i):
    return 2*i+2

def min_heapify(Q,i):
    l = 2*i+1
    r = 2*i+2
    smallest = i
    if l < len(Q) and Q[l].freq < Q[smallest].freq:
        smallest = l
    if r < len(Q) and Q[r].freq < Q[smallest].freq:
        smallest = r
    if i != smallest:
        Q[i],Q[smallest] = Q[smallest],Q[i]
        min_heapify(Q,smallest)


def heap_extract_min(Q):
    if len(Q) == 1:
        return Q.pop()
    minElement = Q[0]
    Q[0] = Q.pop()
    min_heapify(Q,0)
    return minElement

def parent(i):
    return int((i-1)/2)

def min_heap_insert(Q,node):
    Q.append(node)
    i = len(Q) - 1
    while i > 0 and Q[parent(i)].freq > Q[i].freq:
        Q[parent(i)],Q[i] = Q[i],Q[parent(i)]
        i = parent(i)



#  DO NOT EDIT BELOW THIS LINE

tests = ['message0.txt','message1.txt','message2.txt','message3.txt']
correct = ['message0encoded.txt','message1encoded.txt',
           'message2encoded.txt','message3encoded.txt']


#Run test cases, check whether encoding correct
count = 0

try:
    for i in range(len(tests)):
        ("\n---------------------------------------\n")
        print("TEST #",i+1)
        print("Reading message from:",tests[i])
        fp = open(tests[i])
        message = fp.read()
        fp.close()
        print("Reading encoded message from:",correct[i])
        fp2 = open(correct[i])
        encoded = fp2.read()
        fp2.close()

        output = huffmanEncode(message)
        if i < 2:
            print("Running: huffmanEncode on '"+message+"'\n")
            print("Expected:",encoded,"\nGot     :",output)
        assert encoded == output, "Encoding incorrect!"
        print("Test Passed!\n")
        count += 1
except AssertionError as e:
    print("\nFAIL: ",e)

except Exception:
    print("\nFAIL: ",traceback.format_exc())


print(count,"out of",len(tests),"tests passed.")
