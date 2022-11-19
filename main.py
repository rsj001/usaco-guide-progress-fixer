#!/usr/bin/python
import json
updatetime = dict();
filename = "usacoguide-userdata.json"
with open(filename, encoding='utf-8') as a:
    t = json.load(a)
    for key,values in t["userProgressOnProblems"].items():
        updatetime[key] = 19999999999999999999999999999999 # i.e. latest
    for activity in t["userProgressOnProblemsActivity"]:
        tid = activity["problemID"]
        tim = activity["timestamp"]
        sta = activity["problemProgress"]
        if((not(tid in updatetime)) or tim>updatetime[tid]):
            updatetime[tid]=tim
            t["userProgressOnProblems"][tid] = sta
            print("[OK] restore",tid,sta) 
    with open("usacoguide-userdata-fixed.json","w") as f:
        json.dump(t,f)
        print("fixed progress successfully dumped")
