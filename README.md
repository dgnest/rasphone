# Rasphone

# Call a given phone number.

We need to make a post request to this url.

```bash
http://localhost:8000/call/
```

With the following data inside its body:

```json
{
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
    "message": "This is my first sms!",
    "cellphone": 1234567896
}
```