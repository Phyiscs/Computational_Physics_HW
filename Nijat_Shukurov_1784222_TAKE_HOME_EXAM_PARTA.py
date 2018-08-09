##name:Nijat
#surname:Shukurov
#id:1784222
#FINAL TAKEHOME EXAM
#PART A#
import numpy as np
import pylab as pl
import math
import random
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib import style
import scipy.stats as st
import matplotlib.mlab as mlab
from scipy.stats import norm

DATA=np.loadtxt("data.txt","d")## reads the data from data.txt file as matrix array

EXAM_GRADE=DATA[:,0]##sets exam grade to array reading it from DATA Matrix array
LABORATORY_GRADE=DATA[:,1]##sets exam grade to array reading it from DATA Matrix array
HOMEWORK_GRADE=DATA[:,2]##sets exam grade to array reading it from DATA Matrix array
ATTENDANCE_GRADE=DATA[:,3]##sets exam grade to array reading it from DATA Matrix array
##HISTOGRAM PLOTTING============================================================================
fig=plt.figure()##Creates one figure
exam=plt.subplot2grid((2,2),(0,0),rowspan=1,colspan=1,title="EXAM")##creating space for exam data hist
attendance=plt.subplot2grid((2,2),(1,0),title="ATTENDANCE")##creating space for attendance data hist
homework=plt.subplot2grid((2,2),(1,1),title="HOMEWORK")##creating space for homework data hist
laboratory=plt.subplot2grid((2,2),(0,1),title="LABORATORY")##creating space for laboratary data hist
##creating histograms for each data
exam.hist(EXAM_GRADE)
attendance.hist(ATTENDANCE_GRADE)
homework.hist(HOMEWORK_GRADE)
laboratory.hist(LABORATORY_GRADE)
##Attention here!!
#plt.show() shows the figure
#the code above shows the figure of histograms
#but if it runs to complete the program you should close the figure
# for this I didnt write this code it directly will send it to pdf..
##PDF FILE CREATING==========================================================
pdf_file=PdfPages("Total_Grades_histogram.pdf")##opens the pdf file and names it
pdf_file.savefig(fig)## saves the figure of hists in pdf
pdf_file.close()## closes the pdf file
##STANDART DEVIATION AND MEAN====================================================================
print("STANDART DEVIEATIONS")
print("exam grade: ",np.std(EXAM_GRADE))
print("attendance: ",np.std(ATTENDANCE_GRADE))
print("homework grade: ",np.std(HOMEWORK_GRADE))
print("lab grade: ",np.std(LABORATORY_GRADE))
print("****************************")
print("MEAN")
print("exam grade: ",np.mean(EXAM_GRADE))
print("attendance: ",np.mean(ATTENDANCE_GRADE))
print("homework grade: ",np.mean(HOMEWORK_GRADE))
print("lab grade: ",np.mean(LABORATORY_GRADE))
print("****************************")
##END OF PART 1
##PART B 1==============================================================================================================
exam_conf_interval=st.t.interval(0.90,len(EXAM_GRADE)-1,loc=np.mean(EXAM_GRADE),scale=st.sem(EXAM_GRADE))
attendance_conf_interval=st.t.interval(0.90,len(ATTENDANCE_GRADE)-1,loc=np.mean(ATTENDANCE_GRADE),scale=st.sem(ATTENDANCE_GRADE))
homework_conf_interval=st.t.interval(0.90,len(HOMEWORK_GRADE)-1,loc=np.mean(HOMEWORK_GRADE),scale=st.sem(HOMEWORK_GRADE))
lab_conf_interval=st.t.interval(0.90,len(LABORATORY_GRADE)-1,loc=np.mean(LABORATORY_GRADE),scale=st.sem(LABORATORY_GRADE))
print("90 % CONFIDENCE INTERVALS")
print("EXAM GRADE DATA: ",exam_conf_interval)
print("ATTENDANCE DATA: ",attendance_conf_interval)
print("HOMEWORK GRADE DATA: ",homework_conf_interval)
print("LABARATORY GRADE DATA: ",lab_conf_interval)
print("****************************")
plt.show()