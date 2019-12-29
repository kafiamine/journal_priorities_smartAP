import sys
import math
from collections import defaultdict
import numpy as np 



LOG_PATH_random="summary_results_v2.txt"



POUR_PLOT_deficit="plot_deficit"
POUR_PLOT_throughput="plot_throughput"
POUR_PLOT_APs_std_load="plot_APs_std_load"
POUR_PLOT_APs_maximum_load="plot_APs_maximum_load"
POUR_PLOT_clients_Nb_deficit="plot_clients_Nb_deficit"

POUR_PLOT_deficit_classes="plot_deficit_classes"
POUR_PLOT_throughput_classes="plot_throughput_classes"
POUR_PLOT_clients_Nb_deficit_class="plot_clients_Nb_deficit_classes"


f_Q_priority=open(LOG_PATH_random,"r")


g_deficit=open(POUR_PLOT_deficit,"w")
g_throughput=open(POUR_PLOT_throughput,"w")
g_APs_std_load=open(POUR_PLOT_APs_std_load,"w")
g_APs_maximum_load=open(POUR_PLOT_APs_maximum_load,"w")
g_clients_Nb_deficit=open(POUR_PLOT_clients_Nb_deficit,"w")

g_PLOT_deficit_classes=open(POUR_PLOT_deficit_classes,"w")
g_throughput_classes=open(POUR_PLOT_throughput_classes,"w")
g_clients_Nb_deficit_class=open(POUR_PLOT_clients_Nb_deficit_class,"w")



nb_repetition=10
priority_class=4

