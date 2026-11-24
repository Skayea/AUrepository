#!/bin/bash

read -p "Введите имя гена: " GENE_NAME
read -p "Введите уровень экспрессии: " EXP_LEVEL

if [ -z "$GENE_NAME" ] || [ -z "$EXP_LEVEL" ]; then
    echo "Ошибка: недостаток данных."
    exit 1
fi

echo "Экспрессия гена $GENE_NAME составляет $EXP_LEVEL единиц."
