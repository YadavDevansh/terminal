import subprocess 
import time 
import os  
import signal
os.system("cls")
cmd=0  
def square(x): 
    return x * x 

tickers=[]
if __name__ == '__main__': 

    while cmd!="exit":
        for i in tickers:
            print(i)
        print("--------------------")
        cmd=input("command : ")

        if(list(cmd)[0]!='-'):

            os.startfile("terminal.py")


            tickers.append(cmd)
            tickers=set(tickers)
            tickers=list(tickers)
            os.system("cls")
            
        elif(list(cmd)[0]=='-'):
            try:
                f = open("C:/Users/Devansh/Desktop/ai_projects/proj_2/trial.py%s.txt"%cmd, "r")
                proc_id=f.read()
                f.close()

                os.kill(proc_id, signal.SIGKILL)
                tickers.remove(''.join([str(elem) for elem in list(tickers)[1:]]))
            except:
                print("bad command")
        os.system("cls")



        
        
        
        
'''
        pool = multiprocessing.Pool() 
        pool = multiprocessing.Pool(processes=4) 
        inputs = [0,1,2,3,4] 
        outputs = pool.map(square, inputs) 
        print("Input: {}".format(inputs)) 
        print("Output: {}".format(outputs)) 
'''