import pandas as pd
from statistics import mean


roll = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]                              # This is the possible rolls with the dice
modifier = [-2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]                                                   # This is the possible player modifiers
# modifier = [-3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
dc = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]    # This is the possible DC or difficulty challenges
result = []
result1 =[]

data = {"Roll": [],"Modifier": [],"DC": [],"Result": []}
data1 = {"Roll": [],"Modifier": [],"DC": [],"Result": []}


def d20test():
    successes = 0
    failures = 0
    successes1 = 0
    failures1 = 0
    for x in roll:                                          # For determining if the outcome is a success or failure
        for y in modifier:
            for z in dc:
                if x + y >= z:                              # For the current rules
                    result.append(True)
                    data["Roll"].append(x)
                    data["Modifier"].append(y)
                    data["DC"].append(z)
                    data["Result"].append("Success")
                else:
                    result.append(False)
                    data["Roll"].append(x)
                    data["Modifier"].append(y)
                    data["DC"].append(z)
                    data["Result"].append("Failure")


                if x == 1:                                  # For the new rules
                    result1.append(False)
                    data1["Roll"].append(x)
                    data1["Modifier"].append(y)
                    data1["DC"].append(z)
                    data1["Result"].append("Failure")
                else:
                    if x + y >= z or  x == 20:
                        result1.append(True)
                        data1["Roll"].append(x)
                        data1["Modifier"].append(y)
                        data1["DC"].append(z)
                        data1["Result"].append("Success")
                    else:
                        result1.append(False)
                        data1["Roll"].append(x)
                        data1["Modifier"].append(y)
                        data1["DC"].append(z)
                        data1["Result"].append("Failure")

    curtotal = len(result)
    newtotal = len(result1)

    if newtotal == curtotal:
        total = curtotal
    else:
        print(curtotal)
        print(newtotal)
        print("Error")
        return


    for a in result:
        if a == True:
            successes += 1
        else:
            failures += 1

    curpercent = 100 * successes/(total)

    print("In the current Rules")
    print('Total Successes: ' + str(successes))
    print('Total Failures: ' + str(failures))
    print('Probability of Success: ' + str(curpercent))
    for a in result1:
        if a == True:
            successes1 += 1
        else:
            failures1 += 1

    newpercent = 100 * successes1 / (total)

    print("In the New Rules")
    print('Total Successes: ' + str(successes1))
    print('Total Failures: ' + str(failures1))
    print('Probability of Success: ' + str(newpercent))

    print(str(newpercent-curpercent) + " % Increase that a player succeeds in the new system")





    current = pd.DataFrame(data)

    current20 = current[current.Roll.isin([20])]
    cur20suc = current20[current20.Result == "Success"]
    c20s = cur20suc["Result"]
    cur20fail = current20[current20.Result == "Failure"]
    c20f = cur20fail["Result"]

    current1 = current[current.Roll.isin([1])]
    cur1suc = current1[current1.Result == "Success"]
    c1s = cur1suc["Result"]
    cur1fail = current1[current1.Result == "Failure"]
    c1f = cur1fail["Result"]


    b = c20s.count()
    c = c20f.count()
    d = c1s.count()
    e = c1f.count()

    print("Current Rules:")
    print("Total Successes for a roll of 20 is " + str(b))
    print("Total Fails for a of 20 is " + str(c))
    print("Total Successes for a roll of 1 is " + str(d))
    print("Total Fails for a of 1 is " + str(e))

    newrules = pd.DataFrame(data1)

    new20 = newrules[newrules.Roll.isin([20])]
    new20suc = new20[new20.Result == "Success"]
    n20s = new20suc["Result"]
    new20fail = new20[new20.Result == "Failure"]
    n20f = new20fail["Result"]

    new1 = newrules[newrules.Roll.isin([1])]
    new1suc = new1[new1.Result == "Success"]
    n1s = new1suc["Result"]
    new1fail = new1[new1.Result == "Failure"]
    n1f = new1fail["Result"]

    f = n20s.count()
    g = n20f.count()
    h = n1s.count()
    i = n1f.count()

    print("New Rules:")
    print("Total Successes for a roll of 20 is " + str(f))
    print("Total Fails for a of 20 is " + str(g))
    print("Total Successes for a roll of 1 is " + str(h))
    print("Total Fails for a of 1 is " + str(i))



    curmsucc = []
    newmsucc = []
    curmfail = []
    newmfail = []
    modtotal = []

    print("Modifier")                                                   # This is the Modifier Chart

    # print("Current rules")
    for x in modifier:
        currentmod = current[current.Modifier.isin([x])]
        curms = currentmod[currentmod.Result == "Success"]
        cms = curms["Result"]
        cs = cms.count()
        curmf = currentmod[currentmod.Result == "Failure"]
        cmf = curmf["Result"]
        cf = cmf.count()
        curmsucc.append(cs)
        curmfail.append(cf)
        modtotal.append(float(cs)+float(cf))
       # print(str(x) + " modifier will succeed " + str(cs) + " times")
       # print(str(x) + " modifier will fail " + str(cf) + " times")

    # print("New rules")
    for x in modifier:
        newmod = newrules[newrules.Modifier.isin([x])]
        newms= newmod[newmod.Result == "Success"]
        nms = newms["Result"]
        ns = nms.count()
        newmf = newmod[newmod.Result == "Failure"]
        nmf = newmf["Result"]
        nf = nmf.count()
        newmsucc.append(ns)
        newmfail.append(nf)
       # print(str(x) + " modifier will succeed " + str(ns) + " times")
       # print(str(x) + " modifier will fail " + str(nf) + " times")

    smdiff = list()
    for item1, item2 in zip(curmsucc, newmsucc):
        item = item2 - item1
        smdiff.append(float(item))

    smprob = list()
    for item1, item2 in zip(smdiff, modtotal):
        item = 100 * item1 / item2
        smprob.append(item)

    smdict = {"Modifiers": modifier, "Current Rules": curmsucc, "New Rules": newmsucc, "Difference": smdiff, "Rate Increase %": smprob}
    smdict1 = pd.DataFrame(smdict)
    print("Success Rate")
    print(smdict1)
    print(mean(smdiff))
    print("Players are " + str(mean(smprob)) + " % more likely to succeed")

    fmdiff = list()
    for item1, item2 in zip(curmfail, newmfail):
        item = item2 - item1
        fmdiff.append(float(item))

    fmprob = list()
    for item1, item2 in zip(fmdiff, modtotal):
        item = 100 * item1 / item2
        fmprob.append(item)

    fmdict = {"Modifier": modifier, "Current Rules": curmfail, "New Rules": newmfail, "Difference": fmdiff, "Rate Increase %": fmprob}
    fmdict1 = pd.DataFrame(fmdict)
    print("Failure Rate")
    print(fmdict1)
    print(mean(fmdiff))
    print("Players are " + str(mean(smprob)) + " % less likely to fail")



    rcursucc = []
    rnewsucc = []
    rcurfail = []
    rnewfail = []
    rolltotal = []

    print("Roll")                                                             # This is the Roll Chart

    # print("Current rules")
    for x in roll:
        currentroll = current[current.Roll.isin([x])]
        currolls = currentroll[currentroll.Result == "Success"]
        crolls = currolls["Result"]
        crs = crolls.count()
        currollf = currentroll[currentroll.Result == "Failure"]
        crollf = currollf["Result"]
        crf = crollf.count()
        rcursucc.append(crs)
        rcurfail.append(crf)
        rolltotal.append(float(crs) + float(crf))
       # print(str(x) + " DC will be beat " + str(cds) + " times")
       # print(str(x) + " DC will not be beat " + str(cdf) + " times")

    # print("New rules")
    for x in roll:
        newroll = newrules[newrules.Roll.isin([x])]
        newrolls = newroll[newroll.Result == "Success"]
        nrolls = newrolls["Result"]
        nrs = nrolls.count()
        newrollf = newroll[newroll.Result == "Failure"]
        nrollf = newrollf["Result"]
        nrf = nrollf.count()
        rnewsucc.append(nrs)
        rnewfail.append(nrf)
       # print(str(x) + " DC will be beat " + str(nds) + " times")
       # print(str(x) + " DC will not be beat " + str(ndf) + " times")

    srdiff = list()
    for item1, item2 in zip(rcursucc, rnewsucc):
        item = item2 - item1
        srdiff.append(float(item))

    srprob = list()
    for item1, item2 in zip(srdiff, rolltotal):
        item = 100 * item1 / item2
        srprob.append(item)

    srdict = {"Roll": roll, "Current Rules": rcursucc, "New Rules": rnewsucc, "Difference": srdiff,"Rate Increase %":srprob}
    srdict1 = pd.DataFrame(srdict)
    print("Success Rate")
    print(srdict1)
    print(mean(srdiff))
    print("Players are " + str(mean(srprob)) + " % more likely to succeed")

    frdiff = list()
    for item1, item2 in zip(rcurfail, rnewfail):
        item = item2 - item1
        frdiff.append(float(item))

    frprob = list()
    for item1, item2 in zip(frdiff, rolltotal):
        item = 100 * item1/item2
        frprob.append(item)



    frdict = {"Roll": roll, "Current Rules": rcurfail, "New Rules": rnewfail, "Difference": frdiff, "Rate Increase %":frprob}
    frdict1 = pd.DataFrame(frdict)
    print("Failure Rate")
    print(frdict1)
    print(mean(frdiff))
    print("Players are " + str(mean(srprob)) + " % less likely to fail")

    cursucc = []
    newsucc = []
    curfail = []
    newfail = []
    dctotal = []

    print("DC")                                                                                   # This is the DC Chart

    # print("Current rules")
    for x in dc:
        currentdc = current[current.DC.isin([x])]
        curdcs = currentdc[currentdc.Result == "Success"]
        cdcs = curdcs["Result"]
        cds = cdcs.count()
        curdcf = currentdc[currentdc.Result == "Failure"]
        cdcf = curdcf["Result"]
        cdf = cdcf.count()
        cursucc.append(cds)
        curfail.append(cdf)
        dctotal.append(float(cds) + float(cdf))
    # print(str(x) + " DC will be beat " + str(cds) + " times")
    # print(str(x) + " DC will not be beat " + str(cdf) + " times")

    # print("New rules")
    for x in dc:
        newdc = newrules[newrules.DC.isin([x])]
        newdcs = newdc[newdc.Result == "Success"]
        ndcs = newdcs["Result"]
        nds = ndcs.count()
        newdcf = newdc[newdc.Result == "Failure"]
        ndcf = newdcf["Result"]
        ndf = ndcf.count()
        newsucc.append(nds)
        newfail.append(ndf)
    # print(str(x) + " DC will be beat " + str(nds) + " times")
    # print(str(x) + " DC will not be beat " + str(ndf) + " times")

    sdiff = list()
    for item1, item2 in zip(cursucc, newsucc):
        item = item2 - item1
        sdiff.append(float(item))

    sprob = list()
    for item1, item2 in zip(sdiff, dctotal):
        item = 100 * item1 / item2
        sprob.append(item)

    sdict = {"DC": dc, "Current Rules": cursucc, "New Rules": newsucc, "Difference": sdiff, "Rate Increase %": sprob}
    sdict1 = pd.DataFrame(sdict)
    print("Success Rate")
    print(sdict1)
    print(mean(sdiff))
    print("Players are " + str(mean(sprob)) + " % more likely to succeed")

    fdiff = list()
    for item1, item2 in zip(curfail, newfail):
        item = item2 - item1
        fdiff.append(float(item))

    fprob = list()
    for item1, item2 in zip(fdiff, dctotal):
        item = 100 * item1 / item2
        fprob.append(item)

    fdict = {"DC": dc, "Current Rules": curfail, "New Rules": newfail, "Difference": fdiff, "Rate Increase %": fprob}
    fdict1 = pd.DataFrame(fdict)
    print("Failure Rate")
    print(fdict1)
    print(mean(fdiff))
    print("Players are " + str(mean(sprob)) + " % less likely to fail")



d20test()
