#!/bin/sh

time_stamp() {
	TS=`date +%T`
}

main() {
	(
		time_stamp;
		celerycam.sh >> "$PROJECT_LOG/celery_cam.""$TS"".log" &
	)
	(
		time_stamp;
		runserver_plus.sh >> "$PROJECT_LOG/runserver_plus.""$TS"".log" &
	)
	(
		time_stamp;
		worker.sh >> "$PROJECT_LOG/worker.""$TS"".log" &
	)
}

main;
