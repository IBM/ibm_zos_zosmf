//JCLSAMP1 JOB MSGCLASS=H,MSGLEVEL=(1,1),NOTIFY=&SYSUID 
//STEP1  EXEC PGM=IKJEFT01,DYNAMNBR=99                  
//SYSPRINT DD SYSOUT=*                                  
//SYSTSPRT DD SYSOUT=*                                  
//SYSTSIN  DD *                                         
 RL ZMFAPLA BBNBASE.ZOSMF.WORKLOAD_MANAGEMENT.WORKLOAD_MANAGEMENT.INSTALL