AT%SETACFG="manager.urcBootEv.enabled","true"
AT%SETACFG="radiom.config.multi_rat_enable","true"
AT%SETACFG="radiom.config.preferred_rat_list","none" 
AT%SETACFG="radiom.config.auto_preference_mode","none"
AT%SETACFG="locsrv.operation.locsrv_enable","true"
AT%SETACFG="locsrv.internal_gnss.auto_restart","enable"
AT%SETACFG="modem_apps.Mode.AutoConnectMode","true"
ATZ


AT%RATACT="NBNTN","1"
AT+CFUN=0
AT%PDNSET=1,"DATA.MONO","IP"
AT%SETSYSCFG=SW_CFG.nb_band_table.band#1,ENABLE;23
AT%NTNCFG="POS","IGNSS","0"
ATZ


AT+CFUN=0
AT%IGNSSEV="FIX",1        
AT%NOTIFYEV="SIB31",1
AT+CEREG=2
AT%IGNSSACT=1


AT+CFUN=1 