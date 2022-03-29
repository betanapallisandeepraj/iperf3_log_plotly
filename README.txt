################################################################################
#
# Author        : Sandeep Raj Betanapalli
# Email 	: betanapallisandeepraj@gmail.com
# Date          : 30-03-2022 (GMT+8)
# Version       : v00.00
#
# Usage:
#	$python3 iperf3_log_plot.py
#################################################################################

This python software project helps to draw graph of iperf3 log by using plotly. 
After running the iperf3_log_plot.py with python3, window opens to select the
log text file. After selecting the text file, it opens a html file with 
plotly graph. Sample log files(iperf_log_212829032022) and bash shell script(iperf_3days.sh) used to generate log file are in the same project. 

Steps to use:
1. run below command
	$python3 iperf3_log_plot.py
2. select the iperf log file in text format
3. open file.html file created in the same path as in iperf3_log_plot.py.
	file.html file automatically opens in default browser. 
	if not opened, one open file.html
4. browse the image in html with zoomin, zoomout options. 
	picture x-axis represents seconds, y-axis represents 
	the data throughput in megabits per second.


Note: 
if error occurs with modules, please install all required modules 
using pip3 or other ways. For example,
$sudo apt-get install python3-tk
$pip3 install pandas
