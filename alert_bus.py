subscribers = []

def subscribe(func):
    subscribers.append(func)

def publish(event):
    for sub in subscribers:
        sub(event)