for density_nodes in range(1,21):  #case random, jusqu'a density=40 noeuds
#for density_nodes in range(1,7):  #case random, jusqu'a density=30 noeuds
#for density_nodes in range(1,2):
	moy_deficit_priority=0  
	moy_throughput_priority=0
	moy_std_load_priority=0
	moy_maximum_load_priority=0
	moy_clients_deficit_priority=0

	erreur_deficit_priority=0
	erreur_throughput_priority=0
	erreur_std_load_priority=0
	erreur_maximum_load_priority=0
	erreur_clients_deficit_priority=0


	moy_deficit_RSSI=0
	moy_throughput_RSSI=0
	moy_std_load_RSSI=0
	moy_maximum_load_RSSI=0
	moy_clients_deficit_RSSI=0

	erreur_deficit_RSSI=0
	erreur_throughput_RSSI=0
	erreur_std_load_RSSI=0
	erreur_maximum_load_RSSI=0
	erreur_clients_deficit_RSSI=0	
		

	moy_deficit_FF=0
	moy_throughput_FF=0
	moy_std_load_FF=0
	moy_maximum_load_FF=0
	moy_clients_deficit_FF=0

	erreur_deficit_FF=0
	erreur_throughput_FF=0
	erreur_std_load_FF=0
	erreur_maximum_load_FF=0
	erreur_clients_deficit_FF=0


	moy_deficit_LL=0
	moy_throughput_LL=0
	moy_std_load_LL=0
	moy_maximum_load_LL=0
	moy_clients_deficit_LL=0

	erreur_deficit_LL=0
	erreur_throughput_LL=0
	erreur_std_load_LL=0
	erreur_maximum_load_LL=0
	erreur_clients_deficit_LL=0



	moy_deficit_classes=defaultdict()  #c[i][j]=48
	moy_throughput_classes=defaultdict()
	moy_clients_deficit_classes=defaultdict()

	erreur_deficit_classes=defaultdict()  #c[i][j]=48
	erreur_throughput_classes=defaultdict()
	erreur_clients_deficit_classes=defaultdict()

	
	moy_deficit_RSSI_classes=defaultdict()  #c[i][j]=48
	moy_throughput_RSSI_classes=defaultdict()
	moy_clients_deficit_RSSI_classes=defaultdict()

	erreur_deficit_RSSI_classes=defaultdict()  #c[i][j]=48
	erreur_throughput_RSSI_classes=defaultdict()
	erreur_clients_deficit_RSSI_classes=defaultdict()


	moy_deficit_FF_classes=defaultdict()  #c[i][j]=48
	moy_throughput_FF_classes=defaultdict()
	moy_clients_deficit_FF_classes=defaultdict()

	erreur_deficit_FF_classes=defaultdict()  #c[i][j]=48
	erreur_throughput_FF_classes=defaultdict()
	erreur_clients_deficit_FF_classes=defaultdict()


	moy_deficit_LL_classes=defaultdict()  #c[i][j]=48
	moy_throughput_LL_classes=defaultdict()
	moy_clients_deficit_LL_classes=defaultdict()

	erreur_deficit_LL_classes=defaultdict()  #c[i][j]=48
	erreur_throughput_LL_classes=defaultdict()
	erreur_clients_deficit_LL_classes=defaultdict()


	for cla in range(0,priority_class):
		moy_deficit_classes[cla]=0
		moy_throughput_classes[cla]=0
		moy_clients_deficit_classes[cla]=0

		erreur_deficit_classes[cla]=0
		erreur_throughput_classes[cla]=0
		erreur_clients_deficit_classes[cla]=0

	
		moy_deficit_RSSI_classes[cla]=0
		moy_throughput_RSSI_classes[cla]=0
		moy_clients_deficit_RSSI_classes[cla]=0

		erreur_deficit_RSSI_classes[cla]=0
		erreur_throughput_RSSI_classes[cla]=0
		erreur_clients_deficit_RSSI_classes[cla]=0


		moy_deficit_FF_classes[cla]=0
		moy_throughput_FF_classes[cla]=0
		moy_clients_deficit_FF_classes[cla]=0

		erreur_deficit_FF_classes[cla]=0
		erreur_throughput_FF_classes[cla]=0
		erreur_clients_deficit_FF_classes[cla]=0


		moy_deficit_LL_classes[cla]=0
		moy_throughput_LL_classes[cla]=0
		moy_clients_deficit_LL_classes[cla]=0

		erreur_deficit_LL_classes[cla]=0
		erreur_throughput_LL_classes[cla]=0
		erreur_clients_deficit_LL_classes[cla]=0


	
	val_deficit_priority={}       
	val_throughput_priority={} 
	val_std_load_priority={} 
	val_maximum_load_priority={} 
	val_clients_deficit_priority={} 

	val_deficit_RSSI={} 
	val_throughput_RSSI={} 
	val_std_load_RSSI={} 
	val_maximum_load_RSSI={} 
	val_clients_deficit_RSSI={} 

	val_deficit_FF={} 
	val_throughput_FF={} 
	val_std_load_FF={} 
	val_maximum_load_FF={} 
	val_clients_deficit_FF={} 

	val_deficit_LL={} 
	val_throughput_LL={} 
	val_std_load_LL={} 
	val_maximum_load_LL={} 
	val_clients_deficit_LL={} 

	
	val_deficit_classes={}
	val_throughput_classes={}
	val_clients_deficit_classes={}
		
	val_deficit_classes_RSSI={}
	val_throughput_classes_RSSI={}
	val_clients_deficit_classes_RSSI={}

	val_deficit_classes_FF={}
	val_throughput_classes_FF={}
	val_clients_deficit_classes_FF={}

	val_deficit_classes_LL={}
	val_throughput_classes_LL={}
	val_clients_deficit_classes_LL={}


   	for cla in range(0,priority_class):	
		val_deficit_classes[cla]={}
		val_throughput_classes[cla]={}
		val_clients_deficit_classes[cla]={}
		
		val_deficit_classes_RSSI[cla]={}
		val_throughput_classes_RSSI[cla]={}
		val_clients_deficit_classes_RSSI[cla]={}

		val_deficit_classes_FF[cla]={}
		val_throughput_classes_FF[cla]={}
		val_clients_deficit_classes_FF[cla]={}

		val_deficit_classes_LL[cla]={}
		val_throughput_classes_LL[cla]={}
		val_clients_deficit_classes_LL[cla]={}	




	for repetition in range(0,nb_repetition):
		line_den_case_repet=f_Q_priority.readline()
		line_deficit=f_Q_priority.readline()
		line_throughput=f_Q_priority.readline()
		line_std_load=f_Q_priority.readline()
		line_maximum_load=f_Q_priority.readline()
		line_clients_deficit=f_Q_priority.readline()
		line_vide=f_Q_priority.readline()
		
		line_deficit_classes={}
		for cla in range(0,priority_class):
			line_deficit_classes[cla]=f_Q_priority.readline()
		line_vide=f_Q_priority.readline()

		line_throughput_classes={}
		for cla in range(0,priority_class):
			line_throughput_classes[cla]=f_Q_priority.readline()
		line_vide=f_Q_priority.readline()
		
		line_nb_deficit_classes={}
		for cla in range(0,priority_class):
			line_nb_deficit_classes[cla]=f_Q_priority.readline()
		line_vide=f_Q_priority.readline()		
		
		
		analyse_deficit=line_deficit.strip().split()
		analyse_throughput=line_throughput.strip().split()
		analyse_std_load=line_std_load.strip().split()
		analyse_maximum_load=line_maximum_load.strip().split()
		analyse_clients_deficit=line_clients_deficit.strip().split()
		

		analyse_deficit_classes={}
		analyse_throughput_classes={}
		analyse_clients_deficit_classes={}
		
		for cla in range(0,priority_class):		
			analyse_deficit_classes[cla]=line_deficit_classes[cla].strip().split()
			analyse_throughput_classes[cla]=line_throughput_classes[cla].strip().split()
			analyse_clients_deficit_classes[cla]=line_nb_deficit_classes[cla].strip().split()


		val_deficit_priority[repetition]=float(analyse_deficit[2])
		val_throughput_priority[repetition]=float(analyse_throughput[2])
		val_std_load_priority[repetition]=float(analyse_std_load[4])
		val_maximum_load_priority[repetition]=float(analyse_maximum_load[4])
		val_clients_deficit_priority[repetition]=float(analyse_clients_deficit[5])

		val_deficit_RSSI[repetition]=float(analyse_deficit[3])
		val_throughput_RSSI[repetition]=float(analyse_throughput[3])
		val_std_load_RSSI[repetition]=float(analyse_std_load[5])
		val_maximum_load_RSSI[repetition]=float(analyse_maximum_load[5])
		val_clients_deficit_RSSI[repetition]=float(analyse_clients_deficit[6])

		val_deficit_FF[repetition]=float(analyse_deficit[4])
		val_throughput_FF[repetition]=float(analyse_throughput[4])
		val_std_load_FF[repetition]=float(analyse_std_load[6])
		val_maximum_load_FF[repetition]=float(analyse_maximum_load[6])
		val_clients_deficit_FF[repetition]=float(analyse_clients_deficit[7])

		val_deficit_LL[repetition]=float(analyse_deficit[5])
		val_throughput_LL[repetition]=float(analyse_throughput[5])
		val_std_load_LL[repetition]=float(analyse_std_load[7])
		val_maximum_load_LL[repetition]=float(analyse_maximum_load[7])
		val_clients_deficit_LL[repetition]=float(analyse_clients_deficit[8])			
		
		for cla in range(0,priority_class):		
			val_deficit_classes[cla][repetition]=float(analyse_deficit_classes[cla][4])
			val_throughput_classes[cla][repetition]=float(analyse_throughput_classes[cla][4])
			val_clients_deficit_classes[cla][repetition]=float(analyse_clients_deficit_classes[cla][6])

			val_deficit_classes_RSSI[cla][repetition]=float(analyse_deficit_classes[cla][5])
			val_throughput_classes_RSSI[cla][repetition]=float(analyse_throughput_classes[cla][5])
			val_clients_deficit_classes_RSSI[cla][repetition]=float(analyse_clients_deficit_classes[cla][7])

			val_deficit_classes_FF[cla][repetition]=float(analyse_deficit_classes[cla][6])
			val_throughput_classes_FF[cla][repetition]=float(analyse_throughput_classes[cla][6])
			val_clients_deficit_classes_FF[cla][repetition]=float(analyse_clients_deficit_classes[cla][8])

			val_deficit_classes_LL[cla][repetition]=float(analyse_deficit_classes[cla][7])
			val_throughput_classes_LL[cla][repetition]=float(analyse_throughput_classes[cla][7])
			val_clients_deficit_classes_LL[cla][repetition]=float(analyse_clients_deficit_classes[cla][9])			
			

		moy_deficit_priority=moy_deficit_priority+val_deficit_priority[repetition]
		moy_throughput_priority=moy_throughput_priority+val_throughput_priority[repetition]
		moy_std_load_priority=moy_std_load_priority+val_std_load_priority[repetition]
		moy_maximum_load_priority=moy_maximum_load_priority+val_maximum_load_priority[repetition]
		moy_clients_deficit_priority=moy_clients_deficit_priority+val_clients_deficit_priority[repetition]
			
		moy_deficit_RSSI=moy_deficit_RSSI+val_deficit_RSSI[repetition]
		moy_throughput_RSSI=moy_throughput_RSSI+val_throughput_RSSI[repetition]
		moy_std_load_RSSI=moy_std_load_RSSI+val_std_load_RSSI[repetition]
		moy_maximum_load_RSSI=moy_maximum_load_RSSI+val_maximum_load_RSSI[repetition]
		moy_clients_deficit_RSSI=moy_clients_deficit_RSSI+val_clients_deficit_RSSI[repetition]

		moy_deficit_FF=moy_deficit_FF+val_deficit_FF[repetition]
		moy_throughput_FF=moy_throughput_FF+val_throughput_FF[repetition]
		moy_std_load_FF=moy_std_load_FF+val_std_load_FF[repetition]
		moy_maximum_load_FF=moy_maximum_load_FF+val_maximum_load_FF[repetition]
		moy_clients_deficit_FF=moy_clients_deficit_FF+val_clients_deficit_FF[repetition]

		moy_deficit_LL=moy_deficit_LL+val_deficit_LL[repetition]
		moy_throughput_LL=moy_throughput_LL+val_throughput_LL[repetition]
		moy_std_load_LL=moy_std_load_LL+val_std_load_LL[repetition]
		moy_maximum_load_LL=moy_maximum_load_LL+val_maximum_load_LL[repetition]
		moy_clients_deficit_LL=moy_clients_deficit_LL+val_clients_deficit_LL[repetition]

		for cla in range(0,priority_class):
			moy_deficit_classes[cla]=moy_deficit_classes[cla]+val_deficit_classes[cla][repetition]
			moy_throughput_classes[cla]=moy_throughput_classes[cla]+val_throughput_classes[cla][repetition]
			moy_clients_deficit_classes[cla]=moy_clients_deficit_classes[cla]+val_clients_deficit_classes[cla][repetition]
				
			moy_deficit_RSSI_classes[cla]=moy_deficit_RSSI_classes[cla]+val_deficit_classes_RSSI[cla][repetition]
			moy_throughput_RSSI_classes[cla]=moy_throughput_RSSI_classes[cla]+val_throughput_classes_RSSI[cla][repetition]
			moy_clients_deficit_RSSI_classes[cla]=moy_clients_deficit_RSSI_classes[cla]+val_clients_deficit_classes_RSSI[cla][repetition]
			
			moy_deficit_FF_classes[cla]=moy_deficit_FF_classes[cla]+val_deficit_classes_FF[cla][repetition]
			moy_throughput_FF_classes[cla]=moy_throughput_FF_classes[cla]+val_throughput_classes_FF[cla][repetition]
			moy_clients_deficit_FF_classes[cla]=moy_clients_deficit_FF_classes[cla]+val_clients_deficit_classes_FF[cla][repetition]
	
			moy_deficit_LL_classes[cla]=moy_deficit_LL_classes[cla]+val_deficit_classes_LL[cla][repetition]
			moy_throughput_LL_classes[cla]=moy_throughput_LL_classes[cla]+val_throughput_classes_LL[cla][repetition]
			moy_clients_deficit_LL_classes[cla]=moy_clients_deficit_LL_classes[cla]+val_clients_deficit_classes_LL[cla][repetition]




		if repetition==nb_repetition-1:
			moy_deficit_priority=float(moy_deficit_priority)/nb_repetition
			moy_throughput_priority=float(moy_throughput_priority)/nb_repetition	
			moy_std_load_priority=float(moy_std_load_priority)/nb_repetition
			moy_maximum_load_priority=float(moy_maximum_load_priority)/nb_repetition
			moy_clients_deficit_priority=float(moy_clients_deficit_priority)/nb_repetition	
	
			moy_deficit_RSSI=float(moy_deficit_RSSI)/nb_repetition
			moy_throughput_RSSI=float(moy_throughput_RSSI)/nb_repetition
			moy_std_load_RSSI=float(moy_std_load_RSSI)/nb_repetition
			moy_maximum_load_RSSI=float(moy_maximum_load_RSSI)/nb_repetition			
			moy_clients_deficit_RSSI=float(moy_clients_deficit_RSSI)/nb_repetition

			moy_deficit_FF=float(moy_deficit_FF)/nb_repetition
			moy_throughput_FF=float(moy_throughput_FF)/nb_repetition
			moy_std_load_FF=float(moy_std_load_FF)/nb_repetition
			moy_maximum_load_FF=float(moy_maximum_load_FF)/nb_repetition			
			moy_clients_deficit_FF=float(moy_clients_deficit_FF)/nb_repetition
				
			moy_deficit_LL=float(moy_deficit_LL)/nb_repetition
			moy_throughput_LL=float(moy_throughput_LL)/nb_repetition
			moy_std_load_LL=float(moy_std_load_LL)/nb_repetition
			moy_maximum_load_LL=float(moy_maximum_load_LL)/nb_repetition			
			moy_clients_deficit_LL=float(moy_clients_deficit_LL)/nb_repetition		
							
			for cla in range(0,priority_class):
				moy_deficit_classes[cla]=float(moy_deficit_classes[cla])/nb_repetition
				moy_throughput_classes[cla]=float(moy_throughput_classes[cla])/nb_repetition
				moy_clients_deficit_classes[cla]=float(moy_clients_deficit_classes[cla])/nb_repetition
				
				moy_deficit_RSSI_classes[cla]=float(moy_deficit_RSSI_classes[cla])/nb_repetition
				moy_throughput_RSSI_classes[cla]=float(moy_throughput_RSSI_classes[cla])/nb_repetition
				moy_clients_deficit_RSSI_classes[cla]=float(moy_clients_deficit_RSSI_classes[cla])/nb_repetition
			
				moy_deficit_FF_classes[cla]=float(moy_deficit_FF_classes[cla])/nb_repetition
				moy_throughput_FF_classes[cla]=float(moy_throughput_FF_classes[cla])/nb_repetition
				moy_clients_deficit_FF_classes[cla]=float(moy_clients_deficit_FF_classes[cla])/nb_repetition
	
				moy_deficit_LL_classes[cla]=float(moy_deficit_LL_classes[cla])/nb_repetition
				moy_throughput_LL_classes[cla]=float(moy_throughput_LL_classes[cla])/nb_repetition
				moy_clients_deficit_LL_classes[cla]=float(moy_clients_deficit_LL_classes[cla])/nb_repetition
						
			


			SN_deficit_priority=0
			SN_throughput_priority=0
			SN_std_load_priority=0
			SN_maximum_load_priority=0	
			SN_clients_deficit_priority=0

			SE_deficit_priority=0
			SE_throughput_priority=0
			SE_std_load_priority=0
			SE_maximum_load_priority=0	
			SE_clients_deficit_priority=0

				
			SN_deficit_RSSI=0
			SN_throughput_RSSI=0
			SN_std_load_RSSI=0
			SN_maximum_load_RSSI=0	
			SN_clients_deficit_RSSI=0

			SE_deficit_RSSI=0
			SE_throughput_RSSI=0
			SE_std_load_RSSI=0
			SE_maximum_load_RSSI=0	
			SE_clients_deficit_RSSI=0

				
			SN_deficit_FF=0
			SN_throughput_FF=0
			SN_std_load_FF=0
			SN_maximum_load_FF=0	
			SN_clients_deficit_FF=0

			SE_deficit_FF=0
			SE_throughput_FF=0
			SE_std_load_FF=0
			SE_maximum_load_FF=0	
			SE_clients_deficit_FF=0


			SN_deficit_LL=0
			SN_throughput_LL=0
			SN_std_load_LL=0
			SN_maximum_load_LL=0	
			SN_clients_deficit_LL=0

			SE_deficit_LL=0
			SE_throughput_LL=0
			SE_std_load_LL=0
			SE_maximum_load_LL=0	
			SE_clients_deficit_LL=0
			


			SN_deficit_priority_classes={}
			SN_throughput_priority_classes={}
			SN_clients_deficit_priority_classes={}

			SE_deficit_priority_classes={}
			SE_throughput_priority_classes={}
			SE_clients_deficit_priority_classes={}

				
			SN_deficit_RSSI_classes={}
			SN_throughput_RSSI_classes={}
			SN_clients_deficit_RSSI_classes={}

			SE_deficit_RSSI_classes={}
			SE_throughput_RSSI_classes={}
			SE_clients_deficit_RSSI_classes={}

				
			SN_deficit_FF_classes={}
			SN_throughput_FF_classes={}
			SN_clients_deficit_FF_classes={}

			SE_deficit_FF_classes={}
			SE_throughput_FF_classes={}
			SE_clients_deficit_FF_classes={}


			SN_deficit_LL_classes={}
			SN_throughput_LL_classes={}
			SN_clients_deficit_LL_classes={}

			SE_deficit_LL_classes={}
			SE_throughput_LL_classes={}
			SE_clients_deficit_LL_classes={}
			for cla in range(0,priority_class):
				SN_deficit_priority_classes[cla]=0
				SN_throughput_priority_classes[cla]=0
				SN_clients_deficit_priority_classes[cla]=0

				SE_deficit_priority_classes[cla]=0
				SE_throughput_priority_classes[cla]=0
				SE_clients_deficit_priority_classes[cla]=0

				
				SN_deficit_RSSI_classes[cla]=0
				SN_throughput_RSSI_classes[cla]=0
				SN_clients_deficit_RSSI_classes[cla]=0

				SE_deficit_RSSI_classes[cla]=0
				SE_throughput_RSSI_classes[cla]=0
				SE_clients_deficit_RSSI_classes[cla]=0

				
				SN_deficit_FF_classes[cla]=0
				SN_throughput_FF_classes[cla]=0
				SN_clients_deficit_FF_classes[cla]=0

				SE_deficit_FF_classes[cla]=0
				SE_throughput_FF_classes[cla]=0
				SE_clients_deficit_FF_classes[cla]=0


				SN_deficit_LL_classes[cla]=0
				SN_throughput_LL_classes[cla]=0
				SN_clients_deficit_LL_classes[cla]=0

				SE_deficit_LL_classes[cla]=0
				SE_throughput_LL_classes[cla]=0
				SE_clients_deficit_LL_classes[cla]=0			




			for i in range (0,nb_repetition):
				SN_deficit_priority=SN_deficit_priority+(val_deficit_priority[i]-moy_deficit_priority)**2
				SN_throughput_priority=SN_throughput_priority+(val_throughput_priority[i]-moy_throughput_priority)**2
				SN_std_load_priority=SN_std_load_priority+(val_std_load_priority[i]-moy_std_load_priority)**2	
				SN_maximum_load_priority=SN_maximum_load_priority+(val_maximum_load_priority[i]-moy_maximum_load_priority)**2	
				SN_clients_deficit_priority=SN_clients_deficit_priority+(val_clients_deficit_priority[i]-moy_clients_deficit_priority)**2				
					

				SN_deficit_RSSI=SN_deficit_RSSI+(val_deficit_RSSI[i]-moy_deficit_RSSI)**2
				SN_throughput_RSSI=SN_throughput_RSSI+(val_throughput_RSSI[i]-moy_throughput_RSSI)**2
				SN_std_load_RSSI=SN_std_load_RSSI+(val_std_load_RSSI[i]-moy_std_load_RSSI)**2		
				SN_maximum_load_RSSI=SN_maximum_load_RSSI+(val_maximum_load_RSSI[i]-moy_maximum_load_RSSI)**2	
				SN_clients_deficit_RSSI=SN_clients_deficit_RSSI+(val_clients_deficit_RSSI[i]-moy_clients_deficit_RSSI)**2
					
				SN_deficit_FF=SN_deficit_FF+(val_deficit_FF[i]-moy_deficit_FF)**2
				SN_throughput_FF=SN_throughput_FF+(val_throughput_FF[i]-moy_throughput_FF)**2
				SN_std_load_FF=SN_std_load_FF+(val_std_load_FF[i]-moy_std_load_FF)**2		
				SN_maximum_load_FF=SN_maximum_load_FF+(val_maximum_load_FF[i]-moy_maximum_load_FF)**2	
				SN_clients_deficit_FF=SN_clients_deficit_FF+(val_clients_deficit_FF[i]-moy_clients_deficit_FF)**2


				SN_deficit_LL=SN_deficit_LL+(val_deficit_LL[i]-moy_deficit_LL)**2
				SN_throughput_LL=SN_throughput_LL+(val_throughput_LL[i]-moy_throughput_LL)**2
				SN_std_load_LL=SN_std_load_LL+(val_std_load_LL[i]-moy_std_load_LL)**2		
				SN_maximum_load_LL=SN_maximum_load_LL+(val_maximum_load_LL[i]-moy_maximum_load_LL)**2	
				SN_clients_deficit_LL=SN_clients_deficit_LL+(val_clients_deficit_LL[i]-moy_clients_deficit_LL)**2
	
				
				for cla in range(0,priority_class):
					SN_deficit_priority_classes[cla]=SN_deficit_priority_classes[cla]+(val_deficit_classes[cla][i]-moy_deficit_classes[cla])**2
					SN_throughput_priority_classes[cla]=SN_throughput_priority_classes[cla]+(val_throughput_classes[cla][i]-moy_throughput_classes[cla])**2
					SN_clients_deficit_priority_classes[cla]=SN_clients_deficit_priority_classes[cla]+ (val_clients_deficit_classes[cla][i]-moy_clients_deficit_classes[cla])**2				
					

					SN_deficit_RSSI_classes[cla]=SN_deficit_RSSI_classes[cla]+(val_deficit_classes_RSSI[cla][i]-moy_deficit_RSSI_classes[cla])**2
					SN_throughput_RSSI_classes[cla]=SN_throughput_RSSI_classes[cla]+(val_throughput_classes_RSSI[cla][i]-moy_throughput_RSSI_classes[cla])**2
					SN_clients_deficit_RSSI_classes[cla]=SN_clients_deficit_RSSI_classes[cla]+(val_clients_deficit_classes_RSSI[cla][i]-moy_clients_deficit_RSSI_classes[cla])**2
					
					SN_deficit_FF_classes[cla]=SN_deficit_FF_classes[cla]+(val_deficit_classes_FF[cla][i]-moy_deficit_FF_classes[cla])**2
					SN_throughput_FF_classes[cla]=SN_throughput_FF_classes[cla]+(val_throughput_classes_FF[cla][i]-moy_throughput_FF_classes[cla])**2
					SN_clients_deficit_FF_classes[cla]=SN_clients_deficit_FF_classes[cla]+(val_clients_deficit_classes_FF[cla][i]-moy_clients_deficit_FF_classes[cla])**2


					SN_deficit_LL_classes[cla]=SN_deficit_LL_classes[cla]+(val_deficit_classes_LL[cla][i]-moy_deficit_LL_classes[cla])**2
					SN_throughput_LL_classes[cla]=SN_throughput_LL_classes[cla]+(val_throughput_classes_LL[cla][i]-moy_throughput_LL_classes[cla])**2
					SN_clients_deficit_LL_classes[cla]=SN_clients_deficit_LL_classes[cla]+(val_clients_deficit_classes_LL[cla][i]-moy_clients_deficit_LL_classes[cla])**2					



			SN_deficit_priority=math.sqrt(SN_deficit_priority/nb_repetition)
			SN_throughput_priority=math.sqrt(SN_throughput_priority/nb_repetition)
			SN_std_load_priority=math.sqrt(SN_std_load_priority/nb_repetition)
			SN_maximum_load_priority=math.sqrt(SN_maximum_load_priority/nb_repetition)
			SN_clients_deficit_priority=math.sqrt(SN_clients_deficit_priority/nb_repetition)

				
			SE_deficit_priority=SN_deficit_priority/math.sqrt(nb_repetition)
			SE_throughput_priority=SN_throughput_priority/math.sqrt(nb_repetition)
			SE_std_load_priority=SN_std_load_priority/math.sqrt(nb_repetition)
			SE_maximum_load_priority=SN_maximum_load_priority/math.sqrt(nb_repetition)
			SE_clients_deficit_priority=SN_clients_deficit_priority/math.sqrt(nb_repetition)
				
				

			SN_deficit_RSSI=math.sqrt(SN_deficit_RSSI/nb_repetition)
			SN_throughput_RSSI=math.sqrt(SN_throughput_RSSI/nb_repetition)
			SN_std_load_RSSI=math.sqrt(SN_std_load_RSSI/nb_repetition)
			SN_maximum_load_RSSI=math.sqrt(SN_maximum_load_RSSI/nb_repetition)
			SN_clients_deficit_RSSI=math.sqrt(SN_clients_deficit_RSSI/nb_repetition)

				
			SE_deficit_RSSI=SN_deficit_RSSI/math.sqrt(nb_repetition)
			SE_throughput_RSSI=SN_throughput_RSSI/math.sqrt(nb_repetition)
			SE_std_load_RSSI=SN_std_load_RSSI/math.sqrt(nb_repetition)
			SE_maximum_load_RSSI=SN_maximum_load_RSSI/math.sqrt(nb_repetition)
			SE_clients_deficit_RSSI=SN_clients_deficit_RSSI/math.sqrt(nb_repetition)

	
			SN_deficit_FF=math.sqrt(SN_deficit_FF/nb_repetition)
			SN_throughput_FF=math.sqrt(SN_throughput_FF/nb_repetition)
			SN_std_load_FF=math.sqrt(SN_std_load_FF/nb_repetition)
			SN_maximum_load_FF=math.sqrt(SN_maximum_load_FF/nb_repetition)
			SN_clients_deficit_FF=math.sqrt(SN_clients_deficit_FF/nb_repetition)

				
			SE_deficit_FF=SN_deficit_FF/math.sqrt(nb_repetition)
			SE_throughput_FF=SN_throughput_FF/math.sqrt(nb_repetition)
			SE_std_load_FF=SN_std_load_FF/math.sqrt(nb_repetition)
			SE_maximum_load_FF=SN_maximum_load_FF/math.sqrt(nb_repetition)
			SE_clients_deficit_FF=SN_clients_deficit_FF/math.sqrt(nb_repetition)


			SN_deficit_LL=math.sqrt(SN_deficit_LL/nb_repetition)
			SN_throughput_LL=math.sqrt(SN_throughput_LL/nb_repetition)
			SN_std_load_LL=math.sqrt(SN_std_load_LL/nb_repetition)
			SN_maximum_load_LL=math.sqrt(SN_maximum_load_LL/nb_repetition)
			SN_clients_deficit_LL=math.sqrt(SN_clients_deficit_LL/nb_repetition)

				
			SE_deficit_LL=SN_deficit_LL/math.sqrt(nb_repetition)
			SE_throughput_LL=SN_throughput_LL/math.sqrt(nb_repetition)
			SE_std_load_LL=SN_std_load_LL/math.sqrt(nb_repetition)
			SE_maximum_load_LL=SN_maximum_load_LL/math.sqrt(nb_repetition)
			SE_clients_deficit_LL=SN_clients_deficit_LL/math.sqrt(nb_repetition)
			

			
			SE_deficit_priority_classes={}
			SE_throughput_priority_classes={}
			SE_clients_deficit_priority_classes={}

			SE_deficit_RSSI_classes={}
			SE_throughput_RSSI_classes={}
			SE_clients_deficit_RSSI_classes={}

			SE_deficit_FF_classes={}
			SE_throughput_FF_classes={}
			SE_clients_deficit_FF_classes={}

			SE_deficit_LL_classes={}
			SE_throughput_LL_classes={}
			SE_clients_deficit_LL_classes={}
			for cla in range(0,priority_class):
				SN_deficit_priority_classes[cla]=math.sqrt(SN_deficit_priority_classes[cla]/nb_repetition)
				SN_throughput_priority_classes[cla]=math.sqrt(SN_throughput_priority_classes[cla]/nb_repetition)
				SN_clients_deficit_priority_classes[cla]=math.sqrt(SN_clients_deficit_priority_classes[cla]/nb_repetition)

				
				SE_deficit_priority_classes[cla]=SN_deficit_priority_classes[cla]/math.sqrt(nb_repetition)
				SE_throughput_priority_classes[cla]=SN_throughput_priority_classes[cla]/math.sqrt(nb_repetition)
				SE_clients_deficit_priority_classes[cla]=SN_clients_deficit_priority_classes[cla]/math.sqrt(nb_repetition)
				
				

				SN_deficit_RSSI_classes[cla]=math.sqrt(SN_deficit_RSSI_classes[cla]/nb_repetition)
				SN_throughput_RSSI_classes[cla]=math.sqrt(SN_throughput_RSSI_classes[cla]/nb_repetition)
				SN_clients_deficit_RSSI_classes[cla]=math.sqrt(SN_clients_deficit_RSSI_classes[cla]/nb_repetition)

				
				SE_deficit_RSSI_classes[cla]=SN_deficit_RSSI_classes[cla]/math.sqrt(nb_repetition)
				SE_throughput_RSSI_classes[cla]=SN_throughput_RSSI_classes[cla]/math.sqrt(nb_repetition)
				SE_clients_deficit_RSSI_classes[cla]=SN_clients_deficit_RSSI_classes[cla]/math.sqrt(nb_repetition)

	
				SN_deficit_FF_classes[cla]=math.sqrt(SN_deficit_FF_classes[cla]/nb_repetition)
				SN_throughput_FF_classes[cla]=math.sqrt(SN_throughput_FF_classes[cla]/nb_repetition)
				SN_clients_deficit_FF_classes[cla]=math.sqrt(SN_clients_deficit_FF_classes[cla]/nb_repetition)

				
				SE_deficit_FF_classes[cla]=SN_deficit_FF_classes[cla]/math.sqrt(nb_repetition)
				SE_throughput_FF_classes[cla]=SN_throughput_FF_classes[cla]/math.sqrt(nb_repetition)
				SE_clients_deficit_FF_classes[cla]=SN_clients_deficit_FF_classes[cla]/math.sqrt(nb_repetition)


				SN_deficit_LL_classes[cla]=math.sqrt(SN_deficit_LL_classes[cla]/nb_repetition)
				SN_throughput_LL_classes[cla]=math.sqrt(SN_throughput_LL_classes[cla]/nb_repetition)
				SN_clients_deficit_LL_classes[cla]=math.sqrt(SN_clients_deficit_LL_classes[cla]/nb_repetition)

				
				SE_deficit_LL_classes[cla]=SN_deficit_LL_classes[cla]/math.sqrt(nb_repetition)
				SE_throughput_LL_classes[cla]=SN_throughput_LL_classes[cla]/math.sqrt(nb_repetition)
				SE_clients_deficit_LL_classes[cla]=SN_clients_deficit_LL_classes[cla]/math.sqrt(nb_repetition)


			###################la valeur de 1.96 correspond a un interval de confiance ce 95%####################		
				
			erreur_deficit_priority=SE_deficit_priority* 1.96
			erreur_throughput_priority=SE_throughput_priority* 1.96
			erreur_std_load_priority=SE_std_load_priority* 1.96
			erreur_maximum_load_priority=SE_maximum_load_priority* 1.96	
			erreur_clients_deficit_priority=SE_maximum_load_priority* 1.96

				
			erreur_deficit_RSSI=SE_deficit_RSSI* 1.96
			erreur_throughput_RSSI=SE_throughput_RSSI* 1.96
			erreur_std_load_RSSI=SE_std_load_RSSI* 1.96
			erreur_maximum_load_RSSI=SE_maximum_load_RSSI* 1.96	
			erreur_clients_deficit_RSSI=SE_maximum_load_RSSI* 1.96

				
			erreur_deficit_FF=SE_deficit_FF* 1.96
			erreur_throughput_FF=SE_throughput_FF* 1.96
			erreur_std_load_FF=SE_std_load_FF* 1.96
			erreur_maximum_load_FF=SE_maximum_load_FF* 1.96	
			erreur_clients_deficit_FF=SE_maximum_load_FF* 1.96

				
			erreur_deficit_LL=SE_deficit_LL* 1.96
			erreur_throughput_LL=SE_throughput_LL* 1.96
			erreur_std_load_LL=SE_std_load_LL* 1.96
			erreur_maximum_load_LL=SE_maximum_load_LL* 1.96	
			erreur_clients_deficit_LL=SE_maximum_load_LL* 1.96
	

			
			erreur_deficit_priority_classes={}
			erreur_throughput_priority_classes={}
			erreur_clients_deficit_priority_classes={}

				
			erreur_deficit_RSSI_classes={}
			erreur_throughput_RSSI_classes={}
			erreur_clients_deficit_RSSI_classes={}

				
			erreur_deficit_FF_classes={}
			erreur_throughput_FF_classes={}
			erreur_clients_deficit_FF_classes={}

				
			erreur_deficit_LL_classes={}
			erreur_throughput_LL_classes={}
			erreur_clients_deficit_LL_classes={}

			for cla in range(0,priority_class):
				erreur_deficit_priority_classes[cla]=SE_deficit_priority_classes[cla]* 1.96
				erreur_throughput_priority_classes[cla]=SE_throughput_priority_classes[cla]* 1.96
				erreur_clients_deficit_priority_classes[cla]=SE_clients_deficit_priority_classes[cla]* 1.96

				
				erreur_deficit_RSSI_classes[cla]=SE_deficit_RSSI_classes[cla]* 1.96
				erreur_throughput_RSSI_classes[cla]=SE_throughput_RSSI_classes[cla]* 1.96
				erreur_clients_deficit_RSSI_classes[cla]=SE_clients_deficit_RSSI_classes[cla]* 1.96

				
				erreur_deficit_FF_classes[cla]=SE_deficit_FF_classes[cla]* 1.96
				erreur_throughput_FF_classes[cla]=SE_throughput_FF_classes[cla]* 1.96
				erreur_clients_deficit_FF_classes[cla]=SE_clients_deficit_FF_classes[cla]* 1.96

				
				erreur_deficit_LL_classes[cla]=SE_deficit_LL_classes[cla]* 1.96
				erreur_throughput_LL_classes[cla]=SE_throughput_LL_classes[cla]* 1.96
				erreur_clients_deficit_LL_classes[cla]=SE_clients_deficit_LL_classes[cla]* 1.96



			s_deficit_priority=str(5*density_nodes)+" "+str(moy_deficit_priority)+" "+str(erreur_deficit_priority)+" "+str(moy_deficit_RSSI)+" "+str(erreur_deficit_RSSI)+" "+str(moy_deficit_FF)+" "+str(erreur_deficit_FF)+" "+str(moy_deficit_LL)+" "+str(erreur_deficit_LL)+"\n"
					
			s_throughput_priority=str(5*density_nodes)+" "+str(moy_throughput_priority)+" "+str(erreur_throughput_priority)+" "+str(moy_throughput_RSSI)+" "+str(erreur_throughput_RSSI)+" "+str(moy_throughput_FF)+" "+str(erreur_throughput_FF)+" "+str(moy_throughput_LL)+" "+str(erreur_throughput_LL)+"\n"
				
			s_std_load_priority=str(5*density_nodes)+" "+str(moy_std_load_priority)+" "+str(erreur_std_load_priority)+" "+str(moy_std_load_RSSI)+" "+str(erreur_std_load_RSSI)+" "+str(moy_std_load_FF)+" "+str(erreur_std_load_FF)+" "+str(moy_std_load_LL)+" "+str(erreur_std_load_LL)+"\n"
		
			s_maximum_load_priority=str(5*density_nodes)+" "+str(moy_maximum_load_priority)+" "+str(erreur_maximum_load_priority)+" "+str(moy_maximum_load_RSSI)+" "+str(erreur_maximum_load_RSSI)+" "+str(moy_maximum_load_FF)+" "+str(erreur_maximum_load_FF)+" "+str(moy_maximum_load_LL)+" "+str(erreur_maximum_load_LL)+"\n"	

			s_clients_deficit_priority=str(5*density_nodes)+" "+str(moy_clients_deficit_priority)+" "+str(erreur_clients_deficit_priority)+" "+str(moy_clients_deficit_RSSI)+" "+str(erreur_clients_deficit_RSSI)+" "+str(moy_clients_deficit_FF)+" "+str(erreur_clients_deficit_FF)+" "+str(moy_clients_deficit_LL)+" "+str(erreur_clients_deficit_LL)+"\n"		
				
			s_deficit_classes=str(5*density_nodes)
			s_throughput_classes=str(5*density_nodes)
			s_nb_clients_deficit_classes=str(5*density_nodes)
			for cla in range(0,priority_class):
				s_deficit_classes=s_deficit_classes+" "+str(round(moy_deficit_classes[cla],5))+" "+str(round(erreur_deficit_classes[cla],5))+" "+str(round(moy_deficit_RSSI_classes[cla],5))+" "+str(round(erreur_deficit_RSSI_classes[cla],5))+" "+str(round(moy_deficit_FF_classes[cla],5))+" "+str(round(erreur_deficit_FF_classes[cla],5))+" "+str(round(moy_deficit_LL_classes[cla],5))+" "+str(round(erreur_deficit_LL_classes[cla],5))

				s_throughput_classes=s_throughput_classes+" "+str(round(moy_throughput_classes[cla],5))+" "+str(round(erreur_throughput_classes[cla],5))+" "+str(round(moy_throughput_RSSI_classes[cla],5))+" "+str(round(erreur_throughput_RSSI_classes[cla],5))+" "+str(round(moy_throughput_FF_classes[cla],5))+" "+str(round(erreur_throughput_FF_classes[cla],5))+" "+str(round(moy_throughput_LL_classes[cla],5))+" "+str(round(erreur_throughput_LL_classes[cla],5))
	
				s_nb_clients_deficit_classes=s_nb_clients_deficit_classes+" "+str(round(moy_clients_deficit_classes[cla],5))+" "+str(round(erreur_clients_deficit_classes[cla],5))+" "+str(round(moy_clients_deficit_RSSI_classes[cla],5))+" "+str(round(erreur_clients_deficit_RSSI_classes[cla],5))+" "+str(round(moy_clients_deficit_FF_classes[cla],5))+" "+str(round(erreur_clients_deficit_FF_classes[cla],5))+" "+str(round(moy_clients_deficit_LL_classes[cla],5))+" "+str(round(erreur_clients_deficit_LL_classes[cla],5))




			
			s_deficit_classes=s_deficit_classes+"\n"
			s_throughput_classes=s_throughput_classes+"\n"
			s_nb_clients_deficit_classes=s_nb_clients_deficit_classes+"\n"

	
			g_deficit.write(s_deficit_priority)
			g_throughput.write(s_throughput_priority)
			g_APs_std_load.write(s_std_load_priority)
			g_APs_maximum_load.write(s_maximum_load_priority)
			g_clients_Nb_deficit.write(s_clients_deficit_priority)
			g_PLOT_deficit_classes.write(s_deficit_classes)	
			g_throughput_classes.write(s_throughput_classes)
			g_clients_Nb_deficit_class.write(s_nb_clients_deficit_classes)
			

			moy_deficit_priority=0  
			moy_throughput_priority=0
			moy_std_load_priority=0
			moy_maximum_load_priority=0
			moy_clients_deficit_priority=0

			erreur_deficit_priority=0
			erreur_throughput_priority=0
			erreur_std_load_priority=0
			erreur_maximum_load_priority=0
			erreur_clients_deficit_priority=0


			moy_deficit_RSSI=0
			moy_throughput_RSSI=0
			moy_std_load_RSSI=0
			moy_maximum_load_RSSI=0
			moy_clients_deficit_RSSI=0

			erreur_deficit_RSSI=0
			erreur_throughput_RSSI=0
			erreur_std_load_RSSI=0
			erreur_maximum_load_RSSI=0
			erreur_clients_deficit_RSSI=0	
		

			moy_deficit_FF=0
			moy_throughput_FF=0
			moy_std_load_FF=0
			moy_maximum_load_FF=0
			moy_clients_deficit_FF=0

			erreur_deficit_FF=0
			erreur_throughput_FF=0
			erreur_std_load_FF=0
			erreur_maximum_load_FF=0
			erreur_clients_deficit_FF=0
		

			moy_deficit_LL=0
			moy_throughput_LL=0
			moy_std_load_LL=0
			moy_maximum_load_LL=0
			moy_clients_deficit_LL=0

			erreur_deficit_LL=0
			erreur_throughput_LL=0
			erreur_std_load_LL=0
			erreur_maximum_load_LL=0
			erreur_clients_deficit_LL=0


			for cla in range(0,priority_class):
				moy_deficit_classes[cla]=0
				moy_throughput_classes[cla]=0
				moy_clients_deficit_classes[cla]=0

				erreur_deficit_classes[cla]=0
				erreur_throughput_classes[cla]=0
				erreur_clients_deficit_classes[cla]=0

	
				moy_deficit_RSSI_classes[cla]=0
				moy_throughput_RSSI_classes[cla]=0
				moy_clients_deficit_RSSI_classes[cla]=0

				erreur_deficit_RSSI_classes[cla]=0
				erreur_throughput_RSSI_classes[cla]=0
				erreur_clients_deficit_RSSI_classes[cla]=0


				moy_deficit_FF_classes[cla]=0
				moy_throughput_FF_classes[cla]=0
				moy_clients_deficit_FF_classes[cla]=0

				erreur_deficit_FF_classes[cla]=0
				erreur_throughput_FF_classes[cla]=0
				erreur_clients_deficit_FF_classes[cla]=0


				moy_deficit_LL_classes[cla]=0
				moy_throughput_LL_classes[cla]=0
				moy_clients_deficit_LL_classes[cla]=0

				erreur_deficit_LL_classes[cla]=0
				erreur_throughput_LL_classes[cla]=0
				erreur_clients_deficit_LL_classes[cla]=0			

							
				
g_deficit.close()
g_throughput.close()
g_APs_std_load.close()
g_APs_maximum_load.close()
g_clients_Nb_deficit.close()

g_clients_Nb_deficit_class.close()
g_throughput_classes.close()
g_PLOT_deficit_classes.close()					
								
	
