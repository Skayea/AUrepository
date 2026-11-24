#!/bin/bash
awk '
{
	sum += $2
	count += 1
}
END {
	print "Сумма оценок: ", sum
	print "Средняя оценка: ", sum/count
}' students.txt

echo -n "Максимальная оценка: "
awk 'NR==1{max=$2} $2>max{max=$2} END{print max}' students.txt
