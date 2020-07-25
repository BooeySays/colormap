PREFIX ?= /usr/local
HOMEDIR = ~
DX2DIR = $(DESTDIR)$(HOMEDIR)/.DX2
BINDIR = $(DESTDIR)$(PREFIX)/bin
DX2BIN = $(DESTDIR)$(DX2DIR)/bin
DX2ALIASES = $(DESTDIR)$(DX2DIR)/aliases

.PHONY: install uninstall disable-self-upgrade

install:
	install -m755 -d $(DX2DIR)
	install -m755 -d $(DX2BIN)
	install -m755 -d $(DX2ALIASES)
	install -m755 colormap $(DX2BIN)
	install -m755 colormap.aka $(DX2ALIASES)

uninstall:
	rm -f $(DX2BIN)/colormap
	rm -f $(DX2ALIASES)/colormap.aka

# Disable the self-upgrade mechanism entirely. Intended for packagers.
#
# We assume that sed(1) has the -i option, which is not POSIX but seems common
# enough in modern implementations.
disable-self-upgrade:
	sed -i.bak 's/^ENABLE_SELF_UPGRADE_MECHANISM = True$$/ENABLE_SELF_UPGRADE_MECHANISM = False/' googler
