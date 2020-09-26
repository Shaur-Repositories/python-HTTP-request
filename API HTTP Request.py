import time
import datetime
import requests
import xlsxwriter
import fpdf

now = datetime.datetime.now()
dt_string = now.strftime("%d.%m.%Y.%H.%M.%S")

workbook = xlsxwriter.Workbook('aPI_stats_' + dt_string + '.xlsx')
worksheet = workbook.add_worksheet('GET APIs')
worksheet1 = workbook.add_worksheet('POST APIs')

allresG = []

def geturls():
    # allresG.append([" ", " ", " ", " "])
    # allresG.append(["GET", " ", " ", " "])
    allresG.append(["NAME", "DATE/TIME", "EXECUTION TIME", "STATUS CODE"])
    # allresG.append([" ", " ", " ", " "])
    for i in getlist:
        try:
            r = requests.get(i[0], timeout=60)
            r.raise_for_status()
            respTime = str(round(r.elapsed.total_seconds(), 3))
            currDate = datetime.datetime.now()
            currDate = str(currDate.strftime("%d-%m-%Y %H:%M:%S"))
            allresG.append([i[1], currDate, float(respTime), str((r))])
            print(i[1] + "  " + currDate + "  " + respTime + "  " + str((r)))
        except requests.exceptions.HTTPError as err01:
            print(i[1] + "  " + "HTTP error: ", err01)
            allresG.append([i[1], "  ", "HTTP error: ", str(err01)])
        except requests.exceptions.ConnectionError as err02:
            print(i[1] + "  " + "Error connecting: ", err02)
            allresG.append([i[1], "  ", "Error connecting: ", str(err02)])
        except requests.exceptions.Timeout as err03:
            print(i[1] + "  " + "Timeout error:", err03)
            allresG.append([i[1], "  ", "Timeout error:", str(err03)])
        except requests.exceptions.RequestException as err04:
            print(i[1] + "  " + "Error: ", err04)
            allresG.append([i[1], "  ", "Error: ", str(err04)])


    # allresP.append([" ", " ", " ", " "])
