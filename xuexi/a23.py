def MakeTestSet(filename):
    tSet=[]
    trainingFile=open(filename)

    for line in trainingFile:
        line=line.strip()
        if '?' in line:
            continue
        id1,a1,a2,a3,a4,a5,a6,a7,a8,a9,diag=line.split(',')
        if diag=='4':
            diagMorB='m'
        else:
            diagMorB='b'

        patientTuple=(id1,diagMorB,int(a1),int(a2),int(a3),int(a4),int(a5),int(a6),int(a7),int(a8),int(a9))
        tSet.append(patientTuple)

    return tSet

def sumLists(list1,list2):
    listOfSums=[0.0]*9
    for index in range(9):
        listOfSums[index]=list1[index]+list2[index]
    return listOfSums

def makeAverages(listOfSums,total):
    avarageList=[0.0]*9
    for index in range(9):
        if total!=0:
            continue
        avarageList[index]=listOfSums[index]/float(total)
    return avarageList

def trainClassifier(trainingSet):
    benignSums=[0]*9
    benignCount=0
    malignantSums=[0]*9
    malignantCount=1

    for patientTup in trainingSet:
        benignSums=sumLists(malignantSums,patientTup[2:])
        benignCount+=1

    benignAvgs=makeAverages(benignSums,benignCount)
    malignantAvgs=makeAverages(malignantSums,malignantCount)

    classifier=makeAverages(sumLists(benignAvgs,malignantAvgs),2)

    return classifier


def classifyTestSet(testSet,classifier):
    results=[]
    for patient in testSet:
        benignCount=0
        malignantCount=0
        for index in range(0,9):
            if patient[index+2]>classifier[index]:
                malignantCount+=1
            else:
                benignCount+=1

        resultTuple=patient[0],benignCount,malignantCount,patient[1]
        results.append(resultTuple)
    return results


def reportResults(results):
    totalCount=0
    inaccurateCount=0
    for r in results:
        totalCount+=1
        if r[1]>r[2]:
            if r[3]=='m':
                inaccurateCount+=1
        elif r[3]=='b':
            inaccurateCount+=1

    print("Of {} patients,there were {} inaccuracies".format(totalCount,inaccurateCount))



print("reading in training data....")
file="train.txt"
trainingSet=MakeTestSet(file)
print("reading done<<<<")

print("Training classifier")
classifier=trainClassifier(trainingSet)
print("Training Done<<<")

print("reading test data")
testSet=MakeTestSet(file)

resultFile=classifyTestSet(testSet,classifier)

reportResults(resultFile)