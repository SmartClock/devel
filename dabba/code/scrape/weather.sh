#!/bin/bash

while true
do
	wget -O ../../data/weather.dat "http://api.openweathermap.org/data/2.5/weather?q=Kanpur" --quiet
	
	: '
	INFO=$(wget -O- "http://api.openweathermap.org/data/2.5/weather?q=Kanpur" --quiet)
	echo $INFO
	echo $INFO >> ../../data/weather.dat
	'
	
	sleep 10s
done