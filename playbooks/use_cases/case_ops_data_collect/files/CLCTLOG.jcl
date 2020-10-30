//CLCTLOG  JOB (99999),NOTIFY=&SYSUID,
//          CLASS=A,MSGLEVEL=(1,1),REGION=0M
//*************************************************************
//STEP1    EXEC PGM=SORT
//SYSOUT   DD SYSOUT=A
//SORTIN   DD DSN=OPS.DATA.TMP,DISP=SHR
//SORTOUT  DD DSN=OPS.DATA.&DATE,DISP=(NEW,CATLG,DELETE),
//            SPACE=(TRK,(10,10)),UNIT=SYSDA
//SYSIN  DD *
  OPTION COPY
/*
