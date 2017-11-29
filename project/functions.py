import requests
import json
import datetime
i = datetime.datetime.now()
created_on = "%s" % i
created_on = created_on[0:19]

req_campus = requests.get('https://fenix.tecnico.ulisboa.pt/api/fenix/v1/spaces')
req_campus_json = json.loads(req_campus.text)
for campus in req_campus_json:
    print("----------------------------------------\n")
    req_buildings = requests.get('https://fenix.tecnico.ulisboa.pt/api/fenix/v1/spaces/'+campus['id'])
    req_campus_json = json.loads(req_campus.text)
    print (campus['name'])

# with open('campus.json', 'w') as fp:
#     json.dump(req_json, fp, ensure_ascii=False)

# pk_eval = 1
# eval_list = []
# pk = 1
# for entry in req_json:
#     couse_id = entry["id"]
#     ep_courses = "https://fenix.tecnico.ulisboa.pt/api/fenix/v1/degrees/" + couse_id + "/courses"
#     req_courses = requests.get(ep_courses)
#     courses = json.loads(req_courses.text)
#     for course in courses:
#         ep_eval = "https://fenix.tecnico.ulisboa.pt/api/fenix/v1/courses/" + course["id"] + "/evaluations"
#         req_eval = requests.get(ep_eval)
#         evaluations = json.loads(req_eval.text)
#         couse_name = course["name"]
#         for evaluation in evaluations:
#             if evaluation["type"] == "TEST" or evaluation["type"] == "EXAM":
#                 name = str(evaluation["name"])
#                 description = evaluation["type"]
#                 eval_per = evaluation["evaluationPeriod"]
#                 start_format = eval_per["start"]
#                 day,time = start_format.split(" ")
#                 DD,MM,YY = day.split("/")
#                 start = YY + "-" + MM + "-" + DD + " " + time + ":00"
#                 end_format = eval_per["end"]
#                 day,time = end_format.split(" ")
#                 DD,MM,YY = day.split("/")
#                 end = YY + "-" + MM + "-" + DD + " " + time + ":00"
#                 rooms = evaluation["rooms"]
#                 room_id = ""
#                 for room in rooms:
#                     if room_id == "":
#                         room_id = str(room["name"])
#                     else:
#                         room_id = room_id + ";" + str(room["name"])
#                 place = room_id
#                 owner = pk
#                 db_eval = {"pk":pk_eval,"model":"schedule.event","fields":{"title":name, "description":description, "creator":1, "start":start, "end":end, "calendar_id":pk, "created_on":created_on,"updated_on":created_on}}
#                 pk_eval = pk_eval + 1
#                 eval_list.append(db_eval)
#     pk = pk + 1
# with open('eval.json', 'w') as fp:
#     json.dump(eval_list, fp, ensure_ascii=False)



    # couse_id = entry["id"]
    # ep_courses = "https://fenix.tecnico.ulisboa.pt/api/fenix/v1/degrees/" + couse_id + "/courses"
    # req_courses = requests.get(ep_courses)
    # courses = json.loads(req_courses.text)
    # eval_list = dict()
    # days = []
    # for course in courses:
    #     ep_eval = "https://fenix.tecnico.ulisboa.pt/api/fenix/v1/courses/" + course["id"] + "/evaluations"
    #     req_eval = requests.get(ep_eval)
    #     evaluations = json.loads(req_eval.text)
    #     for evaluation in evaluations:
    #         if evaluation["type"] == "TEST" or evaluation["type"] == "EXAM":
    #             per = evaluation["evaluationPeriod"]
    #             day = per["start"][0:10]
    #             if day not in days:
    #                 days.append(day)
    #                 l = []
    #                 l.append(per)
    #                 eval_list[day] = l
    #             else:
    #                 l.append(per)
    #                 eval_list[day]= l
    #
    # return eval_list
