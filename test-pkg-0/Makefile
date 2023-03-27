prefix? = /usr/local
target  = $(DESTDIR)$(prefix)

all:
.PHONY:	all
install:
	@echo INSTALLING CLIENT EXECUTABLE AT /usr/local/bin/ AS checksumClient.py  ...
	@install -d $(target)/bin/ 
	@install -m 755 checksumClient.py $(target)/bin/

	@echo INSTALLING SERVER EXECUTABLE AT /usr/local/bin/ AS checksumServer.py  ...
	@install -d $(target)/bin/ 
	@install -m 755 checksumServer.py $(target)/bin/

	@echo INSTALLING SYSTEMD SERVICE at /etc/systemd/system/  ...
	$(shell sudo cp checksum.service /etc/systemd/system/checksum.service)
	
	@echo RUNNING DAEMON RELOAD  ...
	$(shell sudo systemctl daemon-reload)
	
	@echo STARTING CHECKSUM SERVICE  ...
	$(shell sudo systemctl start checksum.service)
	
	@echo SERVICE INSTALLATION COMPLETED		
