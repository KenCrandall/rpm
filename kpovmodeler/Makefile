SRCDIR := $(shell pwd)
NAME := $(shell basename $(SRCDIR))
SRCVER := $(shell rpmspec -P $(NAME).spec | grep -i '^version' | awk -F ':' '{print $$2}' | tr -d ' ')
SRCNAME := $(shell rpmspec -P $(NAME).spec | grep -i '^source' | head -1 | awk -F ':' '{print $$2}' | tr -d ' ' | xargs basename)
include ../common/Makefile
prepare:
	@echo -e "\033[1;32mDownloading from SVN\033[0m"
	@if [ ! -f $(SRCNAME) ] ; then \
		svn export svn://anonsvn.kde.org/home/kde/trunk/extragear/graphics/kpovmodeler kpovmodeler-$(SRCVER) ; \
		tar -czf $(SRCNAME) kpovmodeler-$(SRCVER) ; \
		rm -rf kpovmodeler-$(SRCVER) ; \
	fi

