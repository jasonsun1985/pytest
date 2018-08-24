#-*- coding:utf-8 -*-
from jira import JIRA 
import csv
import time
import os

class JiraData(object):
    bug_trend=[]
    jira = ''
    start_date = '2018-08-17'
    curr_date = time.strftime("%Y-%m-%d", time.localtime())
    file_name = 'D:/bug_trend.csv'

    def __init__(self):
        super(JiraData, self).__init__()
        self.jira = JIRA('http://172.17.189.3:8080/',basic_auth=('lei_sun@ruijie.com.cn', 'Sljira'))

    def write_CSVFile(self, bug_data,file_type):
        with open(self.file_name, file_type, newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',')
            spamwriter.writerow(bug_data)

    def get_bug_trend_data(self):
        if not os.path.exists(self.file_name):          
            self.write_CSVFile(['create_date','All','Resolved','Closed'],'a')

        self.bug_trend.append(self.curr_date)
        self.bug_trend.append(len(self.jira.search_issues("project = VJFOUR AND issuetype = Bug AND created >= %s " %self.start_date)))
        self.bug_trend.append(len(self.jira.search_issues("project = VJFOUR AND issuetype = Bug AND status in (Resolved, Closed) AND created >= %s " %self.start_date)))
        self.bug_trend.append(len(self.jira.search_issues("project = VJFOUR AND issuetype = Bug AND status = Closed AND created >= %s " %self.start_date)))

        self.write_CSVFile(self.bug_trend,'a')

if __name__ == '__main__':
    jd = JiraData()
    jd.get_bug_trend_data()