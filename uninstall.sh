#!/bin/bash

SUCCESS=1
rm -f $HOME/.local/bin/Bach
rm -f $HOME/.config/autostart/welcomeBach.desktop
if [ -f "/usr/local/bin/Bach" ]; then
	if [ "$(whoami)" == "root" ]; then
		echo "Can't remove Bach from /usr/, try again with sudo!"
		SUCCESS=0
		exit
	else
		rm -f /usr/local/bin/Bach
	fi
fi
if [ $SUCCESS=1 ]; then
	echo "
	@@@  @@@      @@@       @@@@@@@  @@@@@@@@  @@@@@@@   @@@@@@   @@@@@@@ @@@  @@@
	@@!  @@!      @@!       @@!  @@@ @@!       @@!  @@@ @@!  @@@ !@@      @@!  @@@
	!!@  @!!      @!!       @!@!@!@  @!!!:!    @!@!@!@  @!@!@!@! !@!      @!@!@!@!
	!!:  !!:      !!:       !!:  !!! !!:       !!:  !!! !!:  !!! :!!      !!:  !!!
	:    : ::.: : : ::.: :  :: : ::  : :: ::   :: : ::   :   : :  :: :: :  :   : :
	"
	echo "			...        ...
			..,:clooollc:,';cloolllc:,'.                            
                      .:oxkkkkkkOkxdllclooodoooddoll:,.                         
                   .,lkOOOOOkOkkkkkkkkkkkkkkxxodooloolc,.                       
                 .,lkOkOOOOOkkkOOOOOOOOOOOOkxxdxxddoololc,.                     
                ,okOOOOOOkOOOOOOOOOOOOOOOOkkxxdddddddllllc,.                    
              .cdkkOOOOOkkOOOOkkxxkkkkkkxkxdddooollodddlcoc,                    
             .cdOOOOOOOOOOOkkdxkkkkkkkkkkkkkkxxxxdol:cxxlllc'                   
            'cxkOOOOOkOOOOkdoxkOOOOOOOOkkkkkkkkxxxdoc::dxollc.                  
           .:xOOOOOOOkOOOkdlxkkOOOOOOOOkkkkkkkkkxxdoc:;:xdlll;.                 
           ;oOOOOOkkkkOOkkdlkkOOOOOOOOOkkkkkkkkkxxdoc:;,cxollc,                 
          .lxkkkOOOOxOOOkxllkkkOOOOOOOOOkkkkkkkkkxdol:;,.dllllc.                
          ,coxOOOOOkxOOOkdclkkkOOOOOOOOOOkkkkkkkkkxdoc:;.:llool;                
          ;lkkOOkxkkdOOkxd:okkkOOkxoddxkkkkkkkxkkdc;'.',.':oxdoc.               
          :dxkddkkOkdxkxdl;cdkkkkdolc;,;:codOkoc:,,,:::::,'cxolc,               
         'lloxkOOxxxxkkkdc:odol;'',;;;;::;;;,;:;;;:::::::;'doooc;               
         .:ldkOOkxdokOOkxdclkkOO,;;:::::::::.:xc;:::::ccl,'cdolc;               
          :dkdooookkkOOxoo;cxkOOc::::::::::,,xOo;:cllodd;. ,lll::.              
         .cooookOOkxxkddol;lxxkkxcodoooool;:kkkxl;:lolc;,. ;llll:.              
          :lloxkOxollddol;;oxddxxxooooolc:odddxkd:;lolc;'. 'loll:.              
          'cdkdooloxkkdc:;:ldxdddxkkkkkdcodllc::;'':doc;'  ,lool;.              
          .coddolcoxdxdl:;;:odxddxxxxxocokOOkxl:;,;cclc;.  .cllc,.              
           :llccoxlkxdlc:;;:lodxdxxxxdxxdxkOxdlol:;:clc'.  ,cllc'.              
           ,c:cdxocdxddc::;:loodxxdxkkxccllccccc::;;ll;'. .'ccc:..              
            ,;xxol:cool::,':coodxxxxxxddkOkxxolcc:;:::,'   .c:,.                
            .:odolc:llc::;.,:loloddddddxkkkkxoollcc:;''.  .,;'..                
             ;lllcc::cc:;,..;:clccllooodxkkkOOOkdlc,''.   .....                 
             .;llllcc:;;'...odc:cclllllclodxxxdlc;'.'.     ...                  
              .:clc:;;','...cO0kdl:codxxxolc::;,'.''.....   ..                  
               .;;'','.'';,.,x0000Oxolcclllc:;;,'.. ............                
               .''.. ..,;;;'';O000000OOkxdlc:,'....',. ...     ....             
           .. ..     ''..';,.';k0000000000OOOkxooool,....'.         ..          
                   .'.   ...'.';k0000000000000000kc'.''. .'.                    
                   .        ...,;k0000000000000kl;,;;,..  .'                    
                            .'.',;x0000000000kl:;,:;,.      .                   
                .            ...',;x00000000dccc;,;;.                           
                              .....,k000000o:c::;,.                             
                               .,...l00000d::;;;;.                              
                 .          ....,...;O000O;;,',,;.                              
                           '0K0:.  .:O000d'',::.                                
                           .dOk'  ',oO000:..';.                                 
                                   'oO00k'.'.                                   
                                   ,dO00x'...                                   
                          ;c'    ..;d000d'.                                     
                         :OKk...  .:x000o..   .                                 
                          ;,. ..  .lx000o.  .                                   
                             .. ..'ok000o.                                      

				 "
fi
