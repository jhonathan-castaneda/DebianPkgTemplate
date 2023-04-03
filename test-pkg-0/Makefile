prefix? = /usr/local
target  = $(DESTDIR)$(prefix)

all:
.PHONY:	all
install:
	@echo INSTALLING CLIENT EXECUTABLE AT /usr/local/bin/ AS checksumClient.py  ...
	@install -d $(target)/bin/ 
	@install -m 755 scripts/checksumClient.py $(target)/bin/
	
	@echo INSTALLING SERVER EXECUTABLE AT /usr/local/bin/ AS checksumServer.py  ...
	@install -d $(target)/bin/ 
	@install -m 755 scripts/checksumServer.py $(target)/bin/
