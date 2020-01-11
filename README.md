# Bin Buddy
###### Email reminders to take the bins out, sent via GMail using the [smtplib](https://docs.python.org/3/library/smtplib.html) library.

Written as a learning exercise so I could figure out how to send emails using Python.
 
The script is run by the operating system's task scheduler, rather than constantly running on a host. This is due to the fact that it only needs to run once a fortnight, so it would be overkill to have it constantly checking the time and date to see if it was time to execute.
 
###### Note: Script requires sender login credentials and target email address. Excluded from upload for obvious security reasons.