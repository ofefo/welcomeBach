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
	echo "
			     ..',;:cclc:;,'..';:ccccc:;,...
			  .,cldxxxkxkkxxdolc:loooddddddollc;'.
                        .:oxkkOOOOOOkkkxddoooododddoooooddool:,.
                     .'cxOOOOOOkkkkkkkkOOOOOOOOkkkkxxdddooloollc;.
                   .,ldkOkkOOOOOkOOOOOOOOOOOOOOOkkkxxdxxxddoollol:,.
                 .,oxOOOOOOOOkkOOOOOOOOOOOOOOOkOkkxxdddddddddlllolc;.
                .:oxkkOOOOOkkOOOOOOkkxxxxkxkkkxxxdddooooolloddoolloc,
               .;dxOOOOOOOOOOOOkkkdxxkkkkkkkkkkkkkkxxxxddolc:lxxllllc.
              .:dxOOOOOOOkOOOOOkdoxkkkOOOOOOkkkkkkkkkxxxxdolc:cxxolllc.
              :okkOOOOOOkOOOkkxooxkOOOOOOOOOOkkkkkkkkkxxxddlc:;:kxolll:.
             'ckOOOOOOOkkOOOkkdldkkOOOOOOOOOOkkkkkkkkkkxxddlc:;,:kdllll,
            'cdOOOOOOkkkkOOOkxdlxkkOOOOOOOOOOkkkkkkkkkkxxxdoc:;;.oxolcl:.
            ;lxkkkOOOOOxOOOOkxllxkkkOOOOOOOOOOkkkkkkkkkkxxdol:;;.;dlllll:.
           .:loxkOOOOkxxOOOkxdclxkkkOOOOOOOOOOOOkkkkkkkkkxddlc:;'.lcldolc,
           .:lkkOOOkkkkxOkkkddcokkkkOOOkddxxkkkkkkkOkxOOkoc,'..',.;:oddol:.
           .lxkkxdkkOOkdxxkxol:cxkkkkxdoll:;;:clddkOkolc;,',;:::;;.':xdol:.
           ;loodxkOkxkxdkkkxxc;cllcl:;;;:;;;;;;;;::::;;;;;::::::::,'ddoll:,
          .:lllkOOkOkxdxxkxdllllkkkx:.,;:::::::::::.co;;::::::::cc';lodolc;
           .cdxxkOkdoodkOOOkxd::xkkOk,;;::::::::::,.dkl;;:::cccloc..:llc:;,
           'ldkdooddxOxkOkkddo;cdxkOOc:::::::::::;.okOd:;coodxkxc'  ,lllcl:.
           'loollkOOkxdxkddooc;lxxxxkxcoxddddddl;;xkkkxo:;:llc:;;'  ;clllc;
           .clcoxkOkdollodolc;;lxxddxxkooooollc:lxdddxkxc;;odlc:,.  'lolll;.
           .;cokddoolokkxdoc:;:ldxddddxkkkkkkdcldlcc::c:,.,ldol:,.  ,coooc,.
            .coxxdolckxdxdlc:;;:odxdddxxkkxxdclkOOOkxc;,',:clol:'.  .clllc'.
            .colcccoolkkxxoc;;;:lodxddxxxxdodddkkOOkdcol:::cclc;'.  .:llc:..
            .:ccclkxdlxddolc::;;clodxxxdxxxkkdllxdllllc::;;:ooc'.   ,ccll:,.
             .::ldxoc:ddooc::;,:clooxxxxxxkkdcoolloolcccc:;:cl;'.  .'clc,'.
              .:xxllc::odoc::,';cloloxxxxxxxdxkOkkxdlccc::::::,'.   .cc;..
              .:lodocc:clc::;:.':clolooddddddxkkkkxdoooolcc;,''.   .;;'..
               :lllcc:::ccc:;,..,;:clcclloooodxkkkkOOOkdll:,.''    ...,.
               .:llllcccc;:;'...:d:;:cccccccccodxxkkxxoc:;'.'.      ...
                .:cclcc;:,,'....;k0kdl:clodxxxoolccc::;,'.''...       .
                 .:c;,,,,,,'',..,d0000Oxolcloodddoc:;,,'''.......... ..
                  .''''...'';;;.,:O000000OOxolc::;;;,,'..  ...  ...   ...'.
                 .,'..  ..,;;,;'.'cO00000000OOOkxdlc;'...'';:. ....       .....
            ...  .     .''. .,,;..';k000000000000OOOOkxddxdc'.......          ..
                      .'.     ..,..,:O000000000000000000Oo,..''.  .,.
                      .         .'.',;k000000000000000Od:;,;;,'.   .'
                  .              .'.'';x000000000000Ooc:,;;:,.      ..
                  ..             .,'',,:x0000000000xlcc:,,;;'
                   .              ....'';x0000000Ol:cc:;;;,..
                                  .......;k000000o:c::;;,.
                                    .; ..,d00000x;;;;;;;.
                    .           .,'..;. ..o00000:,,,',;;'
                           .   .OKX0,..  'o0000x,',;::.
                               .d00O. ..;,d0000l...:;
                                 ...   .',x000O,.',..
                                        .:k000k'..'.
                               .       .'lk000x'..
                             ,kKk'  . .'.ok000o'..   ..
                             cO0xc ..  .,oO000o..  .
                              ... ..   .:dO000o.  ..
                                 ... ...ldO000o'
				 "
fi
