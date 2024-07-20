from crontab import CronTab

python_path = '/workspace/venv/bin/python'

manage_py_path = '/workspace/rent-car-ireland/manage.py'

command = f'{python_path} {manage_py_path} runcrons'

cron = CronTab(user=True)

job = cron.new(command=command, comment='update_booking_status')

job.minute.on(0)
job.hour.on(0)

cron.write()

print("Cron job added successfully.")