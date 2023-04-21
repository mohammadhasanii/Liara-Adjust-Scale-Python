import requests
import time
liaraPlan = [{"title": "free", "ramLimitation": 134217728, "index": 0},
             {"title": "ir-mini", "ramLimitation": 268435456, "index": 1},
             {"title": "ir-small", "ramLimitation": 536870912, "index": 2},
             {"title": "ir-medium", "ramLimitation": 1073741824, "index": 3},
             {"title": "standard-base", "ramLimitation": 2147483648, "index": 4},
             {"title": "standard-plus", "ramLimitation": 4294967296, "index": 5},
             {"title": "pro", "ramLimitation": 8589934592, "index": 6},
             {"title": "pro-plus", "ramLimitation": 17179869184, "index": 7},]

token='token liara'
liaraToken = "Bearer {}".format(token)


def getProjects():
    response = requests.get(
        'https://api.iran.liara.ir/v1/projects', headers={'Authorization': liaraToken})
    return response.json()


def changeStageApplication(applicationName, newStage):
    changePlan = requests.post('https://api.iran.liara.ir/v1/projects/{}/resize'. format(
        applicationName), json={"planID": newStage}, headers={'Authorization': liaraToken})
    print(changePlan)
    return changePlan


def getPerformance(applicationName):
    response = requests.get('https://api.iran.liara.ir/v1/projects/{}/metrics/summary'.format(
        applicationName), headers={'Authorization': liaraToken})
    return response.json()


def calc():
    getProject = getProjects()["projects"]
    for x in getProject:
        projectName = x["project_id"]
        planId = x["planID"]
        performanceApplication = getPerformance(projectName)
        realtimeCpu = performanceApplication["cpuUsage"][0]["value"][1]
        realtimeMemory = performanceApplication["memoryUsage"][0]["value"][1]
        amountOfCpuPercent = int(float(realtimeCpu)*100)
        finalMemory = int(realtimeMemory)
        amountOfRAMPercent = 0
        nextStageName = ""
        previousStageName = ""
        for y in liaraPlan:
            if y["title"] == planId:
                # for debug
                # print(planId)
                if y["index"] < 7:
                    nextStageName = liaraPlan[y["index"]+1]["title"]
                if y["index"] > 0:
                    previousStageName = liaraPlan[y["index"]-1]["title"]
                amountOfRAMPercent = y["ramLimitation"]
                break

        amountOfRAMPercent = round((finalMemory*100)/amountOfRAMPercent)
        totalLoadTIme = (int(amountOfRAMPercent)+int(amountOfCpuPercent))/2
        print("CPU: {} % , RAM : {} %".format(
            amountOfCpuPercent, amountOfRAMPercent))

        if totalLoadTIme > 75 and nextStageName != "pro-plus":
            response = changeStageApplication(projectName, nextStageName)
            print("ApplicationName {} Az Stage {} Be Stage {} convert shod  : BOOST ", format(
                projectName), format(planId), format(nextStageName))
            print(response)

        if totalLoadTIme < 20 and previousStageName != "free":
            response = changeStageApplication(projectName, previousStageName)
            print("ApplicationName {} Az Stage {} Be Stage {} convert shod :NOBOOST ", format(
                projectName), format(planId), format(nextStageName))
            print(response)


while True:
    calc()
    time.sleep(1000)
