##name:Nijat
#surname:Shukurov
#id:1784222
#FINAL TAKEHOME EXAM
#PART C#
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
from scipy.optimize import curve_fit
import pickle
DATA=np.loadtxt("data.txt","d")## reads the data from data.txt file as matrix array

EXAM_GRADE=DATA[:,0]##sets exam grade to array reading it from DATA Matrix array
LABORATORY_GRADE=DATA[:,1]##sets exam grade to array reading it from DATA Matrix array
HOMEWORK_GRADE=DATA[:,2]##sets exam grade to array reading it from DATA Matrix array
ATTENDANCE_GRADE=DATA[:,3]##sets exam grade to array reading it from DATA Matrix array
##PART a, b, c==============================================================================================================
##scattering plots
fig=plt.figure("Scattering")
exam_vs_homework=plt.subplot2grid((3,1),(0,0),title="EXAM GRADE vs HOMEWORK ")##creating space for exam data hist
exam_vs_attendance=plt.subplot2grid((3,1),(1,0),title="EXAM GRADE VS ATTENDANCE")##creating space for attendance data hist
exam_vs_laboratory=plt.subplot2grid((3,1),(2,0),title="EXAM GRADE VS LABORATORY")##creating space for homework data hist

def scatter_plot(data1,data2,place_of_grap):
    place_of_grap.scatter(data1,data2)

scatter_plot(EXAM_GRADE,HOMEWORK_GRADE,exam_vs_homework)
scatter_plot(EXAM_GRADE,ATTENDANCE_GRADE,exam_vs_attendance)
scatter_plot(EXAM_GRADE,LABORATORY_GRADE,exam_vs_laboratory)
pdf_file=PdfPages("EXAM_VS_GRAPHS.pdf")##opens the pdf file and names it
pdf_file.savefig(fig)## saves the figure of hists in pdf
pdf_file.close()## closes the pdf file

##PART2================================================================================================================
## in this part we gonno do Using the Least Squares Method make a linear fit (y= ? + ?x) to each scattering plot and
#   find ? and ? values and save it in pdf format.
fig1=plt.figure("with best line ")
homework=plt.subplot2grid((3,1),(0,0),title="EXAM GRADE vs HOMEWORK1 ")##creating space for exam data hist
attendance=plt.subplot2grid((3,1),(1,0),title="EXAM GRADE VS ATTENDANCE")##creating space for attendance data hist
laboratory=plt.subplot2grid((3,1),(2,0),title="EXAM GRADE VS LABORATORY")##creating space for homework data hist
def Least_Square_Method(y,place_of_plot):##calculatin alfa and betta
    alfa=0;
    betta=0;
    x=EXAM_GRADE
    x_=0
    y_=0
    xi=0
    yi=0
    xi_2=0
    yi_2=0
    xi_yi=0;
    Sxx=0
    Syy=0
    Sxy=0
    for i in range(0,len(x)):
        xi+=x[i]
        xi_2+=(x[i]*x[i])
    for i in range(0,len(y)):
        yi+=y[i]
        yi_2+=(y[i]*y[i])
        xi_yi+=(x[i]*y[i])
    x_=xi/len(x)
    y_=yi/len(y)
    Sxx=xi_2-(xi*xi)/len(x)
    Syy=yi_2-(yi*yi)/len(y)
    Sxy=xi_yi-(xi*yi)/len(x)
    betta=Sxy/Sxx
    alfa=y_-betta*x_
    ##plottong line and scatter together
    place_of_plot.scatter(EXAM_GRADE,y)##plotting scattering graph again
    place_of_plot.plot(EXAM_GRADE,betta*EXAM_GRADE+alfa,"-")##plotting best line to the scattering graph
    return alfa , betta ,Sxy,Sxx,Syy
## end of function
alfa_1, betta_1,Sxy_1,Sxx_1,Syy_1=Least_Square_Method(HOMEWORK_GRADE,homework)
alfa_2,betta_2,Sxy_2,Sxx_2,Syy_2=Least_Square_Method(ATTENDANCE_GRADE,attendance)
alfa_3,betta_3,Sxy_3,Sxx_3,Syy_3=Least_Square_Method(LABORATORY_GRADE,laboratory)
print("Exam grade vs homework grade alfa and betta ", alfa_1,betta_1)
print("Exam grade vs attendance grade alfa and betta ", alfa_2,betta_2)
print("Exam grade vs laboratory grade alfa and betta ", alfa_3,betta_3)
print("===============================================================")
pdf_fil=PdfPages("EXAM_VS_GRAPHS_with_bestLine.pdf")##opens the pdf file and names it
pdf_fil.savefig(fig1)## saves the figure of hists in pdf
pdf_fil.close()## closes the pdf file

##======================================================================================================================
## THE ANOVA TEST , r2 part e and f

def ANOVA_TEST(Sxx,Sxy,Syy,txtname):##COMPUTES ANOVA TABLE AND GENERATES IT TO TXT FILE also finds the R2
    name=txtname+'_ANOVAtable.txt'
    total_df=len(EXAM_GRADE)-1
    regression_df=1
    error_df=len(EXAM_GRADE)-2
    SSR=(Sxy*Sxy)/Sxx
    total_SS=Syy
    SSE=total_SS-SSR
    #Mean squares
    MSR=SSR/1
    MSE=SSE/(len(EXAM_GRADE)-2)
    F=MSR/MSE
    R2=SSR/total_SS
    R2_=1-SSE/total_SS
    information="SSR/total_SS= ",R2," (1-SSE/total_SS)= ",R2_
    test_data1=[["SOURCE","    DF","  SS","           MS","          F"],["Regression  ",str(regression_df),str(SSR),str(MSR),str(F)],["Error     ",str(error_df),str(SSE),str(MSE)],["Total     ",str(total_df),str(total_SS)]]
    ##test_data_object=np.array(test_data,dtype=str)
    ##writing to text file an array data
    text_file=open(name,"w")
    for i in range(0,len(test_data1)):
        for a in range(0,len(test_data1[i])):
            text_file.write(test_data1[i][a]+" ")
        text_file.write("\n")
    text_file.close()
    return information

print("for exam grade and homework grade: ",ANOVA_TEST(Sxx_1,Sxy_1,Syy_1,"grade_vs_homework"))
print("for exam grade and attendance: ",ANOVA_TEST(Sxx_2,Sxy_2,Syy_2,"grade_vs_attendance"))
print("for exam grade and laboratory grade: ",ANOVA_TEST(Sxx_3,Sxy_3,Syy_3,"grade_vs_laboratory"))
print("===============================================================")
##==================================================================================================================
##part g Chi square for each line
def chi_square(data):
    p=np.polyfit(EXAM_GRADE,data,1)
    chi_squared = np.sum((np.polyval(p, EXAM_GRADE) - data) ** 2)
    return chi_squared
print("CHI_SQUARE FOR ALL LINES")
print("X2 for Exam grade vs Homework grade:",chi_square(HOMEWORK_GRADE))
print("X2 for exam grade and attendance grade:",chi_square(ATTENDANCE_GRADE))
print("X2 for exam grade and laboratory grade: ",chi_square(LABORATORY_GRADE))
print("===============================================================")
plt.show()