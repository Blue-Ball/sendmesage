from zadarma import api
import time

message = ''
numbers = []
senderid = ''

print('sender:--------------------------------------')
with open('sender.txt', 'r') as f:
    senderid = f.read()
    print(senderid)
    f.close()
print('----------------------------------------------')

print('message:--------------------------------------')
with open('message.txt', 'r') as f:
    message = f.read()
    print(message)
    f.close()
print('----------------------------------------------')

print('numbers:--------------------------------------')
with open('numbers.txt', 'r') as f:
    numbers = f.readlines()
    print(numbers)
    f.close()
print('----------------------------------------------')

# 11924f89b69545bf8024
# 9ad010fbd15cfb5b003d

response = ''
timeDiff = 0.0

z_api = api.ZadarmaAPI(key='11924f89b69545bf8024', secret='9ad010fbd15cfb5b003d')
response = z_api.call('/v1/info/balance/', {}, 'GET')
print('Your Banace is :' + response)


canSend = True
timeDiff = time.time()
sentCount = 0

for number in numbers:
    while True:
        if canSend:
            print('sending to:' + number)
            # param = {'number':number, 'message':message, 'caller_id':senderid}
            param = {'number':number, 'message':message}
            response = z_api.call('/v1/sms/send/', param, 'POST')
            print('sent:' + response)
            sentCount += 1
            if sentCount >= 100:
                canSend = False
        else:
            print('can not send. waiting')
            time.sleep(1)
            if time.time() - timeDiff > 60:
                canSend = True
                timeDiff = time.time()
                sentCount = 0
            continue
        break
