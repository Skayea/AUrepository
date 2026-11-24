#!/bin/bash

read -p "Введите ваш вес в кг: " weight
read -p "Введите ваш рост в см: " height

bmi=$((weight*10000 / (height * height)))

echo "Ваш ИМТ: $bmi"
