# Rasphone

# Call a given phone number.

We need to make a post request to this url.

```bash
http://localhost:8000/call/
```

With the following data inside its body:

```json
{
    "id": 441,
    "message_id": 1,
    "cellphone": 984287312
}
```

Where the track file is mapped with help of the message_id.

# Send a SMS to a given number.

We need to make a post request to this url.

```bash
http://localhost:8000/sms/
```

With the following data inside its body:

```json
{
    "id": 666,
    "message": "This is my first sms!",
    "cellphone": 1234567896
}
```

##Run Task queue processes

Before this, we need to [install and setup RabbitMQ](http://celery.readthedocs.org/en/latest/getting-started/brokers/rabbitmq.html#setting-up-rabbitmq).

Then, to use celery we need to create a RabbitMQ user, a virtual host and allow that user access to that virtual host:

```bash
$ sudo rabbitmqctl add_user myuser mypassword
$ sudo rabbitmqctl add_vhost myvhost
$ sudo rabbitmqctl set_permissions -p myvhost myuser ".*" ".*" ".*"
```

Then we set up a BROKER_URL env var and run celery to the same level of manage.py

```bash
$ export BROKER_URL='amqp://myuser:mypassword@localhost:5672/myvhost'
$ celery -A rasphone worker -l info
```

###Run the scheduler

```bash
$ celery -A rasphone beat
```