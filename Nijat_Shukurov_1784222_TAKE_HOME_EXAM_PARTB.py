##name:Nijat
#surname:Shukurov
#id:1784222
#FINAL TAKEHOME EXAM
#PART B#
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
##PART  1==============================================================================================================
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
##PART  2==============================================================================================================
fig=plt.figure()
exam=plt.subplot2grid((2,2),(0,0),rowspan=1,colspan=1,title="EXAM")##creating space for exam data hist
attendance=plt.subplot2grid((2,2),(1,0),title="ATTENDANCE")##creating space for attendance data hist
homework=plt.subplot2grid((2,2),(1,1),title="HOMEWORK")##creating space for homework data hist
laboratory=plt.subplot2grid((2,2),(0,1),title="LABORATORY")##creating space for laboratary data hist
def gaussian_fit(data,place_of_hist):
    (mu,sigma) = norm.fit(data)
    n,bins,patches=place_of_hist.hist(data,normed=1,facecolor='blue',align='mid')
    y = mlab.normpdf(bins,mu,sigma)
    place_of_hist.plot(bins,y,'r--',linewidth=2)

gaussian_fit(EXAM_GRADE,exam)
gaussian_fit(ATTENDANCE_GRADE,attendance)
gaussian_fit(HOMEWORK_GRADE,homework)
gaussian_fit(LABORATORY_GRADE,laboratory)
## save to pdf
pdf_file=PdfPages("Total_Grades_with_gaussianfit.pdf")##opens the pdf file and names it
pdf_file.savefig(fig)## saves the figure of hists in pdf
pdf_file.close()## closes the pdf file