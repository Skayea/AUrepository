#!/bin/bash
check_root( ) {
	if [ "$EUID" -ne 0 ]; then
		echo "Необходимы права суперпользователя."
		exit 1
	fi
}

check_root

echo "Здравствуйте, суперпользователь!"