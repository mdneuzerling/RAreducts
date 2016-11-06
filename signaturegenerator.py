import itertools

# The full signature under consideration. Includes composition, lattice
# operations, a partial order, negation, converse, constants, and domain
# and range operators.
fullsig = [ "comp", "join", "meet", "le", "con", "-", "id", "0", "top", "dom", "ran" ]

# Defines a canonical order on the operations of the signature for aesthetic
# reasons.
# (cdot, lor, land, le, -, con, id, 0, top, dom, ran)
sigKey = {"comp" : 0, "join" : 1, "meet" : 2, "le": 3, "con" : 4, "-" : 5, "id" : 6, "0" : 7, "top" : 8, "dom" : 9, "ran" : 10 }

# Return all nonempty subsets of a set S.
def findSubLists(S):
    allSubLists = []
    for i in range(0,len(S)+1):
        subList = list(itertools.combinations(S, i))
        subList = [list(j) for j in subList]
        allSubLists += subList
    return allSubLists

# Returns True if every element of the list A is in the list B.
def isSublist(A, B):
    isContained = True
    for a in A:
        if a not in B:
            isContained = False
            break
    return isContained

# A sorting key used to order the operations in a signature according to the
# canonical order defined above.
def sigSort(x,y):
    if sigKey[x] > sigKey[y]:
        return 1
    elif sigKey[x] == sigKey[y]:
        return 0
    else:
        return -1

# Create a copy of a signature, given as a list, and define new operations in
# the signature that can be derived from others. For example, a signature
# capable of expressing join and - is also capable of expressing meet.
def complete(S):
    T  = list(S)
    # Standard operations
    if ("join" in S) or ("meet" in S):
        T.append("le")
    if ("-" in S) and ("join" in S):
        T.append("meet")
    if ("-" in S) and ("meet" in S):
        T.append("join")
    if (("0" in S) and ("-" in S)) or (("join" in S) and ("-" in S)):
        T.append("top")
    if (("top" in S) and ("-" in S)) or (("join" in S) and ("-" in S)):
        T.append("0")
    # Domain and range
    if ("con" in S) and ("ran" in S):
        T.append("dom")
    if ("con" in S) and ("dom" in S):
        T.append("ran") 
    if (("top" in S) and ("dom" in S)) or (("top" in S) and ("ran" in S)):
        T.append("id")
    if ("meet" in S) and ("id" in S) and ("con" in S) and ("comp" in S):
        T.append("dom")
        T.append("ran")
    # Remove duplicate operations in the signature, and sort according to the
    # canonical order.
    T = list(set(T))
    T.sort(sigSort)
    # If no operations have been added, then the signature is already complete,
    # so return it. If not, try to complete again.
    if T == S:
        return T
    else:
        return complete(T)

# Generate a list of reducts of the full signature that contain at least the
# minimumSignature. For example, one might be interested in all
# reducts equipped with composition ("comp").
def generateSignatures(minimumSignature = []):
    signatures = []
    # Consider the operations in the full signature that are not in the minimum
    # signature. That is, consider the optional operations.
    optionalOperations = [operation for operation in fullsig if operation not in minimumSignature]
    # Consider the union of the minimum required signature with every possible
    # reduct of the signature of optional operations, and complete as above.
    # Sort by the canonical order, and then add to the output if not already
    # included.
    for partialSignature in findSubLists(optionalOperations):
        S = minimumSignature + partialSignature 
        S = complete(S)
        S.sort(sigSort)
        if S not in signatures:
            signatures.append(S)
    signatures.sort(key = len)
    return signatures